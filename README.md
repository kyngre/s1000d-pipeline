# S1000D XML → JSON AST Pipeline Engine

방산·항공 규격 **S1000D Issue 6** 데이터 모듈(XML)을 웹 에디터에서 바로 렌더링할 수 있는 **무손실(lossless) JSON AST**로 변환하는 백엔드 코어 엔진입니다.

---

## 목차

1. [프로젝트 개요](#1-프로젝트-개요)
2. [사전 준비 및 설치](#2-사전-준비-및-설치)
3. [사용 방법](#3-사용-방법)
4. [아키텍처 및 폴더 구조](#4-아키텍처-및-폴더-구조)
5. [프론트엔드를 위한 JSON AST 구조 안내](#5-프론트엔드를-위한-json-ast-구조-안내)

---

## 1. 프로젝트 개요

S1000D는 항공·방산 분야의 기술 출판 국제 표준이며, 데이터 모듈(Data Module) 한 건이 수십 종의 XSD를 참조하고 깊은 중첩과 혼합 콘텐츠(mixed content)를 가진 매우 복잡한 XML 형태로 작성됩니다. 이 복잡도 때문에 **편집기(Slate.js, ProseMirror 등)에서 직접 XML을 다루기에는 부적합**하며, 실제로는 다음과 같은 중간 표현이 반드시 필요합니다.

> XML 원본 → **타입이 명확하고 순서가 보존된 JSON AST** → 웹 에디터 트리

본 엔진은 그 변환의 백엔드 코어를 담당하며 다음 원칙을 보장합니다.

- **무손실 변환** — 원본 XML의 모든 요소·속성·텍스트가 AST에 그대로 보존됩니다(자전거 샘플 116개 파일이 사용하는 24개 스키마 전 종에 대해, 총 236개 회귀 테스트로 검증).
- **혼합 콘텐츠의 순서 보존** — `<para>Use a <internalRef/> and <emphasis>tighten</emphasis>.</para>` 같은 케이스에서 텍스트 조각과 인라인 요소의 문서 순서가 단일 `children` 배열에 그대로 유지됩니다.
- **편집기 친화적 메타데이터** — 레이아웃 역할(`block`/`inline`/`void`), 참조 ID, 그래픽 엔티티 테이블 등 프론트엔드가 필요로 하는 파생 정보를 별도 슬롯에 미리 가공해 제공합니다.
- **왕복 변환 가능성(Round-trip Safety)** — `attributes`와 `children`은 원본을 그대로 보존하고, `metadata`는 파생 정보로만 사용되므로 `XML → AST → XML` 복원 경로를 안전하게 설계할 수 있습니다.

---

## 2. 사전 준비 및 설치

### 2.1 시스템 요구사항

| 항목 | 권장 버전 |
| --- | --- |
| Python | **3.10 이상** (3.14에서 검증) |
| OS | macOS, Linux, Windows (WSL 권장) |
| Git | 최신 버전 |

### 2.2 pip으로 직접 설치 (권장)

별도 클론 없이 다른 프로젝트에서 라이브러리로 바로 사용할 수 있습니다.

```bash
pip install git+https://github.com/kyngre/s1000d-pipeline.git
```

설치 후 바로 import 가능합니다.

```python
from s1000d_pipeline import parse_to_ast

ast = parse_to_ast("path/to/DMC-...xml")
```

### 2.3 개발용 로컬 설치 (기여 / 수정 목적)

소스를 직접 수정하거나 테스트를 실행하려면 저장소를 클론해 editable 모드로 설치합니다.

```bash
git clone https://github.com/kyngre/s1000d-pipeline.git
cd s1000d-pipeline

# 가상환경 생성
python3 -m venv venv
source venv/bin/activate          # macOS / Linux
# .\venv\Scripts\Activate.ps1    # Windows PowerShell

# editable 설치 (의존성 자동 해결)
pip install -e ".[dev]"
```

의존성은 `pyproject.toml`에서 관리되며 자동으로 설치됩니다.

- **`xsdata[lxml]`** — XSD에서 파이썬 dataclass를 생성·파싱하는 핵심 라이브러리
- **`lxml`** — DOCTYPE 엔티티 추출 및 XML prolog 메타데이터 파싱

### 2.4 (선택) 추가 도구 설치

```bash
# 새로운 XSD를 추가해서 dataclass를 재생성하고 싶을 때
pip install 'xsdata[cli]>=24.0'
```

### 2.5 (선택) S1000D 자전거 샘플 데이터셋

대량 검증(`sweep`) 및 회귀 테스트는 S1000D가 공식 배포하는 **Bike Data Set for Release number 6 R2** 가 있을 때 자동으로 실행됩니다. 데이터셋은 [s1000d.org](https://www.s1000d.org/) 의 다운로드 페이지에서 받을 수 있습니다.

데이터셋이 없으면 sweep 명령은 비활성화되며, 회귀 테스트는 자동으로 skip되므로 코어 엔진 자체는 그대로 동작합니다. 데이터셋을 다른 경로에 두었다면 `S1000D_BIKE_DATASET` 환경변수로 위치를 지정할 수 있습니다.

```bash
export S1000D_BIKE_DATASET="/path/to/Bike Data Set for Release number 6 R2"
```

---

## 3. 사용 방법

활성화된 가상환경(`source venv/bin/activate`) 상태를 가정합니다.

### 3.1 단일 파일 변환 — `main.py`

리포지토리 루트에 포함된 골든 샘플(`samples/golden/procedural_720A.xml`)을 한 번에 JSON AST로 변환해 표준출력으로 덤프합니다.

```bash
# 기본 골든 샘플 (절차형 DM)
python main.py

# 임의의 XML 파일을 지정
python main.py samples/golden/ddn_sample.xml
python main.py /path/to/any/DMC-...xml
```

출력 일부 예시:

```json
{
  "type": "#document",
  "nodeKind": "document",
  "metadata": {
    "rootElement": "dmodule",
    "schemaSource": "proced",
    "schemaLocation": "http://www.s1000d.org/S1000D_6/xml_schema_flat/proced.xsd",
    "xmlNamespaces": { "xlink": "http://www.w3.org/1999/xlink", "...": "..." },
    "docTypeEntities": {
      "ICN-C0419-S1000D0385-001-01": {
        "systemId": "ICN-C0419-S1000D0385-001-01.CGM",
        "ndata": "cgm"
      }
    }
  },
  "children": [ /* 실제 dmodule 트리 */ ]
}
```

파일로 저장하려면 일반적인 쉘 리다이렉션을 사용하세요.

```bash
python main.py > out.ast.json
python main.py samples/golden/ddn_sample.xml > ddn.ast.json
```

### 3.2 대량 스트레스 테스트 — `tools/sweep.py`

S1000D 자전거 샘플 데이터셋의 모든 `.XML` 파일을 일괄 처리하여, **(a)** 파이프라인이 크래시 없이 동작하는지, **(b)** 분류되지 않은 인라인 후보 요소가 새로 등장하는지를 한꺼번에 검증합니다.

```bash
python -m s1000d_pipeline.tools.sweep \
  "/path/to/Bike Data Set for Release number 6 R2"
```

요약 결과 예시(현재 116개 유효 XML 모두 통과):

```text
Files swept   : 116
  parsed ok   : 116
  failed      :   0

By schema (ok / failed):
  appliccrossreftable          3 ok     0 fail
  brex                         2 ok     0 fail
  checklist                    1 ok     0 fail
  comrep                      15 ok     0 fail
  ddn                          1 ok     0 fail
  descript                    14 ok     0 fail
  fault                        5 ok     0 fail
  ipd                          2 ok     0 fail
  proced                      39 ok     0 fail
  ...
  (총 24개 스키마)

No unclassified inline candidates.
```

JSON 형식으로 저장하고 싶다면:

```bash
python -m s1000d_pipeline.tools.sweep \
  "/path/to/Bike Data Set for Release number 6 R2" \
  --json sweep_report.json
```

### 3.3 회귀 테스트 — `pytest`

XML → AST 변환의 **무손실성**과 xsdata 직렬화 라운드트립의 **구조적 동등성**을 자동 검증합니다.

```bash
# 개발용 설치(pip install -e ".[dev]") 시 pytest가 이미 포함됩니다
python -m pytest tests/test_round_trip.py -q
```

출력 예시:

```text
236 passed in 11.77s
```

검증되는 두 가지 명제는 다음과 같습니다.

- **A. XML ⊆ AST** — lxml로 직접 파싱한 원본 XML의 모든 (요소, 속성, 텍스트)가 변환된 AST에서 그대로 발견됩니다.
- **B. xsdata 라운드트립 동등성** — `parse(xml).instance == parse(serialize(parse(xml).instance))`. 즉, AST 빌더가 소비하는 dataclass 트리가 직렬화 후 재파싱해도 구조적으로 일치합니다.

### 3.4 (고급) 신규 XSD 추가 후 dataclass 재생성

S1000D 새 스키마를 추가했거나 dataclass를 재생성하려면 다음 단계를 따릅니다.

1. 대상 `.xsd` 파일을 `schemas/` 에 복사합니다.
2. `s1000d_pipeline/models/_registry.py` 의 `_ROOT_CLASS_NAMES` 딕셔너리에 `"<schema_short_name>": "<RootDataclassName>"` 항목을 추가합니다.
3. 다음 명령으로 dataclass를 재생성합니다.

```bash
pip install 'xsdata[cli]>=24.0'                            # 최초 1회
python -m s1000d_pipeline.tools.generate_models            # 등록된 전체
python -m s1000d_pipeline.tools.generate_models proced     # 특정 스키마만
python -m s1000d_pipeline.tools.generate_models --all      # schemas/ 전체
```

---

## 4. 아키텍처 및 폴더 구조

### 4.1 폴더 구조

```
s1000d-pipeline/
├── pyproject.toml                   # 패키지 메타데이터 및 의존성
├── main.py                          # 단일 파일 변환 데모 스크립트
├── README.md
│
├── src/
│   └── s1000d_pipeline/             # 핵심 엔진 패키지 (pip install 대상)
│       │
│       ├── parsing/                 # 1단계: XML → typed dataclass 트리
│       │   ├── schema_resolver.py   #   xsi:noNamespaceSchemaLocation 해석
│       │   ├── doctype.py           #   DOCTYPE 엔티티 사이드 채널
│       │   └── parser.py            #   xsdata + lxml 통합 오케스트레이터
│       │
│       ├── models/                  # 2단계: 자동 생성된 dataclass 패키지
│       │   ├── _registry.py         #   schema_source → 루트 클래스 라우터
│       │   ├── proced/, descript/,  #   xsdata로 생성됨 (편집 금지)
│       │   ├── ddn/, pm/, ipd/, ... #   총 26개 패키지
│       │   └── ...
│       │
│       ├── ast/                     # 3·4단계: dataclass → AST → JSON
│       │   ├── nodes.py             #   AST TypedDict 정의 (단일 진실 원본)
│       │   ├── classify.py          #   block / inline / BLOCK_IN_MIXED 분류
│       │   ├── builder.py           #   재귀 빌더 (스키마-비의존)
│       │   └── serializer.py        #   AST → JSON-ready 정규화
│       │
│       └── tools/                   # 운영용 CLI 도구
│           ├── generate_models.py   #   xsdata 코드 생성 래퍼
│           └── sweep.py             #   샘플셋 일괄 검증
│
├── schemas/                         # S1000D 평면 XSD 30종 (검증된 카탈로그)
│   ├── ddn.xsd
│   ├── proced.xsd
│   ├── descript.xsd
│   └── ...
│
├── samples/
│   └── golden/                      # 골든 테스트 케이스 (procedural / ddn)
│
└── tests/                           # 회귀 테스트
    ├── conftest.py
    └── test_round_trip.py           # XML ⊆ AST + xsdata 라운드트립 동등성
```

### 4.2 파이프라인 4단계 흐름

```text
┌──────────────────────────────────────────────────────────────────────────┐
│  XML 파일 (e.g. DMC-S1000DBIKE-…720A-A_011-00_EN-US.XML)                  │
└──────────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌──────────────────────────────────────────────────────────────────────────┐
│  1)  parsing.schema_resolver                                             │
│      • 문서 루트의 xsi:noNamespaceSchemaLocation 속성 읽기                │
│      • URL 베이스네임을 단축 키로 변환 (e.g. "proced")                    │
└──────────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌──────────────────────────────────────────────────────────────────────────┐
│  2)  models._registry  (지연 로딩 라우터)                                │
│      • "proced" → s1000d_pipeline.models.proced.Dmodule                  │
│      • "ddn"    → s1000d_pipeline.models.ddn.Ddn                         │
│      • 필요한 dataclass 패키지만 그 시점에 import (메모리 절약)          │
└──────────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌──────────────────────────────────────────────────────────────────────────┐
│  3)  parsing.parser  +  parsing.doctype                                  │
│      • xsdata XmlParser로 dataclass 인스턴스 생성                        │
│      • 동시에 DOCTYPE 엔티티 테이블을 lxml로 사이드 캡처                 │
│      • prolog (xml_version, encoding, namespaces)도 함께 수집            │
│      → ParsedDocument(instance, schema_source, doctype_entities, ...)    │
└──────────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌──────────────────────────────────────────────────────────────────────────┐
│  4)  ast.builder  →  ast.serializer                                      │
│      • dataclass 트리를 재귀 순회하며 ElementNode/TextNode 생성           │
│      • 혼합 콘텐츠는 단일 ordered children 배열에 인터리빙               │
│      • classify.py의 inline/block/BLOCK_IN_MIXED 테이블로 nodeKind 결정  │
│      • Decimal/Enum/date 등을 JSON-ready 값으로 정규화                   │
└──────────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌──────────────────────────────────────────────────────────────────────────┐
│  최종 출력: 단일 #document 노드를 루트로 갖는 JSON AST                   │
│  (5절 참조)                                                              │
└──────────────────────────────────────────────────────────────────────────┘
```

### 4.3 설계 원칙

| 원칙 | 적용 위치 |
| --- | --- |
| **스키마-비의존 빌더** | `ast/builder.py`는 어떤 DM 타입의 dataclass라도 `dataclasses.fields()` 메타데이터만 읽어 변환합니다. DM 타입별 분기 코드 **0줄**. |
| **라우팅은 한 곳에만** | DM 타입 → 루트 클래스 매핑은 `_registry.py` 한 파일에 집중되어 있습니다. 신규 스키마 추가는 1줄 등록 + dataclass 생성으로 끝납니다. |
| **사이드 채널은 명시적으로 분리** | `xsdata`가 처리하지 못하는 DOCTYPE 엔티티는 `doctype.py`에 별도로 캡처되어 root metadata에 합쳐집니다. 본류 파이프라인에 lxml 의존성이 새지 않습니다. |
| **AST는 무상태(stateless)** | 파일 시스템 / 네트워크 접근 0회. 모든 데이터는 ParsedDocument에 담겨 빌더로 들어옵니다. |

---

## 5. 프론트엔드를 위한 JSON AST 구조 안내

### 5.1 노드 기본 형태

모든 AST 노드는 다음 5개 필드를 공유합니다.

```jsonc
{
  "type":       "para",         // 원본 XML 요소명 (camelCase)
  "nodeKind":   "block",        // 에디터 레이아웃 역할
  "attributes": { /* ... */ },  // 원본 XML 속성을 그대로 보존 (왕복용)
  "metadata":   { /* ... */ },  // 파생된 편집기 보조 정보 (재생성 가능)
  "children":   [ /* ... */ ]   // 자식 노드 리스트 (텍스트 노드 포함)
}
```

### 5.2 각 필드의 역할

| 필드 | 의미 | 왕복 변환에 기여 |
| --- | --- | :---: |
| `type` | 원본 XML 요소명 (또는 `"#text"`, `"#document"`) | ✅ |
| `nodeKind` | 편집기 렌더링 역할: `block`, `inline`, `text`, `document` | ❌ (재생성 가능) |
| `attributes` | 원본 XML의 모든 속성. 값은 xsdata가 typed로 변환 (정수, 불리언 등) | ✅ |
| `metadata` | `dataclassName`, `schemaSource`, `void`, `mixedContent`, `refIds` 등 편집기 편의 데이터 | ❌ (재생성 가능) |
| `children` | 자식 ElementNode 또는 TextNode의 **순서가 보존된** 배열 | ✅ |

> 💡 **왕복 변환 계약**: `attributes`와 `children`만 보존되면 XML 원본을 의미적으로 동등하게 복원할 수 있습니다. `nodeKind`와 `metadata`는 프론트엔드가 자유롭게 수정/추가/삭제해도 안전합니다.

### 5.3 `nodeKind` 종류

| 값 | 설명 | 예시 |
| --- | --- | --- |
| `document` | 최상위 래퍼. 정확히 하나의 자식(루트 XML 요소)을 가짐. DOCTYPE 엔티티·네임스페이스 등 문서 메타데이터 보관 | `<dmodule>`, `<ddn>`, `<pm>` 의 부모 |
| `block` | 줄바꿈으로 구분되는 블록 콘텐츠 | `<para>`, `<proceduralStep>`, `<figure>`, `<note>`, `<randomList>` |
| `inline` | 텍스트 흐름 내부에 등장하는 요소 | `<emphasis>`, `<internalRef>`, `<acronym>`, 그리고 `<para>` 안의 `<dmRef>` |
| `text` | 문자열 리프 (혼합 콘텐츠의 텍스트 조각) | `"Push the fork downwards"` |

### 5.4 혼합 콘텐츠 예시 (가장 중요)

```xml
<para>Use a <internalRef internalRefId="sup-0002" internalRefTargetType="irtt04"/> and <emphasis>tighten</emphasis>.</para>
```

는 다음과 같이 **단일 `children` 배열**에 5개 노드가 순서대로 인터리빙됩니다.

```jsonc
{
  "type": "para",
  "nodeKind": "block",
  "attributes": {},
  "metadata": { "mixedContent": true, "void": false, "schemaSource": "proced" },
  "children": [
    { "type": "#text", "nodeKind": "text", "text": "Use a " },
    {
      "type": "internalRef",
      "nodeKind": "inline",
      "attributes": {
        "internalRefId": "sup-0002",
        "internalRefTargetType": "irtt04"
      },
      "metadata": { "void": true, "refIds": ["sup-0002"] },
      "children": []
    },
    { "type": "#text", "nodeKind": "text", "text": " and " },
    {
      "type": "emphasis",
      "nodeKind": "inline",
      "attributes": {},
      "metadata": { "void": false },
      "children": [
        { "type": "#text", "nodeKind": "text", "text": "tighten" }
      ]
    },
    { "type": "#text", "nodeKind": "text", "text": "." }
  ]
}
```

### 5.5 Void 요소 (속성-only)

`<dmCode>`, `<graphic>`, `<internalRef />` 처럼 자식이 없고 속성만 갖는 요소는 `metadata.void: true`, `children: []`로 표현되며 모든 정보는 `attributes`에 보존됩니다.

```jsonc
{
  "type": "dmCode",
  "nodeKind": "block",
  "attributes": {
    "modelIdentCode": "S1000DBIKE",
    "systemDiffCode": "AAA",
    "systemCode": "DA2",
    "subSystemCode": "1",
    "subSubSystemCode": "0",
    "assyCode": "00",
    "disassyCode": "00",
    "disassyCodeVariant": "AA",
    "infoCode": "720",
    "infoCodeVariant": "A",
    "itemLocationCode": "A"
  },
  "metadata": { "void": true, "dataclassName": "DmCode" },
  "children": []
}
```

### 5.6 문서 루트(`#document`)와 그래픽 엔티티

DOCTYPE으로 선언된 ICN 그래픽 엔티티 테이블과 네임스페이스 등은 **루트 `#document` 노드**의 `metadata`에 모입니다. 별도 API 호출 없이 이미지 참조를 즉시 해석할 수 있습니다.

```jsonc
{
  "type": "#document",
  "nodeKind": "document",
  "metadata": {
    "rootElement": "dmodule",
    "schemaSource": "proced",
    "schemaLocation": "http://www.s1000d.org/S1000D_6/xml_schema_flat/proced.xsd",
    "xmlVersion": "1.0",
    "xmlEncoding": "UTF-8",
    "xmlNamespaces": {
      "xlink": "http://www.w3.org/1999/xlink",
      "xsi":   "http://www.w3.org/2001/XMLSchema-instance"
    },
    "docTypeEntities": {
      "ICN-C0419-S1000D0385-001-01": {
        "systemId": "ICN-C0419-S1000D0385-001-01.CGM",
        "ndata": "cgm"
      }
    }
  },
  "children": [ /* 단 하나의 루트 ElementNode */ ]
}
```

### 5.7 왜 이 구조가 Slate.js / ProseMirror에 적합한가

- **단일 `children` 배열 모델**은 Slate.js의 `Node[]` 모델, ProseMirror의 `Fragment` 모델과 동일한 사고 방식입니다. 변환 어댑터가 매우 얇아집니다.
- **인라인/블록 결정이 미리 끝나 있어** 에디터의 스키마 정의(`schema.nodes`, `schema.marks`)에 그대로 매핑할 수 있습니다. 프론트엔드가 S1000D XSD를 다시 해석할 필요가 없습니다.
- **`metadata.refIds`, `metadata.void`** 같은 파생 정보가 노드별로 미리 계산되어, 하이퍼링크/참조 해석·드래그 앤 드롭 가능 여부 등의 UI 의사결정이 노드 단위 검사만으로 끝납니다.
- **`attributes`는 그대로 둔 채 `metadata`만 자유롭게 수정**해도 왕복 변환이 안전합니다. 편집기는 스타일 캐시·셀렉션 상태·undo 스택 같은 UI 상태를 metadata에 자유롭게 추가·삭제해도 됩니다.
- **DOCTYPE 그래픽 테이블이 루트 메타데이터에 있어** `<graphic infoEntityIdent="ICN-..." />` 같은 참조를 별도 네트워크 호출 없이 즉시 해석할 수 있습니다.

---

## 부록: 검증 현황 요약 

| 검증 항목 | 결과 |
| --- | --- |
| 자전거 샘플셋 sweep | **116 / 116 통과** (24개 스키마, 0 실패, 0 미분류 인라인 후보) |
| pytest 회귀 테스트 | **236 / 236 통과** (XML ⊆ AST + xsdata 라운드트립) |
| 평균 단일 변환 소요 시간 | ~50ms (procedural 720A 기준, MacBook Air M3) |

