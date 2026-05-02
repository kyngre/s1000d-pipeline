from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import ForwardRef

from s1000d_pipeline.models.comrep.rdf import Description
from s1000d_pipeline.models.comrep.xlink import (
    ActuateValue,
    ShowValue,
    TypeValue,
)
from s1000d_pipeline.models.comrep.xml import SpaceValue


@dataclass(kw_only=True)
class Sita:
    class Meta:
        name = "SITA"

    value: str = field(default="")


class AccessPointTypeValueAttType(Enum):
    ACCPNL01 = "accpnl01"
    ACCPNL02 = "accpnl02"
    ACCPNL03 = "accpnl03"
    ACCPNL04 = "accpnl04"
    ACCPNL05 = "accpnl05"
    ACCPNL06 = "accpnl06"
    ACCPNL07 = "accpnl07"
    ACCPNL08 = "accpnl08"
    ACCPNL09 = "accpnl09"
    ACCPNL10 = "accpnl10"
    ACCPNL11 = "accpnl11"
    ACCPNL12 = "accpnl12"
    ACCPNL13 = "accpnl13"
    ACCPNL14 = "accpnl14"
    ACCPNL15 = "accpnl15"
    ACCPNL16 = "accpnl16"
    ACCPNL17 = "accpnl17"
    ACCPNL18 = "accpnl18"
    ACCPNL19 = "accpnl19"
    ACCPNL20 = "accpnl20"
    ACCPNL21 = "accpnl21"
    ACCPNL22 = "accpnl22"
    ACCPNL23 = "accpnl23"
    ACCPNL24 = "accpnl24"
    ACCPNL25 = "accpnl25"
    ACCPNL26 = "accpnl26"
    ACCPNL27 = "accpnl27"
    ACCPNL28 = "accpnl28"
    ACCPNL29 = "accpnl29"
    ACCPNL30 = "accpnl30"
    ACCPNL31 = "accpnl31"
    ACCPNL32 = "accpnl32"
    ACCPNL33 = "accpnl33"
    ACCPNL34 = "accpnl34"
    ACCPNL35 = "accpnl35"
    ACCPNL36 = "accpnl36"
    ACCPNL37 = "accpnl37"
    ACCPNL38 = "accpnl38"
    ACCPNL39 = "accpnl39"
    ACCPNL40 = "accpnl40"
    ACCPNL41 = "accpnl41"
    ACCPNL42 = "accpnl42"
    ACCPNL43 = "accpnl43"
    ACCPNL44 = "accpnl44"
    ACCPNL45 = "accpnl45"
    ACCPNL46 = "accpnl46"
    ACCPNL47 = "accpnl47"
    ACCPNL48 = "accpnl48"
    ACCPNL49 = "accpnl49"
    ACCPNL50 = "accpnl50"
    ACCPNL51 = "accpnl51"
    ACCPNL52 = "accpnl52"
    ACCPNL53 = "accpnl53"
    ACCPNL54 = "accpnl54"
    ACCPNL55 = "accpnl55"
    ACCPNL56 = "accpnl56"
    ACCPNL57 = "accpnl57"
    ACCPNL58 = "accpnl58"
    ACCPNL59 = "accpnl59"
    ACCPNL60 = "accpnl60"
    ACCPNL61 = "accpnl61"
    ACCPNL62 = "accpnl62"
    ACCPNL63 = "accpnl63"
    ACCPNL64 = "accpnl64"
    ACCPNL65 = "accpnl65"
    ACCPNL66 = "accpnl66"
    ACCPNL67 = "accpnl67"
    ACCPNL68 = "accpnl68"
    ACCPNL69 = "accpnl69"
    ACCPNL70 = "accpnl70"
    ACCPNL71 = "accpnl71"
    ACCPNL72 = "accpnl72"
    ACCPNL73 = "accpnl73"
    ACCPNL74 = "accpnl74"
    ACCPNL75 = "accpnl75"
    ACCPNL76 = "accpnl76"
    ACCPNL77 = "accpnl77"
    ACCPNL78 = "accpnl78"
    ACCPNL79 = "accpnl79"
    ACCPNL80 = "accpnl80"
    ACCPNL81 = "accpnl81"
    ACCPNL82 = "accpnl82"
    ACCPNL83 = "accpnl83"
    ACCPNL84 = "accpnl84"
    ACCPNL85 = "accpnl85"
    ACCPNL86 = "accpnl86"
    ACCPNL87 = "accpnl87"
    ACCPNL88 = "accpnl88"
    ACCPNL89 = "accpnl89"
    ACCPNL90 = "accpnl90"
    ACCPNL91 = "accpnl91"
    ACCPNL92 = "accpnl92"
    ACCPNL93 = "accpnl93"
    ACCPNL94 = "accpnl94"
    ACCPNL95 = "accpnl95"
    ACCPNL96 = "accpnl96"
    ACCPNL97 = "accpnl97"
    ACCPNL98 = "accpnl98"
    ACCPNL99 = "accpnl99"


class AcronymTypeAttType(Enum):
    AT01 = "at01"
    AT02 = "at02"
    AT03 = "at03"
    AT04 = "at04"
    AT05 = "at05"
    AT06 = "at06"
    AT07 = "at07"
    AT08 = "at08"
    AT09 = "at09"
    AT10 = "at10"
    AT11 = "at11"
    AT12 = "at12"
    AT13 = "at13"
    AT14 = "at14"
    AT15 = "at15"
    AT16 = "at16"
    AT17 = "at17"
    AT18 = "at18"
    AT19 = "at19"
    AT20 = "at20"
    AT21 = "at21"
    AT22 = "at22"
    AT23 = "at23"
    AT24 = "at24"
    AT25 = "at25"
    AT26 = "at26"
    AT27 = "at27"
    AT28 = "at28"
    AT29 = "at29"
    AT30 = "at30"
    AT31 = "at31"
    AT32 = "at32"
    AT33 = "at33"
    AT34 = "at34"
    AT35 = "at35"
    AT36 = "at36"
    AT37 = "at37"
    AT38 = "at38"
    AT39 = "at39"
    AT40 = "at40"
    AT41 = "at41"
    AT42 = "at42"
    AT43 = "at43"
    AT44 = "at44"
    AT45 = "at45"
    AT46 = "at46"
    AT47 = "at47"
    AT48 = "at48"
    AT49 = "at49"
    AT50 = "at50"
    AT51 = "at51"
    AT52 = "at52"
    AT53 = "at53"
    AT54 = "at54"
    AT55 = "at55"
    AT56 = "at56"
    AT57 = "at57"
    AT58 = "at58"
    AT59 = "at59"
    AT60 = "at60"
    AT61 = "at61"
    AT62 = "at62"
    AT63 = "at63"
    AT64 = "at64"
    AT65 = "at65"
    AT66 = "at66"
    AT67 = "at67"
    AT68 = "at68"
    AT69 = "at69"
    AT70 = "at70"
    AT71 = "at71"
    AT72 = "at72"
    AT73 = "at73"
    AT74 = "at74"
    AT75 = "at75"
    AT76 = "at76"
    AT77 = "at77"
    AT78 = "at78"
    AT79 = "at79"
    AT80 = "at80"
    AT81 = "at81"
    AT82 = "at82"
    AT83 = "at83"
    AT84 = "at84"
    AT85 = "at85"
    AT86 = "at86"
    AT87 = "at87"
    AT88 = "at88"
    AT89 = "at89"
    AT90 = "at90"
    AT91 = "at91"
    AT92 = "at92"
    AT93 = "at93"
    AT94 = "at94"
    AT95 = "at95"
    AT96 = "at96"
    AT97 = "at97"
    AT98 = "at98"
    AT99 = "at99"


class ActionIdentTypeAttType(Enum):
    AI01 = "ai01"
    AI02 = "ai02"
    AI03 = "ai03"
    AI04 = "ai04"
    AI05 = "ai05"
    AI06 = "ai06"
    AI07 = "ai07"
    AI08 = "ai08"
    AI09 = "ai09"
    AI10 = "ai10"
    AI11 = "ai11"
    AI12 = "ai12"
    AI13 = "ai13"
    AI14 = "ai14"
    AI15 = "ai15"
    AI16 = "ai16"
    AI17 = "ai17"
    AI18 = "ai18"
    AI19 = "ai19"
    AI20 = "ai20"
    AI21 = "ai21"
    AI22 = "ai22"
    AI23 = "ai23"
    AI24 = "ai24"
    AI25 = "ai25"
    AI26 = "ai26"
    AI27 = "ai27"
    AI28 = "ai28"
    AI29 = "ai29"
    AI30 = "ai30"
    AI31 = "ai31"
    AI32 = "ai32"
    AI33 = "ai33"
    AI34 = "ai34"
    AI35 = "ai35"
    AI36 = "ai36"
    AI37 = "ai37"
    AI38 = "ai38"
    AI39 = "ai39"
    AI40 = "ai40"
    AI41 = "ai41"
    AI42 = "ai42"
    AI43 = "ai43"
    AI44 = "ai44"
    AI45 = "ai45"
    AI46 = "ai46"
    AI47 = "ai47"
    AI48 = "ai48"
    AI49 = "ai49"
    AI50 = "ai50"
    AI51 = "ai51"
    AI52 = "ai52"
    AI53 = "ai53"
    AI54 = "ai54"
    AI55 = "ai55"
    AI56 = "ai56"
    AI57 = "ai57"
    AI58 = "ai58"
    AI59 = "ai59"
    AI60 = "ai60"
    AI61 = "ai61"
    AI62 = "ai62"
    AI63 = "ai63"
    AI64 = "ai64"
    AI65 = "ai65"
    AI66 = "ai66"
    AI67 = "ai67"
    AI68 = "ai68"
    AI69 = "ai69"
    AI70 = "ai70"
    AI71 = "ai71"
    AI72 = "ai72"
    AI73 = "ai73"
    AI74 = "ai74"
    AI75 = "ai75"
    AI76 = "ai76"
    AI77 = "ai77"
    AI78 = "ai78"
    AI79 = "ai79"
    AI80 = "ai80"
    AI81 = "ai81"
    AI82 = "ai82"
    AI83 = "ai83"
    AI84 = "ai84"
    AI85 = "ai85"
    AI86 = "ai86"
    AI87 = "ai87"
    AI88 = "ai88"
    AI89 = "ai89"
    AI90 = "ai90"
    AI91 = "ai91"
    AI92 = "ai92"
    AI93 = "ai93"
    AI94 = "ai94"
    AI95 = "ai95"
    AI96 = "ai96"
    AI97 = "ai97"
    AI98 = "ai98"
    AI99 = "ai99"


@dataclass(kw_only=True)
class AdditionalModification:
    class Meta:
        name = "additionalModification"

    value: str = field(default="")


class AlignAttType(Enum):
    LEFT = "left"
    RIGHT = "right"
    CENTER = "center"
    JUSTIFY = "justify"
    CHAR = "char"


@dataclass(kw_only=True)
class AmperageElemType:
    class Meta:
        name = "amperageElemType"

    unit_of_measure: None | str = field(
        default=None,
        metadata={
            "name": "unitOfMeasure",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


class AndOrAttType(Enum):
    AND = "and"
    OR = "or"


class ApplicConfigurationAttType(Enum):
    ALLOWED = "allowed"
    BUILT = "built"
    DESIGNED = "designed"
    INSTALLED = "installed"
    MANUFACTURED = "manufactured"
    SUPPORTED = "supported"


class ApplicPropertyTypeAttType(Enum):
    CONDITION = "condition"
    PRODATTR = "prodattr"


@dataclass(kw_only=True)
class AuthorityInfo:
    class Meta:
        name = "authorityInfo"

    value: str = field(default="")


@dataclass(kw_only=True)
class AuthorityNotes:
    class Meta:
        name = "authorityNotes"

    value: str = field(default="")


@dataclass(kw_only=True)
class AuthorizationStatusElemType:
    class Meta:
        name = "authorizationStatusElemType"

    authorization_status_date: None | str = field(
        default=None,
        metadata={
            "name": "authorizationStatusDate",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


class BooleanActionAttType(Enum):
    DEFINED = "defined"
    NOT = "not"


class BooleanOperationAttType(Enum):
    AND = "and"
    EQUAL = "equal"
    EXCLUSIVE_OR = "exclusiveOr"
    NOT_EQUAL = "notEqual"
    OR = "or"


@dataclass(kw_only=True)
class Building:
    class Meta:
        name = "building"

    value: str = field(default="")


@dataclass(kw_only=True)
class BusinessUnitName:
    class Meta:
        name = "businessUnitName"

    value: str = field(default="")


class CaveatAttType(Enum):
    CV01 = "cv01"
    CV02 = "cv02"
    CV03 = "cv03"
    CV04 = "cv04"
    CV05 = "cv05"
    CV06 = "cv06"
    CV07 = "cv07"
    CV08 = "cv08"
    CV09 = "cv09"
    CV10 = "cv10"
    CV11 = "cv11"
    CV12 = "cv12"
    CV13 = "cv13"
    CV14 = "cv14"
    CV15 = "cv15"
    CV16 = "cv16"
    CV17 = "cv17"
    CV18 = "cv18"
    CV19 = "cv19"
    CV20 = "cv20"
    CV21 = "cv21"
    CV22 = "cv22"
    CV23 = "cv23"
    CV24 = "cv24"
    CV25 = "cv25"
    CV26 = "cv26"
    CV27 = "cv27"
    CV28 = "cv28"
    CV29 = "cv29"
    CV30 = "cv30"
    CV31 = "cv31"
    CV32 = "cv32"
    CV33 = "cv33"
    CV34 = "cv34"
    CV35 = "cv35"
    CV36 = "cv36"
    CV37 = "cv37"
    CV38 = "cv38"
    CV39 = "cv39"
    CV40 = "cv40"
    CV41 = "cv41"
    CV42 = "cv42"
    CV43 = "cv43"
    CV44 = "cv44"
    CV45 = "cv45"
    CV46 = "cv46"
    CV47 = "cv47"
    CV48 = "cv48"
    CV49 = "cv49"
    CV50 = "cv50"
    CV51 = "cv51"
    CV52 = "cv52"
    CV53 = "cv53"
    CV54 = "cv54"
    CV55 = "cv55"
    CV56 = "cv56"
    CV57 = "cv57"
    CV58 = "cv58"
    CV59 = "cv59"
    CV60 = "cv60"
    CV61 = "cv61"
    CV62 = "cv62"
    CV63 = "cv63"
    CV64 = "cv64"
    CV65 = "cv65"
    CV66 = "cv66"
    CV67 = "cv67"
    CV68 = "cv68"
    CV69 = "cv69"
    CV70 = "cv70"
    CV71 = "cv71"
    CV72 = "cv72"
    CV73 = "cv73"
    CV74 = "cv74"
    CV75 = "cv75"
    CV76 = "cv76"
    CV77 = "cv77"
    CV78 = "cv78"
    CV79 = "cv79"
    CV80 = "cv80"
    CV81 = "cv81"
    CV82 = "cv82"
    CV83 = "cv83"
    CV84 = "cv84"
    CV85 = "cv85"
    CV86 = "cv86"
    CV87 = "cv87"
    CV88 = "cv88"
    CV89 = "cv89"
    CV90 = "cv90"
    CV91 = "cv91"
    CV92 = "cv92"
    CV93 = "cv93"
    CV94 = "cv94"
    CV95 = "cv95"
    CV96 = "cv96"
    CV97 = "cv97"
    CV98 = "cv98"
    CV99 = "cv99"


class ChangeTypeAttType(Enum):
    ADD = "add"
    DELETE = "delete"
    MODIFY = "modify"


class CircuitBreakerActionAttType(Enum):
    OPEN = "open"
    CLOSE = "close"
    VERIF_OPEN = "verif-open"
    VERIF_CLOSE = "verif-close"
    OPEN_ORDER = "open-order"
    CLOSE_ORDER = "close-order"


class CircuitBreakerRefTypeAttType(Enum):
    CBR01 = "cbr01"
    CBR02 = "cbr02"
    CBR03 = "cbr03"
    CBR04 = "cbr04"
    CBR05 = "cbr05"
    CBR06 = "cbr06"
    CBR07 = "cbr07"
    CBR08 = "cbr08"
    CBR09 = "cbr09"
    CBR10 = "cbr10"
    CBR11 = "cbr11"
    CBR12 = "cbr12"
    CBR13 = "cbr13"
    CBR14 = "cbr14"
    CBR15 = "cbr15"
    CBR16 = "cbr16"
    CBR17 = "cbr17"
    CBR18 = "cbr18"
    CBR19 = "cbr19"
    CBR20 = "cbr20"
    CBR21 = "cbr21"
    CBR22 = "cbr22"
    CBR23 = "cbr23"
    CBR24 = "cbr24"
    CBR25 = "cbr25"
    CBR26 = "cbr26"
    CBR27 = "cbr27"
    CBR28 = "cbr28"
    CBR29 = "cbr29"
    CBR30 = "cbr30"
    CBR31 = "cbr31"
    CBR32 = "cbr32"
    CBR33 = "cbr33"
    CBR34 = "cbr34"
    CBR35 = "cbr35"
    CBR36 = "cbr36"
    CBR37 = "cbr37"
    CBR38 = "cbr38"
    CBR39 = "cbr39"
    CBR40 = "cbr40"
    CBR41 = "cbr41"
    CBR42 = "cbr42"
    CBR43 = "cbr43"
    CBR44 = "cbr44"
    CBR45 = "cbr45"
    CBR46 = "cbr46"
    CBR47 = "cbr47"
    CBR48 = "cbr48"
    CBR49 = "cbr49"
    CBR50 = "cbr50"
    CBR51 = "cbr51"
    CBR52 = "cbr52"
    CBR53 = "cbr53"
    CBR54 = "cbr54"
    CBR55 = "cbr55"
    CBR56 = "cbr56"
    CBR57 = "cbr57"
    CBR58 = "cbr58"
    CBR59 = "cbr59"
    CBR60 = "cbr60"
    CBR61 = "cbr61"
    CBR62 = "cbr62"
    CBR63 = "cbr63"
    CBR64 = "cbr64"
    CBR65 = "cbr65"
    CBR66 = "cbr66"
    CBR67 = "cbr67"
    CBR68 = "cbr68"
    CBR69 = "cbr69"
    CBR70 = "cbr70"
    CBR71 = "cbr71"
    CBR72 = "cbr72"
    CBR73 = "cbr73"
    CBR74 = "cbr74"
    CBR75 = "cbr75"
    CBR76 = "cbr76"
    CBR77 = "cbr77"
    CBR78 = "cbr78"
    CBR79 = "cbr79"
    CBR80 = "cbr80"
    CBR81 = "cbr81"
    CBR82 = "cbr82"
    CBR83 = "cbr83"
    CBR84 = "cbr84"
    CBR85 = "cbr85"
    CBR86 = "cbr86"
    CBR87 = "cbr87"
    CBR88 = "cbr88"
    CBR89 = "cbr89"
    CBR90 = "cbr90"
    CBR91 = "cbr91"
    CBR92 = "cbr92"
    CBR93 = "cbr93"
    CBR94 = "cbr94"
    CBR95 = "cbr95"
    CBR96 = "cbr96"
    CBR97 = "cbr97"
    CBR98 = "cbr98"
    CBR99 = "cbr99"


class CircuitBreakerTypeAttType(Enum):
    CBT01 = "cbt01"
    CBT02 = "cbt02"
    CBT03 = "cbt03"
    CBT04 = "cbt04"
    CBT05 = "cbt05"
    CBT06 = "cbt06"
    CBT07 = "cbt07"
    CBT08 = "cbt08"
    CBT09 = "cbt09"
    CBT10 = "cbt10"
    CBT11 = "cbt11"
    CBT12 = "cbt12"
    CBT13 = "cbt13"
    CBT14 = "cbt14"
    CBT15 = "cbt15"
    CBT16 = "cbt16"
    CBT17 = "cbt17"
    CBT18 = "cbt18"
    CBT19 = "cbt19"
    CBT20 = "cbt20"
    CBT21 = "cbt21"
    CBT22 = "cbt22"
    CBT23 = "cbt23"
    CBT24 = "cbt24"
    CBT25 = "cbt25"
    CBT26 = "cbt26"
    CBT27 = "cbt27"
    CBT28 = "cbt28"
    CBT29 = "cbt29"
    CBT30 = "cbt30"
    CBT31 = "cbt31"
    CBT32 = "cbt32"
    CBT33 = "cbt33"
    CBT34 = "cbt34"
    CBT35 = "cbt35"
    CBT36 = "cbt36"
    CBT37 = "cbt37"
    CBT38 = "cbt38"
    CBT39 = "cbt39"
    CBT40 = "cbt40"
    CBT41 = "cbt41"
    CBT42 = "cbt42"
    CBT43 = "cbt43"
    CBT44 = "cbt44"
    CBT45 = "cbt45"
    CBT46 = "cbt46"
    CBT47 = "cbt47"
    CBT48 = "cbt48"
    CBT49 = "cbt49"
    CBT50 = "cbt50"
    CBT51 = "cbt51"
    CBT52 = "cbt52"
    CBT53 = "cbt53"
    CBT54 = "cbt54"
    CBT55 = "cbt55"
    CBT56 = "cbt56"
    CBT57 = "cbt57"
    CBT58 = "cbt58"
    CBT59 = "cbt59"
    CBT60 = "cbt60"
    CBT61 = "cbt61"
    CBT62 = "cbt62"
    CBT63 = "cbt63"
    CBT64 = "cbt64"
    CBT65 = "cbt65"
    CBT66 = "cbt66"
    CBT67 = "cbt67"
    CBT68 = "cbt68"
    CBT69 = "cbt69"
    CBT70 = "cbt70"
    CBT71 = "cbt71"
    CBT72 = "cbt72"
    CBT73 = "cbt73"
    CBT74 = "cbt74"
    CBT75 = "cbt75"
    CBT76 = "cbt76"
    CBT77 = "cbt77"
    CBT78 = "cbt78"
    CBT79 = "cbt79"
    CBT80 = "cbt80"
    CBT81 = "cbt81"
    CBT82 = "cbt82"
    CBT83 = "cbt83"
    CBT84 = "cbt84"
    CBT85 = "cbt85"
    CBT86 = "cbt86"
    CBT87 = "cbt87"
    CBT88 = "cbt88"
    CBT89 = "cbt89"
    CBT90 = "cbt90"
    CBT91 = "cbt91"
    CBT92 = "cbt92"
    CBT93 = "cbt93"
    CBT94 = "cbt94"
    CBT95 = "cbt95"
    CBT96 = "cbt96"
    CBT97 = "cbt97"
    CBT98 = "cbt98"
    CBT99 = "cbt99"


@dataclass(kw_only=True)
class City:
    class Meta:
        name = "city"

    value: str = field(default="")


class CommercialClassificationAttType(Enum):
    CC01 = "cc01"
    CC02 = "cc02"
    CC03 = "cc03"
    CC04 = "cc04"
    CC05 = "cc05"
    CC06 = "cc06"
    CC07 = "cc07"
    CC08 = "cc08"
    CC09 = "cc09"
    CC10 = "cc10"
    CC11 = "cc11"
    CC12 = "cc12"
    CC13 = "cc13"
    CC14 = "cc14"
    CC15 = "cc15"
    CC16 = "cc16"
    CC17 = "cc17"
    CC18 = "cc18"
    CC19 = "cc19"
    CC20 = "cc20"
    CC21 = "cc21"
    CC22 = "cc22"
    CC23 = "cc23"
    CC24 = "cc24"
    CC25 = "cc25"
    CC26 = "cc26"
    CC27 = "cc27"
    CC28 = "cc28"
    CC29 = "cc29"
    CC30 = "cc30"
    CC31 = "cc31"
    CC32 = "cc32"
    CC33 = "cc33"
    CC34 = "cc34"
    CC35 = "cc35"
    CC36 = "cc36"
    CC37 = "cc37"
    CC38 = "cc38"
    CC39 = "cc39"
    CC40 = "cc40"
    CC41 = "cc41"
    CC42 = "cc42"
    CC43 = "cc43"
    CC44 = "cc44"
    CC45 = "cc45"
    CC46 = "cc46"
    CC47 = "cc47"
    CC48 = "cc48"
    CC49 = "cc49"
    CC50 = "cc50"
    CC51 = "cc51"
    CC52 = "cc52"
    CC53 = "cc53"
    CC54 = "cc54"
    CC55 = "cc55"
    CC56 = "cc56"
    CC57 = "cc57"
    CC58 = "cc58"
    CC59 = "cc59"
    CC60 = "cc60"
    CC61 = "cc61"
    CC62 = "cc62"
    CC63 = "cc63"
    CC64 = "cc64"
    CC65 = "cc65"
    CC66 = "cc66"
    CC67 = "cc67"
    CC68 = "cc68"
    CC69 = "cc69"
    CC70 = "cc70"
    CC71 = "cc71"
    CC72 = "cc72"
    CC73 = "cc73"
    CC74 = "cc74"
    CC75 = "cc75"
    CC76 = "cc76"
    CC77 = "cc77"
    CC78 = "cc78"
    CC79 = "cc79"
    CC80 = "cc80"
    CC81 = "cc81"
    CC82 = "cc82"
    CC83 = "cc83"
    CC84 = "cc84"
    CC85 = "cc85"
    CC86 = "cc86"
    CC87 = "cc87"
    CC88 = "cc88"
    CC89 = "cc89"
    CC90 = "cc90"
    CC91 = "cc91"
    CC92 = "cc92"
    CC93 = "cc93"
    CC94 = "cc94"
    CC95 = "cc95"
    CC96 = "cc96"
    CC97 = "cc97"
    CC98 = "cc98"
    CC99 = "cc99"


class ComplianceCategoryValueAttType(Enum):
    A = "A"
    B = "B"
    C = "C"


class ControlAuthorityTypeAttType(Enum):
    CAT01 = "cat01"
    CAT02 = "cat02"
    CAT03 = "cat03"
    CAT04 = "cat04"
    CAT05 = "cat05"
    CAT06 = "cat06"
    CAT07 = "cat07"
    CAT08 = "cat08"
    CAT09 = "cat09"
    CAT10 = "cat10"
    CAT11 = "cat11"
    CAT12 = "cat12"
    CAT13 = "cat13"
    CAT14 = "cat14"
    CAT15 = "cat15"
    CAT16 = "cat16"
    CAT17 = "cat17"
    CAT18 = "cat18"
    CAT19 = "cat19"
    CAT20 = "cat20"
    CAT21 = "cat21"
    CAT22 = "cat22"
    CAT23 = "cat23"
    CAT24 = "cat24"
    CAT25 = "cat25"
    CAT26 = "cat26"
    CAT27 = "cat27"
    CAT28 = "cat28"
    CAT29 = "cat29"
    CAT30 = "cat30"
    CAT31 = "cat31"
    CAT32 = "cat32"
    CAT33 = "cat33"
    CAT34 = "cat34"
    CAT35 = "cat35"
    CAT36 = "cat36"
    CAT37 = "cat37"
    CAT38 = "cat38"
    CAT39 = "cat39"
    CAT40 = "cat40"
    CAT41 = "cat41"
    CAT42 = "cat42"
    CAT43 = "cat43"
    CAT44 = "cat44"
    CAT45 = "cat45"
    CAT46 = "cat46"
    CAT47 = "cat47"
    CAT48 = "cat48"
    CAT49 = "cat49"
    CAT50 = "cat50"
    CAT51 = "cat51"
    CAT52 = "cat52"
    CAT53 = "cat53"
    CAT54 = "cat54"
    CAT55 = "cat55"
    CAT56 = "cat56"
    CAT57 = "cat57"
    CAT58 = "cat58"
    CAT59 = "cat59"
    CAT60 = "cat60"
    CAT61 = "cat61"
    CAT62 = "cat62"
    CAT63 = "cat63"
    CAT64 = "cat64"
    CAT65 = "cat65"
    CAT66 = "cat66"
    CAT67 = "cat67"
    CAT68 = "cat68"
    CAT69 = "cat69"
    CAT70 = "cat70"
    CAT71 = "cat71"
    CAT72 = "cat72"
    CAT73 = "cat73"
    CAT74 = "cat74"
    CAT75 = "cat75"
    CAT76 = "cat76"
    CAT77 = "cat77"
    CAT78 = "cat78"
    CAT79 = "cat79"
    CAT80 = "cat80"
    CAT81 = "cat81"
    CAT82 = "cat82"
    CAT83 = "cat83"
    CAT84 = "cat84"
    CAT85 = "cat85"
    CAT86 = "cat86"
    CAT87 = "cat87"
    CAT88 = "cat88"
    CAT89 = "cat89"
    CAT90 = "cat90"
    CAT91 = "cat91"
    CAT92 = "cat92"
    CAT93 = "cat93"
    CAT94 = "cat94"
    CAT95 = "cat95"
    CAT96 = "cat96"
    CAT97 = "cat97"
    CAT98 = "cat98"
    CAT99 = "cat99"


@dataclass(kw_only=True)
class Country:
    class Meta:
        name = "country"

    value: str = field(default="")


@dataclass(kw_only=True)
class Department:
    class Meta:
        name = "department"

    value: str = field(default="")


@dataclass(kw_only=True)
class DerivativeSource:
    class Meta:
        name = "derivativeSource"

    value: str = field(default="")


@dataclass(kw_only=True)
class EmailElemType:
    class Meta:
        name = "emailElemType"

    contact_role: None | str = field(
        default=None,
        metadata={
            "name": "contactRole",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


class EmphasisTypeAttType(Enum):
    EM01 = "em01"
    EM02 = "em02"
    EM03 = "em03"
    EM04 = "em04"
    EM05 = "em05"
    EM06 = "em06"
    EM07 = "em07"
    EM08 = "em08"
    EM09 = "em09"
    EM10 = "em10"
    EM11 = "em11"
    EM12 = "em12"
    EM13 = "em13"
    EM14 = "em14"
    EM15 = "em15"
    EM16 = "em16"
    EM17 = "em17"
    EM18 = "em18"
    EM19 = "em19"
    EM20 = "em20"
    EM21 = "em21"
    EM22 = "em22"
    EM23 = "em23"
    EM24 = "em24"
    EM25 = "em25"
    EM26 = "em26"
    EM27 = "em27"
    EM28 = "em28"
    EM29 = "em29"
    EM30 = "em30"
    EM31 = "em31"
    EM32 = "em32"
    EM33 = "em33"
    EM34 = "em34"
    EM35 = "em35"
    EM36 = "em36"
    EM37 = "em37"
    EM38 = "em38"
    EM39 = "em39"
    EM40 = "em40"
    EM41 = "em41"
    EM42 = "em42"
    EM43 = "em43"
    EM44 = "em44"
    EM45 = "em45"
    EM46 = "em46"
    EM47 = "em47"
    EM48 = "em48"
    EM49 = "em49"
    EM50 = "em50"
    EM51 = "em51"
    EM52 = "em52"
    EM53 = "em53"
    EM54 = "em54"
    EM55 = "em55"
    EM56 = "em56"
    EM57 = "em57"
    EM58 = "em58"
    EM59 = "em59"
    EM60 = "em60"
    EM61 = "em61"
    EM62 = "em62"
    EM63 = "em63"
    EM64 = "em64"
    EM65 = "em65"
    EM66 = "em66"
    EM67 = "em67"
    EM68 = "em68"
    EM69 = "em69"
    EM70 = "em70"
    EM71 = "em71"
    EM72 = "em72"
    EM73 = "em73"
    EM74 = "em74"
    EM75 = "em75"
    EM76 = "em76"
    EM77 = "em77"
    EM78 = "em78"
    EM79 = "em79"
    EM80 = "em80"
    EM81 = "em81"
    EM82 = "em82"
    EM83 = "em83"
    EM84 = "em84"
    EM85 = "em85"
    EM86 = "em86"
    EM87 = "em87"
    EM88 = "em88"
    EM89 = "em89"
    EM90 = "em90"
    EM91 = "em91"
    EM92 = "em92"
    EM93 = "em93"
    EM94 = "em94"
    EM95 = "em95"
    EM96 = "em96"
    EM97 = "em97"
    EM98 = "em98"
    EM99 = "em99"


@dataclass(kw_only=True)
class EmptyElemType:
    class Meta:
        name = "emptyElemType"


@dataclass(kw_only=True)
class EnterpriseIdentAltElemType:
    class Meta:
        name = "enterpriseIdentAltElemType"

    alt_code: str = field(
        metadata={
            "name": "altCode",
            "type": "Attribute",
        }
    )
    alt_code_type: str = field(
        metadata={
            "name": "altCodeType",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class EnterpriseName:
    class Meta:
        name = "enterpriseName"

    value: str = field(default="")


@dataclass(kw_only=True)
class ExcludedModification:
    class Meta:
        name = "excludedModification"

    value: str = field(default="")


@dataclass(kw_only=True)
class ExportRegistrationCodeElemType:
    class Meta:
        name = "exportRegistrationCodeElemType"

    export_regulation_code_type: None | str = field(
        default=None,
        metadata={
            "name": "exportRegulationCodeType",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


class ExportRoleAttType(Enum):
    PARTIAL = "partial"
    FULL = "full"


@dataclass(kw_only=True)
class ExternalPubIssueDateElemType:
    class Meta:
        name = "externalPubIssueDateElemType"

    year: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d{4}",
        },
    )
    month: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_inclusive": "12",
            "pattern": r"\d{2}",
        },
    )
    day: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_inclusive": "31",
            "pattern": r"\d{2}",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FaxNumberElemType:
    class Meta:
        name = "faxNumberElemType"

    contact_role: None | str = field(
        default=None,
        metadata={
            "name": "contactRole",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FirstName:
    class Meta:
        name = "firstName"

    value: str = field(default="")


class FitmentCodeValueAttType(Enum):
    VALUE_1 = "1"
    M = "m"


class FrameAttType(Enum):
    TOP = "top"
    BOTTOM = "bottom"
    TOPBOT = "topbot"
    ALL = "all"
    SIDES = "sides"
    NONE = "none"


@dataclass(kw_only=True)
class FullNatoStockNumber:
    class Meta:
        name = "fullNatoStockNumber"

    value: str = field(default="")


@dataclass(kw_only=True)
class FunctionalItemCode:
    class Meta:
        name = "functionalItemCode"

    value: str = field(default="")


class FunctionalItemRefTypeAttType(Enum):
    FIR01 = "fir01"
    FIR02 = "fir02"
    FIR03 = "fir03"
    FIR04 = "fir04"
    FIR05 = "fir05"
    FIR06 = "fir06"
    FIR07 = "fir07"
    FIR08 = "fir08"
    FIR09 = "fir09"
    FIR10 = "fir10"
    FIR11 = "fir11"
    FIR12 = "fir12"
    FIR13 = "fir13"
    FIR14 = "fir14"
    FIR15 = "fir15"
    FIR16 = "fir16"
    FIR17 = "fir17"
    FIR18 = "fir18"
    FIR19 = "fir19"
    FIR20 = "fir20"
    FIR21 = "fir21"
    FIR22 = "fir22"
    FIR23 = "fir23"
    FIR24 = "fir24"
    FIR25 = "fir25"
    FIR26 = "fir26"
    FIR27 = "fir27"
    FIR28 = "fir28"
    FIR29 = "fir29"
    FIR30 = "fir30"
    FIR31 = "fir31"
    FIR32 = "fir32"
    FIR33 = "fir33"
    FIR34 = "fir34"
    FIR35 = "fir35"
    FIR36 = "fir36"
    FIR37 = "fir37"
    FIR38 = "fir38"
    FIR39 = "fir39"
    FIR40 = "fir40"
    FIR41 = "fir41"
    FIR42 = "fir42"
    FIR43 = "fir43"
    FIR44 = "fir44"
    FIR45 = "fir45"
    FIR46 = "fir46"
    FIR47 = "fir47"
    FIR48 = "fir48"
    FIR49 = "fir49"
    FIR50 = "fir50"
    FIR51 = "fir51"
    FIR52 = "fir52"
    FIR53 = "fir53"
    FIR54 = "fir54"
    FIR55 = "fir55"
    FIR56 = "fir56"
    FIR57 = "fir57"
    FIR58 = "fir58"
    FIR59 = "fir59"
    FIR60 = "fir60"
    FIR61 = "fir61"
    FIR62 = "fir62"
    FIR63 = "fir63"
    FIR64 = "fir64"
    FIR65 = "fir65"
    FIR66 = "fir66"
    FIR67 = "fir67"
    FIR68 = "fir68"
    FIR69 = "fir69"
    FIR70 = "fir70"
    FIR71 = "fir71"
    FIR72 = "fir72"
    FIR73 = "fir73"
    FIR74 = "fir74"
    FIR75 = "fir75"
    FIR76 = "fir76"
    FIR77 = "fir77"
    FIR78 = "fir78"
    FIR79 = "fir79"
    FIR80 = "fir80"
    FIR81 = "fir81"
    FIR82 = "fir82"
    FIR83 = "fir83"
    FIR84 = "fir84"
    FIR85 = "fir85"
    FIR86 = "fir86"
    FIR87 = "fir87"
    FIR88 = "fir88"
    FIR89 = "fir89"
    FIR90 = "fir90"
    FIR91 = "fir91"
    FIR92 = "fir92"
    FIR93 = "fir93"
    FIR94 = "fir94"
    FIR95 = "fir95"
    FIR96 = "fir96"
    FIR97 = "fir97"
    FIR98 = "fir98"
    FIR99 = "fir99"


class FunctionalItemTypeAttType(Enum):
    FIT01 = "fit01"
    FIT02 = "fit02"
    FIT03 = "fit03"
    FIT04 = "fit04"
    FIT05 = "fit05"
    FIT06 = "fit06"
    FIT07 = "fit07"
    FIT08 = "fit08"
    FIT09 = "fit09"
    FIT10 = "fit10"
    FIT11 = "fit11"
    FIT12 = "fit12"
    FIT13 = "fit13"
    FIT14 = "fit14"
    FIT15 = "fit15"
    FIT16 = "fit16"
    FIT17 = "fit17"
    FIT18 = "fit18"
    FIT19 = "fit19"
    FIT20 = "fit20"
    FIT21 = "fit21"
    FIT22 = "fit22"
    FIT23 = "fit23"
    FIT24 = "fit24"
    FIT25 = "fit25"
    FIT26 = "fit26"
    FIT27 = "fit27"
    FIT28 = "fit28"
    FIT29 = "fit29"
    FIT30 = "fit30"
    FIT31 = "fit31"
    FIT32 = "fit32"
    FIT33 = "fit33"
    FIT34 = "fit34"
    FIT35 = "fit35"
    FIT36 = "fit36"
    FIT37 = "fit37"
    FIT38 = "fit38"
    FIT39 = "fit39"
    FIT40 = "fit40"
    FIT41 = "fit41"
    FIT42 = "fit42"
    FIT43 = "fit43"
    FIT44 = "fit44"
    FIT45 = "fit45"
    FIT46 = "fit46"
    FIT47 = "fit47"
    FIT48 = "fit48"
    FIT49 = "fit49"
    FIT50 = "fit50"
    FIT51 = "fit51"
    FIT52 = "fit52"
    FIT53 = "fit53"
    FIT54 = "fit54"
    FIT55 = "fit55"
    FIT56 = "fit56"
    FIT57 = "fit57"
    FIT58 = "fit58"
    FIT59 = "fit59"
    FIT60 = "fit60"
    FIT61 = "fit61"
    FIT62 = "fit62"
    FIT63 = "fit63"
    FIT64 = "fit64"
    FIT65 = "fit65"
    FIT66 = "fit66"
    FIT67 = "fit67"
    FIT68 = "fit68"
    FIT69 = "fit69"
    FIT70 = "fit70"
    FIT71 = "fit71"
    FIT72 = "fit72"
    FIT73 = "fit73"
    FIT74 = "fit74"
    FIT75 = "fit75"
    FIT76 = "fit76"
    FIT77 = "fit77"
    FIT78 = "fit78"
    FIT79 = "fit79"
    FIT80 = "fit80"
    FIT81 = "fit81"
    FIT82 = "fit82"
    FIT83 = "fit83"
    FIT84 = "fit84"
    FIT85 = "fit85"
    FIT86 = "fit86"
    FIT87 = "fit87"
    FIT88 = "fit88"
    FIT89 = "fit89"
    FIT90 = "fit90"
    FIT91 = "fit91"
    FIT92 = "fit92"
    FIT93 = "fit93"
    FIT94 = "fit94"
    FIT95 = "fit95"
    FIT96 = "fit96"
    FIT97 = "fit97"
    FIT98 = "fit98"
    FIT99 = "fit99"


@dataclass(kw_only=True)
class FunctionalPhysicalAreaIdentElemType:
    class Meta:
        name = "functionalPhysicalAreaIdentElemType"

    system_diff_code: None | str = field(
        default=None,
        metadata={
            "name": "systemDiffCode",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{1,4}",
        },
    )
    system_code: str = field(
        metadata={
            "name": "systemCode",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{2,3}",
        }
    )
    sub_system_code: None | str = field(
        default=None,
        metadata={
            "name": "subSystemCode",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{1}",
        },
    )
    sub_sub_system_code: None | str = field(
        default=None,
        metadata={
            "name": "subSubSystemCode",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{1}",
        },
    )
    assy_code: None | str = field(
        default=None,
        metadata={
            "name": "assyCode",
            "type": "Attribute",
            "pattern": r"([A-Z0-9]{2}|[A-Z0-9]{4})",
        },
    )
    disassy_code: None | str = field(
        default=None,
        metadata={
            "name": "disassyCode",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{2}",
        },
    )
    disassy_code_variant: None | str = field(
        default=None,
        metadata={
            "name": "disassyCodeVariant",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{1,3}",
        },
    )


class HazardousClassValueAttType(Enum):
    HZ01 = "hz01"
    HZ02 = "hz02"
    HZ03 = "hz03"
    HZ04 = "hz04"
    HZ05 = "hz05"
    HZ06 = "hz06"
    HZ07 = "hz07"
    HZ08 = "hz08"
    HZ09 = "hz09"
    HZ10 = "hz10"
    HZ11 = "hz11"
    HZ12 = "hz12"
    HZ13 = "hz13"
    HZ14 = "hz14"
    HZ15 = "hz15"
    HZ16 = "hz16"
    HZ17 = "hz17"
    HZ18 = "hz18"
    HZ19 = "hz19"
    HZ20 = "hz20"
    HZ21 = "hz21"
    HZ22 = "hz22"
    HZ23 = "hz23"
    HZ24 = "hz24"
    HZ25 = "hz25"
    HZ26 = "hz26"
    HZ27 = "hz27"
    HZ28 = "hz28"
    HZ29 = "hz29"
    HZ30 = "hz30"
    HZ31 = "hz31"
    HZ32 = "hz32"
    HZ33 = "hz33"
    HZ34 = "hz34"
    HZ35 = "hz35"
    HZ36 = "hz36"
    HZ37 = "hz37"
    HZ38 = "hz38"
    HZ39 = "hz39"
    HZ40 = "hz40"
    HZ41 = "hz41"
    HZ42 = "hz42"
    HZ43 = "hz43"
    HZ44 = "hz44"
    HZ45 = "hz45"
    HZ46 = "hz46"
    HZ47 = "hz47"
    HZ48 = "hz48"
    HZ49 = "hz49"
    HZ50 = "hz50"
    HZ51 = "hz51"
    HZ52 = "hz52"
    HZ53 = "hz53"
    HZ54 = "hz54"
    HZ55 = "hz55"
    HZ56 = "hz56"
    HZ57 = "hz57"
    HZ58 = "hz58"
    HZ59 = "hz59"
    HZ60 = "hz60"
    HZ61 = "hz61"
    HZ62 = "hz62"
    HZ63 = "hz63"
    HZ64 = "hz64"
    HZ65 = "hz65"
    HZ66 = "hz66"
    HZ67 = "hz67"
    HZ68 = "hz68"
    HZ69 = "hz69"
    HZ70 = "hz70"
    HZ71 = "hz71"
    HZ72 = "hz72"
    HZ73 = "hz73"
    HZ74 = "hz74"
    HZ75 = "hz75"
    HZ76 = "hz76"
    HZ77 = "hz77"
    HZ78 = "hz78"
    HZ79 = "hz79"
    HZ80 = "hz80"
    HZ81 = "hz81"
    HZ82 = "hz82"
    HZ83 = "hz83"
    HZ84 = "hz84"
    HZ85 = "hz85"
    HZ86 = "hz86"
    HZ87 = "hz87"
    HZ88 = "hz88"
    HZ89 = "hz89"
    HZ90 = "hz90"
    HZ91 = "hz91"
    HZ92 = "hz92"
    HZ93 = "hz93"
    HZ94 = "hz94"
    HZ95 = "hz95"
    HZ96 = "hz96"
    HZ97 = "hz97"
    HZ98 = "hz98"
    HZ99 = "hz99"


@dataclass(kw_only=True)
class IdentExtensionElemType:
    class Meta:
        name = "identExtensionElemType"

    extension_producer: str = field(
        metadata={
            "name": "extensionProducer",
            "type": "Attribute",
        }
    )
    extension_code: str = field(
        metadata={
            "name": "extensionCode",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class IndexFlagElemType:
    class Meta:
        name = "indexFlagElemType"

    index_level_one: None | str = field(
        default=None,
        metadata={
            "name": "indexLevelOne",
            "type": "Attribute",
        },
    )
    index_level_two: None | str = field(
        default=None,
        metadata={
            "name": "indexLevelTwo",
            "type": "Attribute",
        },
    )
    index_level_three: None | str = field(
        default=None,
        metadata={
            "name": "indexLevelThree",
            "type": "Attribute",
        },
    )
    index_level_four: None | str = field(
        default=None,
        metadata={
            "name": "indexLevelFour",
            "type": "Attribute",
        },
    )


class InstallationLocationTypeAttType(Enum):
    INSTLOCTYP01 = "instloctyp01"
    INSTLOCTYP02 = "instloctyp02"
    INSTLOCTYP03 = "instloctyp03"
    INSTLOCTYP04 = "instloctyp04"
    INSTLOCTYP05 = "instloctyp05"
    INSTLOCTYP06 = "instloctyp06"
    INSTLOCTYP07 = "instloctyp07"
    INSTLOCTYP08 = "instloctyp08"
    INSTLOCTYP09 = "instloctyp09"
    INSTLOCTYP10 = "instloctyp10"
    INSTLOCTYP11 = "instloctyp11"
    INSTLOCTYP12 = "instloctyp12"
    INSTLOCTYP13 = "instloctyp13"
    INSTLOCTYP14 = "instloctyp14"
    INSTLOCTYP15 = "instloctyp15"
    INSTLOCTYP16 = "instloctyp16"
    INSTLOCTYP17 = "instloctyp17"
    INSTLOCTYP18 = "instloctyp18"
    INSTLOCTYP19 = "instloctyp19"
    INSTLOCTYP20 = "instloctyp20"
    INSTLOCTYP21 = "instloctyp21"
    INSTLOCTYP22 = "instloctyp22"
    INSTLOCTYP23 = "instloctyp23"
    INSTLOCTYP24 = "instloctyp24"
    INSTLOCTYP25 = "instloctyp25"
    INSTLOCTYP26 = "instloctyp26"
    INSTLOCTYP27 = "instloctyp27"
    INSTLOCTYP28 = "instloctyp28"
    INSTLOCTYP29 = "instloctyp29"
    INSTLOCTYP30 = "instloctyp30"
    INSTLOCTYP31 = "instloctyp31"
    INSTLOCTYP32 = "instloctyp32"
    INSTLOCTYP33 = "instloctyp33"
    INSTLOCTYP34 = "instloctyp34"
    INSTLOCTYP35 = "instloctyp35"
    INSTLOCTYP36 = "instloctyp36"
    INSTLOCTYP37 = "instloctyp37"
    INSTLOCTYP38 = "instloctyp38"
    INSTLOCTYP39 = "instloctyp39"
    INSTLOCTYP40 = "instloctyp40"
    INSTLOCTYP41 = "instloctyp41"
    INSTLOCTYP42 = "instloctyp42"
    INSTLOCTYP43 = "instloctyp43"
    INSTLOCTYP44 = "instloctyp44"
    INSTLOCTYP45 = "instloctyp45"
    INSTLOCTYP46 = "instloctyp46"
    INSTLOCTYP47 = "instloctyp47"
    INSTLOCTYP48 = "instloctyp48"
    INSTLOCTYP49 = "instloctyp49"
    INSTLOCTYP50 = "instloctyp50"
    INSTLOCTYP51 = "instloctyp51"
    INSTLOCTYP52 = "instloctyp52"
    INSTLOCTYP53 = "instloctyp53"
    INSTLOCTYP54 = "instloctyp54"
    INSTLOCTYP55 = "instloctyp55"
    INSTLOCTYP56 = "instloctyp56"
    INSTLOCTYP57 = "instloctyp57"
    INSTLOCTYP58 = "instloctyp58"
    INSTLOCTYP59 = "instloctyp59"
    INSTLOCTYP60 = "instloctyp60"
    INSTLOCTYP61 = "instloctyp61"
    INSTLOCTYP62 = "instloctyp62"
    INSTLOCTYP63 = "instloctyp63"
    INSTLOCTYP64 = "instloctyp64"
    INSTLOCTYP65 = "instloctyp65"
    INSTLOCTYP66 = "instloctyp66"
    INSTLOCTYP67 = "instloctyp67"
    INSTLOCTYP68 = "instloctyp68"
    INSTLOCTYP69 = "instloctyp69"
    INSTLOCTYP70 = "instloctyp70"
    INSTLOCTYP71 = "instloctyp71"
    INSTLOCTYP72 = "instloctyp72"
    INSTLOCTYP73 = "instloctyp73"
    INSTLOCTYP74 = "instloctyp74"
    INSTLOCTYP75 = "instloctyp75"
    INSTLOCTYP76 = "instloctyp76"
    INSTLOCTYP77 = "instloctyp77"
    INSTLOCTYP78 = "instloctyp78"
    INSTLOCTYP79 = "instloctyp79"
    INSTLOCTYP80 = "instloctyp80"
    INSTLOCTYP81 = "instloctyp81"
    INSTLOCTYP82 = "instloctyp82"
    INSTLOCTYP83 = "instloctyp83"
    INSTLOCTYP84 = "instloctyp84"
    INSTLOCTYP85 = "instloctyp85"
    INSTLOCTYP86 = "instloctyp86"
    INSTLOCTYP87 = "instloctyp87"
    INSTLOCTYP88 = "instloctyp88"
    INSTLOCTYP89 = "instloctyp89"
    INSTLOCTYP90 = "instloctyp90"
    INSTLOCTYP91 = "instloctyp91"
    INSTLOCTYP92 = "instloctyp92"
    INSTLOCTYP93 = "instloctyp93"
    INSTLOCTYP94 = "instloctyp94"
    INSTLOCTYP95 = "instloctyp95"
    INSTLOCTYP96 = "instloctyp96"
    INSTLOCTYP97 = "instloctyp97"
    INSTLOCTYP98 = "instloctyp98"
    INSTLOCTYP99 = "instloctyp99"


@dataclass(kw_only=True)
class IntegerValue:
    class Meta:
        name = "integerValue"

    value: str = field(default="")


class InternalRefTargetTypeAttType(Enum):
    IRTT01 = "irtt01"
    IRTT02 = "irtt02"
    IRTT03 = "irtt03"
    IRTT04 = "irtt04"
    IRTT05 = "irtt05"
    IRTT06 = "irtt06"
    IRTT07 = "irtt07"
    IRTT08 = "irtt08"
    IRTT09 = "irtt09"
    IRTT10 = "irtt10"
    IRTT11 = "irtt11"
    IRTT12 = "irtt12"
    IRTT13 = "irtt13"
    IRTT14 = "irtt14"
    IRTT15 = "irtt15"
    IRTT16 = "irtt16"
    IRTT17 = "irtt17"
    IRTT18 = "irtt18"
    IRTT19 = "irtt19"
    IRTT20 = "irtt20"
    IRTT21 = "irtt21"
    IRTT22 = "irtt22"
    IRTT23 = "irtt23"
    IRTT24 = "irtt24"
    IRTT25 = "irtt25"
    IRTT26 = "irtt26"
    IRTT27 = "irtt27"
    IRTT28 = "irtt28"
    IRTT29 = "irtt29"
    IRTT30 = "irtt30"
    IRTT31 = "irtt31"
    IRTT32 = "irtt32"
    IRTT33 = "irtt33"
    IRTT34 = "irtt34"
    IRTT35 = "irtt35"
    IRTT36 = "irtt36"
    IRTT37 = "irtt37"
    IRTT38 = "irtt38"
    IRTT39 = "irtt39"
    IRTT40 = "irtt40"
    IRTT41 = "irtt41"
    IRTT42 = "irtt42"
    IRTT43 = "irtt43"
    IRTT44 = "irtt44"
    IRTT45 = "irtt45"
    IRTT46 = "irtt46"
    IRTT47 = "irtt47"
    IRTT48 = "irtt48"
    IRTT49 = "irtt49"
    IRTT50 = "irtt50"
    IRTT51 = "irtt51"
    IRTT52 = "irtt52"
    IRTT53 = "irtt53"
    IRTT54 = "irtt54"
    IRTT55 = "irtt55"
    IRTT56 = "irtt56"
    IRTT57 = "irtt57"
    IRTT58 = "irtt58"
    IRTT59 = "irtt59"
    IRTT60 = "irtt60"
    IRTT61 = "irtt61"
    IRTT62 = "irtt62"
    IRTT63 = "irtt63"
    IRTT64 = "irtt64"
    IRTT65 = "irtt65"
    IRTT66 = "irtt66"
    IRTT67 = "irtt67"
    IRTT68 = "irtt68"
    IRTT69 = "irtt69"
    IRTT70 = "irtt70"
    IRTT71 = "irtt71"
    IRTT72 = "irtt72"
    IRTT73 = "irtt73"
    IRTT74 = "irtt74"
    IRTT75 = "irtt75"
    IRTT76 = "irtt76"
    IRTT77 = "irtt77"
    IRTT78 = "irtt78"
    IRTT79 = "irtt79"
    IRTT80 = "irtt80"
    IRTT81 = "irtt81"
    IRTT82 = "irtt82"
    IRTT83 = "irtt83"
    IRTT84 = "irtt84"
    IRTT85 = "irtt85"
    IRTT86 = "irtt86"
    IRTT87 = "irtt87"
    IRTT88 = "irtt88"
    IRTT89 = "irtt89"
    IRTT90 = "irtt90"
    IRTT91 = "irtt91"
    IRTT92 = "irtt92"
    IRTT93 = "irtt93"
    IRTT94 = "irtt94"
    IRTT95 = "irtt95"
    IRTT96 = "irtt96"
    IRTT97 = "irtt97"
    IRTT98 = "irtt98"
    IRTT99 = "irtt99"


@dataclass(kw_only=True)
class InternetElemType:
    class Meta:
        name = "internetElemType"

    contact_role: None | str = field(
        default=None,
        metadata={
            "name": "contactRole",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class IssueDateElemType:
    class Meta:
        name = "issueDateElemType"

    year: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"\d{4}",
        }
    )
    month: str = field(
        metadata={
            "type": "Attribute",
            "max_inclusive": "12",
            "pattern": r"\d{2}",
        }
    )
    day: str = field(
        metadata={
            "type": "Attribute",
            "max_inclusive": "31",
            "pattern": r"\d{2}",
        }
    )


@dataclass(kw_only=True)
class IssueInfoGenericElemType:
    class Meta:
        name = "issueInfoGenericElemType"

    issue_number: str = field(
        metadata={
            "name": "issueNumber",
            "type": "Attribute",
            "pattern": r"\d{3,5}",
        }
    )
    in_work: str = field(
        metadata={
            "name": "inWork",
            "type": "Attribute",
            "pattern": r"\d{2}",
        }
    )


class IssueTypeAttType(Enum):
    NEW = "new"
    CHANGED = "changed"
    DELETED = "deleted"
    REVISED = "revised"
    STATUS = "status"
    RINSTATE_CHANGED = "rinstate-changed"
    RINSTATE_REVISED = "rinstate-revised"
    RINSTATE_STATUS = "rinstate-status"


class ItemLocationCodeAttType(Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    T = "T"


class ItemOriginatorAttType(Enum):
    ORIG01 = "orig01"
    ORIG02 = "orig02"
    ORIG03 = "orig03"
    ORIG04 = "orig04"
    ORIG05 = "orig05"
    ORIG06 = "orig06"
    ORIG07 = "orig07"
    ORIG08 = "orig08"
    ORIG09 = "orig09"
    ORIG10 = "orig10"
    ORIG11 = "orig11"
    ORIG12 = "orig12"
    ORIG13 = "orig13"
    ORIG14 = "orig14"
    ORIG15 = "orig15"
    ORIG16 = "orig16"
    ORIG17 = "orig17"
    ORIG18 = "orig18"
    ORIG19 = "orig19"
    ORIG20 = "orig20"
    ORIG21 = "orig21"
    ORIG22 = "orig22"
    ORIG23 = "orig23"
    ORIG24 = "orig24"
    ORIG25 = "orig25"
    ORIG26 = "orig26"
    ORIG27 = "orig27"
    ORIG28 = "orig28"
    ORIG29 = "orig29"
    ORIG30 = "orig30"
    ORIG31 = "orig31"
    ORIG32 = "orig32"
    ORIG33 = "orig33"
    ORIG34 = "orig34"
    ORIG35 = "orig35"
    ORIG36 = "orig36"
    ORIG37 = "orig37"
    ORIG38 = "orig38"
    ORIG39 = "orig39"
    ORIG40 = "orig40"
    ORIG41 = "orig41"
    ORIG42 = "orig42"
    ORIG43 = "orig43"
    ORIG44 = "orig44"
    ORIG45 = "orig45"
    ORIG46 = "orig46"
    ORIG47 = "orig47"
    ORIG48 = "orig48"
    ORIG49 = "orig49"
    ORIG50 = "orig50"
    ORIG51 = "orig51"
    ORIG52 = "orig52"
    ORIG53 = "orig53"
    ORIG54 = "orig54"
    ORIG55 = "orig55"
    ORIG56 = "orig56"
    ORIG57 = "orig57"
    ORIG58 = "orig58"
    ORIG59 = "orig59"
    ORIG60 = "orig60"
    ORIG61 = "orig61"
    ORIG62 = "orig62"
    ORIG63 = "orig63"
    ORIG64 = "orig64"
    ORIG65 = "orig65"
    ORIG66 = "orig66"
    ORIG67 = "orig67"
    ORIG68 = "orig68"
    ORIG69 = "orig69"
    ORIG70 = "orig70"
    ORIG71 = "orig71"
    ORIG72 = "orig72"
    ORIG73 = "orig73"
    ORIG74 = "orig74"
    ORIG75 = "orig75"
    ORIG76 = "orig76"
    ORIG77 = "orig77"
    ORIG78 = "orig78"
    ORIG79 = "orig79"
    ORIG80 = "orig80"
    ORIG81 = "orig81"
    ORIG82 = "orig82"
    ORIG83 = "orig83"
    ORIG84 = "orig84"
    ORIG85 = "orig85"
    ORIG86 = "orig86"
    ORIG87 = "orig87"
    ORIG88 = "orig88"
    ORIG89 = "orig89"
    ORIG90 = "orig90"
    ORIG91 = "orig91"
    ORIG92 = "orig92"
    ORIG93 = "orig93"
    ORIG94 = "orig94"
    ORIG95 = "orig95"
    ORIG96 = "orig96"
    ORIG97 = "orig97"
    ORIG98 = "orig98"
    ORIG99 = "orig99"


@dataclass(kw_only=True)
class JobTitle:
    class Meta:
        name = "jobTitle"

    value: str = field(default="")


@dataclass(kw_only=True)
class LanguageElemType:
    class Meta:
        name = "languageElemType"

    language_iso_code: str = field(
        metadata={
            "name": "languageIsoCode",
            "type": "Attribute",
            "pattern": r"[a-z]{2,3}",
        }
    )
    country_iso_code: str = field(
        metadata={
            "name": "countryIsoCode",
            "type": "Attribute",
            "pattern": r"[A-Z]{2}",
        }
    )


@dataclass(kw_only=True)
class LastName:
    class Meta:
        name = "lastName"

    value: str = field(default="")


class LearnEventCodeAttType(Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"


class LinkActuateAttType(Enum):
    ON_LOAD = "onLoad"
    ON_REQUEST = "onRequest"


class LinkShowAttType(Enum):
    NEW_PANE = "newPane"
    EMBED_IN_CONTEXT = "embedInContext"
    REPLACE_AND_RETURN_TO_SOURCE = "replaceAndReturnToSource"
    REPLACE_AND_NO_RETURN = "replaceAndNoReturn"


class ListItemPrefixAttType(Enum):
    PF01 = "pf01"
    PF02 = "pf02"
    PF03 = "pf03"
    PF04 = "pf04"
    PF05 = "pf05"
    PF06 = "pf06"
    PF07 = "pf07"
    PF08 = "pf08"
    PF09 = "pf09"
    PF10 = "pf10"
    PF11 = "pf11"
    PF12 = "pf12"
    PF13 = "pf13"
    PF14 = "pf14"
    PF15 = "pf15"
    PF16 = "pf16"
    PF17 = "pf17"
    PF18 = "pf18"
    PF19 = "pf19"
    PF20 = "pf20"
    PF21 = "pf21"
    PF22 = "pf22"
    PF23 = "pf23"
    PF24 = "pf24"
    PF25 = "pf25"
    PF26 = "pf26"
    PF27 = "pf27"
    PF28 = "pf28"
    PF29 = "pf29"
    PF30 = "pf30"
    PF31 = "pf31"
    PF32 = "pf32"
    PF33 = "pf33"
    PF34 = "pf34"
    PF35 = "pf35"
    PF36 = "pf36"
    PF37 = "pf37"
    PF38 = "pf38"
    PF39 = "pf39"
    PF40 = "pf40"
    PF41 = "pf41"
    PF42 = "pf42"
    PF43 = "pf43"
    PF44 = "pf44"
    PF45 = "pf45"
    PF46 = "pf46"
    PF47 = "pf47"
    PF48 = "pf48"
    PF49 = "pf49"
    PF50 = "pf50"
    PF51 = "pf51"
    PF52 = "pf52"
    PF53 = "pf53"
    PF54 = "pf54"
    PF55 = "pf55"
    PF56 = "pf56"
    PF57 = "pf57"
    PF58 = "pf58"
    PF59 = "pf59"
    PF60 = "pf60"
    PF61 = "pf61"
    PF62 = "pf62"
    PF63 = "pf63"
    PF64 = "pf64"
    PF65 = "pf65"
    PF66 = "pf66"
    PF67 = "pf67"
    PF68 = "pf68"
    PF69 = "pf69"
    PF70 = "pf70"
    PF71 = "pf71"
    PF72 = "pf72"
    PF73 = "pf73"
    PF74 = "pf74"
    PF75 = "pf75"
    PF76 = "pf76"
    PF77 = "pf77"
    PF78 = "pf78"
    PF79 = "pf79"
    PF80 = "pf80"
    PF81 = "pf81"
    PF82 = "pf82"
    PF83 = "pf83"
    PF84 = "pf84"
    PF85 = "pf85"
    PF86 = "pf86"
    PF87 = "pf87"
    PF88 = "pf88"
    PF89 = "pf89"
    PF90 = "pf90"
    PF91 = "pf91"
    PF92 = "pf92"
    PF93 = "pf93"
    PF94 = "pf94"
    PF95 = "pf95"
    PF96 = "pf96"
    PF97 = "pf97"
    PF98 = "pf98"
    PF99 = "pf99"


class LowestLevelAttType(Enum):
    LA01 = "la01"
    LA02 = "la02"
    LA03 = "la03"
    LA04 = "la04"
    LA05 = "la05"
    LA06 = "la06"
    LA07 = "la07"
    LA08 = "la08"
    LA09 = "la09"
    LA10 = "la10"
    LA11 = "la11"
    LA12 = "la12"
    LA13 = "la13"
    LA14 = "la14"
    LA15 = "la15"
    LA16 = "la16"
    LA17 = "la17"
    LA18 = "la18"
    LA19 = "la19"
    LA20 = "la20"
    LA21 = "la21"
    LA22 = "la22"
    LA23 = "la23"
    LA24 = "la24"
    LA25 = "la25"
    LA26 = "la26"
    LA27 = "la27"
    LA28 = "la28"
    LA29 = "la29"
    LA30 = "la30"
    LA31 = "la31"
    LA32 = "la32"
    LA33 = "la33"
    LA34 = "la34"
    LA35 = "la35"
    LA36 = "la36"
    LA37 = "la37"
    LA38 = "la38"
    LA39 = "la39"
    LA40 = "la40"
    LA41 = "la41"
    LA42 = "la42"
    LA43 = "la43"
    LA44 = "la44"
    LA45 = "la45"
    LA46 = "la46"
    LA47 = "la47"
    LA48 = "la48"
    LA49 = "la49"
    LA50 = "la50"
    LA51 = "la51"
    LA52 = "la52"
    LA53 = "la53"
    LA54 = "la54"
    LA55 = "la55"
    LA56 = "la56"
    LA57 = "la57"
    LA58 = "la58"
    LA59 = "la59"
    LA60 = "la60"
    LA61 = "la61"
    LA62 = "la62"
    LA63 = "la63"
    LA64 = "la64"
    LA65 = "la65"
    LA66 = "la66"
    LA67 = "la67"
    LA68 = "la68"
    LA69 = "la69"
    LA70 = "la70"
    LA71 = "la71"
    LA72 = "la72"
    LA73 = "la73"
    LA74 = "la74"
    LA75 = "la75"
    LA76 = "la76"
    LA77 = "la77"
    LA78 = "la78"
    LA79 = "la79"
    LA80 = "la80"
    LA81 = "la81"
    LA82 = "la82"
    LA83 = "la83"
    LA84 = "la84"
    LA85 = "la85"
    LA86 = "la86"
    LA87 = "la87"
    LA88 = "la88"
    LA89 = "la89"
    LA90 = "la90"
    LA91 = "la91"
    LA92 = "la92"
    LA93 = "la93"
    LA94 = "la94"
    LA95 = "la95"
    LA96 = "la96"
    LA97 = "la97"
    LA98 = "la98"
    LA99 = "la99"


@dataclass(kw_only=True)
class MiddleName:
    class Meta:
        name = "middleName"

    value: str = field(default="")


@dataclass(kw_only=True)
class ModificationTitle:
    class Meta:
        name = "modificationTitle"

    value: str = field(default="")


class ModificationTypeAttType(Enum):
    PRE = "pre"
    POST = "post"
    PRANDPO = "prandpo"


class MultimediaTypeAttType(Enum):
    VALUE_3_D = "3D"
    AUDIO = "audio"
    VIDEO = "video"
    OTHER = "other"


class NumberActionAttType(Enum):
    COMMON_LOGARITHM = "commonLogarithm"
    COSECANT = "cosecant"
    COSINE = "cosine"
    COTANGENT = "cotangent"
    EXPONENTIAL = "exponential"
    FACTORIAL = "factorial"
    FLOAT = "float"
    HYPERBOLIC_COSECANT = "hyperbolicCosecant"
    HYPERBOLIC_COSINE = "hyperbolicCosine"
    HYPERBOLIC_COTANGENT = "hyperbolicCotangent"
    HYPERBOLIC_SECANT = "hyperbolicSecant"
    HYPERBOLIC_SINE = "hyperbolicSine"
    HYPERBOLIC_TANGENT = "hyperbolicTangent"
    INVERSE_COSECANT = "inverseCosecant"
    INVERSE_COSINE = "inverseCosine"
    INVERSE_COTANGENT = "inverseCotangent"
    INVERSE_SECANT = "inverseSecant"
    INVERSE_SINE = "inverseSine"
    INVERSE_TANGENT = "inverseTangent"
    NATURAL_LOGARITHM = "naturalLogarithm"
    NEGATIVE = "negative"
    SECANT = "secant"
    SINE = "sine"
    SQUARE_ROOT = "squareRoot"
    TANGENT = "tangent"
    TRUNCATE = "truncate"


class NumberOperationAttType(Enum):
    DIVIDE = "divide"
    EQUAL = "equal"
    EXPONENT = "exponent"
    GREATER_THAN = "greaterThan"
    GREATER_THAN_OR_EQUAL = "greaterThanOrEqual"
    INTEGER_DIVIDE = "integerDivide"
    LESS_THAN = "lessThan"
    LESS_THAN_OR_EQUAL = "lessThanOrEqual"
    MINUS = "minus"
    MODULUS = "modulus"
    NOT_EQUAL = "notEqual"
    PLUS = "plus"
    TIMES = "times"


class OrientAttType(Enum):
    PORT = "port"
    LAND = "land"


@dataclass(kw_only=True)
class ParameterElemType:
    class Meta:
        name = "parameterElemType"

    id: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    parameter_ident: None | str = field(
        default=None,
        metadata={
            "name": "parameterIdent",
            "type": "Attribute",
        },
    )
    parameter_value: None | str = field(
        default=None,
        metadata={
            "name": "parameterValue",
            "type": "Attribute",
        },
    )
    parameter_name: None | str = field(
        default=None,
        metadata={
            "name": "parameterName",
            "type": "Attribute",
        },
    )


class PartUsageCodeAttType(Enum):
    PU01 = "pu01"
    PU02 = "pu02"
    PU03 = "pu03"
    PU04 = "pu04"
    PU05 = "pu05"
    PU06 = "pu06"
    PU07 = "pu07"
    PU08 = "pu08"
    PU09 = "pu09"
    PU10 = "pu10"
    PU11 = "pu11"
    PU12 = "pu12"
    PU13 = "pu13"
    PU14 = "pu14"
    PU15 = "pu15"
    PU16 = "pu16"
    PU17 = "pu17"
    PU18 = "pu18"
    PU19 = "pu19"
    PU20 = "pu20"
    PU21 = "pu21"
    PU22 = "pu22"
    PU23 = "pu23"
    PU24 = "pu24"
    PU25 = "pu25"
    PU26 = "pu26"
    PU27 = "pu27"
    PU28 = "pu28"
    PU29 = "pu29"
    PU30 = "pu30"
    PU31 = "pu31"
    PU32 = "pu32"
    PU33 = "pu33"
    PU34 = "pu34"
    PU35 = "pu35"
    PU36 = "pu36"
    PU37 = "pu37"
    PU38 = "pu38"
    PU39 = "pu39"
    PU40 = "pu40"
    PU41 = "pu41"
    PU42 = "pu42"
    PU43 = "pu43"
    PU44 = "pu44"
    PU45 = "pu45"
    PU46 = "pu46"
    PU47 = "pu47"
    PU48 = "pu48"
    PU49 = "pu49"
    PU50 = "pu50"
    PU51 = "pu51"
    PU52 = "pu52"
    PU53 = "pu53"
    PU54 = "pu54"
    PU55 = "pu55"
    PU56 = "pu56"
    PU57 = "pu57"
    PU58 = "pu58"
    PU59 = "pu59"
    PU60 = "pu60"
    PU61 = "pu61"
    PU62 = "pu62"
    PU63 = "pu63"
    PU64 = "pu64"
    PU65 = "pu65"
    PU66 = "pu66"
    PU67 = "pu67"
    PU68 = "pu68"
    PU69 = "pu69"
    PU70 = "pu70"
    PU71 = "pu71"
    PU72 = "pu72"
    PU73 = "pu73"
    PU74 = "pu74"
    PU75 = "pu75"
    PU76 = "pu76"
    PU77 = "pu77"
    PU78 = "pu78"
    PU79 = "pu79"
    PU80 = "pu80"
    PU81 = "pu81"
    PU82 = "pu82"
    PU83 = "pu83"
    PU84 = "pu84"
    PU85 = "pu85"
    PU86 = "pu86"
    PU87 = "pu87"
    PU88 = "pu88"
    PU89 = "pu89"
    PU90 = "pu90"
    PU91 = "pu91"
    PU92 = "pu92"
    PU93 = "pu93"
    PU94 = "pu94"
    PU95 = "pu95"
    PU96 = "pu96"
    PU97 = "pu97"
    PU98 = "pu98"
    PU99 = "pu99"


@dataclass(kw_only=True)
class PhoneNumberElemType:
    class Meta:
        name = "phoneNumberElemType"

    contact_role: None | str = field(
        default=None,
        metadata={
            "name": "contactRole",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PhysicalChemicalDescr:
    class Meta:
        name = "physicalChemicalDescr"

    value: str = field(default="")


@dataclass(kw_only=True)
class PlacardText:
    class Meta:
        name = "placardText"

    value: str = field(default="")


@dataclass(kw_only=True)
class PmCodeElemType:
    class Meta:
        name = "pmCodeElemType"

    model_ident_code: str = field(
        metadata={
            "name": "modelIdentCode",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{2,14}",
        }
    )
    pm_issuer: str = field(
        metadata={
            "name": "pmIssuer",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{5}",
        }
    )
    pm_number: str = field(
        metadata={
            "name": "pmNumber",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{5}",
        }
    )
    pm_volume: str = field(
        metadata={
            "name": "pmVolume",
            "type": "Attribute",
            "pattern": r"\d{2}",
        }
    )


@dataclass(kw_only=True)
class PmTitle:
    class Meta:
        name = "pmTitle"

    value: str = field(default="")


@dataclass(kw_only=True)
class PostOfficeBox:
    class Meta:
        name = "postOfficeBox"

    value: str = field(default="")


@dataclass(kw_only=True)
class PostalZipCode:
    class Meta:
        name = "postalZipCode"

    value: str = field(default="")


@dataclass(kw_only=True)
class ProcessCategory:
    class Meta:
        name = "processCategory"

    value: str = field(default="")


class ProductCategoryAttType(Enum):
    PCG01 = "pcg01"
    PCG02 = "pcg02"
    PCG03 = "pcg03"
    PCG04 = "pcg04"
    PCG05 = "pcg05"
    PCG06 = "pcg06"
    PCG07 = "pcg07"
    PCG08 = "pcg08"
    PCG09 = "pcg09"
    PCG10 = "pcg10"
    PCG11 = "pcg11"
    PCG12 = "pcg12"
    PCG13 = "pcg13"
    PCG14 = "pcg14"
    PCG15 = "pcg15"
    PCG16 = "pcg16"
    PCG17 = "pcg17"
    PCG18 = "pcg18"
    PCG19 = "pcg19"
    PCG20 = "pcg20"
    PCG21 = "pcg21"
    PCG22 = "pcg22"
    PCG23 = "pcg23"
    PCG24 = "pcg24"
    PCG25 = "pcg25"
    PCG26 = "pcg26"
    PCG27 = "pcg27"
    PCG28 = "pcg28"
    PCG29 = "pcg29"
    PCG30 = "pcg30"
    PCG31 = "pcg31"
    PCG32 = "pcg32"
    PCG33 = "pcg33"
    PCG34 = "pcg34"
    PCG35 = "pcg35"
    PCG36 = "pcg36"
    PCG37 = "pcg37"
    PCG38 = "pcg38"
    PCG39 = "pcg39"
    PCG40 = "pcg40"
    PCG41 = "pcg41"
    PCG42 = "pcg42"
    PCG43 = "pcg43"
    PCG44 = "pcg44"
    PCG45 = "pcg45"
    PCG46 = "pcg46"
    PCG47 = "pcg47"
    PCG48 = "pcg48"
    PCG49 = "pcg49"
    PCG50 = "pcg50"
    PCG51 = "pcg51"
    PCG52 = "pcg52"
    PCG53 = "pcg53"
    PCG54 = "pcg54"
    PCG55 = "pcg55"
    PCG56 = "pcg56"
    PCG57 = "pcg57"
    PCG58 = "pcg58"
    PCG59 = "pcg59"
    PCG60 = "pcg60"
    PCG61 = "pcg61"
    PCG62 = "pcg62"
    PCG63 = "pcg63"
    PCG64 = "pcg64"
    PCG65 = "pcg65"
    PCG66 = "pcg66"
    PCG67 = "pcg67"
    PCG68 = "pcg68"
    PCG69 = "pcg69"
    PCG70 = "pcg70"
    PCG71 = "pcg71"
    PCG72 = "pcg72"
    PCG73 = "pcg73"
    PCG74 = "pcg74"
    PCG75 = "pcg75"
    PCG76 = "pcg76"
    PCG77 = "pcg77"
    PCG78 = "pcg78"
    PCG79 = "pcg79"
    PCG80 = "pcg80"
    PCG81 = "pcg81"
    PCG82 = "pcg82"
    PCG83 = "pcg83"
    PCG84 = "pcg84"
    PCG85 = "pcg85"
    PCG86 = "pcg86"
    PCG87 = "pcg87"
    PCG88 = "pcg88"
    PCG89 = "pcg89"
    PCG90 = "pcg90"
    PCG91 = "pcg91"
    PCG92 = "pcg92"
    PCG93 = "pcg93"
    PCG94 = "pcg94"
    PCG95 = "pcg95"
    PCG96 = "pcg96"
    PCG97 = "pcg97"
    PCG98 = "pcg98"
    PCG99 = "pcg99"


@dataclass(kw_only=True)
class ProductSafetyElemType:
    class Meta:
        name = "productSafetyElemType"

    safety_label: str = field(
        metadata={
            "name": "safetyLabel",
            "type": "Attribute",
        }
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Province:
    class Meta:
        name = "province"

    value: str = field(default="")


@dataclass(kw_only=True)
class PubMediaElemType:
    class Meta:
        name = "pubMediaElemType"

    pub_media_type: str = field(
        metadata={
            "name": "pubMediaType",
            "type": "Attribute",
        }
    )
    pub_media_code: str = field(
        metadata={
            "name": "pubMediaCode",
            "type": "Attribute",
        }
    )
    volume_number: None | str = field(
        default=None,
        metadata={
            "name": "volumeNumber",
            "type": "Attribute",
        },
    )
    media_location: None | str = field(
        default=None,
        metadata={
            "name": "mediaLocation",
            "type": "Attribute",
        },
    )


class QuantityGroupTypeAttType(Enum):
    NOMINAL = "nominal"
    MINIMUM = "minimum"
    MAXIMUM = "maximum"


@dataclass(kw_only=True)
class QuantityPerUnit:
    class Meta:
        name = "quantityPerUnit"

    value: str = field(default="")


class QuantityToleranceTypeAttType(Enum):
    PLUS = "plus"
    MINUS = "minus"
    PLUSORMINUS = "plusorminus"


class QuantityTypeAttType(Enum):
    QTY01 = "qty01"
    QTY02 = "qty02"
    QTY03 = "qty03"
    QTY04 = "qty04"
    QTY05 = "qty05"
    QTY06 = "qty06"
    QTY07 = "qty07"
    QTY08 = "qty08"
    QTY09 = "qty09"
    QTY10 = "qty10"
    QTY11 = "qty11"
    QTY12 = "qty12"
    QTY13 = "qty13"
    QTY14 = "qty14"
    QTY15 = "qty15"
    QTY16 = "qty16"
    QTY17 = "qty17"
    QTY18 = "qty18"
    QTY19 = "qty19"
    QTY20 = "qty20"
    QTY21 = "qty21"
    QTY22 = "qty22"
    QTY23 = "qty23"
    QTY24 = "qty24"
    QTY25 = "qty25"
    QTY26 = "qty26"
    QTY27 = "qty27"
    QTY28 = "qty28"
    QTY29 = "qty29"
    QTY30 = "qty30"
    QTY31 = "qty31"
    QTY32 = "qty32"
    QTY33 = "qty33"
    QTY34 = "qty34"
    QTY35 = "qty35"
    QTY36 = "qty36"
    QTY37 = "qty37"
    QTY38 = "qty38"
    QTY39 = "qty39"
    QTY40 = "qty40"
    QTY41 = "qty41"
    QTY42 = "qty42"
    QTY43 = "qty43"
    QTY44 = "qty44"
    QTY45 = "qty45"
    QTY46 = "qty46"
    QTY47 = "qty47"
    QTY48 = "qty48"
    QTY49 = "qty49"
    QTY50 = "qty50"
    QTY51 = "qty51"
    QTY52 = "qty52"
    QTY53 = "qty53"
    QTY54 = "qty54"
    QTY55 = "qty55"
    QTY56 = "qty56"
    QTY57 = "qty57"
    QTY58 = "qty58"
    QTY59 = "qty59"
    QTY60 = "qty60"
    QTY61 = "qty61"
    QTY62 = "qty62"
    QTY63 = "qty63"
    QTY64 = "qty64"
    QTY65 = "qty65"
    QTY66 = "qty66"
    QTY67 = "qty67"
    QTY68 = "qty68"
    QTY69 = "qty69"
    QTY70 = "qty70"
    QTY71 = "qty71"
    QTY72 = "qty72"
    QTY73 = "qty73"
    QTY74 = "qty74"
    QTY75 = "qty75"
    QTY76 = "qty76"
    QTY77 = "qty77"
    QTY78 = "qty78"
    QTY79 = "qty79"
    QTY80 = "qty80"
    QTY81 = "qty81"
    QTY82 = "qty82"
    QTY83 = "qty83"
    QTY84 = "qty84"
    QTY85 = "qty85"
    QTY86 = "qty86"
    QTY87 = "qty87"
    QTY88 = "qty88"
    QTY89 = "qty89"
    QTY90 = "qty90"
    QTY91 = "qty91"
    QTY92 = "qty92"
    QTY93 = "qty93"
    QTY94 = "qty94"
    QTY95 = "qty95"
    QTY96 = "qty96"
    QTY97 = "qty97"
    QTY98 = "qty98"
    QTY99 = "qty99"


class QuantityUnitOfMeasureAttType(Enum):
    VALUE_1_H = "1/H"
    VALUE_1_K = "1/K"
    VALUE_1_KG = "1/kg"
    VALUE_1_M = "1/m"
    VALUE_1_M2 = "1/m2"
    VALUE_1_M3 = "1/m3"
    VALUE_1_N = "1/N"
    VALUE_1_PA = "1/Pa"
    VALUE_1_S = "1/s"
    VALUE_1_V = "1/V"
    A = "A"
    A_M2 = "A.m2"
    A_M = "A/m"
    A_M2_1 = "A/m2"
    B = "B"
    B_M = "B/m"
    B_O = "B/O"
    BD = "Bd"
    BQ = "Bq"
    BQ_KG = "Bq/kg"
    BYTE = "byte"
    C = "C"
    C_M = "C.m"
    C_KG = "C/kg"
    C_M2 = "C/m2"
    C_M3 = "C/m3"
    CD = "cd"
    CD_M2 = "cd/m2"
    EQ = "eq"
    EQ_KG = "eq/kg"
    EQ_M3 = "eq/m3"
    EUC = "Euc"
    F = "F"
    F_M = "F/m"
    GU = "gu"
    G_API = "gAPI"
    GY = "Gy"
    H = "H"
    H_M = "H/m"
    HZ = "Hz"
    J = "J"
    J_K = "J/K"
    J_KG = "J/kg"
    J_KG_K = "J/kg.K"
    J_M3 = "J/m3"
    J_MOL = "J/mol"
    J_MOL_K = "J/mol.K"
    K = "K"
    K_M2_W = "K.m2/W"
    K_M = "K/m"
    K_S = "K/s"
    K_W = "K/W"
    KG = "kg"
    KG_M = "kg.m"
    KG_M_S = "kg.m/s"
    KG_M2 = "kg.m2"
    KG_J = "kg/J"
    KG_M_1 = "kg/m"
    KG_M2_1 = "kg/m2"
    KG_M2_S = "kg/m2.s"
    KG_M3 = "kg/m3"
    KG_M4 = "kg/m4"
    KG_S = "kg/s"
    LM = "lm"
    LM_S = "lm.s"
    LM_W = "lm/W"
    LX = "lx"
    LX_S = "lx.s"
    M = "m"
    M_K = "m/K"
    M_S = "m/s"
    M_S2 = "m/s2"
    M2 = "m2"
    M2_KG = "m2/kg"
    M2_MOL = "m2/mol"
    M2_PA_S = "m2/Pa.s"
    M2_S = "m2/s"
    M3 = "m3"
    M3_J = "m3/J"
    M3_KG = "m3/kg"
    M3_MOL = "m3/mol"
    M3_PA_S = "m3/Pa.s"
    M3_PA_S_1 = "m3/Pa/s"
    M3_PA2_S2 = "m3/Pa2.s2"
    M3_S = "m3/s"
    M3_S2 = "m3/s2"
    M3_SCM_0_C = "m3/scm(0C)"
    M3_SCM_15_C = "m3/scm(15C)"
    M4 = "m4"
    M4_S = "m4/s"
    MOL = "mol"
    MOL_M2 = "mol/m2"
    MOL_M2_S = "mol/m2.s"
    MOL_M3 = "mol/m3"
    MOL_S = "mol/s"
    N = "N"
    N_M2 = "N.m2"
    N_M = "N/m"
    N_M3 = "N/m3"
    N4_KG_M7 = "N4/kg.m7"
    N_API = "nAPI"
    O = "O"
    OHM = "ohm"
    OHM_M = "ohm.m"
    OHM_M_1 = "ohm/m"
    PA = "Pa"
    PA_S = "Pa.s"
    PA_S_M3 = "Pa.s/m3"
    PA_S_M6 = "Pa.s/m6"
    PA_M = "Pa/m"
    PA_M3 = "Pa/m3"
    PA_S_1 = "Pa/s"
    PA2 = "Pa2"
    P_H = "pH"
    RAD = "rad"
    RAD_M = "rad/m"
    RAD_M3 = "rad/m3"
    RAD_S = "rad/s"
    RAD_S2 = "rad/s2"
    S = "S"
    S_1 = "s"
    S_M = "S/m"
    S_M_1 = "s/m"
    S_M3 = "s/m3"
    SCM_0_C = "scm(0C)"
    SCM_0_C_M2 = "scm(0C)/m2"
    SCM_0_C_M3 = "scm(0C)/m3"
    SCM_15_C = "scm(15C)"
    SCM_15_C_M2 = "scm(15C)/m2"
    SCM_15_C_M3 = "scm(15C)/m3"
    SCM_15_C_S = "scm(15C)/s"
    SR = "sr"
    SV = "Sv"
    SV_S = "Sv/s"
    T = "T"
    V = "V"
    V_B = "V/B"
    V_M = "V/m"
    W = "W"
    W_K = "W/K"
    W_M_K = "W/m.K"
    W_M2 = "W/m2"
    W_M2_K = "W/m2.K"
    W_M2_SR = "W/m2.sr"
    W_M3 = "W/m3"
    W_M3_K = "W/m3.K"
    W_SR = "W/sr"
    WB = "Wb"
    WB_M = "Wb.m"
    WB_M_1 = "Wb/m"
    PERCENT_SIGN = "%"
    VALUE_1_A = "1/a"
    VALUE_1_ANGSTROM = "1/angstrom"
    VALUE_1_BAR = "1/bar"
    VALUE_1_BBL = "1/bbl"
    VALUE_1_CM = "1/cm"
    VALUE_1_D = "1/d"
    VALUE_1_DEG_C = "1/degC"
    VALUE_1_DEG_F = "1/degF"
    VALUE_1_DEG_R = "1/degR"
    VALUE_1_FT = "1/ft"
    VALUE_1_FT2 = "1/ft2"
    VALUE_1_FT3 = "1/ft3"
    VALUE_1_G = "1/g"
    VALUE_1_GAL_UK = "1/galUK"
    VALUE_1_GAL_US = "1/galUS"
    VALUE_1_H_1 = "1/h"
    VALUE_1_IN = "1/in"
    VALUE_1_KM2 = "1/km2"
    VALUE_1_K_PA = "1/kPa"
    VALUE_1_L = "1/L"
    VALUE_1_LBF = "1/lbf"
    VALUE_1_LBM = "1/lbm"
    VALUE_1_MI = "1/mi"
    VALUE_1_MI2 = "1/mi2"
    VALUE_1_MIN = "1/min"
    VALUE_1_MM = "1/mm"
    VALUE_1_NM = "1/nm"
    VALUE_1_P_PA = "1/pPa"
    VALUE_1_PSI = "1/psi"
    VALUE_1_UPSI = "1/upsi"
    VALUE_1_U_V = "1/uV"
    VALUE_1_WK = "1/wk"
    VALUE_1_YD = "1/yd"
    VALUE_1000FT3 = "1000ft3"
    VALUE_1000FT3_BBL = "1000ft3/bbl"
    VALUE_1000FT3_D = "1000ft3/d"
    VALUE_1000FT3_D_FT = "1000ft3/d.ft"
    VALUE_1000FT3_PSI_D = "1000ft3/psi.d"
    VALUE_1000M3_D = "1000m3/d"
    VALUE_1000M3_D_M = "1000m3/d.m"
    VALUE_1000M3_H = "1000m3/h"
    VALUE_1000M3_H_M = "1000m3/h.m"
    VALUE_1000M4_D = "1000m4/d"
    VALUE_100KA = "100ka"
    VALUE_10_MG_M3 = "10Mg/m3"
    A_1 = "a"
    A_H = "A.h"
    A_CM2 = "A/cm2"
    A_FT2 = "A/ft2"
    A_MM = "A/mm"
    A_MM2 = "A/mm2"
    ACRE = "acre"
    ACRE_FT = "acre.ft"
    ACRE_FT_MMSTB = "acre.ft/MMstb"
    AG = "ag"
    A_J = "aJ"
    ANGSTROM = "angstrom"
    AT = "at"
    ATM = "atm"
    ATM_FT = "atm/ft"
    ATM_H = "atm/h"
    ATM_HM = "atm/hm"
    ATM_M = "atm/m"
    B_1 = "b"
    B_CM3 = "b/cm3"
    B_ELEC = "b/elec"
    BAR = "bar"
    BAR_H = "bar/h"
    BAR_KM = "bar/km"
    BAR_M = "bar/m"
    BAR2 = "bar2"
    BAR2_C_P = "bar2/cP"
    BBL = "bbl"
    BBL_100BBL = "bbl/100bbl"
    BBL_ACRE = "bbl/acre"
    BBL_ACRE_FT = "bbl/acre.ft"
    BBL_BBL = "bbl/bbl"
    BBL_C_P_D_PSI = "bbl/cP.d.psi"
    BBL_D = "bbl/d"
    BBL_D_ACRE_FT = "bbl/d.acre.ft"
    BBL_D_FT = "bbl/d.ft"
    BBL_D_FT_PSI = "bbl/d.ft.psi"
    BBL_D_PSI = "bbl/d.psi"
    BBL_D2 = "bbl/d2"
    BBL_FT = "bbl/ft"
    BBL_FT3 = "bbl/ft3"
    BBL_HR = "bbl/hr"
    BBL_HR2 = "bbl/hr2"
    BBL_IN = "bbl/in"
    BBL_K_FT3 = "bbl/k(ft3)"
    BBL_K_PA_D = "bbl/kPa.d"
    BBL_M_FT3 = "bbl/M(ft3)"
    BBL_MI = "bbl/mi"
    BBL_MIN = "bbl/min"
    BBL_MMSCF_60_F = "bbl/MMscf(60F)"
    BBL_PSI_D = "bbl/psi.d"
    BBL_STB_60_F = "bbl/stb(60F)"
    BBL_TON_UK = "bbl/tonUK"
    BBL_TON_US = "bbl/tonUS"
    BCF = "bcf"
    BIT = "bit"
    BTU = "Btu"
    BTU_IN_HR_FT2_F = "Btu.in/hr.ft2.F"
    BTU_MILLION_HR = "Btu(million)/hr"
    BTU_BBL = "Btu/bbl"
    BTU_BHP_HR = "Btu/bhp.hr"
    BTU_FT3 = "Btu/ft3"
    BTU_GAL_UK = "Btu/galUK"
    BTU_GAL_US = "Btu/galUS"
    BTU_HR = "Btu/hr"
    BTU_HR_FT_DEG_F = "Btu/hr.ft.degF"
    BTU_HR_FT2 = "Btu/hr.ft2"
    BTU_HR_FT2_DEG_F = "Btu/hr.ft2.degF"
    BTU_HR_FT2_DEG_R = "Btu/hr.ft2.degR"
    BTU_HR_FT3 = "Btu/hr.ft3"
    BTU_HR_FT3_DEG_F = "Btu/hr.ft3.degF"
    BTU_HR_M2_DEG_C = "Btu/hr.m2.degC"
    BTU_LBM = "Btu/lbm"
    BTU_LBM_DEG_F = "Btu/lbm.degF"
    BTU_LBM_DEG_R = "Btu/lbm.degR"
    BTU_MIN = "Btu/min"
    BTU_MOL_LBM = "Btu/mol(lbm)"
    BTU_MOL_LBM_F = "Btu/mol(lbm).F"
    BTU_S = "Btu/s"
    BTU_S_FT2 = "Btu/s.ft2"
    BTU_S_FT2_DEG_F = "Btu/s.ft2.degF"
    BTU_S_FT3 = "Btu/s.ft3"
    BTU_S_FT3_DEG_F = "Btu/s.ft3.degF"
    C_1 = "c"
    C_CM2 = "C/cm2"
    C_CM3 = "C/cm3"
    C_G = "C/g"
    C_MM2 = "C/mm2"
    C_MM3 = "C/mm3"
    C_S = "c/s"
    CAL = "cal"
    CAL_CM3 = "cal/cm3"
    CAL_G = "cal/g"
    CAL_G_K = "cal/g.K"
    CAL_H_CM_DEG_C = "cal/h.cm.degC"
    CAL_H_CM2 = "cal/h.cm2"
    CAL_H_CM2_DEG_C = "cal/h.cm2.degC"
    CAL_H_CM3 = "cal/h.cm3"
    CAL_KG = "cal/kg"
    CAL_LBM = "cal/lbm"
    CAL_M_L = "cal/mL"
    CAL_MM3 = "cal/mm3"
    CAL_MOL_G_DEG_C = "cal/mol(g).degC"
    CAL_S_CM_DEG_C = "cal/s.cm.degC"
    CAL_S_CM2_DEG_C = "cal/s.cm2.degC"
    CAL_S_CM3 = "cal/s.cm3"
    CCGR = "ccgr"
    C_EUC = "cEuc"
    CGR = "cgr"
    CH = "ch"
    CH_H = "ch.h"
    CH_BN_A = "chBnA"
    CH_BN_B = "chBnB"
    CH_CLA = "chCla"
    CH_SE = "chSe"
    CHU = "Chu"
    CH_US = "chUS"
    CI = "Ci"
    C_L = "cL"
    CM_1 = "cm"
    CM_A = "cm/a"
    CM_S = "cm/s"
    CM_S2 = "cm/s2"
    CM2_1 = "cm2"
    CM2_G = "cm2/g"
    CM2_S = "cm2/s"
    CM3_1 = "cm3"
    CM3_30MIN = "cm3/30min"
    CM3_CM3 = "cm3/cm3"
    CM3_G = "cm3/g"
    CM3_H = "cm3/h"
    CM3_M3 = "cm3/m3"
    CM3_MIN = "cm3/min"
    CM3_S = "cm3/s"
    CM4 = "cm4"
    CM_H2_O_4DEG_C = "cmH2O(4degC)"
    C_P = "cP"
    CS_1 = "cs"
    C_ST = "cSt"
    CT = "ct"
    CU = "cu"
    CU_FT = "cu ft"
    CU_IN = "cu in"
    CU_YD = "cu yd"
    CUBEM = "cubem"
    CURIE = "curie"
    CV = "CV"
    CV_H = "CV.h"
    CWT_UK = "cwtUK"
    CWT_US = "cwtUS"
    D = "D"
    D_1 = "d"
    D_FT = "D.ft"
    D_M = "D.m"
    D_BBL = "d/bbl"
    D_FT3 = "d/ft3"
    D_K_FT3 = "d/k(ft3)"
    D_M3 = "d/m3"
    DA_N = "daN"
    DA_N_M = "daN.m"
    D_API = "dAPI"
    D_B = "dB"
    D_B_100M = "dB/100m"
    D_B_FT = "dB/ft"
    D_B_M = "dB/m"
    D_B_KM = "dB/km"
    D_B_O = "dB/O"
    DDEG_C = "ddegC"
    DDEG_F = "ddegF"
    DDEG_K = "ddegK"
    DDEG_R = "ddegR"
    DEGA = "dega"
    DEGA_100FT = "dega/100ft"
    DEGA_30FT = "dega/30ft"
    DEGA_30M = "dega/30m"
    DEGA_FT = "dega/ft"
    DEGA_FT_100 = "dega/ft(100)"
    DEGA_H = "dega/h"
    DEGA_M = "dega/m"
    DEGA_M_30 = "dega/m(30)"
    DEGA_MIN = "dega/min"
    DEGA_S = "dega/s"
    DEG_C = "degC"
    DEG_C_M2_H_KCAL = "degC.m2.h/kcal"
    DEG_C_100M = "degC/100m"
    DEG_C_FT = "degC/ft"
    DEG_C_H = "degC/h"
    DEG_C_KM = "degC/km"
    DEG_C_M = "degC/m"
    DEG_C_MIN = "degC/min"
    DEG_C_S = "degC/s"
    DEG_F = "degF"
    DEG_F_FT2_H_BTU = "degF.ft2.h/Btu"
    DEG_F_100FT = "degF/100ft"
    DEG_F_FT = "degF/ft"
    DEG_F_FT_100 = "degF/ft(100)"
    DEG_F_H = "degF/h"
    DEG_F_M = "degF/m"
    DEG_F_MIN = "degF/min"
    DEG_F_S = "degF/s"
    DEG_R = "degR"
    D_L = "dL"
    DM_1 = "dm"
    DM_S = "dm/s"
    DM3_1 = "dm3"
    DM3_100KM = "dm3/100km"
    DM3_KG = "dm3/kg"
    DM3_KM_100 = "dm3/km(100)"
    DM3_K_W_H = "dm3/kW.h"
    DM3_M = "dm3/m"
    DM3_M3 = "dm3/m3"
    DM3_MJ = "dm3/MJ"
    DM3_MOL_KG = "dm3/mol(kg)"
    DM3_S = "dm3/s"
    DM3_S2 = "dm3/s2"
    DM3_T = "dm3/t"
    D_N_M = "dN.m"
    DYNE = "dyne"
    DYNE_CM2 = "dyne.cm2"
    DYNE_S_CM2 = "dyne.s/cm2"
    DYNE_CM = "dyne/cm"
    DYNE_CM2_1 = "dyne/cm2"
    DYNE_CM_4_GCM3 = "(dyne/cm)4/gcm3"
    N_M_4_KG_M3 = "(N/m)4/kg.m3"
    EHP = "ehp"
    EJ = "EJ"
    EJ_A = "EJ/a"
    EQ_L = "eq/L"
    ERG = "erg"
    ERG_A = "erg/a"
    ERG_CM2 = "erg/cm2"
    ERG_CM3 = "erg/cm3"
    ERG_G = "erg/g"
    ERG_KG = "erg/kg"
    ERG_M3 = "erg/m3"
    E_V = "eV"
    FATHOM = "fathom"
    F_C = "fC"
    FL_OZ_UK = "fl ozUK"
    FL_OZ_US = "fl ozUS"
    FLOPS = "flops"
    FLOZ_UK_1 = "flozUK"
    FLOZ_US_1 = "flozUS"
    FM_1 = "fm"
    FOOTCANDLE = "footcandle"
    FOOTCANDLE_S = "footcandle.s"
    FT = "ft"
    FT_LBF = "ft.lbf"
    FT_LBF_BBL = "ft.lbf/bbl"
    FT_LBF_GAL_US = "ft.lbf/galUS"
    FT_LBF_LBM = "ft.lbf/lbm"
    FT_LBF_MIN = "ft.lbf/min"
    FT_LBF_S = "ft.lbf/s"
    FT_LBM = "ft.lbm"
    FT_100FT = "ft/100ft"
    FT_BBL = "ft/bbl"
    FT_D = "ft/d"
    FT_DEG_F = "ft/degF"
    FT_FT = "ft/ft"
    FT_FT3 = "ft/ft3"
    FT_GAL_US = "ft/galUS"
    FT_H = "ft/h"
    FT_IN = "ft/in"
    FT_M = "ft/m"
    FT_MI = "ft/mi"
    FT_MIN = "ft/min"
    FT_MS = "ft/ms"
    FT_S = "ft/s"
    FT_S2 = "ft/s2"
    FT_US = "ft/us"
    FT2 = "ft2"
    FT2_H = "ft2/h"
    FT2_IN3 = "ft2/in3"
    FT2_S = "ft2/s"
    FT3 = "ft3"
    FT3_STD_60_F = "ft3(std,60F)"
    FT3_BBL = "ft3/bbl"
    FT3_D = "ft3/d"
    FT3_D_FT_PSI = "ft3/d.ft.psi"
    FT3_D2 = "ft3/d2"
    FT3_FT = "ft3/ft"
    FT3_FT3 = "ft3/ft3"
    FT3_H = "ft3/h"
    FT3_H2 = "ft3/h2"
    FT3_KG = "ft3/kg"
    FT3_LBM = "ft3/lbm"
    FT3_MIN = "ft3/min"
    FT3_MIN_FT2 = "ft3/min.ft2"
    FT3_MIN2 = "ft3/min2"
    FT3_MOL_LBM = "ft3/mol(lbm)"
    FT3_S = "ft3/s"
    FT3_S_FT2 = "ft3/s.ft2"
    FT3_S2 = "ft3/s2"
    FT3_SACK94 = "ft3/sack94"
    FT3_SCF_60_F = "ft3/scf(60F)"
    FT_BN_A = "ftBnA"
    FT_BN_B = "ftBnB"
    FT_BR_65 = "ftBr(65)"
    FT_CLA = "ftCla"
    FT_GC = "ftGC"
    FT_IND = "ftInd"
    FT_IND_37 = "ftInd(37)"
    FT_IND_62 = "ftInd(62)"
    FT_IND_75 = "ftInd(75)"
    FT_MA = "ftMA"
    FT_SE = "ftSe"
    FT_US_1 = "ftUS"
    G = "g"
    G_FT_CM3_S = "g.ft/cm3.s"
    G_CM3 = "g/cm3"
    G_CM4 = "g/cm4"
    G_DM3 = "g/dm3"
    G_GAL_UK = "g/galUK"
    G_GAL_US = "g/galUS"
    G_KG = "g/kg"
    G_L = "g/L"
    G_M3 = "g/m3"
    G_S = "g/s"
    GA = "Ga"
    GAL = "Gal"
    GAL_SACK = "gal/sack"
    GAL_UK = "galUK"
    GAL_UK_D = "galUK/d"
    GAL_UK_FT3 = "galUK/ft3"
    GAL_UK_HR = "galUK/hr"
    GAL_UK_HR_FT = "galUK/hr.ft"
    GAL_UK_HR_FT2 = "galUK/hr.ft2"
    GAL_UK_HR_IN = "galUK/hr.in"
    GAL_UK_HR_IN2 = "galUK/hr.in2"
    GAL_UK_HR2 = "galUK/hr2"
    GAL_UK_KGAL_UK = "galUK/kgalUK"
    GAL_UK_LBM = "galUK/lbm"
    GAL_UK_MBBL = "galUK/Mbbl"
    GAL_UK_MI = "galUK/mi"
    GAL_UK_MIN = "galUK/min"
    GAL_UK_MIN_FT = "galUK/min.ft"
    GAL_UK_MIN_FT2 = "galUK/min.ft2"
    GAL_UK_MIN2 = "galUK/min2"
    GAL_US = "galUS"
    GAL_US_10BBL = "galUS/10bbl"
    GAL_US_BBL = "galUS/bbl"
    GAL_US_D = "galUS/d"
    GAL_US_FT = "galUS/ft"
    GAL_US_FT3 = "galUS/ft3"
    GAL_US_HR = "galUS/hr"
    GAL_US_HR_FT = "galUS/hr.ft"
    GAL_US_HR_FT2 = "galUS/hr.ft2"
    GAL_US_HR_IN = "galUS/hr.in"
    GAL_US_HR_IN2 = "galUS/hr.in2"
    GAL_US_HR2 = "galUS/hr2"
    GAL_US_KGAL_US = "galUS/kgalUS"
    GAL_US_LBM = "galUS/lbm"
    GAL_US_MBBL = "galUS/Mbbl"
    GAL_US_MI = "galUS/mi"
    GAL_US_MIN = "galUS/min"
    GAL_US_MIN_FT = "galUS/min.ft"
    GAL_US_MIN_FT2 = "galUS/min.ft2"
    GAL_US_MIN2 = "galUS/min2"
    GAL_US_MSCF_60_F = "galUS/Mscf(60F)"
    GAL_US_SACK94 = "galUS/sack94"
    GAL_US_TON_UK = "galUS/tonUK"
    GAL_US_TON_US = "galUS/tonUS"
    GAMMA = "gamma"
    GAUSS = "gauss"
    GBQ = "GBq"
    GE_V = "GeV"
    GF = "gf"
    GHZ = "GHz"
    GJ = "GJ"
    GN = "gn"
    GOHM = "Gohm"
    GON = "gon"
    GPA = "GPa"
    GPA_CM = "GPa/cm"
    GPA2 = "GPa2"
    GR = "gr"
    GRAD = "Grad"
    GRAIN = "grain"
    GRAIN_100FT3 = "grain/100ft3"
    GRAIN_FT3 = "grain/ft3"
    GRAIN_FT3_100 = "grain/ft3(100)"
    GRAIN_GAL_US = "grain/galUS"
    GS_1 = "GS"
    GSM3 = "Gsm3"
    GW = "GW"
    GW_H = "GW.h"
    H_1 = "h"
    H_FT3 = "h/ft3"
    H_KFT = "h/kft"
    H_KM = "h/km"
    H_M3 = "h/m3"
    HA = "ha"
    HA_M = "ha.m"
    HBAR = "hbar"
    HHP = "hhp"
    HHP_IN2 = "hhp/in2"
    H_L = "hL"
    HP = "hp"
    H_PA = "hPa"
    HP_HR = "hp.hr"
    HP_HR_BBL = "hp.hr/bbl"
    HP_HR_LBM = "hp.hr/lbm"
    HP_FT3 = "hp/ft3"
    HP_IN2 = "hp/in2"
    HS = "hs"
    IN = "in"
    IN_10 = "in/10"
    IN_16 = "in/16"
    IN_32 = "in/32"
    IN_64 = "in/64"
    IN_A = "in/a"
    IN_IN_DEG_F = "in/in.degF"
    IN_MIN = "in/min"
    IN_S = "in/s"
    IN2 = "in2"
    IN2_FT2 = "in2/ft2"
    IN2_IN2 = "in2/in2"
    IN2_S = "in2/s"
    IN3 = "in3"
    IN3_FT = "in3/ft"
    IN4 = "in4"
    IN_H2_O_39_2_F = "inH2O(39.2F)"
    IN_H2_O_60_F = "inH2O(60F)"
    IN_HG_32_F = "inHg(32F)"
    IN_HG_60_F = "inHg(60F)"
    IN_US = "inUS"
    J_CM2 = "J/cm2"
    J_DM3 = "J/dm3"
    J_G = "J/g"
    J_G_K = "J/g.K"
    J_M = "J/m"
    J_M2 = "J/m2"
    J_S_M2_DEG_C = "J/s.m2.degC"
    K_M2_K_W = "K.m2/kW"
    K_A = "kA"
    KBBL_D = "kbbl/d"
    KBYTE = "kbyte"
    K_C = "kC"
    KCAL = "kcal"
    KCAL_M_CM2 = "kcal.m/cm2"
    KCAL_CM3 = "kcal/cm3"
    KCAL_G = "kcal/g"
    KCAL_H = "kcal/h"
    KCAL_H_M_DEG_C = "kcal/h.m.degC"
    KCAL_H_M2_DEG_C = "kcal/h.m2.degC"
    KCAL_KG = "kcal/kg"
    KCAL_KG_DEG_C = "kcal/kg.degC"
    KCAL_M3 = "kcal/m3"
    KCAL_MOL_G = "kcal/mol(g)"
    KCD = "kcd"
    KDYNE = "kdyne"
    K_EUC_S = "kEuc/s"
    KE_V = "keV"
    KFT_LBF = "kft.lbf"
    KFT_H = "kft/h"
    KFT_S = "kft/s"
    KG_M_CM2 = "kg.m/cm2"
    KG_D = "kg/d"
    KG_DM3 = "kg/dm3"
    KG_DM4 = "kg/dm4"
    KG_H = "kg/h"
    KG_KG = "kg/kg"
    KG_K_W_H = "kg/kW.h"
    KG_L = "kg/L"
    KG_M_S_1 = "kg/m.s"
    KG_MIN = "kg/min"
    KG_MJ = "kg/MJ"
    KG_SACK94 = "kg/sack94"
    KGF = "kgf"
    KGF_M = "kgf.m"
    KGF_M_CM2 = "kgf.m/cm2"
    KGF_M_M = "kgf.m/m"
    KGF_M2 = "kgf.m2"
    KGF_S_M2 = "kgf.s/m2"
    KGF_CM = "kgf/cm"
    KGF_CM2 = "kgf/cm2"
    KGF_KGF = "kgf/kgf"
    KGF_MM2 = "kgf/mm2"
    K_HZ = "kHz"
    K_J = "kJ"
    K_J_M_H_M2_K = "kJ.m/h.m2.K"
    K_J_DM3 = "kJ/dm3"
    K_J_H_M2_K = "kJ/h.m2.K"
    K_J_KG = "kJ/kg"
    K_J_KG_K = "kJ/kg.K"
    K_J_M3 = "kJ/m3"
    K_J_MOL_KG = "kJ/mol(kg)"
    K_J_MOL_KG_K = "kJ/mol(kg).K"
    KLBF = "klbf"
    KLBM = "klbm"
    KLBM_IN = "klbm/in"
    KLX = "klx"
    KM_1 = "km"
    KM_CM = "km/cm"
    KM_DM3 = "km/dm3"
    KM_H = "km/h"
    KM_L = "km/L"
    KM_S = "km/s"
    KM2 = "km2"
    KM3 = "km3"
    KMOL = "kmol"
    K_N = "kN"
    K_N_M = "kN.m"
    K_N_M2 = "kN.m2"
    K_N_M_1 = "kN/m"
    K_N_M2_1 = "kN/m2"
    KNOT = "knot"
    KOHM = "kohm"
    KOHM_M = "kohm.m"
    K_PA = "kPa"
    K_PA_S_M = "kPa.s/m"
    K_PA_100M = "kPa/100m"
    K_PA_H = "kPa/h"
    K_PA_M = "kPa/m"
    K_PA_MIN = "kPa/min"
    K_PA2 = "kPa2"
    K_PA2_C_P = "kPa2/cP"
    K_PA2_KC_P = "kPa2/kcP"
    KPSI = "kpsi"
    KPSI2 = "kpsi2"
    KRAD = "krad"
    K_S_1 = "kS"
    KSM3 = "ksm3"
    KSM3_D = "ksm3/d"
    KSM3_SM3 = "ksm3/sm3"
    K_V = "kV"
    K_W_1 = "kW"
    K_W_H = "kW.h"
    K_W_H_DM3 = "kW.h/dm3"
    K_W_H_KG = "kW.h/kg"
    K_W_H_KG_DEG_C = "kW.h/kg.degC"
    K_W_H_M3 = "kW.h/m3"
    K_W_CM2 = "kW/cm2"
    K_W_M2 = "kW/m2"
    K_W_M2_K = "kW/m2.K"
    K_W_M3 = "kW/m3"
    K_W_M3_K = "kW/m3.K"
    L = "L"
    L_100KG = "L/100kg"
    L_100KM = "L/100km"
    L_10BBL = "L/10bbl"
    L_BAR_MIN = "L/bar.min"
    L_H = "L/h"
    L_KG = "L/kg"
    L_KM_100 = "L/km(100)"
    L_M_1 = "L/m"
    L_M3 = "L/m3"
    L_MIN = "L/min"
    L_MOL_G = "L/mol(g)"
    L_MOL_KG = "L/mol(kg)"
    L_S = "L/s"
    L_S2 = "L/s2"
    L_T = "L/t"
    L_TON_UK = "L/tonUK"
    LBF = "lbf"
    LBF_FT = "lbf.ft"
    LBF_FT_BBL = "lbf.ft/bbl"
    LBF_FT_IN = "lbf.ft/in"
    LBF_FT_IN2 = "lbf.ft/in2"
    LBF_FT_LBM = "lbf.ft/lbm"
    LBF_IN = "lbf.in"
    LBF_IN_IN = "lbf.in/in"
    LBF_IN2 = "lbf.in2"
    LBF_S_FT2 = "lbf.s/ft2"
    LBF_S_IN2 = "lbf.s/in2"
    LBF_100FT = "lbf/100ft"
    LBF_100FT2 = "lbf/100ft2"
    LBF_30M = "lbf/30m"
    LBF_FT_1 = "lbf/ft"
    LBF_FT2 = "lbf/ft2"
    LBF_FT2_100 = "lbf/ft2(100)"
    LBF_FT3 = "lbf/ft3"
    LBF_GAL_US = "lbf/galUS"
    LBF_IN_1 = "lbf/in"
    LBF_IN2_1 = "lbf/in2"
    LBF_LBF = "lbf/lbf"
    LBM = "lbm"
    LBM_FT_S = "lbm.ft/s"
    LBM_FT2 = "lbm.ft2"
    LBM_FT2_S2 = "lbm.ft2/s2"
    LBM_MILLION_YR = "lbm(million)/yr"
    LBM_1000GAL_UK = "lbm/1000galUK"
    LBM_1000GAL_US = "lbm/1000galUS"
    LBM_100FT2 = "lbm/100ft2"
    LBM_10BBL = "lbm/10bbl"
    LBM_BBL = "lbm/bbl"
    LBM_D = "lbm/d"
    LBM_FT = "lbm/ft"
    LBM_FT_H = "lbm/ft.h"
    LBM_FT_S_1 = "lbm/ft.s"
    LBM_FT2_1 = "lbm/ft2"
    LBM_FT3 = "lbm/ft3"
    LBM_FT4 = "lbm/ft4"
    LBM_GAL_UK = "lbm/galUK"
    LBM_GAL_UK_FT = "lbm/galUK.ft"
    LBM_GAL_UK_1000 = "lbm/galUK(1000)"
    LBM_GAL_US = "lbm/galUS"
    LBM_GAL_US_FT = "lbm/galUS.ft"
    LBM_GAL_US_1000 = "lbm/galUS(1000)"
    LBM_H = "lbm/h"
    LBM_H_FT = "lbm/h.ft"
    LBM_H_FT2 = "lbm/h.ft2"
    LBM_HP_H = "lbm/hp.h"
    LBM_IN3 = "lbm/in3"
    LBM_MBBL = "lbm/Mbbl"
    LBM_MIN = "lbm/min"
    LBM_S = "lbm/s"
    LBM_S_FT = "lbm/s.ft"
    LBM_S_FT2 = "lbm/s.ft2"
    LK_BN_A = "lkBnA"
    LK_BN_B = "lkBnB"
    LK_CLA = "lkCla"
    LK_SE = "lkSe"
    LK_US = "lkUS"
    LM_M2 = "lm/m2"
    M_FT3 = "M(ft3)"
    M_FT3_ACRE_FT = "M(ft3)/acre.ft"
    M_FT3_D = "M(ft3)/d"
    M_M3 = "M(m3)"
    M_M3_D = "M(m3)/d"
    M_30M = "m/30m"
    M_CM = "m/cm"
    M_D = "m/d"
    M_H = "m/h"
    M_KM = "m/km"
    M_M = "m/m"
    M_M_K = "m/m.K"
    M_M3_1 = "m/m3"
    M_MIN = "m/min"
    M_MS = "m/ms"
    M2_CM3 = "m2/cm3"
    M2_D_K_PA = "m2/d.kPa"
    M2_G = "m2/g"
    M2_H = "m2/h"
    M2_M2 = "m2/m2"
    M2_M3 = "m2/m3"
    M3_STD_0_C = "m3(std,0C)"
    M3_STD_15_C = "m3(std,15C)"
    M3_BAR_D = "m3/bar.d"
    M3_BAR_H = "m3/bar.h"
    M3_BAR_MIN = "m3/bar.min"
    M3_C_P_D_K_PA = "m3/cP.d.kPa"
    M3_C_P_PA_S = "m3/cP.Pa.s"
    M3_D = "m3/d"
    M3_D_K_PA = "m3/d.kPa"
    M3_D_M = "m3/d.m"
    M3_D2 = "m3/d2"
    M3_G = "m3/g"
    M3_H = "m3/h"
    M3_H_M = "m3/h.m"
    M3_HA_M = "m3/ha.m"
    M3_KM = "m3/km"
    M3_K_PA_D = "m3/kPa.d"
    M3_K_PA_H = "m3/kPa.h"
    M3_K_W_H = "m3/kW.h"
    M3_M = "m3/m"
    M3_M2 = "m3/m2"
    M3_M3 = "m3/m3"
    M3_MIN = "m3/min"
    M3_MOL_KG = "m3/mol(kg)"
    M3_PSI_D = "m3/psi.d"
    M3_S_FT = "m3/s.ft"
    M3_S_M = "m3/s.m"
    M3_S_M2 = "m3/s.m2"
    M3_T = "m3/t"
    M3_TON_UK = "m3/tonUK"
    M3_TON_US = "m3/tonUS"
    M_A = "mA"
    MA_1 = "Ma"
    MA_2 = "MA"
    M_A_CM2 = "mA/cm2"
    M_A_FT2 = "mA/ft2"
    MBAR = "mbar"
    MBBL = "Mbbl"
    MBBL_FT_D = "Mbbl.ft/d"
    MBBL_D = "Mbbl/d"
    MBQ = "MBq"
    MBTU_HR = "MBtu/hr"
    MBYTE = "Mbyte"
    M_C = "mC"
    M_C_M2 = "mC/m2"
    MCF = "Mcf"
    M_CI = "mCi"
    MCURIE = "mcurie"
    M_D_1 = "mD"
    M_D_FT = "mD.ft"
    M_D_FT2_LBF_S = "mD.ft2/lbf.s"
    M_D_IN2_LBF_S = "mD.in2/lbf.s"
    M_D_M = "mD.m"
    M_D_C_P = "mD/cP"
    M_D_PA_S = "mD/Pa.s"
    MEQ = "meq"
    MEQ_100G = "meq/100g"
    MEQ_CM3 = "meq/cm3"
    MEQ_G = "meq/g"
    M_EUC = "mEuc"
    ME_V = "MeV"
    MFLOPS = "Mflops"
    MG = "Mg"
    MG_1 = "mg"
    MG_A = "Mg/a"
    MG_D = "Mg/d"
    MG_DM3 = "mg/dm3"
    MG_GAL_US = "mg/galUS"
    MG_H = "Mg/h"
    MG_IN = "Mg/in"
    MG_J = "mg/J"
    MG_KG = "mg/kg"
    MG_L = "mg/L"
    MG_M2 = "Mg/m2"
    MG_M3 = "mg/m3"
    MG_M3_1 = "Mg/m3"
    M_GAL = "mGal"
    MGAUSS = "mgauss"
    M_GER = "mGer"
    MGF = "Mgf"
    MGN = "mgn"
    M_GY = "mGy"
    M_H_1 = "mH"
    MHO = "mho"
    MHO_M = "mho/m"
    MHZ = "MHz"
    M_HZ_1 = "mHz"
    MI = "mi"
    MI_GAL_UK = "mi/galUK"
    MI_GAL_US = "mi/galUS"
    MI_H = "mi/h"
    MI_IN = "mi/in"
    MI2 = "mi2"
    MI3 = "mi3"
    MIL = "mil"
    MIL_YR = "mil/yr"
    MILA = "mila"
    MIN = "min"
    MIN_FT = "min/ft"
    MIN_M = "min/m"
    MINA = "mina"
    MI_US = "miUS"
    MI_US2 = "miUS2"
    MJ = "MJ"
    M_J_1 = "mJ"
    MJ_A = "MJ/a"
    M_J_CM2 = "mJ/cm2"
    MJ_KG = "MJ/kg"
    MJ_M = "MJ/m"
    M_J_M2 = "mJ/m2"
    MJ_M3 = "MJ/m3"
    MJ_MOL_KG = "MJ/mol(kg)"
    M_K_M_1 = "mK/m"
    M_L = "mL"
    M_L_GAL_UK = "mL/galUK"
    M_L_GAL_US = "mL/galUS"
    M_L_M_L = "mL/mL"
    MLBM_YR = "Mlbm/yr"
    MM_1 = "mm"
    MM_4 = "Mm"
    MM_A = "mm/a"
    MM_MM_K = "mm/mm.K"
    MM_S_1 = "mm/s"
    MM2 = "mm2"
    MM2_MM2 = "mm2/mm2"
    MM2_S = "mm2/s"
    MM3_2 = "mm3"
    MM3_J = "mm3/J"
    MMBBL = "MMbbl"
    MMBBL_ACRE_FT = "MMbbl/acre.ft"
    MMCF = "MMcf"
    MM_HG_0_C = "mmHg(0C)"
    MMHO_M = "mmho/m"
    MMOL = "mmol"
    MMSCF_60_F = "MMscf(60F)"
    MMSCF_60_F_D = "MMscf(60F)/d"
    MMSCF60_STB60 = "MMscf60/stb60"
    MMSCM_15_C = "MMscm(15C)"
    MMSCM_15_C_D = "MMscm(15C)/d"
    MMSTB_60_F = "MMstb(60F)"
    MMSTB_60_F_D = "MMstb(60F)/d"
    MMSTB_ACRE = "MMstb/acre"
    MMSTB_ACRE_FT = "MMstb/acre.ft"
    MN = "MN"
    M_N_1 = "mN"
    M_N_M2 = "mN.m2"
    M_N_KM = "mN/km"
    M_N_M = "mN/m"
    MOHM = "Mohm"
    MOHM_1 = "mohm"
    MOHM_M = "mohm/m"
    MOL_G = "mol(g)"
    MOL_KG = "mol(kg)"
    MOL_KG_H = "mol(kg)/h"
    MOL_KG_M3 = "mol(kg)/m3"
    MOL_KG_S = "mol(kg)/s"
    MOL_LBM = "mol(lbm)"
    MOL_LBM_FT3 = "mol(lbm)/ft3"
    MOL_LBM_GAL_UK = "mol(lbm)/galUK"
    MOL_LBM_GAL_US = "mol(lbm)/galUS"
    MOL_LBM_H = "mol(lbm)/h"
    MOL_LBM_H_FT2 = "mol(lbm)/h.ft2"
    MOL_LBM_S = "mol(lbm)/s"
    MOL_LBM_S_FT2 = "mol(lbm)/s.ft2"
    M_PA = "mPa"
    MPA_1 = "MPa"
    M_PA_S = "mPa.s"
    MPA_S_M = "MPa.s/m"
    MPA_H = "MPa/h"
    MPA_M = "MPa/m"
    MPSI = "Mpsi"
    MRAD = "mrad"
    MRAD_1 = "Mrad"
    MREM = "mrem"
    MREM_H = "mrem/h"
    M_S_1 = "mS"
    MS_3 = "ms"
    MS_2_1 = "ms/2"
    MS_CM = "ms/cm"
    MS_FT = "ms/ft"
    MS_IN = "ms/in"
    M_S_M = "mS/m"
    MS_M_1 = "ms/m"
    MS_S = "ms/s"
    MSCF_60_F = "Mscf(60F)"
    MSCF_60_F_D = "Mscf(60F)/d"
    MSCF60_STB60 = "Mscf60/stb60"
    MSCM_15_C_D = "Mscm(15C)/d"
    MSECA = "mseca"
    MSM3 = "Msm3"
    MSTB_60_F = "Mstb(60F)"
    MSTB_60_F_D = "Mstb(60F)/d"
    M_SV = "mSv"
    M_SV_H = "mSv/h"
    M_T = "mT"
    MV = "MV"
    M_V_1 = "mV"
    M_V_FT = "mV/ft"
    M_V_M = "mV/m"
    MW = "MW"
    M_W_1 = "mW"
    MW_H = "MW.h"
    MW_H_KG = "MW.h/kg"
    MW_H_M3 = "MW.h/m3"
    M_W_M2 = "mW/m2"
    M_WB = "mWb"
    MY = "MY"
    N_M_1 = "N.m"
    N_M_M = "N.m/m"
    N_S_M2 = "N.s/m2"
    N_30M = "N/30m"
    N_M2_1 = "N/m2"
    N_MM2 = "N/mm2"
    N_A = "nA"
    NAUTMI = "nautmi"
    N_C = "nC"
    N_CI = "nCi"
    NCURIE = "ncurie"
    N_EUC = "nEuc"
    N_H = "nH"
    N_J = "nJ"
    NM_4 = "nm"
    NM_S = "nm/s"
    NOHM = "nohm"
    NS = "ns"
    NS_FT = "ns/ft"
    NS_M = "ns/m"
    N_T = "nT"
    N_W = "nW"
    OE = "Oe"
    OHM_CM = "ohm.cm"
    OHM_KM = "ohm/km"
    OZ_AV = "oz(av)"
    OZ_TROY = "oz(troy)"
    OZF = "ozf"
    OZM = "ozm"
    P = "P"
    P_A_1 = "pA"
    PA_S2_M3 = "Pa.s2/m3"
    PA_G = "Pa(g)"
    PA_H = "Pa/h"
    P_C = "pC"
    P_CI = "pCi"
    P_CI_G = "pCi/g"
    PCURIE = "pcurie"
    PDL = "pdl"
    PDL_CM2 = "pdl.cm2"
    PDL_FT = "pdl.ft"
    PDL_CM = "pdl/cm"
    PERMIL = "permil"
    P_F = "pF"
    PM = "pm"
    P_PA = "pPa"
    PPDK = "ppdk"
    PPK = "ppk"
    PPM = "ppm"
    PPM_DEG_C = "ppm/degC"
    PPM_DEG_F = "ppm/degF"
    PS = "ps"
    P_S_1 = "pS"
    PSF = "psf"
    PSI = "psi"
    PSI_D_BBL = "psi.d/bbl"
    PSI_S = "psi.s"
    PSI_100FT = "psi/100ft"
    PSI_FT = "psi/ft"
    PSI_FT_100 = "psi/ft(100)"
    PSI_H = "psi/h"
    PSI_KFT = "psi/kft"
    PSI_M = "psi/m"
    PSI_MIN = "psi/min"
    PSI2 = "psi2"
    PSI2_D_C_P_FT3 = "psi2.d/cP.ft3"
    PSI2_D_CP_FT3_1 = "psi2.d/cp.ft3"
    PSI2_D2_C_P_FT6 = "psi2.d2/cP.ft6"
    PSI2_D2_CP_FT6_1 = "psi2.d2/cp.ft6"
    PSI2_C_P = "psi2/cP"
    PSIA = "psia"
    PSIG = "psig"
    PT_UK = "ptUK"
    PT_UK_HP_HR = "ptUK/hp.hr"
    PT_UK_MBBL = "ptUK/Mbbl"
    PT_US = "ptUS"
    PT_US_10BBL = "ptUS/10bbl"
    QT_UK = "qtUK"
    QT_US = "qtUS"
    QUAD = "quad"
    QUAD_YR = "quad/yr"
    RAD_FT = "rad/ft"
    RAD_FT3 = "rad/ft3"
    RD = "rd"
    REM = "rem"
    REM_H = "rem/h"
    REV_MIN = "rev/min"
    REV_S = "rev/s"
    RPM = "rpm"
    RPM_S = "rpm/s"
    S_CM = "s/cm"
    S_FT = "s/ft"
    S_FT3 = "s/ft3"
    S_IN = "s/in"
    S_L = "s/L"
    S_QT_UK = "s/qtUK"
    S_QT_US = "s/qtUS"
    SACK94 = "sack94"
    SCF_60_F = "scf(60F)"
    SCF_60_F_BBL = "scf(60F)/bbl"
    SCF_60_F_D = "scf(60F)/d"
    SCF_60_F_FT2 = "scf(60F)/ft2"
    SCF_60_F_FT3 = "scf(60F)/ft3"
    SCM_15_C_D = "scm(15C)/d"
    SCM15_STB60 = "scm15/stb60"
    SECA = "seca"
    SIGMA = "sigma"
    SM3_KSM3 = "sm3/ksm3"
    SM3_SM3 = "sm3/sm3"
    SQ_FT = "sq ft"
    SQ_IN = "sq in"
    SQ_MI = "sq mi"
    SQ_YD = "sq yd"
    STB_60_F = "stb(60F)"
    STB_60_F_ACRE = "stb(60F)/acre"
    STB_60_F_BBL = "stb(60F)/bbl"
    STB_60_F_D = "stb(60F)/d"
    STB60_MMSCF60 = "stb60/MMscf60"
    STB60_MMSCM15 = "stb60/MMscm15"
    STB60_MSCF60 = "stb60/Mscf60"
    STB60_MSCM15 = "stb60/Mscm15"
    STB60_SCM15 = "stb60/scm15"
    SV_H = "Sv/h"
    T_1 = "t"
    T_A = "t/a"
    T_D = "t/d"
    T_H = "t/h"
    T_MIN = "t/min"
    TALBOT = "talbot"
    TBQ = "TBq"
    TCF = "tcf"
    TE_V = "TeV"
    THERM = "therm"
    THERM_FT3 = "therm/ft3"
    THERM_GAL_UK = "therm/galUK"
    THERM_LBM = "therm/lbm"
    TJ = "TJ"
    TJ_A = "TJ/a"
    TOHM = "Tohm"
    TON_OF_REFRIG = "ton of refrig"
    TONF_UK = "tonfUK"
    TONF_UK_FT2 = "tonfUK.ft2"
    TONF_UK_FT = "tonfUK/ft"
    TONF_UK_FT2_1 = "tonfUK/ft2"
    TONF_US = "tonfUS"
    TONF_US_FT = "tonfUS.ft"
    TONF_US_FT2 = "tonfUS.ft2"
    TONF_US_MI = "tonfUS.mi"
    TONF_US_MI_BBL = "tonfUS.mi/bbl"
    TONF_US_MI_FT = "tonfUS.mi/ft"
    TONF_US_FT_1 = "tonfUS/ft"
    TONF_US_FT2_1 = "tonfUS/ft2"
    TONF_US_IN2 = "tonfUS/in2"
    TON_UK = "tonUK"
    TON_UK_A = "tonUK/a"
    TON_UK_D = "tonUK/d"
    TON_UK_H = "tonUK/h"
    TON_UK_MIN = "tonUK/min"
    TON_US = "tonUS"
    TON_US_A = "tonUS/a"
    TON_US_D = "tonUS/d"
    TON_US_FT2 = "tonUS/ft2"
    TON_US_H = "tonUS/h"
    TON_US_MIN = "tonUS/min"
    TORR = "torr"
    TW = "TW"
    TW_H = "TW.h"
    U_A = "uA"
    U_A_CM2 = "uA/cm2"
    U_A_IN2 = "uA/in2"
    UBAR = "ubar"
    U_C = "uC"
    UCAL_S_CM2 = "ucal/s.cm2"
    U_CI = "uCi"
    UCURIE = "ucurie"
    U_EUC = "uEuc"
    U_F = "uF"
    U_F_M = "uF/m"
    UG = "ug"
    UG_CM3 = "ug/cm3"
    U_H = "uH"
    U_H_M = "uH/m"
    U_HZ = "uHz"
    U_J = "uJ"
    UM = "um"
    UM_S = "um/s"
    UM2 = "um2"
    UM2_M = "um2.m"
    UM_HG_0_C = "umHg(0C)"
    UMOL = "umol"
    U_N = "uN"
    UNITLESS = "unitless"
    UOHM = "uohm"
    UOHM_FT = "uohm/ft"
    UOHM_M = "uohm/m"
    U_PA = "uPa"
    UPSI = "upsi"
    URAD = "urad"
    U_S = "uS"
    US_1 = "us"
    US_FT = "us/ft"
    US_M = "us/m"
    U_T = "uT"
    U_V = "uV"
    U_V_FT = "uV/ft"
    U_V_M = "uV/m"
    U_W = "uW"
    U_W_M3 = "uW/m3"
    U_WB = "uWb"
    V_D_B = "V/dB"
    VOLPERCENT = "volpercent"
    VOLPPM = "volppm"
    W_CM2 = "W/cm2"
    W_K_W = "W/kW"
    W_MM2 = "W/mm2"
    W_W = "W/W"
    WB_MM = "Wb/mm"
    WK_1 = "wk"
    WTPERCENT = "wtpercent"
    WTPPM = "wtppm"
    YD = "yd"
    YD2 = "yd2"
    YD3 = "yd3"
    YD_BN_A = "ydBnA"
    YD_BN_B = "ydBnB"
    YD_CLA = "ydCla"
    YD_IM = "ydIm"
    YD_IND = "ydInd"
    YD_IND_37 = "ydInd(37)"
    YD_IND_62 = "ydInd(62)"
    YD_IND_75 = "ydInd(75)"
    YD_SE = "ydSe"
    YR_100K = "yr(100k)"
    UM01 = "um01"
    UM02 = "um02"
    UM03 = "um03"
    UM04 = "um04"
    UM05 = "um05"
    UM06 = "um06"
    UM07 = "um07"
    UM08 = "um08"
    UM09 = "um09"
    UM10 = "um10"
    UM11 = "um11"
    UM12 = "um12"
    UM13 = "um13"
    UM14 = "um14"
    UM15 = "um15"
    UM16 = "um16"
    UM17 = "um17"
    UM18 = "um18"
    UM19 = "um19"
    UM20 = "um20"
    UM21 = "um21"
    UM22 = "um22"
    UM23 = "um23"
    UM24 = "um24"
    UM25 = "um25"
    UM26 = "um26"
    UM27 = "um27"
    UM28 = "um28"
    UM29 = "um29"
    UM30 = "um30"
    UM31 = "um31"
    UM32 = "um32"
    UM33 = "um33"
    UM34 = "um34"
    UM35 = "um35"
    UM36 = "um36"
    UM37 = "um37"
    UM38 = "um38"
    UM39 = "um39"
    UM40 = "um40"
    UM41 = "um41"
    UM42 = "um42"
    UM43 = "um43"
    UM44 = "um44"
    UM45 = "um45"
    UM46 = "um46"
    UM47 = "um47"
    UM48 = "um48"
    UM49 = "um49"
    UM50 = "um50"
    UM51 = "um51"
    UM52 = "um52"
    UM53 = "um53"
    UM54 = "um54"
    UM55 = "um55"
    UM56 = "um56"
    UM57 = "um57"
    UM58 = "um58"
    UM59 = "um59"
    UM60 = "um60"
    UM61 = "um61"
    UM62 = "um62"
    UM63 = "um63"
    UM64 = "um64"
    UM65 = "um65"
    UM66 = "um66"
    UM67 = "um67"
    UM68 = "um68"
    UM69 = "um69"
    UM70 = "um70"
    UM71 = "um71"
    UM72 = "um72"
    UM73 = "um73"
    UM74 = "um74"
    UM75 = "um75"
    UM76 = "um76"
    UM77 = "um77"
    UM78 = "um78"
    UM79 = "um79"
    UM80 = "um80"
    UM81 = "um81"
    UM82 = "um82"
    UM83 = "um83"
    UM84 = "um84"
    UM85 = "um85"
    UM86 = "um86"
    UM87 = "um87"
    UM88 = "um88"
    UM89 = "um89"
    UM90 = "um90"
    UM91 = "um91"
    UM92 = "um92"
    UM93 = "um93"
    UM94 = "um94"
    UM95 = "um95"
    UM96 = "um96"
    UM97 = "um97"
    UM98 = "um98"
    UM99 = "um99"


@dataclass(kw_only=True)
class RealValue:
    class Meta:
        name = "realValue"

    value: str = field(default="")


class ReferenceUsageAttType(Enum):
    RUS01 = "rus01"
    RUS02 = "rus02"
    RUS03 = "rus03"
    RUS04 = "rus04"
    RUS05 = "rus05"
    RUS06 = "rus06"
    RUS07 = "rus07"
    RUS08 = "rus08"
    RUS09 = "rus09"
    RUS10 = "rus10"
    RUS11 = "rus11"
    RUS12 = "rus12"
    RUS13 = "rus13"
    RUS14 = "rus14"
    RUS15 = "rus15"
    RUS16 = "rus16"
    RUS17 = "rus17"
    RUS18 = "rus18"
    RUS19 = "rus19"
    RUS20 = "rus20"
    RUS21 = "rus21"
    RUS22 = "rus22"
    RUS23 = "rus23"
    RUS24 = "rus24"
    RUS25 = "rus25"
    RUS26 = "rus26"
    RUS27 = "rus27"
    RUS28 = "rus28"
    RUS29 = "rus29"
    RUS30 = "rus30"
    RUS31 = "rus31"
    RUS32 = "rus32"
    RUS33 = "rus33"
    RUS34 = "rus34"
    RUS35 = "rus35"
    RUS36 = "rus36"
    RUS37 = "rus37"
    RUS38 = "rus38"
    RUS39 = "rus39"
    RUS40 = "rus40"
    RUS41 = "rus41"
    RUS42 = "rus42"
    RUS43 = "rus43"
    RUS44 = "rus44"
    RUS45 = "rus45"
    RUS46 = "rus46"
    RUS47 = "rus47"
    RUS48 = "rus48"
    RUS49 = "rus49"
    RUS50 = "rus50"
    RUS51 = "rus51"
    RUS52 = "rus52"
    RUS53 = "rus53"
    RUS54 = "rus54"
    RUS55 = "rus55"
    RUS56 = "rus56"
    RUS57 = "rus57"
    RUS58 = "rus58"
    RUS59 = "rus59"
    RUS60 = "rus60"
    RUS61 = "rus61"
    RUS62 = "rus62"
    RUS63 = "rus63"
    RUS64 = "rus64"
    RUS65 = "rus65"
    RUS66 = "rus66"
    RUS67 = "rus67"
    RUS68 = "rus68"
    RUS69 = "rus69"
    RUS70 = "rus70"
    RUS71 = "rus71"
    RUS72 = "rus72"
    RUS73 = "rus73"
    RUS74 = "rus74"
    RUS75 = "rus75"
    RUS76 = "rus76"
    RUS77 = "rus77"
    RUS78 = "rus78"
    RUS79 = "rus79"
    RUS80 = "rus80"
    RUS81 = "rus81"
    RUS82 = "rus82"
    RUS83 = "rus83"
    RUS84 = "rus84"
    RUS85 = "rus85"
    RUS86 = "rus86"
    RUS87 = "rus87"
    RUS88 = "rus88"
    RUS89 = "rus89"
    RUS90 = "rus90"
    RUS91 = "rus91"
    RUS92 = "rus92"
    RUS93 = "rus93"
    RUS94 = "rus94"
    RUS95 = "rus95"
    RUS96 = "rus96"
    RUS97 = "rus97"
    RUS98 = "rus98"
    RUS99 = "rus99"


@dataclass(kw_only=True)
class Room:
    class Meta:
        name = "room"

    value: str = field(default="")


class SafetyCategoryValueAttType(Enum):
    A = "A"
    B = "B"
    C = "C"


class SecurityClassificationAttType(Enum):
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_18 = "18"
    VALUE_19 = "19"
    VALUE_20 = "20"
    VALUE_21 = "21"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_24 = "24"
    VALUE_25 = "25"
    VALUE_26 = "26"
    VALUE_27 = "27"
    VALUE_28 = "28"
    VALUE_29 = "29"
    VALUE_30 = "30"
    VALUE_31 = "31"
    VALUE_32 = "32"
    VALUE_33 = "33"
    VALUE_34 = "34"
    VALUE_35 = "35"
    VALUE_36 = "36"
    VALUE_37 = "37"
    VALUE_38 = "38"
    VALUE_39 = "39"
    VALUE_40 = "40"
    VALUE_41 = "41"
    VALUE_42 = "42"
    VALUE_43 = "43"
    VALUE_44 = "44"
    VALUE_45 = "45"
    VALUE_46 = "46"
    VALUE_47 = "47"
    VALUE_48 = "48"
    VALUE_49 = "49"
    VALUE_50 = "50"
    VALUE_51 = "51"
    VALUE_52 = "52"
    VALUE_53 = "53"
    VALUE_54 = "54"
    VALUE_55 = "55"
    VALUE_56 = "56"
    VALUE_57 = "57"
    VALUE_58 = "58"
    VALUE_59 = "59"
    VALUE_60 = "60"
    VALUE_61 = "61"
    VALUE_62 = "62"
    VALUE_63 = "63"
    VALUE_64 = "64"
    VALUE_65 = "65"
    VALUE_66 = "66"
    VALUE_67 = "67"
    VALUE_68 = "68"
    VALUE_69 = "69"
    VALUE_70 = "70"
    VALUE_71 = "71"
    VALUE_72 = "72"
    VALUE_73 = "73"
    VALUE_74 = "74"
    VALUE_75 = "75"
    VALUE_76 = "76"
    VALUE_77 = "77"
    VALUE_78 = "78"
    VALUE_79 = "79"
    VALUE_80 = "80"
    VALUE_81 = "81"
    VALUE_82 = "82"
    VALUE_83 = "83"
    VALUE_84 = "84"
    VALUE_85 = "85"
    VALUE_86 = "86"
    VALUE_87 = "87"
    VALUE_88 = "88"
    VALUE_89 = "89"
    VALUE_90 = "90"
    VALUE_91 = "91"
    VALUE_92 = "92"
    VALUE_93 = "93"
    VALUE_94 = "94"
    VALUE_95 = "95"
    VALUE_96 = "96"
    VALUE_97 = "97"
    VALUE_98 = "98"
    VALUE_99 = "99"


class SetActionAttType(Enum):
    EMPTY = "empty"
    SIZE_OF = "sizeOf"


class SetOperationAttType(Enum):
    ADD = "add"
    DISJOINT = "disjoint"
    EQUAL = "equal"
    INTERSECTION = "intersection"
    MEMBER = "member"
    NOT_EQUAL = "notEqual"
    REMOVE = "remove"
    SET_DIFFERENCE = "setDifference"
    SUBSET = "subset"
    UNION = "union"


@dataclass(kw_only=True)
class ShortPmTitle:
    class Meta:
        name = "shortPmTitle"

    value: str = field(default="")


class ShowPluginControlsAttType(Enum):
    HIDE = "hide"
    SHOW = "show"


class SignificantParaDataTypeAttType(Enum):
    PSD01 = "psd01"
    PSD02 = "psd02"
    PSD03 = "psd03"
    PSD04 = "psd04"
    PSD05 = "psd05"
    PSD06 = "psd06"
    PSD07 = "psd07"
    PSD08 = "psd08"
    PSD09 = "psd09"
    PSD10 = "psd10"
    PSD11 = "psd11"
    PSD12 = "psd12"
    PSD13 = "psd13"
    PSD14 = "psd14"
    PSD15 = "psd15"
    PSD16 = "psd16"
    PSD17 = "psd17"
    PSD18 = "psd18"
    PSD19 = "psd19"
    PSD20 = "psd20"
    PSD21 = "psd21"
    PSD22 = "psd22"
    PSD23 = "psd23"
    PSD24 = "psd24"
    PSD25 = "psd25"
    PSD26 = "psd26"
    PSD27 = "psd27"
    PSD28 = "psd28"
    PSD29 = "psd29"
    PSD30 = "psd30"
    PSD31 = "psd31"
    PSD32 = "psd32"
    PSD33 = "psd33"
    PSD34 = "psd34"
    PSD35 = "psd35"
    PSD36 = "psd36"
    PSD37 = "psd37"
    PSD38 = "psd38"
    PSD39 = "psd39"
    PSD40 = "psd40"
    PSD41 = "psd41"
    PSD42 = "psd42"
    PSD43 = "psd43"
    PSD44 = "psd44"
    PSD45 = "psd45"
    PSD46 = "psd46"
    PSD47 = "psd47"
    PSD48 = "psd48"
    PSD49 = "psd49"
    PSD50 = "psd50"
    PSD51 = "psd51"
    PSD52 = "psd52"
    PSD53 = "psd53"
    PSD54 = "psd54"
    PSD55 = "psd55"
    PSD56 = "psd56"
    PSD57 = "psd57"
    PSD58 = "psd58"
    PSD59 = "psd59"
    PSD60 = "psd60"
    PSD61 = "psd61"
    PSD62 = "psd62"
    PSD63 = "psd63"
    PSD64 = "psd64"
    PSD65 = "psd65"
    PSD66 = "psd66"
    PSD67 = "psd67"
    PSD68 = "psd68"
    PSD69 = "psd69"
    PSD70 = "psd70"
    PSD71 = "psd71"
    PSD72 = "psd72"
    PSD73 = "psd73"
    PSD74 = "psd74"
    PSD75 = "psd75"
    PSD76 = "psd76"
    PSD77 = "psd77"
    PSD78 = "psd78"
    PSD79 = "psd79"
    PSD80 = "psd80"
    PSD81 = "psd81"
    PSD82 = "psd82"
    PSD83 = "psd83"
    PSD84 = "psd84"
    PSD85 = "psd85"
    PSD86 = "psd86"
    PSD87 = "psd87"
    PSD88 = "psd88"
    PSD89 = "psd89"
    PSD90 = "psd90"
    PSD91 = "psd91"
    PSD92 = "psd92"
    PSD93 = "psd93"
    PSD94 = "psd94"
    PSD95 = "psd95"
    PSD96 = "psd96"
    PSD97 = "psd97"
    PSD98 = "psd98"
    PSD99 = "psd99"


class SkillLevelCodeAttType(Enum):
    SK01 = "sk01"
    SK02 = "sk02"
    SK03 = "sk03"
    SK04 = "sk04"
    SK05 = "sk05"
    SK06 = "sk06"
    SK07 = "sk07"
    SK08 = "sk08"
    SK09 = "sk09"
    SK10 = "sk10"
    SK11 = "sk11"
    SK12 = "sk12"
    SK13 = "sk13"
    SK14 = "sk14"
    SK15 = "sk15"
    SK16 = "sk16"
    SK17 = "sk17"
    SK18 = "sk18"
    SK19 = "sk19"
    SK20 = "sk20"
    SK21 = "sk21"
    SK22 = "sk22"
    SK23 = "sk23"
    SK24 = "sk24"
    SK25 = "sk25"
    SK26 = "sk26"
    SK27 = "sk27"
    SK28 = "sk28"
    SK29 = "sk29"
    SK30 = "sk30"
    SK31 = "sk31"
    SK32 = "sk32"
    SK33 = "sk33"
    SK34 = "sk34"
    SK35 = "sk35"
    SK36 = "sk36"
    SK37 = "sk37"
    SK38 = "sk38"
    SK39 = "sk39"
    SK40 = "sk40"
    SK41 = "sk41"
    SK42 = "sk42"
    SK43 = "sk43"
    SK44 = "sk44"
    SK45 = "sk45"
    SK46 = "sk46"
    SK47 = "sk47"
    SK48 = "sk48"
    SK49 = "sk49"
    SK50 = "sk50"
    SK51 = "sk51"
    SK52 = "sk52"
    SK53 = "sk53"
    SK54 = "sk54"
    SK55 = "sk55"
    SK56 = "sk56"
    SK57 = "sk57"
    SK58 = "sk58"
    SK59 = "sk59"
    SK60 = "sk60"
    SK61 = "sk61"
    SK62 = "sk62"
    SK63 = "sk63"
    SK64 = "sk64"
    SK65 = "sk65"
    SK66 = "sk66"
    SK67 = "sk67"
    SK68 = "sk68"
    SK69 = "sk69"
    SK70 = "sk70"
    SK71 = "sk71"
    SK72 = "sk72"
    SK73 = "sk73"
    SK74 = "sk74"
    SK75 = "sk75"
    SK76 = "sk76"
    SK77 = "sk77"
    SK78 = "sk78"
    SK79 = "sk79"
    SK80 = "sk80"
    SK81 = "sk81"
    SK82 = "sk82"
    SK83 = "sk83"
    SK84 = "sk84"
    SK85 = "sk85"
    SK86 = "sk86"
    SK87 = "sk87"
    SK88 = "sk88"
    SK89 = "sk89"
    SK90 = "sk90"
    SK91 = "sk91"
    SK92 = "sk92"
    SK93 = "sk93"
    SK94 = "sk94"
    SK95 = "sk95"
    SK96 = "sk96"
    SK97 = "sk97"
    SK98 = "sk98"
    SK99 = "sk99"


class SoftwareClassificationValueAttType(Enum):
    SCV01 = "scv01"
    SCV02 = "scv02"
    SCV03 = "scv03"
    SCV04 = "scv04"
    SCV05 = "scv05"
    SCV06 = "scv06"
    SCV07 = "scv07"
    SCV08 = "scv08"
    SCV09 = "scv09"
    SCV10 = "scv10"
    SCV11 = "scv11"
    SCV12 = "scv12"
    SCV13 = "scv13"
    SCV14 = "scv14"
    SCV15 = "scv15"
    SCV16 = "scv16"
    SCV17 = "scv17"
    SCV18 = "scv18"
    SCV19 = "scv19"
    SCV20 = "scv20"
    SCV21 = "scv21"
    SCV22 = "scv22"
    SCV23 = "scv23"
    SCV24 = "scv24"
    SCV25 = "scv25"
    SCV26 = "scv26"
    SCV27 = "scv27"
    SCV28 = "scv28"
    SCV29 = "scv29"
    SCV30 = "scv30"
    SCV31 = "scv31"
    SCV32 = "scv32"
    SCV33 = "scv33"
    SCV34 = "scv34"
    SCV35 = "scv35"
    SCV36 = "scv36"
    SCV37 = "scv37"
    SCV38 = "scv38"
    SCV39 = "scv39"
    SCV40 = "scv40"
    SCV41 = "scv41"
    SCV42 = "scv42"
    SCV43 = "scv43"
    SCV44 = "scv44"
    SCV45 = "scv45"
    SCV46 = "scv46"
    SCV47 = "scv47"
    SCV48 = "scv48"
    SCV49 = "scv49"
    SCV50 = "scv50"
    SCV51 = "scv51"
    SCV52 = "scv52"
    SCV53 = "scv53"
    SCV54 = "scv54"
    SCV55 = "scv55"
    SCV56 = "scv56"
    SCV57 = "scv57"
    SCV58 = "scv58"
    SCV59 = "scv59"
    SCV60 = "scv60"
    SCV61 = "scv61"
    SCV62 = "scv62"
    SCV63 = "scv63"
    SCV64 = "scv64"
    SCV65 = "scv65"
    SCV66 = "scv66"
    SCV67 = "scv67"
    SCV68 = "scv68"
    SCV69 = "scv69"
    SCV70 = "scv70"
    SCV71 = "scv71"
    SCV72 = "scv72"
    SCV73 = "scv73"
    SCV74 = "scv74"
    SCV75 = "scv75"
    SCV76 = "scv76"
    SCV77 = "scv77"
    SCV78 = "scv78"
    SCV79 = "scv79"
    SCV80 = "scv80"
    SCV81 = "scv81"
    SCV82 = "scv82"
    SCV83 = "scv83"
    SCV84 = "scv84"
    SCV85 = "scv85"
    SCV86 = "scv86"
    SCV87 = "scv87"
    SCV88 = "scv88"
    SCV89 = "scv89"
    SCV90 = "scv90"
    SCV91 = "scv91"
    SCV92 = "scv92"
    SCV93 = "scv93"
    SCV94 = "scv94"
    SCV95 = "scv95"
    SCV96 = "scv96"
    SCV97 = "scv97"
    SCV98 = "scv98"
    SCV99 = "scv99"


class SoftwareCustomizationStatusValueAttType(Enum):
    SCS01 = "scs01"
    SCS02 = "scs02"
    SCS03 = "scs03"
    SCS04 = "scs04"
    SCS05 = "scs05"
    SCS06 = "scs06"
    SCS07 = "scs07"
    SCS08 = "scs08"
    SCS09 = "scs09"
    SCS10 = "scs10"
    SCS11 = "scs11"
    SCS12 = "scs12"
    SCS13 = "scs13"
    SCS14 = "scs14"
    SCS15 = "scs15"
    SCS16 = "scs16"
    SCS17 = "scs17"
    SCS18 = "scs18"
    SCS19 = "scs19"
    SCS20 = "scs20"
    SCS21 = "scs21"
    SCS22 = "scs22"
    SCS23 = "scs23"
    SCS24 = "scs24"
    SCS25 = "scs25"
    SCS26 = "scs26"
    SCS27 = "scs27"
    SCS28 = "scs28"
    SCS29 = "scs29"
    SCS30 = "scs30"
    SCS31 = "scs31"
    SCS32 = "scs32"
    SCS33 = "scs33"
    SCS34 = "scs34"
    SCS35 = "scs35"
    SCS36 = "scs36"
    SCS37 = "scs37"
    SCS38 = "scs38"
    SCS39 = "scs39"
    SCS40 = "scs40"
    SCS41 = "scs41"
    SCS42 = "scs42"
    SCS43 = "scs43"
    SCS44 = "scs44"
    SCS45 = "scs45"
    SCS46 = "scs46"
    SCS47 = "scs47"
    SCS48 = "scs48"
    SCS49 = "scs49"
    SCS50 = "scs50"
    SCS51 = "scs51"
    SCS52 = "scs52"
    SCS53 = "scs53"
    SCS54 = "scs54"
    SCS55 = "scs55"
    SCS56 = "scs56"
    SCS57 = "scs57"
    SCS58 = "scs58"
    SCS59 = "scs59"
    SCS60 = "scs60"
    SCS61 = "scs61"
    SCS62 = "scs62"
    SCS63 = "scs63"
    SCS64 = "scs64"
    SCS65 = "scs65"
    SCS66 = "scs66"
    SCS67 = "scs67"
    SCS68 = "scs68"
    SCS69 = "scs69"
    SCS70 = "scs70"
    SCS71 = "scs71"
    SCS72 = "scs72"
    SCS73 = "scs73"
    SCS74 = "scs74"
    SCS75 = "scs75"
    SCS76 = "scs76"
    SCS77 = "scs77"
    SCS78 = "scs78"
    SCS79 = "scs79"
    SCS80 = "scs80"
    SCS81 = "scs81"
    SCS82 = "scs82"
    SCS83 = "scs83"
    SCS84 = "scs84"
    SCS85 = "scs85"
    SCS86 = "scs86"
    SCS87 = "scs87"
    SCS88 = "scs88"
    SCS89 = "scs89"
    SCS90 = "scs90"
    SCS91 = "scs91"
    SCS92 = "scs92"
    SCS93 = "scs93"
    SCS94 = "scs94"
    SCS95 = "scs95"
    SCS96 = "scs96"
    SCS97 = "scs97"
    SCS98 = "scs98"
    SCS99 = "scs99"


class SourcingTypeValueAttType(Enum):
    STV01 = "stv01"
    STV02 = "stv02"
    STV03 = "stv03"
    STV04 = "stv04"
    STV05 = "stv05"
    STV06 = "stv06"
    STV07 = "stv07"
    STV08 = "stv08"
    STV09 = "stv09"
    STV10 = "stv10"
    STV11 = "stv11"
    STV12 = "stv12"
    STV13 = "stv13"
    STV14 = "stv14"
    STV15 = "stv15"
    STV16 = "stv16"
    STV17 = "stv17"
    STV18 = "stv18"
    STV19 = "stv19"
    STV20 = "stv20"
    STV21 = "stv21"
    STV22 = "stv22"
    STV23 = "stv23"
    STV24 = "stv24"
    STV25 = "stv25"
    STV26 = "stv26"
    STV27 = "stv27"
    STV28 = "stv28"
    STV29 = "stv29"
    STV30 = "stv30"
    STV31 = "stv31"
    STV32 = "stv32"
    STV33 = "stv33"
    STV34 = "stv34"
    STV35 = "stv35"
    STV36 = "stv36"
    STV37 = "stv37"
    STV38 = "stv38"
    STV39 = "stv39"
    STV40 = "stv40"
    STV41 = "stv41"
    STV42 = "stv42"
    STV43 = "stv43"
    STV44 = "stv44"
    STV45 = "stv45"
    STV46 = "stv46"
    STV47 = "stv47"
    STV48 = "stv48"
    STV49 = "stv49"
    STV50 = "stv50"
    STV51 = "stv51"
    STV52 = "stv52"
    STV53 = "stv53"
    STV54 = "stv54"
    STV55 = "stv55"
    STV56 = "stv56"
    STV57 = "stv57"
    STV58 = "stv58"
    STV59 = "stv59"
    STV60 = "stv60"
    STV61 = "stv61"
    STV62 = "stv62"
    STV63 = "stv63"
    STV64 = "stv64"
    STV65 = "stv65"
    STV66 = "stv66"
    STV67 = "stv67"
    STV68 = "stv68"
    STV69 = "stv69"
    STV70 = "stv70"
    STV71 = "stv71"
    STV72 = "stv72"
    STV73 = "stv73"
    STV74 = "stv74"
    STV75 = "stv75"
    STV76 = "stv76"
    STV77 = "stv77"
    STV78 = "stv78"
    STV79 = "stv79"
    STV80 = "stv80"
    STV81 = "stv81"
    STV82 = "stv82"
    STV83 = "stv83"
    STV84 = "stv84"
    STV85 = "stv85"
    STV86 = "stv86"
    STV87 = "stv87"
    STV88 = "stv88"
    STV89 = "stv89"
    STV90 = "stv90"
    STV91 = "stv91"
    STV92 = "stv92"
    STV93 = "stv93"
    STV94 = "stv94"
    STV95 = "stv95"
    STV96 = "stv96"
    STV97 = "stv97"
    STV98 = "stv98"
    STV99 = "stv99"


class SparePartClassCodeAttType(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_6 = "6"


@dataclass(kw_only=True)
class State:
    class Meta:
        name = "state"

    value: str = field(default="")


@dataclass(kw_only=True)
class Street:
    class Meta:
        name = "street"

    value: str = field(default="")


class StringActionAttType(Enum):
    EMPTY = "empty"
    SIZE_OF = "sizeOf"


class StringOperationAttType(Enum):
    CONCATENATE = "concatenate"
    CONTAINS = "contains"
    EQUAL = "equal"
    GREATER_THAN = "greaterThan"
    GREATER_THAN_OR_EQUAL = "greaterThanOrEqual"
    LESS_THAN = "lessThan"
    LESS_THAN_OR_EQUAL = "lessThanOrEqual"
    NOT_EQUAL = "notEqual"


@dataclass(kw_only=True)
class StringValue:
    class Meta:
        name = "stringValue"

    value: str = field(default="")


@dataclass(kw_only=True)
class SubScript:
    class Meta:
        name = "subScript"

    value: str = field(default="")


@dataclass(kw_only=True)
class SubStringLength:
    class Meta:
        name = "subStringLength"

    value: int = field()


@dataclass(kw_only=True)
class SubStringPosition:
    class Meta:
        name = "subStringPosition"

    value: int = field()


@dataclass(kw_only=True)
class SuperScript:
    class Meta:
        name = "superScript"

    value: str = field(default="")


class SupplementalSafetyCategoryAttType(Enum):
    SSC01 = "ssc01"
    SSC02 = "ssc02"
    SSC03 = "ssc03"
    SSC04 = "ssc04"
    SSC05 = "ssc05"
    SSC06 = "ssc06"
    SSC07 = "ssc07"
    SSC08 = "ssc08"
    SSC09 = "ssc09"
    SSC10 = "ssc10"
    SSC11 = "ssc11"
    SSC12 = "ssc12"
    SSC13 = "ssc13"
    SSC14 = "ssc14"
    SSC15 = "ssc15"
    SSC16 = "ssc16"
    SSC17 = "ssc17"
    SSC18 = "ssc18"
    SSC19 = "ssc19"
    SSC20 = "ssc20"
    SSC21 = "ssc21"
    SSC22 = "ssc22"
    SSC23 = "ssc23"
    SSC24 = "ssc24"
    SSC25 = "ssc25"
    SSC26 = "ssc26"
    SSC27 = "ssc27"
    SSC28 = "ssc28"
    SSC29 = "ssc29"
    SSC30 = "ssc30"
    SSC31 = "ssc31"
    SSC32 = "ssc32"
    SSC33 = "ssc33"
    SSC34 = "ssc34"
    SSC35 = "ssc35"
    SSC36 = "ssc36"
    SSC37 = "ssc37"
    SSC38 = "ssc38"
    SSC39 = "ssc39"
    SSC40 = "ssc40"
    SSC41 = "ssc41"
    SSC42 = "ssc42"
    SSC43 = "ssc43"
    SSC44 = "ssc44"
    SSC45 = "ssc45"
    SSC46 = "ssc46"
    SSC47 = "ssc47"
    SSC48 = "ssc48"
    SSC49 = "ssc49"
    SSC50 = "ssc50"
    SSC51 = "ssc51"
    SSC52 = "ssc52"
    SSC53 = "ssc53"
    SSC54 = "ssc54"
    SSC55 = "ssc55"
    SSC56 = "ssc56"
    SSC57 = "ssc57"
    SSC58 = "ssc58"
    SSC59 = "ssc59"
    SSC60 = "ssc60"
    SSC61 = "ssc61"
    SSC62 = "ssc62"
    SSC63 = "ssc63"
    SSC64 = "ssc64"
    SSC65 = "ssc65"
    SSC66 = "ssc66"
    SSC67 = "ssc67"
    SSC68 = "ssc68"
    SSC69 = "ssc69"
    SSC70 = "ssc70"
    SSC71 = "ssc71"
    SSC72 = "ssc72"
    SSC73 = "ssc73"
    SSC74 = "ssc74"
    SSC75 = "ssc75"
    SSC76 = "ssc76"
    SSC77 = "ssc77"
    SSC78 = "ssc78"
    SSC79 = "ssc79"
    SSC80 = "ssc80"
    SSC81 = "ssc81"
    SSC82 = "ssc82"
    SSC83 = "ssc83"
    SSC84 = "ssc84"
    SSC85 = "ssc85"
    SSC86 = "ssc86"
    SSC87 = "ssc87"
    SSC88 = "ssc88"
    SSC89 = "ssc89"
    SSC90 = "ssc90"
    SSC91 = "ssc91"
    SSC92 = "ssc92"
    SSC93 = "ssc93"
    SSC94 = "ssc94"
    SSC95 = "ssc95"
    SSC96 = "ssc96"
    SSC97 = "ssc97"
    SSC98 = "ssc98"
    SSC99 = "ssc99"


class SupplyCategoryAttType(Enum):
    SUPCAT01 = "supcat01"
    SUPCAT02 = "supcat02"
    SUPCAT03 = "supcat03"
    SUPCAT04 = "supcat04"
    SUPCAT05 = "supcat05"
    SUPCAT06 = "supcat06"
    SUPCAT07 = "supcat07"
    SUPCAT08 = "supcat08"
    SUPCAT09 = "supcat09"
    SUPCAT10 = "supcat10"
    SUPCAT11 = "supcat11"
    SUPCAT12 = "supcat12"
    SUPCAT13 = "supcat13"
    SUPCAT14 = "supcat14"
    SUPCAT15 = "supcat15"
    SUPCAT16 = "supcat16"
    SUPCAT17 = "supcat17"
    SUPCAT18 = "supcat18"
    SUPCAT19 = "supcat19"
    SUPCAT20 = "supcat20"
    SUPCAT21 = "supcat21"
    SUPCAT22 = "supcat22"
    SUPCAT23 = "supcat23"
    SUPCAT24 = "supcat24"
    SUPCAT25 = "supcat25"
    SUPCAT26 = "supcat26"
    SUPCAT27 = "supcat27"
    SUPCAT28 = "supcat28"
    SUPCAT29 = "supcat29"
    SUPCAT30 = "supcat30"
    SUPCAT31 = "supcat31"
    SUPCAT32 = "supcat32"
    SUPCAT33 = "supcat33"
    SUPCAT34 = "supcat34"
    SUPCAT35 = "supcat35"
    SUPCAT36 = "supcat36"
    SUPCAT37 = "supcat37"
    SUPCAT38 = "supcat38"
    SUPCAT39 = "supcat39"
    SUPCAT40 = "supcat40"
    SUPCAT41 = "supcat41"
    SUPCAT42 = "supcat42"
    SUPCAT43 = "supcat43"
    SUPCAT44 = "supcat44"
    SUPCAT45 = "supcat45"
    SUPCAT46 = "supcat46"
    SUPCAT47 = "supcat47"
    SUPCAT48 = "supcat48"
    SUPCAT49 = "supcat49"
    SUPCAT50 = "supcat50"
    SUPCAT51 = "supcat51"
    SUPCAT52 = "supcat52"
    SUPCAT53 = "supcat53"
    SUPCAT54 = "supcat54"
    SUPCAT55 = "supcat55"
    SUPCAT56 = "supcat56"
    SUPCAT57 = "supcat57"
    SUPCAT58 = "supcat58"
    SUPCAT59 = "supcat59"
    SUPCAT60 = "supcat60"
    SUPCAT61 = "supcat61"
    SUPCAT62 = "supcat62"
    SUPCAT63 = "supcat63"
    SUPCAT64 = "supcat64"
    SUPCAT65 = "supcat65"
    SUPCAT66 = "supcat66"
    SUPCAT67 = "supcat67"
    SUPCAT68 = "supcat68"
    SUPCAT69 = "supcat69"
    SUPCAT70 = "supcat70"
    SUPCAT71 = "supcat71"
    SUPCAT72 = "supcat72"
    SUPCAT73 = "supcat73"
    SUPCAT74 = "supcat74"
    SUPCAT75 = "supcat75"
    SUPCAT76 = "supcat76"
    SUPCAT77 = "supcat77"
    SUPCAT78 = "supcat78"
    SUPCAT79 = "supcat79"
    SUPCAT80 = "supcat80"
    SUPCAT81 = "supcat81"
    SUPCAT82 = "supcat82"
    SUPCAT83 = "supcat83"
    SUPCAT84 = "supcat84"
    SUPCAT85 = "supcat85"
    SUPCAT86 = "supcat86"
    SUPCAT87 = "supcat87"
    SUPCAT88 = "supcat88"
    SUPCAT89 = "supcat89"
    SUPCAT90 = "supcat90"
    SUPCAT91 = "supcat91"
    SUPCAT92 = "supcat92"
    SUPCAT93 = "supcat93"
    SUPCAT94 = "supcat94"
    SUPCAT95 = "supcat95"
    SUPCAT96 = "supcat96"
    SUPCAT97 = "supcat97"
    SUPCAT98 = "supcat98"
    SUPCAT99 = "supcat99"


@dataclass(kw_only=True)
class SupplyClassification:
    class Meta:
        name = "supplyClassification"

    value: str = field(default="")


class SupplyNumberTypeAttType(Enum):
    SP01 = "sp01"
    SP02 = "sp02"
    SP03 = "sp03"
    SP04 = "sp04"
    SP05 = "sp05"
    SP06 = "sp06"
    SP07 = "sp07"
    SP08 = "sp08"
    SP09 = "sp09"
    SP10 = "sp10"
    SP11 = "sp11"
    SP12 = "sp12"
    SP13 = "sp13"
    SP14 = "sp14"
    SP15 = "sp15"
    SP16 = "sp16"
    SP17 = "sp17"
    SP18 = "sp18"
    SP19 = "sp19"
    SP20 = "sp20"
    SP21 = "sp21"
    SP22 = "sp22"
    SP23 = "sp23"
    SP24 = "sp24"
    SP25 = "sp25"
    SP26 = "sp26"
    SP27 = "sp27"
    SP28 = "sp28"
    SP29 = "sp29"
    SP30 = "sp30"
    SP31 = "sp31"
    SP32 = "sp32"
    SP33 = "sp33"
    SP34 = "sp34"
    SP35 = "sp35"
    SP36 = "sp36"
    SP37 = "sp37"
    SP38 = "sp38"
    SP39 = "sp39"
    SP40 = "sp40"
    SP41 = "sp41"
    SP42 = "sp42"
    SP43 = "sp43"
    SP44 = "sp44"
    SP45 = "sp45"
    SP46 = "sp46"
    SP47 = "sp47"
    SP48 = "sp48"
    SP49 = "sp49"
    SP50 = "sp50"
    SP51 = "sp51"
    SP52 = "sp52"
    SP53 = "sp53"
    SP54 = "sp54"
    SP55 = "sp55"
    SP56 = "sp56"
    SP57 = "sp57"
    SP58 = "sp58"
    SP59 = "sp59"
    SP60 = "sp60"
    SP61 = "sp61"
    SP62 = "sp62"
    SP63 = "sp63"
    SP64 = "sp64"
    SP65 = "sp65"
    SP66 = "sp66"
    SP67 = "sp67"
    SP68 = "sp68"
    SP69 = "sp69"
    SP70 = "sp70"
    SP71 = "sp71"
    SP72 = "sp72"
    SP73 = "sp73"
    SP74 = "sp74"
    SP75 = "sp75"
    SP76 = "sp76"
    SP77 = "sp77"
    SP78 = "sp78"
    SP79 = "sp79"
    SP80 = "sp80"
    SP81 = "sp81"
    SP82 = "sp82"
    SP83 = "sp83"
    SP84 = "sp84"
    SP85 = "sp85"
    SP86 = "sp86"
    SP87 = "sp87"
    SP88 = "sp88"
    SP89 = "sp89"
    SP90 = "sp90"
    SP91 = "sp91"
    SP92 = "sp92"
    SP93 = "sp93"
    SP94 = "sp94"
    SP95 = "sp95"
    SP96 = "sp96"
    SP97 = "sp97"
    SP98 = "sp98"
    SP99 = "sp99"


@dataclass(kw_only=True)
class SystemBreakdownCodeElemType:
    class Meta:
        name = "systemBreakdownCodeElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TechPubBase:
    class Meta:
        name = "techPubBase"

    value: str = field(default="")


class TermTypeAttType(Enum):
    TT01 = "tt01"
    TT02 = "tt02"
    TT03 = "tt03"
    TT04 = "tt04"
    TT05 = "tt05"
    TT06 = "tt06"
    TT07 = "tt07"
    TT08 = "tt08"
    TT09 = "tt09"
    TT10 = "tt10"
    TT11 = "tt11"
    TT12 = "tt12"
    TT13 = "tt13"
    TT14 = "tt14"
    TT15 = "tt15"
    TT16 = "tt16"
    TT17 = "tt17"
    TT18 = "tt18"
    TT19 = "tt19"
    TT20 = "tt20"
    TT21 = "tt21"
    TT22 = "tt22"
    TT23 = "tt23"
    TT24 = "tt24"
    TT25 = "tt25"
    TT26 = "tt26"
    TT27 = "tt27"
    TT28 = "tt28"
    TT29 = "tt29"
    TT30 = "tt30"
    TT31 = "tt31"
    TT32 = "tt32"
    TT33 = "tt33"
    TT34 = "tt34"
    TT35 = "tt35"
    TT36 = "tt36"
    TT37 = "tt37"
    TT38 = "tt38"
    TT39 = "tt39"
    TT40 = "tt40"
    TT41 = "tt41"
    TT42 = "tt42"
    TT43 = "tt43"
    TT44 = "tt44"
    TT45 = "tt45"
    TT46 = "tt46"
    TT47 = "tt47"
    TT48 = "tt48"
    TT49 = "tt49"
    TT50 = "tt50"
    TT51 = "tt51"
    TT52 = "tt52"
    TT53 = "tt53"
    TT54 = "tt54"
    TT55 = "tt55"
    TT56 = "tt56"
    TT57 = "tt57"
    TT58 = "tt58"
    TT59 = "tt59"
    TT60 = "tt60"
    TT61 = "tt61"
    TT62 = "tt62"
    TT63 = "tt63"
    TT64 = "tt64"
    TT65 = "tt65"
    TT66 = "tt66"
    TT67 = "tt67"
    TT68 = "tt68"
    TT69 = "tt69"
    TT70 = "tt70"
    TT71 = "tt71"
    TT72 = "tt72"
    TT73 = "tt73"
    TT74 = "tt74"
    TT75 = "tt75"
    TT76 = "tt76"
    TT77 = "tt77"
    TT78 = "tt78"
    TT79 = "tt79"
    TT80 = "tt80"
    TT81 = "tt81"
    TT82 = "tt82"
    TT83 = "tt83"
    TT84 = "tt84"
    TT85 = "tt85"
    TT86 = "tt86"
    TT87 = "tt87"
    TT88 = "tt88"
    TT89 = "tt89"
    TT90 = "tt90"
    TT91 = "tt91"
    TT92 = "tt92"
    TT93 = "tt93"
    TT94 = "tt94"
    TT95 = "tt95"
    TT96 = "tt96"
    TT97 = "tt97"
    TT98 = "tt98"
    TT99 = "tt99"


@dataclass(kw_only=True)
class UnverifiedElemType:
    class Meta:
        name = "unverifiedElemType"


class UpdateReasonTypeAttType(Enum):
    URT01 = "urt01"
    URT02 = "urt02"
    URT03 = "urt03"
    URT04 = "urt04"
    URT05 = "urt05"
    URT06 = "urt06"
    URT07 = "urt07"
    URT08 = "urt08"
    URT09 = "urt09"
    URT10 = "urt10"
    URT11 = "urt11"
    URT12 = "urt12"
    URT13 = "urt13"
    URT14 = "urt14"
    URT15 = "urt15"
    URT16 = "urt16"
    URT17 = "urt17"
    URT18 = "urt18"
    URT19 = "urt19"
    URT20 = "urt20"
    URT21 = "urt21"
    URT22 = "urt22"
    URT23 = "urt23"
    URT24 = "urt24"
    URT25 = "urt25"
    URT26 = "urt26"
    URT27 = "urt27"
    URT28 = "urt28"
    URT29 = "urt29"
    URT30 = "urt30"
    URT31 = "urt31"
    URT32 = "urt32"
    URT33 = "urt33"
    URT34 = "urt34"
    URT35 = "urt35"
    URT36 = "urt36"
    URT37 = "urt37"
    URT38 = "urt38"
    URT39 = "urt39"
    URT40 = "urt40"
    URT41 = "urt41"
    URT42 = "urt42"
    URT43 = "urt43"
    URT44 = "urt44"
    URT45 = "urt45"
    URT46 = "urt46"
    URT47 = "urt47"
    URT48 = "urt48"
    URT49 = "urt49"
    URT50 = "urt50"
    URT51 = "urt51"
    URT52 = "urt52"
    URT53 = "urt53"
    URT54 = "urt54"
    URT55 = "urt55"
    URT56 = "urt56"
    URT57 = "urt57"
    URT58 = "urt58"
    URT59 = "urt59"
    URT60 = "urt60"
    URT61 = "urt61"
    URT62 = "urt62"
    URT63 = "urt63"
    URT64 = "urt64"
    URT65 = "urt65"
    URT66 = "urt66"
    URT67 = "urt67"
    URT68 = "urt68"
    URT69 = "urt69"
    URT70 = "urt70"
    URT71 = "urt71"
    URT72 = "urt72"
    URT73 = "urt73"
    URT74 = "urt74"
    URT75 = "urt75"
    URT76 = "urt76"
    URT77 = "urt77"
    URT78 = "urt78"
    URT79 = "urt79"
    URT80 = "urt80"
    URT81 = "urt81"
    URT82 = "urt82"
    URT83 = "urt83"
    URT84 = "urt84"
    URT85 = "urt85"
    URT86 = "urt86"
    URT87 = "urt87"
    URT88 = "urt88"
    URT89 = "urt89"
    URT90 = "urt90"
    URT91 = "urt91"
    URT92 = "urt92"
    URT93 = "urt93"
    URT94 = "urt94"
    URT95 = "urt95"
    URT96 = "urt96"
    URT97 = "urt97"
    URT98 = "urt98"
    URT99 = "urt99"


class ValignAttType(Enum):
    TOP = "top"
    BOTTOM = "bottom"
    MIDDLE = "middle"


@dataclass(kw_only=True)
class VariableRefElemType:
    class Meta:
        name = "variableRefElemType"

    variable_name: str = field(
        metadata={
            "name": "variableName",
            "type": "Attribute",
        }
    )


class VerbatimStyleAttType(Enum):
    VS01 = "vs01"
    VS02 = "vs02"
    VS03 = "vs03"
    VS04 = "vs04"
    VS05 = "vs05"
    VS06 = "vs06"
    VS07 = "vs07"
    VS08 = "vs08"
    VS09 = "vs09"
    VS10 = "vs10"
    VS11 = "vs11"
    VS12 = "vs12"
    VS13 = "vs13"
    VS14 = "vs14"
    VS15 = "vs15"
    VS16 = "vs16"
    VS17 = "vs17"
    VS18 = "vs18"
    VS19 = "vs19"
    VS20 = "vs20"
    VS21 = "vs21"
    VS22 = "vs22"
    VS23 = "vs23"
    VS24 = "vs24"
    VS25 = "vs25"
    VS26 = "vs26"
    VS27 = "vs27"
    VS28 = "vs28"
    VS29 = "vs29"
    VS30 = "vs30"
    VS31 = "vs31"
    VS32 = "vs32"
    VS33 = "vs33"
    VS34 = "vs34"
    VS35 = "vs35"
    VS36 = "vs36"
    VS37 = "vs37"
    VS38 = "vs38"
    VS39 = "vs39"
    VS40 = "vs40"
    VS41 = "vs41"
    VS42 = "vs42"
    VS43 = "vs43"
    VS44 = "vs44"
    VS45 = "vs45"
    VS46 = "vs46"
    VS47 = "vs47"
    VS48 = "vs48"
    VS49 = "vs49"
    VS50 = "vs50"
    VS51 = "vs51"
    VS52 = "vs52"
    VS53 = "vs53"
    VS54 = "vs54"
    VS55 = "vs55"
    VS56 = "vs56"
    VS57 = "vs57"
    VS58 = "vs58"
    VS59 = "vs59"
    VS60 = "vs60"
    VS61 = "vs61"
    VS62 = "vs62"
    VS63 = "vs63"
    VS64 = "vs64"
    VS65 = "vs65"
    VS66 = "vs66"
    VS67 = "vs67"
    VS68 = "vs68"
    VS69 = "vs69"
    VS70 = "vs70"
    VS71 = "vs71"
    VS72 = "vs72"
    VS73 = "vs73"
    VS74 = "vs74"
    VS75 = "vs75"
    VS76 = "vs76"
    VS77 = "vs77"
    VS78 = "vs78"
    VS79 = "vs79"
    VS80 = "vs80"
    VS81 = "vs81"
    VS82 = "vs82"
    VS83 = "vs83"
    VS84 = "vs84"
    VS85 = "vs85"
    VS86 = "vs86"
    VS87 = "vs87"
    VS88 = "vs88"
    VS89 = "vs89"
    VS90 = "vs90"
    VS91 = "vs91"
    VS92 = "vs92"
    VS93 = "vs93"
    VS94 = "vs94"
    VS95 = "vs95"
    VS96 = "vs96"
    VS97 = "vs97"
    VS98 = "vs98"
    VS99 = "vs99"


class VerificationTypeAttType(Enum):
    TABTOP = "tabtop"
    ONOBJECT = "onobject"
    TTANDOO = "ttandoo"


class VisibilityAttType(Enum):
    VISIBLE = "visible"
    HIDDEN = "hidden"


@dataclass(kw_only=True)
class AccessPointIdentElemType:
    class Meta:
        name = "accessPointIdentElemType"

    access_point_number: str = field(
        metadata={
            "name": "accessPointNumber",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class AccessPointTypeElemType:
    class Meta:
        name = "accessPointTypeElemType"

    access_point_type_value: AccessPointTypeValueAttType = field(
        metadata={
            "name": "accessPointTypeValue",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class AcronymDefinitionElemType:
    class Meta:
        name = "acronymDefinitionElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "subScript",
                    "type": SubScript,
                },
                {
                    "name": "superScript",
                    "type": SuperScript,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class AcronymTermElemType:
    class Meta:
        name = "acronymTermElemType"

    internal_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "internalRefId",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "subScript",
                    "type": SubScript,
                },
                {
                    "name": "superScript",
                    "type": SuperScript,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class AlteredFromPartDescrElemType:
    class Meta:
        name = "alteredFromPartDescrElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Amperage(AmperageElemType):
    class Meta:
        name = "amperage"


@dataclass(kw_only=True)
class ApplicSpecIdentElemType:
    class Meta:
        name = "applicSpecIdentElemType"

    applic_ident_value: str = field(
        metadata={
            "name": "applicIdentValue",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class AssertElemType:
    class Meta:
        name = "assertElemType"

    applic_property_ident: None | str = field(
        default=None,
        metadata={
            "name": "applicPropertyIdent",
            "type": "Attribute",
        },
    )
    applic_property_type: None | ApplicPropertyTypeAttType = field(
        default=None,
        metadata={
            "name": "applicPropertyType",
            "type": "Attribute",
        },
    )
    applic_property_values: None | str = field(
        default=None,
        metadata={
            "name": "applicPropertyValues",
            "type": "Attribute",
            "pattern": r"[^~|\t\n\r]+(~[^~|\t\n\r]+)?(\|[^~|\t\n\r]+(~[^~|\t\n\r]+)?)*",
        },
    )
    applic_display_class: None | str = field(
        default=None,
        metadata={
            "name": "applicDisplayClass",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class AuthorityInfoAndTpElemType:
    class Meta:
        name = "authorityInfoAndTpElemType"

    authority_info: AuthorityInfo = field(
        metadata={
            "name": "authorityInfo",
            "type": "Element",
        }
    )
    tech_pub_base: TechPubBase = field(
        metadata={
            "name": "techPubBase",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class AuthorizationStatus(AuthorizationStatusElemType):
    class Meta:
        name = "authorizationStatus"


@dataclass(kw_only=True)
class BehaviorElemType:
    class Meta:
        name = "behaviorElemType"

    link_show: None | LinkShowAttType = field(
        default=None,
        metadata={
            "name": "linkShow",
            "type": "Attribute",
        },
    )
    link_actuate: None | LinkActuateAttType = field(
        default=None,
        metadata={
            "name": "linkActuate",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class BooleanFunctionElemType:
    class Meta:
        name = "booleanFunctionElemType"

    boolean_action: BooleanActionAttType = field(
        metadata={
            "name": "booleanAction",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class BooleanOperatorElemType:
    class Meta:
        name = "booleanOperatorElemType"

    boolean_operation: BooleanOperationAttType = field(
        metadata={
            "name": "booleanOperation",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class BuyerFurnishedEquipFlagElemType:
    class Meta:
        name = "buyerFurnishedEquipFlagElemType"

    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class CalibrationMarkerElemType:
    class Meta:
        name = "calibrationMarkerElemType"

    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CautionIdentElemType:
    class Meta:
        name = "cautionIdentElemType"

    caution_ident_number: str = field(
        metadata={
            "name": "cautionIdentNumber",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class CircuitBreakerClassElemType:
    class Meta:
        name = "circuitBreakerClassElemType"

    circuit_breaker_type: CircuitBreakerTypeAttType = field(
        metadata={
            "name": "circuitBreakerType",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class CircuitBreakerIdentElemType:
    class Meta:
        name = "circuitBreakerIdentElemType"

    circuit_breaker_number: str = field(
        metadata={
            "name": "circuitBreakerNumber",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    installation_ident: None | str = field(
        default=None,
        metadata={
            "name": "installationIdent",
            "type": "Attribute",
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    context_ident: None | str = field(
        default=None,
        metadata={
            "name": "contextIdent",
            "type": "Attribute",
        },
    )
    manufacturer_code_value: None | str = field(
        default=None,
        metadata={
            "name": "manufacturerCodeValue",
            "type": "Attribute",
        },
    )
    item_originator: None | ItemOriginatorAttType = field(
        default=None,
        metadata={
            "name": "itemOriginator",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ColspecElemType:
    class Meta:
        name = "colspecElemType"

    colnum: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    colname: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    align: None | AlignAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charoff: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    colwidth: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\d+(\.\d+)?\s*(\*|cm|in|mm|pc|pt)(\+\d+(\.\d+)?\s*(cm|in|mm|pc|pt))?",
        },
    )
    colsep: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    rowsep: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )


@dataclass(kw_only=True)
class ComplianceCategoryElemType:
    class Meta:
        name = "complianceCategoryElemType"

    compliance_category_value: None | ComplianceCategoryValueAttType = field(
        default=None,
        metadata={
            "name": "complianceCategoryValue",
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ControlIndicatorKeyElemType:
    class Meta:
        name = "controlIndicatorKeyElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ControlIndicatorNameElemType:
    class Meta:
        name = "controlIndicatorNameElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "subScript",
                    "type": SubScript,
                },
                {
                    "name": "superScript",
                    "type": SuperScript,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class CustomerStockNumberElemType:
    class Meta:
        name = "customerStockNumberElemType"

    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DataCondsElemType:
    class Meta:
        name = "dataCondsElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DataDestructionElemType:
    class Meta:
        name = "dataDestructionElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DataDisclosureElemType:
    class Meta:
        name = "dataDisclosureElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DataDistributionElemType:
    class Meta:
        name = "dataDistributionElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DataHandlingElemType:
    class Meta:
        name = "dataHandlingElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DescrForPartElemType:
    class Meta:
        name = "descrForPartElemType"

    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class DmCodeElemType:
    class Meta:
        name = "dmCodeElemType"

    model_ident_code: str = field(
        metadata={
            "name": "modelIdentCode",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{2,14}",
        }
    )
    system_diff_code: str = field(
        metadata={
            "name": "systemDiffCode",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{1,4}",
        }
    )
    system_code: str = field(
        metadata={
            "name": "systemCode",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{2,3}",
        }
    )
    sub_system_code: str = field(
        metadata={
            "name": "subSystemCode",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{1}",
        }
    )
    sub_sub_system_code: str = field(
        metadata={
            "name": "subSubSystemCode",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{1}",
        }
    )
    assy_code: str = field(
        metadata={
            "name": "assyCode",
            "type": "Attribute",
            "pattern": r"([A-Z0-9]{2}|[A-Z0-9]{4})",
        }
    )
    disassy_code: str = field(
        metadata={
            "name": "disassyCode",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{2}",
        }
    )
    disassy_code_variant: str = field(
        metadata={
            "name": "disassyCodeVariant",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{1,3}",
        }
    )
    info_code: str = field(
        metadata={
            "name": "infoCode",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{3}",
        }
    )
    info_code_variant: str = field(
        metadata={
            "name": "infoCodeVariant",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{1}",
        }
    )
    item_location_code: ItemLocationCodeAttType = field(
        metadata={
            "name": "itemLocationCode",
            "type": "Attribute",
        }
    )
    learn_code: None | str = field(
        default=None,
        metadata={
            "name": "learnCode",
            "type": "Attribute",
            "pattern": r"([T|H][A-Z0-9]{2})",
        },
    )
    learn_event_code: None | LearnEventCodeAttType = field(
        default=None,
        metadata={
            "name": "learnEventCode",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Email(EmailElemType):
    class Meta:
        name = "email"


@dataclass(kw_only=True)
class EnterpriseIdentAlt(EnterpriseIdentAltElemType):
    class Meta:
        name = "enterpriseIdentAlt"


@dataclass(kw_only=True)
class EnterpriseIdentElemType:
    class Meta:
        name = "enterpriseIdentElemType"

    manufacturer_code_value: str = field(
        metadata={
            "name": "manufacturerCodeValue",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ExportRegistrationCode(ExportRegistrationCodeElemType):
    class Meta:
        name = "exportRegistrationCode"


@dataclass(kw_only=True)
class ExternalPubIssueDate(ExternalPubIssueDateElemType):
    class Meta:
        name = "externalPubIssueDate"


@dataclass(kw_only=True)
class FalseValue(EmptyElemType):
    class Meta:
        name = "falseValue"


@dataclass(kw_only=True)
class FastenerQuantityElemType:
    class Meta:
        name = "fastenerQuantityElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FastenerTypeElemType:
    class Meta:
        name = "fastenerTypeElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FaxNumber(FaxNumberElemType):
    class Meta:
        name = "faxNumber"


@dataclass(kw_only=True)
class FirstVerificationElemType:
    class Meta:
        name = "firstVerificationElemType"

    verification_type: VerificationTypeAttType = field(
        metadata={
            "name": "verificationType",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class FitmentCodeElemType:
    class Meta:
        name = "fitmentCodeElemType"

    fitment_code_value: FitmentCodeValueAttType = field(
        metadata={
            "name": "fitmentCodeValue",
            "type": "Attribute",
        }
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class FunctionalItemFamilyElemType:
    class Meta:
        name = "functionalItemFamilyElemType"

    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class FunctionalItemIdentElemType:
    class Meta:
        name = "functionalItemIdentElemType"

    functional_item_number: str = field(
        metadata={
            "name": "functionalItemNumber",
            "type": "Attribute",
        }
    )
    functional_item_type: FunctionalItemTypeAttType = field(
        metadata={
            "name": "functionalItemType",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    installation_ident: None | str = field(
        default=None,
        metadata={
            "name": "installationIdent",
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    context_ident: None | str = field(
        default=None,
        metadata={
            "name": "contextIdent",
            "type": "Attribute",
        },
    )
    manufacturer_code_value: None | str = field(
        default=None,
        metadata={
            "name": "manufacturerCodeValue",
            "type": "Attribute",
        },
    )
    item_originator: None | ItemOriginatorAttType = field(
        default=None,
        metadata={
            "name": "itemOriginator",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class FunctionalPhysicalAreaIdent(FunctionalPhysicalAreaIdentElemType):
    class Meta:
        name = "functionalPhysicalAreaIdent"


@dataclass(kw_only=True)
class GlobalPropertyRefElemType:
    class Meta:
        name = "globalPropertyRefElemType"

    applic_property_ident: str = field(
        metadata={
            "name": "applicPropertyIdent",
            "type": "Attribute",
        }
    )
    applic_property_type: ApplicPropertyTypeAttType = field(
        metadata={
            "name": "applicPropertyType",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class GroundingTypeElemType:
    class Meta:
        name = "groundingTypeElemType"

    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HazardIdentElemType:
    class Meta:
        name = "hazardIdentElemType"

    hazard_ident_number: str = field(
        metadata={
            "name": "hazardIdentNumber",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class HazardousClassElemType:
    class Meta:
        name = "hazardousClassElemType"

    hazardous_class_value: HazardousClassValueAttType = field(
        metadata={
            "name": "hazardousClassValue",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class HoursToCloseElemType:
    class Meta:
        name = "hoursToCloseElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class HoursToOpenElemType:
    class Meta:
        name = "hoursToOpenElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class IdentExtension(IdentExtensionElemType):
    class Meta:
        name = "identExtension"


@dataclass(kw_only=True)
class IndexFlag(IndexFlagElemType):
    class Meta:
        name = "indexFlag"


@dataclass(kw_only=True)
class InfoNameElemType:
    class Meta:
        name = "infoNameElemType"

    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class InlineSignificantDataElemType:
    class Meta:
        name = "inlineSignificantDataElemType"

    significant_para_data_type: SignificantParaDataTypeAttType = field(
        metadata={
            "name": "significantParaDataType",
            "type": "Attribute",
        }
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class InstallationLocationElemType:
    class Meta:
        name = "installationLocationElemType"

    unit_of_measure: None | str = field(
        default=None,
        metadata={
            "name": "unitOfMeasure",
            "type": "Attribute",
        },
    )
    installation_location_type: None | InstallationLocationTypeAttType = field(
        default=None,
        metadata={
            "name": "installationLocationType",
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class InternalRefElemType:
    class Meta:
        name = "internalRefElemType"

    internal_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "internalRefId",
            "type": "Attribute",
        },
    )
    internal_ref_target_type: None | InternalRefTargetTypeAttType = field(
        default=None,
        metadata={
            "name": "internalRefTargetType",
            "type": "Attribute",
        },
    )
    referred_fragment: None | str = field(
        default=None,
        metadata={
            "name": "referredFragment",
            "type": "Attribute",
        },
    )
    target_title: None | str = field(
        default=None,
        metadata={
            "name": "targetTitle",
            "type": "Attribute",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    type_value: TypeValue = field(
        init=False,
        default=TypeValue.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: ShowValue = field(
        default=ShowValue.REPLACE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: ActuateValue = field(
        default=ActuateValue.ON_REQUEST,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "subScript",
                    "type": SubScript,
                },
                {
                    "name": "superScript",
                    "type": SuperScript,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Internet(InternetElemType):
    class Meta:
        name = "internet"


@dataclass(kw_only=True)
class IssueDate(IssueDateElemType):
    class Meta:
        name = "issueDate"


@dataclass(kw_only=True)
class IssueInfo(IssueInfoGenericElemType):
    class Meta:
        name = "issueInfo"


@dataclass(kw_only=True)
class ItemDescrElemType:
    class Meta:
        name = "itemDescrElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Language(LanguageElemType):
    class Meta:
        name = "language"


@dataclass(kw_only=True)
class LimitedPartNumberElemType:
    class Meta:
        name = "limitedPartNumberElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class LowestAuthorizedLevelElemType:
    class Meta:
        name = "lowestAuthorizedLevelElemType"

    lowest_level: LowestLevelAttType = field(
        metadata={
            "name": "lowestLevel",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class ModificationElemType:
    class Meta:
        name = "modificationElemType"

    modification_title: None | ModificationTitle = field(
        default=None,
        metadata={
            "name": "modificationTitle",
            "type": "Element",
        },
    )
    authorization_ident: str = field(
        metadata={
            "name": "authorizationIdent",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    modification_type: ModificationTypeAttType = field(
        metadata={
            "name": "modificationType",
            "type": "Attribute",
        }
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class NameElemType:
    class Meta:
        name = "nameElemType"

    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class NoValue(EmptyElemType):
    class Meta:
        name = "noValue"


@dataclass(kw_only=True)
class NumberFunctionElemType:
    class Meta:
        name = "numberFunctionElemType"

    number_action: NumberActionAttType = field(
        metadata={
            "name": "numberAction",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class NumberOperatorElemType:
    class Meta:
        name = "numberOperatorElemType"

    number_operation: NumberOperationAttType = field(
        metadata={
            "name": "numberOperation",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class OriginatorElemType:
    class Meta:
        name = "originatorElemType"

    enterprise_name: None | EnterpriseName = field(
        default=None,
        metadata={
            "name": "enterpriseName",
            "type": "Element",
        },
    )
    enterprise_code: None | str = field(
        default=None,
        metadata={
            "name": "enterpriseCode",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class OtherItemsElemType:
    class Meta:
        name = "otherItemsElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class OverLengthPartNumberElemType:
    class Meta:
        name = "overLengthPartNumberElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PackagingElemType:
    class Meta:
        name = "packagingElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Parameter(ParameterElemType):
    class Meta:
        name = "parameter"


@dataclass(kw_only=True)
class PartIdentElemType:
    class Meta:
        name = "partIdentElemType"

    part_number_value: str = field(
        metadata={
            "name": "partNumberValue",
            "type": "Attribute",
        }
    )
    manufacturer_code_value: str = field(
        metadata={
            "name": "manufacturerCodeValue",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class PartKeywordElemType:
    class Meta:
        name = "partKeywordElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PartUsageElemType:
    class Meta:
        name = "partUsageElemType"

    part_usage_code: PartUsageCodeAttType = field(
        metadata={
            "name": "partUsageCode",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class PhoneNumber(PhoneNumberElemType):
    class Meta:
        name = "phoneNumber"


@dataclass(kw_only=True)
class PhysicalSecurityPilferageCodeElemType:
    class Meta:
        name = "physicalSecurityPilferageCodeElemType"

    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class PmCode(PmCodeElemType):
    class Meta:
        name = "pmCode"


@dataclass(kw_only=True)
class PolicyStatementElemType:
    class Meta:
        name = "policyStatementElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ProductConfigurationElemType:
    class Meta:
        name = "productConfigurationElemType"

    excluded_modification: list[ExcludedModification] = field(
        default_factory=list,
        metadata={
            "name": "excludedModification",
            "type": "Element",
        },
    )
    additional_modification: list[AdditionalModification] = field(
        default_factory=list,
        metadata={
            "name": "additionalModification",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ProductSafety(ProductSafetyElemType):
    class Meta:
        name = "productSafety"


@dataclass(kw_only=True)
class PubMedia(PubMediaElemType):
    class Meta:
        name = "pubMedia"


@dataclass(kw_only=True)
class QuantityToleranceElemType:
    class Meta:
        name = "quantityToleranceElemType"

    value: Decimal = field()
    quantity_tolerance_type: QuantityToleranceTypeAttType = field(
        default=QuantityToleranceTypeAttType.PLUSORMINUS,
        metadata={
            "name": "quantityToleranceType",
            "type": "Attribute",
        },
    )
    quantity_unit_of_measure: None | QuantityUnitOfMeasureAttType = field(
        default=None,
        metadata={
            "name": "quantityUnitOfMeasure",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class QuantityValueElemType:
    class Meta:
        name = "quantityValueElemType"

    value: Decimal = field()
    quantity_unit_of_measure: None | QuantityUnitOfMeasureAttType = field(
        default=None,
        metadata={
            "name": "quantityUnitOfMeasure",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class RcmdElemType:
    class Meta:
        name = "rcmdElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class RcmdQuantityElemType:
    class Meta:
        name = "rcmdQuantityElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ReplacementCondElemType:
    class Meta:
        name = "replacementCondElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ReqQuantityElemType:
    class Meta:
        name = "reqQuantityElemType"

    unit_of_measure: None | str = field(
        default=None,
        metadata={
            "name": "unitOfMeasure",
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ResponsiblePartnerCompanyElemType:
    class Meta:
        name = "responsiblePartnerCompanyElemType"

    enterprise_name: None | EnterpriseName = field(
        default=None,
        metadata={
            "name": "enterpriseName",
            "type": "Element",
        },
    )
    enterprise_code: None | str = field(
        default=None,
        metadata={
            "name": "enterpriseCode",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class SafetyCategoryElemType:
    class Meta:
        name = "safetyCategoryElemType"

    safety_category_value: SafetyCategoryValueAttType = field(
        metadata={
            "name": "safetyCategoryValue",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class SecondVerificationElemType:
    class Meta:
        name = "secondVerificationElemType"

    verification_type: VerificationTypeAttType = field(
        metadata={
            "name": "verificationType",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class SecurityElemType:
    class Meta:
        name = "securityElemType"

    security_classification: SecurityClassificationAttType = field(
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        }
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class SetFunctionElemType:
    class Meta:
        name = "setFunctionElemType"

    set_action: SetActionAttType = field(
        metadata={
            "name": "setAction",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class SetOperatorElemType:
    class Meta:
        name = "setOperatorElemType"

    set_operation: SetOperationAttType = field(
        metadata={
            "name": "setOperation",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class ShelfLifeElemType:
    class Meta:
        name = "shelfLifeElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ShortNameElemType:
    class Meta:
        name = "shortNameElemType"

    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SimpleParaElemType:
    class Meta:
        name = "simpleParaElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "subScript",
                    "type": SubScript,
                },
                {
                    "name": "superScript",
                    "type": SuperScript,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class SimpleRemarkElemType:
    class Meta:
        name = "simpleRemarkElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class SkillLevelElemType:
    class Meta:
        name = "skillLevelElemType"

    skill_level_code: SkillLevelCodeAttType = field(
        metadata={
            "name": "skillLevelCode",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class SoftwareClassificationElemType:
    class Meta:
        name = "softwareClassificationElemType"

    software_classification_value: SoftwareClassificationValueAttType = field(
        metadata={
            "name": "softwareClassificationValue",
            "type": "Attribute",
        }
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class SoftwareCustomizationStatusElemType:
    class Meta:
        name = "softwareCustomizationStatusElemType"

    software_customization_status_value: SoftwareCustomizationStatusValueAttType = field(
        metadata={
            "name": "softwareCustomizationStatusValue",
            "type": "Attribute",
        }
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class SourcingTypeElemType:
    class Meta:
        name = "sourcingTypeElemType"

    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    sourcing_type_value: SourcingTypeValueAttType = field(
        metadata={
            "name": "sourcingTypeValue",
            "type": "Attribute",
        }
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class SpanspecElemType:
    class Meta:
        name = "spanspecElemType"

    namest: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    nameend: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    spanname: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    align: AlignAttType = field(
        default=AlignAttType.CENTER,
        metadata={
            "type": "Attribute",
        },
    )
    charoff: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    colsep: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    rowsep: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )


@dataclass(kw_only=True)
class SparePartClassElemType:
    class Meta:
        name = "sparePartClassElemType"

    spare_part_class_code: SparePartClassCodeAttType = field(
        metadata={
            "name": "sparePartClassCode",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class SpecialStorageElemType:
    class Meta:
        name = "specialStorageElemType"

    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class StringFunctionElemType:
    class Meta:
        name = "stringFunctionElemType"

    string_action: StringActionAttType = field(
        metadata={
            "name": "stringAction",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class StringOperatorElemType:
    class Meta:
        name = "stringOperatorElemType"

    string_operation: StringOperationAttType = field(
        metadata={
            "name": "stringOperation",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class SubStringFunctionElemType:
    class Meta:
        name = "subStringFunctionElemType"

    sub_string_position: list[SubStringPosition] = field(
        default_factory=list,
        metadata={
            "name": "subStringPosition",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )
    sub_string_length: None | SubStringLength = field(
        default=None,
        metadata={
            "name": "subStringLength",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class SupersedureElemType:
    class Meta:
        name = "supersedureElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "subScript",
                    "type": SubScript,
                },
                {
                    "name": "superScript",
                    "type": SuperScript,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class SupplyIdentElemType:
    class Meta:
        name = "supplyIdentElemType"

    supply_number: str = field(
        metadata={
            "name": "supplyNumber",
            "type": "Attribute",
        }
    )
    supply_number_type: SupplyNumberTypeAttType = field(
        metadata={
            "name": "supplyNumberType",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class SupplyRqmtAltIdentElemType:
    class Meta:
        name = "supplyRqmtAltIdentElemType"

    material_category: None | str = field(
        default=None,
        metadata={
            "name": "materialCategory",
            "type": "Attribute",
        },
    )
    supply_rqmt_number: str = field(
        metadata={
            "name": "supplyRqmtNumber",
            "type": "Attribute",
        }
    )
    vendor_flag: None | str = field(
        default=None,
        metadata={
            "name": "vendorFlag",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class SupplyRqmtIdentElemType:
    class Meta:
        name = "supplyRqmtIdentElemType"

    material_category: None | str = field(
        default=None,
        metadata={
            "name": "materialCategory",
            "type": "Attribute",
        },
    )
    supply_rqmt_number: str = field(
        metadata={
            "name": "supplyRqmtNumber",
            "type": "Attribute",
        }
    )
    vendor_flag: None | str = field(
        default=None,
        metadata={
            "name": "vendorFlag",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class SymbolElemType:
    class Meta:
        name = "symbolElemType"

    info_entity_ident: str = field(
        metadata={
            "name": "infoEntityIdent",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    reproduction_width: None | str = field(
        default=None,
        metadata={
            "name": "reproductionWidth",
            "type": "Attribute",
            "pattern": r"\d+(\.\d+)?\s*(cm|in|mm|pc|pt)",
        },
    )
    reproduction_height: None | str = field(
        default=None,
        metadata={
            "name": "reproductionHeight",
            "type": "Attribute",
            "pattern": r"\d+(\.\d+)?\s*(cm|in|mm|pc|pt)",
        },
    )
    reproduction_scale: None | int = field(
        default=None,
        metadata={
            "name": "reproductionScale",
            "type": "Attribute",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    type_value: TypeValue = field(
        init=False,
        default=TypeValue.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: ShowValue = field(
        init=False,
        default=ShowValue.EMBED,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: ActuateValue = field(
        init=False,
        default=ActuateValue.ON_LOAD,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class SystemBreakdownCode(SystemBreakdownCodeElemType):
    class Meta:
        name = "systemBreakdownCode"


@dataclass(kw_only=True)
class TaskCategoryElemType:
    class Meta:
        name = "taskCategoryElemType"

    task_category_code: str = field(
        metadata={
            "name": "taskCategoryCode",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class TechNameElemType:
    class Meta:
        name = "techNameElemType"

    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TerminologyIdentElemType:
    class Meta:
        name = "terminologyIdentElemType"

    terminology_ident_number: str = field(
        metadata={
            "name": "terminologyIdentNumber",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ToolIdentElemType:
    class Meta:
        name = "toolIdentElemType"

    tool_number: str = field(
        metadata={
            "name": "toolNumber",
            "type": "Attribute",
        }
    )
    manufacturer_code_value: str = field(
        metadata={
            "name": "manufacturerCodeValue",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class TransportElemType:
    class Meta:
        name = "transportElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class TrueValue(EmptyElemType):
    class Meta:
        name = "trueValue"


@dataclass(kw_only=True)
class UnitOfIssueElemType:
    class Meta:
        name = "unitOfIssueElemType"

    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class UnitOfIssueQualificationSegmentElemType:
    class Meta:
        name = "unitOfIssueQualificationSegmentElemType"

    quantity_per_unit: QuantityPerUnit = field(
        metadata={
            "name": "quantityPerUnit",
            "type": "Element",
        }
    )
    unit_of_measure: str = field(
        metadata={
            "name": "unitOfMeasure",
            "type": "Attribute",
        }
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class Unverified(UnverifiedElemType):
    class Meta:
        name = "unverified"


@dataclass(kw_only=True)
class UsageElemType:
    class Meta:
        name = "usageElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class ValueAfterActionElemType:
    class Meta:
        name = "valueAfterActionElemType"

    action_ident_type: ActionIdentTypeAttType = field(
        metadata={
            "name": "actionIdentType",
            "type": "Attribute",
        }
    )
    year: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"\d{4}",
        }
    )
    month: str = field(
        metadata={
            "type": "Attribute",
            "max_inclusive": "12",
            "pattern": r"\d{2}",
        }
    )
    day: str = field(
        metadata={
            "type": "Attribute",
            "max_inclusive": "31",
            "pattern": r"\d{2}",
        }
    )


@dataclass(kw_only=True)
class VariableRef(VariableRefElemType):
    class Meta:
        name = "variableRef"


@dataclass(kw_only=True)
class VerbatimTextElemType:
    class Meta:
        name = "verbatimTextElemType"

    verbatim_style: None | VerbatimStyleAttType = field(
        default=None,
        metadata={
            "name": "verbatimStyle",
            "type": "Attribute",
        },
    )
    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class WarningIdentElemType:
    class Meta:
        name = "warningIdentElemType"

    warning_ident_number: str = field(
        metadata={
            "name": "warningIdentNumber",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ZoneIdentElemType:
    class Meta:
        name = "zoneIdentElemType"

    zone_number: str = field(
        metadata={
            "name": "zoneNumber",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ZoneSideElemType:
    class Meta:
        name = "zoneSideElemType"

    zone_side_value: str = field(
        metadata={
            "name": "zoneSideValue",
            "type": "Attribute",
            "pattern": r"lh|rh|lr",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class AccessPointIdent(AccessPointIdentElemType):
    class Meta:
        name = "accessPointIdent"


@dataclass(kw_only=True)
class AccessPointType(AccessPointTypeElemType):
    class Meta:
        name = "accessPointType"


@dataclass(kw_only=True)
class AcronymDefinition(AcronymDefinitionElemType):
    class Meta:
        name = "acronymDefinition"


@dataclass(kw_only=True)
class AcronymTerm(AcronymTermElemType):
    class Meta:
        name = "acronymTerm"


@dataclass(kw_only=True)
class AddressElemType:
    class Meta:
        name = "addressElemType"

    department: None | Department = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    street: None | Street = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    post_office_box: None | PostOfficeBox = field(
        default=None,
        metadata={
            "name": "postOfficeBox",
            "type": "Element",
        },
    )
    postal_zip_code: None | PostalZipCode = field(
        default=None,
        metadata={
            "name": "postalZipCode",
            "type": "Element",
        },
    )
    city: City = field(
        metadata={
            "type": "Element",
        }
    )
    country: Country = field(
        metadata={
            "type": "Element",
        }
    )
    state: None | State = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    province: None | Province = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    building: None | Building = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    room: None | Room = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    phone_number: list[PhoneNumber] = field(
        default_factory=list,
        metadata={
            "name": "phoneNumber",
            "type": "Element",
        },
    )
    fax_number: list[FaxNumber] = field(
        default_factory=list,
        metadata={
            "name": "faxNumber",
            "type": "Element",
        },
    )
    email: list[Email] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    internet: list[Internet] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    sita: None | Sita = field(
        default=None,
        metadata={
            "name": "SITA",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class AlteredFromPartDescr(AlteredFromPartDescrElemType):
    class Meta:
        name = "alteredFromPartDescr"


@dataclass(kw_only=True)
class ApplicSpecIdent(ApplicSpecIdentElemType):
    class Meta:
        name = "applicSpecIdent"


@dataclass(kw_only=True)
class Assert(AssertElemType):
    class Meta:
        name = "assert"


@dataclass(kw_only=True)
class AuthorityInfoAndTp(AuthorityInfoAndTpElemType):
    class Meta:
        name = "authorityInfoAndTp"


@dataclass(kw_only=True)
class Behavior(BehaviorElemType):
    class Meta:
        name = "behavior"


@dataclass(kw_only=True)
class BooleanFunction(BooleanFunctionElemType):
    class Meta:
        name = "booleanFunction"


@dataclass(kw_only=True)
class BooleanOperator(BooleanOperatorElemType):
    class Meta:
        name = "booleanOperator"


@dataclass(kw_only=True)
class BooleanValueElemType:
    class Meta:
        name = "booleanValueElemType"

    true_value: None | TrueValue = field(
        default=None,
        metadata={
            "name": "trueValue",
            "type": "Element",
        },
    )
    false_value: None | FalseValue = field(
        default=None,
        metadata={
            "name": "falseValue",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class BuyerFurnishedEquipFlag(BuyerFurnishedEquipFlagElemType):
    class Meta:
        name = "buyerFurnishedEquipFlag"


@dataclass(kw_only=True)
class CalibrationMarker(CalibrationMarkerElemType):
    class Meta:
        name = "calibrationMarker"


@dataclass(kw_only=True)
class CautionIdent(CautionIdentElemType):
    class Meta:
        name = "cautionIdent"


@dataclass(kw_only=True)
class CircuitBreakerClass(CircuitBreakerClassElemType):
    class Meta:
        name = "circuitBreakerClass"


@dataclass(kw_only=True)
class CircuitBreakerIdent(CircuitBreakerIdentElemType):
    class Meta:
        name = "circuitBreakerIdent"


@dataclass(kw_only=True)
class Colspec(ColspecElemType):
    class Meta:
        name = "colspec"


@dataclass(kw_only=True)
class ComplianceCategory(ComplianceCategoryElemType):
    class Meta:
        name = "complianceCategory"


@dataclass(kw_only=True)
class ControlIndicatorKey(ControlIndicatorKeyElemType):
    class Meta:
        name = "controlIndicatorKey"


@dataclass(kw_only=True)
class ControlIndicatorName(ControlIndicatorNameElemType):
    class Meta:
        name = "controlIndicatorName"


@dataclass(kw_only=True)
class CustomerStockNumber(CustomerStockNumberElemType):
    class Meta:
        name = "customerStockNumber"


@dataclass(kw_only=True)
class DataConds(DataCondsElemType):
    class Meta:
        name = "dataConds"


@dataclass(kw_only=True)
class DataDestruction(DataDestructionElemType):
    class Meta:
        name = "dataDestruction"


@dataclass(kw_only=True)
class DataDisclosure(DataDisclosureElemType):
    class Meta:
        name = "dataDisclosure"


@dataclass(kw_only=True)
class DataDistribution(DataDistributionElemType):
    class Meta:
        name = "dataDistribution"


@dataclass(kw_only=True)
class DataHandling(DataHandlingElemType):
    class Meta:
        name = "dataHandling"


@dataclass(kw_only=True)
class DescrForPart(DescrForPartElemType):
    class Meta:
        name = "descrForPart"


@dataclass(kw_only=True)
class DmCode(DmCodeElemType):
    class Meta:
        name = "dmCode"


@dataclass(kw_only=True)
class EnterpriseIdent(EnterpriseIdentElemType):
    class Meta:
        name = "enterpriseIdent"


@dataclass(kw_only=True)
class FastenerQuantity(FastenerQuantityElemType):
    class Meta:
        name = "fastenerQuantity"


@dataclass(kw_only=True)
class FastenerType(FastenerTypeElemType):
    class Meta:
        name = "fastenerType"


@dataclass(kw_only=True)
class FirstVerification(FirstVerificationElemType):
    class Meta:
        name = "firstVerification"


@dataclass(kw_only=True)
class FitmentCode(FitmentCodeElemType):
    class Meta:
        name = "fitmentCode"


@dataclass(kw_only=True)
class FunctionalItemFamily(FunctionalItemFamilyElemType):
    class Meta:
        name = "functionalItemFamily"


@dataclass(kw_only=True)
class FunctionalItemIdent(FunctionalItemIdentElemType):
    class Meta:
        name = "functionalItemIdent"


@dataclass(kw_only=True)
class GlobalPropertyRef(GlobalPropertyRefElemType):
    class Meta:
        name = "globalPropertyRef"


@dataclass(kw_only=True)
class GroundingType(GroundingTypeElemType):
    class Meta:
        name = "groundingType"


@dataclass(kw_only=True)
class HazardIdent(HazardIdentElemType):
    class Meta:
        name = "hazardIdent"


@dataclass(kw_only=True)
class HazardousClass(HazardousClassElemType):
    class Meta:
        name = "hazardousClass"


@dataclass(kw_only=True)
class HoursToClose(HoursToCloseElemType):
    class Meta:
        name = "hoursToClose"


@dataclass(kw_only=True)
class HoursToOpen(HoursToOpenElemType):
    class Meta:
        name = "hoursToOpen"


@dataclass(kw_only=True)
class InfoName(InfoNameElemType):
    class Meta:
        name = "infoName"


@dataclass(kw_only=True)
class InfoNameVariant(InfoNameElemType):
    class Meta:
        name = "infoNameVariant"


@dataclass(kw_only=True)
class InlineSignificantData(InlineSignificantDataElemType):
    class Meta:
        name = "inlineSignificantData"


@dataclass(kw_only=True)
class InstallationLocation(InstallationLocationElemType):
    class Meta:
        name = "installationLocation"


@dataclass(kw_only=True)
class InternalRef(InternalRefElemType):
    class Meta:
        name = "internalRef"


@dataclass(kw_only=True)
class ItemDescr(ItemDescrElemType):
    class Meta:
        name = "itemDescr"


@dataclass(kw_only=True)
class LimitedPartNumber(LimitedPartNumberElemType):
    class Meta:
        name = "limitedPartNumber"


@dataclass(kw_only=True)
class LowestAuthorizedLevel(LowestAuthorizedLevelElemType):
    class Meta:
        name = "lowestAuthorizedLevel"


@dataclass(kw_only=True)
class Modification(ModificationElemType):
    class Meta:
        name = "modification"


@dataclass(kw_only=True)
class Name(NameElemType):
    class Meta:
        name = "name"


@dataclass(kw_only=True)
class NumberFunction(NumberFunctionElemType):
    class Meta:
        name = "numberFunction"


@dataclass(kw_only=True)
class NumberOperator(NumberOperatorElemType):
    class Meta:
        name = "numberOperator"


@dataclass(kw_only=True)
class Originator(OriginatorElemType):
    class Meta:
        name = "originator"


@dataclass(kw_only=True)
class OtherItems(OtherItemsElemType):
    class Meta:
        name = "otherItems"


@dataclass(kw_only=True)
class OverLengthPartNumber(OverLengthPartNumberElemType):
    class Meta:
        name = "overLengthPartNumber"


@dataclass(kw_only=True)
class Packaging(PackagingElemType):
    class Meta:
        name = "packaging"


@dataclass(kw_only=True)
class PartIdent(PartIdentElemType):
    class Meta:
        name = "partIdent"


@dataclass(kw_only=True)
class PartKeyword(PartKeywordElemType):
    class Meta:
        name = "partKeyword"


@dataclass(kw_only=True)
class PartUsage(PartUsageElemType):
    class Meta:
        name = "partUsage"


@dataclass(kw_only=True)
class PhysicalSecurityPilferageCode(PhysicalSecurityPilferageCodeElemType):
    class Meta:
        name = "physicalSecurityPilferageCode"


@dataclass(kw_only=True)
class PmRefIdentElemType:
    class Meta:
        name = "pmRefIdentElemType"

    ident_extension: None | IdentExtension = field(
        default=None,
        metadata={
            "name": "identExtension",
            "type": "Element",
        },
    )
    pm_code: PmCode = field(
        metadata={
            "name": "pmCode",
            "type": "Element",
        }
    )
    issue_info: None | IssueInfo = field(
        default=None,
        metadata={
            "name": "issueInfo",
            "type": "Element",
        },
    )
    language: None | Language = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PolicyStatement(PolicyStatementElemType):
    class Meta:
        name = "policyStatement"


@dataclass(kw_only=True)
class ProductConfiguration(ProductConfigurationElemType):
    class Meta:
        name = "productConfiguration"


@dataclass(kw_only=True)
class QuantityTolerance(QuantityToleranceElemType):
    class Meta:
        name = "quantityTolerance"


@dataclass(kw_only=True)
class QuantityValue(QuantityValueElemType):
    class Meta:
        name = "quantityValue"


@dataclass(kw_only=True)
class Rcmd(RcmdElemType):
    class Meta:
        name = "rcmd"


@dataclass(kw_only=True)
class RcmdQuantity(RcmdQuantityElemType):
    class Meta:
        name = "rcmdQuantity"


@dataclass(kw_only=True)
class ReplacementCond(ReplacementCondElemType):
    class Meta:
        name = "replacementCond"


@dataclass(kw_only=True)
class ReqQuantity(ReqQuantityElemType):
    class Meta:
        name = "reqQuantity"


@dataclass(kw_only=True)
class ResponsiblePartnerCompany(ResponsiblePartnerCompanyElemType):
    class Meta:
        name = "responsiblePartnerCompany"


@dataclass(kw_only=True)
class SafetyCategory(SafetyCategoryElemType):
    class Meta:
        name = "safetyCategory"


@dataclass(kw_only=True)
class SecondVerification(SecondVerificationElemType):
    class Meta:
        name = "secondVerification"


@dataclass(kw_only=True)
class Security(SecurityElemType):
    class Meta:
        name = "security"


@dataclass(kw_only=True)
class SetFunction(SetFunctionElemType):
    class Meta:
        name = "setFunction"


@dataclass(kw_only=True)
class SetOperator(SetOperatorElemType):
    class Meta:
        name = "setOperator"


@dataclass(kw_only=True)
class SetValueElemType:
    class Meta:
        name = "setValueElemType"

    string_value: list[StringValue] = field(
        default_factory=list,
        metadata={
            "name": "stringValue",
            "type": "Element",
        },
    )
    real_value: list[RealValue] = field(
        default_factory=list,
        metadata={
            "name": "realValue",
            "type": "Element",
        },
    )
    integer_value: list[IntegerValue] = field(
        default_factory=list,
        metadata={
            "name": "integerValue",
            "type": "Element",
        },
    )
    no_value: None | NoValue = field(
        default=None,
        metadata={
            "name": "noValue",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ShelfLife(ShelfLifeElemType):
    class Meta:
        name = "shelfLife"


@dataclass(kw_only=True)
class ShortName(ShortNameElemType):
    class Meta:
        name = "shortName"


@dataclass(kw_only=True)
class SimplePara(SimpleParaElemType):
    class Meta:
        name = "simplePara"


@dataclass(kw_only=True)
class SimpleRemark(SimpleRemarkElemType):
    class Meta:
        name = "simpleRemark"


@dataclass(kw_only=True)
class SkillLevel(SkillLevelElemType):
    class Meta:
        name = "skillLevel"


@dataclass(kw_only=True)
class SoftwareClassification(SoftwareClassificationElemType):
    class Meta:
        name = "softwareClassification"


@dataclass(kw_only=True)
class SoftwareCustomizationStatus(SoftwareCustomizationStatusElemType):
    class Meta:
        name = "softwareCustomizationStatus"


@dataclass(kw_only=True)
class SourcingType(SourcingTypeElemType):
    class Meta:
        name = "sourcingType"


@dataclass(kw_only=True)
class Spanspec(SpanspecElemType):
    class Meta:
        name = "spanspec"


@dataclass(kw_only=True)
class SparePartClass(SparePartClassElemType):
    class Meta:
        name = "sparePartClass"


@dataclass(kw_only=True)
class SpecialStorage(SpecialStorageElemType):
    class Meta:
        name = "specialStorage"


@dataclass(kw_only=True)
class StringFunction(StringFunctionElemType):
    class Meta:
        name = "stringFunction"


@dataclass(kw_only=True)
class StringOperator(StringOperatorElemType):
    class Meta:
        name = "stringOperator"


@dataclass(kw_only=True)
class SubStringFunction(SubStringFunctionElemType):
    class Meta:
        name = "subStringFunction"


@dataclass(kw_only=True)
class Supersedure(SupersedureElemType):
    class Meta:
        name = "supersedure"


@dataclass(kw_only=True)
class SupplyIdent(SupplyIdentElemType):
    class Meta:
        name = "supplyIdent"


@dataclass(kw_only=True)
class SupplyRqmtAltIdent(SupplyRqmtAltIdentElemType):
    class Meta:
        name = "supplyRqmtAltIdent"


@dataclass(kw_only=True)
class SupplyRqmtIdent(SupplyRqmtIdentElemType):
    class Meta:
        name = "supplyRqmtIdent"


@dataclass(kw_only=True)
class Symbol(SymbolElemType):
    class Meta:
        name = "symbol"


@dataclass(kw_only=True)
class TaskCategory(TaskCategoryElemType):
    class Meta:
        name = "taskCategory"


@dataclass(kw_only=True)
class TechName(TechNameElemType):
    class Meta:
        name = "techName"


@dataclass(kw_only=True)
class TerminologyIdent(TerminologyIdentElemType):
    class Meta:
        name = "terminologyIdent"


@dataclass(kw_only=True)
class ToolIdent(ToolIdentElemType):
    class Meta:
        name = "toolIdent"


@dataclass(kw_only=True)
class Transport(TransportElemType):
    class Meta:
        name = "transport"


@dataclass(kw_only=True)
class UnitOfIssue(UnitOfIssueElemType):
    class Meta:
        name = "unitOfIssue"


@dataclass(kw_only=True)
class UnitOfIssueQualificationSegment(UnitOfIssueQualificationSegmentElemType):
    class Meta:
        name = "unitOfIssueQualificationSegment"


@dataclass(kw_only=True)
class Usage(UsageElemType):
    class Meta:
        name = "usage"


@dataclass(kw_only=True)
class ValueAfterAction(ValueAfterActionElemType):
    class Meta:
        name = "valueAfterAction"


@dataclass(kw_only=True)
class VerbatimText(VerbatimTextElemType):
    class Meta:
        name = "verbatimText"


@dataclass(kw_only=True)
class WarningIdent(WarningIdentElemType):
    class Meta:
        name = "warningIdent"


@dataclass(kw_only=True)
class ZoneIdent(ZoneIdentElemType):
    class Meta:
        name = "zoneIdent"


@dataclass(kw_only=True)
class ZoneSide(ZoneSideElemType):
    class Meta:
        name = "zoneSide"


@dataclass(kw_only=True)
class AcronymElemType:
    class Meta:
        name = "acronymElemType"

    acronym_term: AcronymTerm = field(
        metadata={
            "name": "acronymTerm",
            "type": "Element",
        }
    )
    acronym_definition: AcronymDefinition = field(
        metadata={
            "name": "acronymDefinition",
            "type": "Element",
        }
    )
    acronym_type: AcronymTypeAttType = field(
        default=AcronymTypeAttType.AT01,
        metadata={
            "name": "acronymType",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class BooleanValue(BooleanValueElemType):
    class Meta:
        name = "booleanValue"


@dataclass(kw_only=True)
class BusinessUnitAddress(AddressElemType):
    class Meta:
        name = "businessUnitAddress"


@dataclass(kw_only=True)
class ContactPersonAddress(AddressElemType):
    class Meta:
        name = "contactPersonAddress"


@dataclass(kw_only=True)
class ControlIndicatorFunctionElemType:
    class Meta:
        name = "controlIndicatorFunctionElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "symbol",
                    "type": Symbol,
                },
                {
                    "name": "inlineSignificantData",
                    "type": InlineSignificantData,
                },
                {
                    "name": "subScript",
                    "type": SubScript,
                },
                {
                    "name": "superScript",
                    "type": SuperScript,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class DisplayTextElemType:
    class Meta:
        name = "displayTextElemType"

    simple_para: list[SimplePara] = field(
        default_factory=list,
        metadata={
            "name": "simplePara",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class DmIdentElemType:
    class Meta:
        name = "dmIdentElemType"

    ident_extension: None | IdentExtension = field(
        default=None,
        metadata={
            "name": "identExtension",
            "type": "Element",
        },
    )
    dm_code: DmCode = field(
        metadata={
            "name": "dmCode",
            "type": "Element",
        }
    )
    language: Language = field(
        metadata={
            "type": "Element",
        }
    )
    issue_info: IssueInfo = field(
        metadata={
            "name": "issueInfo",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class DmRefIdentElemType:
    class Meta:
        name = "dmRefIdentElemType"

    ident_extension: None | IdentExtension = field(
        default=None,
        metadata={
            "name": "identExtension",
            "type": "Element",
        },
    )
    dm_code: DmCode = field(
        metadata={
            "name": "dmCode",
            "type": "Element",
        }
    )
    issue_info: None | IssueInfo = field(
        default=None,
        metadata={
            "name": "issueInfo",
            "type": "Element",
        },
    )
    language: None | Language = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class DmTitleElemType:
    class Meta:
        name = "dmTitleElemType"

    tech_name: TechName = field(
        metadata={
            "name": "techName",
            "type": "Element",
        }
    )
    info_name: None | InfoName = field(
        default=None,
        metadata={
            "name": "infoName",
            "type": "Element",
        },
    )
    info_name_variant: None | InfoNameVariant = field(
        default=None,
        metadata={
            "name": "infoNameVariant",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class EvaluateElemType:
    class Meta:
        name = "evaluateElemType"

    evaluate: list[Evaluate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 2,
        },
    )
    assert_value: list[Assert] = field(
        default_factory=list,
        metadata={
            "name": "assert",
            "type": "Element",
            "min_occurs": 2,
        },
    )
    and_or: AndOrAttType = field(
        metadata={
            "name": "andOr",
            "type": "Attribute",
        }
    )
    applic_display_class: None | str = field(
        default=None,
        metadata={
            "name": "applicDisplayClass",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class FastenerElemType:
    class Meta:
        name = "fastenerElemType"

    fastener_type: FastenerType = field(
        metadata={
            "name": "fastenerType",
            "type": "Element",
        }
    )
    fastener_quantity: FastenerQuantity = field(
        metadata={
            "name": "fastenerQuantity",
            "type": "Element",
        }
    )
    hinged_fastener_flag: None | str = field(
        default=None,
        metadata={
            "name": "hingedFastenerFlag",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class LogoElemType:
    class Meta:
        name = "logoElemType"

    symbol: list[Symbol] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class LowestAuthorizedLevelGroupElemType:
    class Meta:
        name = "lowestAuthorizedLevelGroupElemType"

    lowest_authorized_level: list[LowestAuthorizedLevel] = field(
        default_factory=list,
        metadata={
            "name": "lowestAuthorizedLevel",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class PmRefAddressItemsElemType:
    class Meta:
        name = "pmRefAddressItemsElemType"

    pm_title: None | PmTitle = field(
        default=None,
        metadata={
            "name": "pmTitle",
            "type": "Element",
        },
    )
    issue_date: None | IssueDate = field(
        default=None,
        metadata={
            "name": "issueDate",
            "type": "Element",
        },
    )
    security: None | Security = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    responsible_partner_company: None | ResponsiblePartnerCompany = field(
        default=None,
        metadata={
            "name": "responsiblePartnerCompany",
            "type": "Element",
        },
    )
    pub_media: list[PubMedia] = field(
        default_factory=list,
        metadata={
            "name": "pubMedia",
            "type": "Element",
        },
    )
    short_pm_title: None | ShortPmTitle = field(
        default=None,
        metadata={
            "name": "shortPmTitle",
            "type": "Element",
        },
    )
    type_value: TypeValue = field(
        default=TypeValue.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: ShowValue = field(
        default=ShowValue.REPLACE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: ActuateValue = field(
        default=ActuateValue.ON_REQUEST,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )


@dataclass(kw_only=True)
class PmRefIdent(PmRefIdentElemType):
    class Meta:
        name = "pmRefIdent"


@dataclass(kw_only=True)
class QualityAssuranceElemType:
    class Meta:
        name = "qualityAssuranceElemType"

    unverified: None | Unverified = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    first_verification: None | FirstVerification = field(
        default=None,
        metadata={
            "name": "firstVerification",
            "type": "Element",
        },
    )
    second_verification: None | SecondVerification = field(
        default=None,
        metadata={
            "name": "secondVerification",
            "type": "Element",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class QuantityGroupElemType:
    class Meta:
        name = "quantityGroupElemType"

    quantity_value: list[QuantityValue] = field(
        default_factory=list,
        metadata={
            "name": "quantityValue",
            "type": "Element",
        },
    )
    quantity_tolerance: list[QuantityTolerance] = field(
        default_factory=list,
        metadata={
            "name": "quantityTolerance",
            "type": "Element",
            "max_occurs": 4,
            "sequence": 1,
        },
    )
    quantity_group_type: QuantityGroupTypeAttType = field(
        default=QuantityGroupTypeAttType.NOMINAL,
        metadata={
            "name": "quantityGroupType",
            "type": "Attribute",
        },
    )
    quantity_unit_of_measure: None | QuantityUnitOfMeasureAttType = field(
        default=None,
        metadata={
            "name": "quantityUnitOfMeasure",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class RemarksElemType:
    class Meta:
        name = "remarksElemType"

    simple_para: list[SimplePara] = field(
        default_factory=list,
        metadata={
            "name": "simplePara",
            "type": "Element",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class RetrofitElemType:
    class Meta:
        name = "retrofitElemType"

    modification: list[Modification] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class SetValue(SetValueElemType):
    class Meta:
        name = "setValue"


@dataclass(kw_only=True)
class ShippingInfoElemType:
    class Meta:
        name = "shippingInfoElemType"

    packaging: list[Packaging] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    transport: list[Transport] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    shelf_life: list[ShelfLife] = field(
        default_factory=list,
        metadata={
            "name": "shelfLife",
            "type": "Element",
        },
    )
    simple_remark: list[SimpleRemark] = field(
        default_factory=list,
        metadata={
            "name": "simpleRemark",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class SourceDmIdentGenericElemType:
    class Meta:
        name = "sourceDmIdentGenericElemType"

    ident_extension: None | IdentExtension = field(
        default=None,
        metadata={
            "name": "identExtension",
            "type": "Element",
        },
    )
    dm_code: DmCode = field(
        metadata={
            "name": "dmCode",
            "type": "Element",
        }
    )
    language: Language = field(
        metadata={
            "type": "Element",
        }
    )
    issue_info: IssueInfo = field(
        metadata={
            "name": "issueInfo",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class TerminologyTermElemType:
    class Meta:
        name = "terminologyTermElemType"

    internal_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "internalRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "subScript",
                    "type": SubScript,
                },
                {
                    "name": "superScript",
                    "type": SuperScript,
                },
                {
                    "name": "symbol",
                    "type": Symbol,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Acronym(AcronymElemType):
    class Meta:
        name = "acronym"


@dataclass(kw_only=True)
class ContactPersonElemType:
    class Meta:
        name = "contactPersonElemType"

    last_name: LastName = field(
        metadata={
            "name": "lastName",
            "type": "Element",
        }
    )
    middle_name: None | MiddleName = field(
        default=None,
        metadata={
            "name": "middleName",
            "type": "Element",
        },
    )
    first_name: None | FirstName = field(
        default=None,
        metadata={
            "name": "firstName",
            "type": "Element",
        },
    )
    job_title: None | JobTitle = field(
        default=None,
        metadata={
            "name": "jobTitle",
            "type": "Element",
        },
    )
    contact_person_address: None | ContactPersonAddress = field(
        default=None,
        metadata={
            "name": "contactPersonAddress",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    person_prefix: None | str = field(
        default=None,
        metadata={
            "name": "personPrefix",
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ControlIndicatorFunction(ControlIndicatorFunctionElemType):
    class Meta:
        name = "controlIndicatorFunction"


@dataclass(kw_only=True)
class DisplayText(DisplayTextElemType):
    class Meta:
        name = "displayText"


@dataclass(kw_only=True)
class DmIdent(DmIdentElemType):
    class Meta:
        name = "dmIdent"


@dataclass(kw_only=True)
class DmRefIdent(DmRefIdentElemType):
    class Meta:
        name = "dmRefIdent"


@dataclass(kw_only=True)
class DmTitle(DmTitleElemType):
    class Meta:
        name = "dmTitle"


@dataclass(kw_only=True)
class Evaluate(EvaluateElemType):
    class Meta:
        name = "evaluate"


@dataclass(kw_only=True)
class ExpressionElemType:
    class Meta:
        name = "expressionElemType"

    expression: list[Expression] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 3,
        },
    )
    boolean_operator: None | BooleanOperator = field(
        default=None,
        metadata={
            "name": "booleanOperator",
            "type": "Element",
        },
    )
    number_operator: None | NumberOperator = field(
        default=None,
        metadata={
            "name": "numberOperator",
            "type": "Element",
        },
    )
    set_operator: None | SetOperator = field(
        default=None,
        metadata={
            "name": "setOperator",
            "type": "Element",
        },
    )
    string_operator: None | StringOperator = field(
        default=None,
        metadata={
            "name": "stringOperator",
            "type": "Element",
        },
    )
    boolean_function: None | BooleanFunction = field(
        default=None,
        metadata={
            "name": "booleanFunction",
            "type": "Element",
        },
    )
    number_function: None | NumberFunction = field(
        default=None,
        metadata={
            "name": "numberFunction",
            "type": "Element",
        },
    )
    set_function: None | SetFunction = field(
        default=None,
        metadata={
            "name": "setFunction",
            "type": "Element",
        },
    )
    string_function: None | StringFunction = field(
        default=None,
        metadata={
            "name": "stringFunction",
            "type": "Element",
        },
    )
    sub_string_function: None | SubStringFunction = field(
        default=None,
        metadata={
            "name": "subStringFunction",
            "type": "Element",
        },
    )
    variable_ref: None | VariableRef = field(
        default=None,
        metadata={
            "name": "variableRef",
            "type": "Element",
        },
    )
    global_property_ref: None | GlobalPropertyRef = field(
        default=None,
        metadata={
            "name": "globalPropertyRef",
            "type": "Element",
        },
    )
    assert_value: None | Assert = field(
        default=None,
        metadata={
            "name": "assert",
            "type": "Element",
        },
    )
    boolean_value: None | BooleanValue = field(
        default=None,
        metadata={
            "name": "booleanValue",
            "type": "Element",
        },
    )
    string_value: None | StringValue = field(
        default=None,
        metadata={
            "name": "stringValue",
            "type": "Element",
        },
    )
    real_value: None | RealValue = field(
        default=None,
        metadata={
            "name": "realValue",
            "type": "Element",
        },
    )
    integer_value: None | IntegerValue = field(
        default=None,
        metadata={
            "name": "integerValue",
            "type": "Element",
        },
    )
    set_value: None | SetValue = field(
        default=None,
        metadata={
            "name": "setValue",
            "type": "Element",
        },
    )
    no_value: None | NoValue = field(
        default=None,
        metadata={
            "name": "noValue",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    human_readable_form: None | str = field(
        default=None,
        metadata={
            "name": "humanReadableForm",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Fastener(FastenerElemType):
    class Meta:
        name = "fastener"


@dataclass(kw_only=True)
class Logo(LogoElemType):
    class Meta:
        name = "logo"


@dataclass(kw_only=True)
class LowestAuthorizedLevelGroup(LowestAuthorizedLevelGroupElemType):
    class Meta:
        name = "lowestAuthorizedLevelGroup"


@dataclass(kw_only=True)
class PmRefAddressItems(PmRefAddressItemsElemType):
    class Meta:
        name = "pmRefAddressItems"


@dataclass(kw_only=True)
class QualityAssurance(QualityAssuranceElemType):
    class Meta:
        name = "qualityAssurance"


@dataclass(kw_only=True)
class QuantityGroup(QuantityGroupElemType):
    class Meta:
        name = "quantityGroup"


@dataclass(kw_only=True)
class Remarks(RemarksElemType):
    class Meta:
        name = "remarks"


@dataclass(kw_only=True)
class RepositorySourceDmIdent(SourceDmIdentGenericElemType):
    class Meta:
        name = "repositorySourceDmIdent"


@dataclass(kw_only=True)
class Retrofit(RetrofitElemType):
    class Meta:
        name = "retrofit"


@dataclass(kw_only=True)
class ShippingInfo(ShippingInfoElemType):
    class Meta:
        name = "shippingInfo"


@dataclass(kw_only=True)
class SourceDmIdent(SourceDmIdentGenericElemType):
    class Meta:
        name = "sourceDmIdent"


@dataclass(kw_only=True)
class TerminologyTerm(TerminologyTermElemType):
    class Meta:
        name = "terminologyTerm"


@dataclass(kw_only=True)
class AuthorityExceptionsElemType:
    class Meta:
        name = "authorityExceptionsElemType"

    product_configuration: None | ProductConfiguration = field(
        default=None,
        metadata={
            "name": "productConfiguration",
            "type": "Element",
        },
    )
    retrofit: None | Retrofit = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ContactPerson(ContactPersonElemType):
    class Meta:
        name = "contactPerson"


@dataclass(kw_only=True)
class DmAddressItemsElemType:
    class Meta:
        name = "dmAddressItemsElemType"

    issue_date: IssueDate = field(
        metadata={
            "name": "issueDate",
            "type": "Element",
        }
    )
    dm_title: DmTitle = field(
        metadata={
            "name": "dmTitle",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class DmRefAddressItemsElemType:
    class Meta:
        name = "dmRefAddressItemsElemType"

    dm_title: None | DmTitle = field(
        default=None,
        metadata={
            "name": "dmTitle",
            "type": "Element",
        },
    )
    issue_date: None | IssueDate = field(
        default=None,
        metadata={
            "name": "issueDate",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Expression(ExpressionElemType):
    class Meta:
        name = "expression"


@dataclass(kw_only=True)
class ExternalPubCodeElemType:
    class Meta:
        name = "externalPubCodeElemType"

    pub_coding_scheme: None | str = field(
        default=None,
        metadata={
            "name": "pubCodingScheme",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "indexFlag",
                    "type": IndexFlag,
                },
                {
                    "name": "subScript",
                    "type": SubScript,
                },
                {
                    "name": "superScript",
                    "type": SuperScript,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
                {
                    "name": "acronymTerm",
                    "type": AcronymTerm,
                },
                {
                    "name": "verbatimText",
                    "type": VerbatimText,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class ExternalPubIssueElemType:
    class Meta:
        name = "externalPubIssueElemType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "indexFlag",
                    "type": IndexFlag,
                },
                {
                    "name": "subScript",
                    "type": SubScript,
                },
                {
                    "name": "superScript",
                    "type": SuperScript,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
                {
                    "name": "acronymTerm",
                    "type": AcronymTerm,
                },
                {
                    "name": "verbatimText",
                    "type": VerbatimText,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class ExternalPubTitleElemType:
    class Meta:
        name = "externalPubTitleElemType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "indexFlag",
                    "type": IndexFlag,
                },
                {
                    "name": "subScript",
                    "type": SubScript,
                },
                {
                    "name": "superScript",
                    "type": SuperScript,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
                {
                    "name": "acronymTerm",
                    "type": AcronymTerm,
                },
                {
                    "name": "verbatimText",
                    "type": VerbatimText,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class PmRefElemType:
    class Meta:
        name = "pmRefElemType"

    pm_ref_ident: PmRefIdent = field(
        metadata={
            "name": "pmRefIdent",
            "type": "Element",
        }
    )
    pm_ref_address_items: None | PmRefAddressItems = field(
        default=None,
        metadata={
            "name": "pmRefAddressItems",
            "type": "Element",
        },
    )
    behavior: None | Behavior = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    reference_usage: None | ReferenceUsageAttType = field(
        default=None,
        metadata={
            "name": "referenceUsage",
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    type_value: TypeValue = field(
        default=TypeValue.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: ShowValue = field(
        default=ShowValue.REPLACE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: ActuateValue = field(
        default=ActuateValue.ON_REQUEST,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class QuantityElemType:
    class Meta:
        name = "quantityElemType"

    quantity_type: None | QuantityTypeAttType = field(
        default=None,
        metadata={
            "name": "quantityType",
            "type": "Attribute",
        },
    )
    quantity_type_specifics: None | str = field(
        default=None,
        metadata={
            "name": "quantityTypeSpecifics",
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "quantityGroup",
                    "type": QuantityGroup,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class ShortExternalPubTitleElemType:
    class Meta:
        name = "shortExternalPubTitleElemType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "indexFlag",
                    "type": IndexFlag,
                },
                {
                    "name": "subScript",
                    "type": SubScript,
                },
                {
                    "name": "superScript",
                    "type": SuperScript,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
                {
                    "name": "acronymTerm",
                    "type": AcronymTerm,
                },
                {
                    "name": "verbatimText",
                    "type": VerbatimText,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class ApplicElemType:
    class Meta:
        name = "applicElemType"

    display_text: None | DisplayText = field(
        default=None,
        metadata={
            "name": "displayText",
            "type": "Element",
        },
    )
    assert_value: None | Assert = field(
        default=None,
        metadata={
            "name": "assert",
            "type": "Element",
        },
    )
    evaluate: None | Evaluate = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    expression: None | Expression = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    applic_configuration: None | ApplicConfigurationAttType = field(
        default=None,
        metadata={
            "name": "applicConfiguration",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class AuthorityExceptions(AuthorityExceptionsElemType):
    class Meta:
        name = "authorityExceptions"


@dataclass(kw_only=True)
class BusinessUnitElemType:
    class Meta:
        name = "businessUnitElemType"

    business_unit_name: BusinessUnitName = field(
        metadata={
            "name": "businessUnitName",
            "type": "Element",
        }
    )
    business_unit_address: None | BusinessUnitAddress = field(
        default=None,
        metadata={
            "name": "businessUnitAddress",
            "type": "Element",
        },
    )
    contact_person: list[ContactPerson] = field(
        default_factory=list,
        metadata={
            "name": "contactPerson",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class DmAddressItems(DmAddressItemsElemType):
    class Meta:
        name = "dmAddressItems"


@dataclass(kw_only=True)
class DmRefAddressItems(DmRefAddressItemsElemType):
    class Meta:
        name = "dmRefAddressItems"


@dataclass(kw_only=True)
class ExternalPubCode(ExternalPubCodeElemType):
    class Meta:
        name = "externalPubCode"


@dataclass(kw_only=True)
class ExternalPubIssue(ExternalPubIssueElemType):
    class Meta:
        name = "externalPubIssue"


@dataclass(kw_only=True)
class ExternalPubTitle(ExternalPubTitleElemType):
    class Meta:
        name = "externalPubTitle"


@dataclass(kw_only=True)
class PmRef(PmRefElemType):
    class Meta:
        name = "pmRef"


@dataclass(kw_only=True)
class Quantity(QuantityElemType):
    class Meta:
        name = "quantity"


@dataclass(kw_only=True)
class ShortExternalPubTitle(ShortExternalPubTitleElemType):
    class Meta:
        name = "shortExternalPubTitle"


@dataclass(kw_only=True)
class Applic(ApplicElemType):
    class Meta:
        name = "applic"


@dataclass(kw_only=True)
class BoundaryElemType:
    class Meta:
        name = "boundaryElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "quantity",
                    "type": Quantity,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class BusinessUnit(BusinessUnitElemType):
    class Meta:
        name = "businessUnit"


@dataclass(kw_only=True)
class DmAddressElemType:
    class Meta:
        name = "dmAddressElemType"

    dm_ident: DmIdent = field(
        metadata={
            "name": "dmIdent",
            "type": "Element",
        }
    )
    dm_address_items: DmAddressItems = field(
        metadata={
            "name": "dmAddressItems",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class DmRefElemType:
    class Meta:
        name = "dmRefElemType"

    dm_ref_ident: DmRefIdent = field(
        metadata={
            "name": "dmRefIdent",
            "type": "Element",
        }
    )
    dm_ref_address_items: None | DmRefAddressItems = field(
        default=None,
        metadata={
            "name": "dmRefAddressItems",
            "type": "Element",
        },
    )
    behavior: None | Behavior = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    referred_fragment: None | str = field(
        default=None,
        metadata={
            "name": "referredFragment",
            "type": "Attribute",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    reference_usage: None | ReferenceUsageAttType = field(
        default=None,
        metadata={
            "name": "referenceUsage",
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    type_value: TypeValue = field(
        default=TypeValue.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: ShowValue = field(
        default=ShowValue.REPLACE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: ActuateValue = field(
        default=ActuateValue.ON_REQUEST,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ExternalPubIssueInfoElemType:
    class Meta:
        name = "externalPubIssueInfoElemType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "externalPubIssue",
                    "type": ExternalPubIssue,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class ExternalPubRefAddressItemsElemType:
    class Meta:
        name = "externalPubRefAddressItemsElemType"

    external_pub_issue_date: None | ExternalPubIssueDate = field(
        default=None,
        metadata={
            "name": "externalPubIssueDate",
            "type": "Element",
        },
    )
    security: None | Security = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    responsible_partner_company: None | ResponsiblePartnerCompany = field(
        default=None,
        metadata={
            "name": "responsiblePartnerCompany",
            "type": "Element",
        },
    )
    pub_media: list[PubMedia] = field(
        default_factory=list,
        metadata={
            "name": "pubMedia",
            "type": "Element",
        },
    )
    short_external_pub_title: None | ShortExternalPubTitle = field(
        default=None,
        metadata={
            "name": "shortExternalPubTitle",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class TechStandardElemType:
    class Meta:
        name = "techStandardElemType"

    authority_info_and_tp: None | AuthorityInfoAndTp = field(
        default=None,
        metadata={
            "name": "authorityInfoAndTp",
            "type": "Element",
        },
    )
    authority_info: None | AuthorityInfo = field(
        default=None,
        metadata={
            "name": "authorityInfo",
            "type": "Element",
        },
    )
    tech_pub_base: None | TechPubBase = field(
        default=None,
        metadata={
            "name": "techPubBase",
            "type": "Element",
        },
    )
    authority_exceptions: AuthorityExceptions = field(
        metadata={
            "name": "authorityExceptions",
            "type": "Element",
        }
    )
    authority_notes: AuthorityNotes = field(
        metadata={
            "name": "authorityNotes",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Boundary(BoundaryElemType):
    class Meta:
        name = "boundary"


@dataclass(kw_only=True)
class ClassificationActionElemType:
    class Meta:
        name = "classificationActionElemType"

    value_after_action: None | ValueAfterAction = field(
        default=None,
        metadata={
            "name": "valueAfterAction",
            "type": "Element",
        },
    )
    business_unit: BusinessUnit = field(
        metadata={
            "name": "businessUnit",
            "type": "Element",
        }
    )
    derivative_source: DerivativeSource = field(
        metadata={
            "name": "derivativeSource",
            "type": "Element",
        }
    )
    action_ident_type: ActionIdentTypeAttType = field(
        metadata={
            "name": "actionIdentType",
            "type": "Attribute",
        }
    )
    year: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"\d{4}",
        }
    )
    month: str = field(
        metadata={
            "type": "Attribute",
            "max_inclusive": "12",
            "pattern": r"\d{2}",
        }
    )
    day: str = field(
        metadata={
            "type": "Attribute",
            "max_inclusive": "31",
            "pattern": r"\d{2}",
        }
    )


@dataclass(kw_only=True)
class DmAddress(DmAddressElemType):
    class Meta:
        name = "dmAddress"


@dataclass(kw_only=True)
class DmRef(DmRefElemType):
    class Meta:
        name = "dmRef"


@dataclass(kw_only=True)
class ExternalPubIssueInfo(ExternalPubIssueInfoElemType):
    class Meta:
        name = "externalPubIssueInfo"


@dataclass(kw_only=True)
class ExternalPubRefAddressItems(ExternalPubRefAddressItemsElemType):
    class Meta:
        name = "externalPubRefAddressItems"


@dataclass(kw_only=True)
class ReferencedApplicGroupElemType:
    class Meta:
        name = "referencedApplicGroupElemType"

    applic: list[Applic] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class TechStandard(TechStandardElemType):
    class Meta:
        name = "techStandard"


@dataclass(kw_only=True)
class ApplicCrossRefTableRefElemType:
    class Meta:
        name = "applicCrossRefTableRefElemType"

    dm_ref: DmRef = field(
        metadata={
            "name": "dmRef",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ApplicRefElemType:
    class Meta:
        name = "applicRefElemType"

    dm_ref: None | DmRef = field(
        default=None,
        metadata={
            "name": "dmRef",
            "type": "Element",
        },
    )
    applic_ident_value: str = field(
        metadata={
            "name": "applicIdentValue",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class BoundaryFromElemType:
    class Meta:
        name = "boundaryFromElemType"

    boundary: list[Boundary] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class BoundaryToElemType:
    class Meta:
        name = "boundaryToElemType"

    boundary: list[Boundary] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class BrexDmRefElemType:
    class Meta:
        name = "brexDmRefElemType"

    dm_ref: DmRef = field(
        metadata={
            "name": "dmRef",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ClassificationAction(ClassificationActionElemType):
    class Meta:
        name = "classificationAction"


@dataclass(kw_only=True)
class EnterpriseRefElemType:
    class Meta:
        name = "enterpriseRefElemType"

    name: None | Name = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    short_name: None | ShortName = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
        },
    )
    dm_ref: None | DmRef = field(
        default=None,
        metadata={
            "name": "dmRef",
            "type": "Element",
        },
    )
    business_unit: list[BusinessUnit] = field(
        default_factory=list,
        metadata={
            "name": "businessUnit",
            "type": "Element",
        },
    )
    enterprise_type: None | str = field(
        default=None,
        metadata={
            "name": "enterpriseType",
            "type": "Attribute",
        },
    )
    enterprise_ref_type: None | str = field(
        default=None,
        metadata={
            "name": "enterpriseRefType",
            "type": "Attribute",
        },
    )
    manufacturer_code_value: str = field(
        metadata={
            "name": "manufacturerCodeValue",
            "type": "Attribute",
        }
    )
    qualified_site_flag: None | str = field(
        default=None,
        metadata={
            "name": "qualifiedSiteFlag",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ExportRegistrationStmtElemType:
    class Meta:
        name = "exportRegistrationStmtElemType"

    simple_para: list[SimplePara] = field(
        default_factory=list,
        metadata={
            "name": "simplePara",
            "type": "Element",
        },
    )
    dm_ref: list[DmRef] = field(
        default_factory=list,
        metadata={
            "name": "dmRef",
            "type": "Element",
        },
    )
    export_role: None | ExportRoleAttType = field(
        default=None,
        metadata={
            "name": "exportRole",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ExternalPubRefIdentElemType:
    class Meta:
        name = "externalPubRefIdentElemType"

    external_pub_code: None | ExternalPubCode = field(
        default=None,
        metadata={
            "name": "externalPubCode",
            "type": "Element",
        },
    )
    external_pub_title: None | ExternalPubTitle = field(
        default=None,
        metadata={
            "name": "externalPubTitle",
            "type": "Element",
        },
    )
    external_pub_issue_info: None | ExternalPubIssueInfo = field(
        default=None,
        metadata={
            "name": "externalPubIssueInfo",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class FunctionalPhysicalAreaRefElemType:
    class Meta:
        name = "functionalPhysicalAreaRefElemType"

    dm_ref: None | DmRef = field(
        default=None,
        metadata={
            "name": "dmRef",
            "type": "Element",
        },
    )
    system_diff_code: None | str = field(
        default=None,
        metadata={
            "name": "systemDiffCode",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{1,4}",
        },
    )
    system_code: str = field(
        metadata={
            "name": "systemCode",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{2,3}",
        }
    )
    sub_system_code: None | str = field(
        default=None,
        metadata={
            "name": "subSystemCode",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{1}",
        },
    )
    sub_sub_system_code: None | str = field(
        default=None,
        metadata={
            "name": "subSubSystemCode",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{1}",
        },
    )
    assy_code: None | str = field(
        default=None,
        metadata={
            "name": "assyCode",
            "type": "Attribute",
            "pattern": r"([A-Z0-9]{2}|[A-Z0-9]{4})",
        },
    )
    disassy_code: None | str = field(
        default=None,
        metadata={
            "name": "disassyCode",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{2}",
        },
    )
    disassy_code_variant: None | str = field(
        default=None,
        metadata={
            "name": "disassyCodeVariant",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{1,3}",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class HazardRefElemType:
    class Meta:
        name = "hazardRefElemType"

    dm_ref: None | DmRef = field(
        default=None,
        metadata={
            "name": "dmRef",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    hazard_ident_number: str = field(
        metadata={
            "name": "hazardIdentNumber",
            "type": "Attribute",
        }
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ReferencedApplicGroup(ReferencedApplicGroupElemType):
    class Meta:
        name = "referencedApplicGroup"


@dataclass(kw_only=True)
class ApplicCrossRefTableRef(ApplicCrossRefTableRefElemType):
    class Meta:
        name = "applicCrossRefTableRef"


@dataclass(kw_only=True)
class ApplicRef(ApplicRefElemType):
    class Meta:
        name = "applicRef"


@dataclass(kw_only=True)
class BoundaryFrom(BoundaryFromElemType):
    class Meta:
        name = "boundaryFrom"


@dataclass(kw_only=True)
class BoundaryTo(BoundaryToElemType):
    class Meta:
        name = "boundaryTo"


@dataclass(kw_only=True)
class BrexDmRef(BrexDmRefElemType):
    class Meta:
        name = "brexDmRef"


@dataclass(kw_only=True)
class ClassificationActionGroupElemType:
    class Meta:
        name = "classificationActionGroupElemType"

    classification_action: list[ClassificationAction] = field(
        default_factory=list,
        metadata={
            "name": "classificationAction",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class EnterpriseRef(EnterpriseRefElemType):
    class Meta:
        name = "enterpriseRef"


@dataclass(kw_only=True)
class ExportRegistrationStmt(ExportRegistrationStmtElemType):
    class Meta:
        name = "exportRegistrationStmt"


@dataclass(kw_only=True)
class ExternalPubRefIdent(ExternalPubRefIdentElemType):
    class Meta:
        name = "externalPubRefIdent"


@dataclass(kw_only=True)
class FunctionalPhysicalAreaRef(FunctionalPhysicalAreaRefElemType):
    class Meta:
        name = "functionalPhysicalAreaRef"


@dataclass(kw_only=True)
class HazardRef(HazardRefElemType):
    class Meta:
        name = "hazardRef"


@dataclass(kw_only=True)
class ClassificationActionGroup(ClassificationActionGroupElemType):
    class Meta:
        name = "classificationActionGroup"


@dataclass(kw_only=True)
class EnterpriseInfoElemType:
    class Meta:
        name = "enterpriseInfoElemType"

    enterprise_ref: EnterpriseRef = field(
        metadata={
            "name": "enterpriseRef",
            "type": "Element",
        }
    )
    shipping_info: None | ShippingInfo = field(
        default=None,
        metadata={
            "name": "shippingInfo",
            "type": "Element",
        },
    )
    locally_supplied_flag: str = field(
        metadata={
            "name": "locallySuppliedFlag",
            "type": "Attribute",
            "pattern": r"[01]",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ExportControlElemType:
    class Meta:
        name = "exportControlElemType"

    export_registration_stmt: list[ExportRegistrationStmt] = field(
        default_factory=list,
        metadata={
            "name": "exportRegistrationStmt",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    export_registration_code: list[ExportRegistrationCode] = field(
        default_factory=list,
        metadata={
            "name": "exportRegistrationCode",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    export_regulation_type: None | str = field(
        default=None,
        metadata={
            "name": "exportRegulationType",
            "type": "Attribute",
        },
    )
    government_authority: None | str = field(
        default=None,
        metadata={
            "name": "governmentAuthority",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ExternalPubRefElemType:
    class Meta:
        name = "externalPubRefElemType"

    external_pub_ref_ident: ExternalPubRefIdent = field(
        metadata={
            "name": "externalPubRefIdent",
            "type": "Element",
        }
    )
    external_pub_ref_address_items: None | ExternalPubRefAddressItems = field(
        default=None,
        metadata={
            "name": "externalPubRefAddressItems",
            "type": "Element",
        },
    )
    behavior: None | Behavior = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ext_entity_ident: None | str = field(
        default=None,
        metadata={
            "name": "extEntityIdent",
            "type": "Attribute",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    reference_usage: None | ReferenceUsageAttType = field(
        default=None,
        metadata={
            "name": "referenceUsage",
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    type_value: TypeValue = field(
        default=TypeValue.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: ShowValue = field(
        default=ShowValue.NEW,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: ActuateValue = field(
        default=ActuateValue.ON_REQUEST,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class FunctionalPhysicalAreaRefGroupElemType:
    class Meta:
        name = "functionalPhysicalAreaRefGroupElemType"

    functional_physical_area_ref: list[FunctionalPhysicalAreaRef] = field(
        default_factory=list,
        metadata={
            "name": "functionalPhysicalAreaRef",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ProcurementDataElemType:
    class Meta:
        name = "procurementDataElemType"

    enterprise_ref: list[EnterpriseRef] = field(
        default_factory=list,
        metadata={
            "name": "enterpriseRef",
            "type": "Element",
        },
    )
    buyer_furnished_equip_flag: None | BuyerFurnishedEquipFlag = field(
        default=None,
        metadata={
            "name": "buyerFurnishedEquipFlag",
            "type": "Element",
        },
    )
    sourcing_type: list[SourcingType] = field(
        default_factory=list,
        metadata={
            "name": "sourcingType",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ReferencedApplicGroupRefElemType:
    class Meta:
        name = "referencedApplicGroupRefElemType"

    applic_ref: list[ApplicRef] = field(
        default_factory=list,
        metadata={
            "name": "applicRef",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class DerivativeClassificationElemType:
    class Meta:
        name = "derivativeClassificationElemType"

    classification_action_group: list[ClassificationActionGroup] = field(
        default_factory=list,
        metadata={
            "name": "classificationActionGroup",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class EnterpriseInfo(EnterpriseInfoElemType):
    class Meta:
        name = "enterpriseInfo"


@dataclass(kw_only=True)
class ExportControl(ExportControlElemType):
    class Meta:
        name = "exportControl"


@dataclass(kw_only=True)
class ExternalPubRef(ExternalPubRefElemType):
    class Meta:
        name = "externalPubRef"


@dataclass(kw_only=True)
class FunctionalPhysicalAreaRefGroup(FunctionalPhysicalAreaRefGroupElemType):
    class Meta:
        name = "functionalPhysicalAreaRefGroup"


@dataclass(kw_only=True)
class ProcurementData(ProcurementDataElemType):
    class Meta:
        name = "procurementData"


@dataclass(kw_only=True)
class ReferencedApplicGroupRef(ReferencedApplicGroupRefElemType):
    class Meta:
        name = "referencedApplicGroupRef"


@dataclass(kw_only=True)
class DerivativeClassification(DerivativeClassificationElemType):
    class Meta:
        name = "derivativeClassification"


@dataclass(kw_only=True)
class EnterpriseGroupElemType:
    class Meta:
        name = "enterpriseGroupElemType"

    enterprise_info: list[EnterpriseInfo] = field(
        default_factory=list,
        metadata={
            "name": "enterpriseInfo",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class FunctionalPhysicalAreaSpecElemType:
    class Meta:
        name = "functionalPhysicalAreaSpecElemType"

    functional_physical_area_ident: FunctionalPhysicalAreaIdent = field(
        metadata={
            "name": "functionalPhysicalAreaIdent",
            "type": "Element",
        }
    )
    name: None | Name = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    short_name: None | ShortName = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
        },
    )
    functional_physical_area_ref_group: (
        None | FunctionalPhysicalAreaRefGroup
    ) = field(
        default=None,
        metadata={
            "name": "functionalPhysicalAreaRefGroup",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class RefsElemType:
    class Meta:
        name = "refsElemType"

    dm_ref: list[DmRef] = field(
        default_factory=list,
        metadata={
            "name": "dmRef",
            "type": "Element",
        },
    )
    pm_ref: list[PmRef] = field(
        default_factory=list,
        metadata={
            "name": "pmRef",
            "type": "Element",
        },
    )
    external_pub_ref: list[ExternalPubRef] = field(
        default_factory=list,
        metadata={
            "name": "externalPubRef",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class RestrictionInstructionsElemType:
    class Meta:
        name = "restrictionInstructionsElemType"

    data_distribution: DataDistribution = field(
        metadata={
            "name": "dataDistribution",
            "type": "Element",
        }
    )
    export_control: None | ExportControl = field(
        default=None,
        metadata={
            "name": "exportControl",
            "type": "Element",
        },
    )
    data_handling: None | DataHandling = field(
        default=None,
        metadata={
            "name": "dataHandling",
            "type": "Element",
        },
    )
    data_destruction: None | DataDestruction = field(
        default=None,
        metadata={
            "name": "dataDestruction",
            "type": "Element",
        },
    )
    data_disclosure: None | DataDisclosure = field(
        default=None,
        metadata={
            "name": "dataDisclosure",
            "type": "Element",
        },
    )
    supersedure: None | Supersedure = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class EnterpriseGroup(EnterpriseGroupElemType):
    class Meta:
        name = "enterpriseGroup"


@dataclass(kw_only=True)
class FunctionalPhysicalAreaSpec(FunctionalPhysicalAreaSpecElemType):
    class Meta:
        name = "functionalPhysicalAreaSpec"


@dataclass(kw_only=True)
class Refs(RefsElemType):
    class Meta:
        name = "refs"


@dataclass(kw_only=True)
class RestrictionInstructions(RestrictionInstructionsElemType):
    class Meta:
        name = "restrictionInstructions"


@dataclass(kw_only=True)
class AccessPointRefElemType:
    class Meta:
        name = "accessPointRefElemType"

    name: None | Name = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    short_name: None | ShortName = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
        },
    )
    refs: None | Refs = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    access_point_number: None | str = field(
        default=None,
        metadata={
            "name": "accessPointNumber",
            "type": "Attribute",
        },
    )
    access_point_type_value: None | AccessPointTypeValueAttType = field(
        default=None,
        metadata={
            "name": "accessPointTypeValue",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lsar_data: str = field(
        default="0",
        metadata={
            "name": "lsarData",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ApplicSpecElemType:
    class Meta:
        name = "applicSpecElemType"

    applic_spec_ident: ApplicSpecIdent = field(
        metadata={
            "name": "applicSpecIdent",
            "type": "Element",
        }
    )
    refs: None | Refs = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    applic_map_ref_id: str = field(
        metadata={
            "name": "applicMapRefId",
            "type": "Attribute",
        }
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class CatalogSeqNumberRefElemType:
    class Meta:
        name = "catalogSeqNumberRefElemType"

    refs: None | Refs = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    model_ident_code: None | str = field(
        default=None,
        metadata={
            "name": "modelIdentCode",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{2,14}",
        },
    )
    system_diff_code: None | str = field(
        default=None,
        metadata={
            "name": "systemDiffCode",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{1,4}",
        },
    )
    system_code: None | str = field(
        default=None,
        metadata={
            "name": "systemCode",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{2,3}",
        },
    )
    sub_system_code: None | str = field(
        default=None,
        metadata={
            "name": "subSystemCode",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{1}",
        },
    )
    sub_sub_system_code: None | str = field(
        default=None,
        metadata={
            "name": "subSubSystemCode",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{1}",
        },
    )
    assy_code: None | str = field(
        default=None,
        metadata={
            "name": "assyCode",
            "type": "Attribute",
            "pattern": r"([A-Z0-9]{2}|[A-Z0-9]{4})",
        },
    )
    figure_number: str = field(
        metadata={
            "name": "figureNumber",
            "type": "Attribute",
            "pattern": r"[A-Z0-9]{1}[0-9]{1}",
        }
    )
    figure_number_variant: None | str = field(
        default=None,
        metadata={
            "name": "figureNumberVariant",
            "type": "Attribute",
            "pattern": r"([A-Z-[IO]]{1})",
        },
    )
    item_location_code: None | ItemLocationCodeAttType = field(
        default=None,
        metadata={
            "name": "itemLocationCode",
            "type": "Attribute",
        },
    )
    item: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"\d{3}",
        }
    )
    item_variant: None | str = field(
        default=None,
        metadata={
            "name": "itemVariant",
            "type": "Attribute",
            "pattern": r"([A-Z-[IO]]{1})",
        },
    )
    item_seq_number_value: None | str = field(
        default=None,
        metadata={
            "name": "itemSeqNumberValue",
            "type": "Attribute",
        },
    )
    initial_provisioning_project_number: None | str = field(
        default=None,
        metadata={
            "name": "initialProvisioningProjectNumber",
            "type": "Attribute",
        },
    )
    responsible_partner_company_code: None | str = field(
        default=None,
        metadata={
            "name": "responsiblePartnerCompanyCode",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    type_value: TypeValue = field(
        init=False,
        default=TypeValue.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: ShowValue = field(
        default=ShowValue.NEW,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: ActuateValue = field(
        default=ActuateValue.ON_REQUEST,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class CircuitBreakerRefElemType:
    class Meta:
        name = "circuitBreakerRefElemType"

    name: None | Name = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    short_name: None | ShortName = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
        },
    )
    refs: None | Refs = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    circuit_breaker_number: str = field(
        metadata={
            "name": "circuitBreakerNumber",
            "type": "Attribute",
        }
    )
    circuit_breaker_type: None | CircuitBreakerTypeAttType = field(
        default=None,
        metadata={
            "name": "circuitBreakerType",
            "type": "Attribute",
        },
    )
    circuit_breaker_action: None | CircuitBreakerActionAttType = field(
        default=None,
        metadata={
            "name": "circuitBreakerAction",
            "type": "Attribute",
        },
    )
    check_sum: None | str = field(
        default=None,
        metadata={
            "name": "checkSum",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    installation_ident: None | str = field(
        default=None,
        metadata={
            "name": "installationIdent",
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    context_ident: None | str = field(
        default=None,
        metadata={
            "name": "contextIdent",
            "type": "Attribute",
        },
    )
    manufacturer_code_value: None | str = field(
        default=None,
        metadata={
            "name": "manufacturerCodeValue",
            "type": "Attribute",
        },
    )
    item_originator: None | ItemOriginatorAttType = field(
        default=None,
        metadata={
            "name": "itemOriginator",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ControlIndicatorRefElemType:
    class Meta:
        name = "controlIndicatorRefElemType"

    name: None | Name = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    short_name: None | ShortName = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
        },
    )
    refs: None | Refs = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    control_indicator_number: None | str = field(
        default=None,
        metadata={
            "name": "controlIndicatorNumber",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class EnterpriseSpecElemType:
    class Meta:
        name = "enterpriseSpecElemType"

    enterprise_ident: EnterpriseIdent = field(
        metadata={
            "name": "enterpriseIdent",
            "type": "Element",
        }
    )
    enterprise_ident_alt: list[EnterpriseIdentAlt] = field(
        default_factory=list,
        metadata={
            "name": "enterpriseIdentAlt",
            "type": "Element",
        },
    )
    enterprise_name: EnterpriseName = field(
        metadata={
            "name": "enterpriseName",
            "type": "Element",
        }
    )
    short_name: None | ShortName = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
        },
    )
    business_unit: list[BusinessUnit] = field(
        default_factory=list,
        metadata={
            "name": "businessUnit",
            "type": "Element",
        },
    )
    enterprise_ref: list[EnterpriseRef] = field(
        default_factory=list,
        metadata={
            "name": "enterpriseRef",
            "type": "Element",
        },
    )
    refs: None | Refs = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class FunctionalItemRefElemType:
    class Meta:
        name = "functionalItemRefElemType"

    name: None | Name = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    short_name: None | ShortName = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
        },
    )
    refs: None | Refs = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    functional_item_number: str = field(
        metadata={
            "name": "functionalItemNumber",
            "type": "Attribute",
        }
    )
    functional_item_type: None | FunctionalItemTypeAttType = field(
        default=None,
        metadata={
            "name": "functionalItemType",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    installation_ident: None | str = field(
        default=None,
        metadata={
            "name": "installationIdent",
            "type": "Attribute",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    context_ident: None | str = field(
        default=None,
        metadata={
            "name": "contextIdent",
            "type": "Attribute",
        },
    )
    manufacturer_code_value: None | str = field(
        default=None,
        metadata={
            "name": "manufacturerCodeValue",
            "type": "Attribute",
        },
    )
    item_originator: None | ItemOriginatorAttType = field(
        default=None,
        metadata={
            "name": "itemOriginator",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class FunctionalPhysicalAreaRepositoryElemType:
    class Meta:
        name = "functionalPhysicalAreaRepositoryElemType"

    functional_physical_area_spec: list[FunctionalPhysicalAreaSpec] = field(
        default_factory=list,
        metadata={
            "name": "functionalPhysicalAreaSpec",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class NatoStockNumberElemType:
    class Meta:
        name = "natoStockNumberElemType"

    nato_supply_class: None | int = field(
        default=None,
        metadata={
            "name": "natoSupplyClass",
            "type": "Attribute",
        },
    )
    nato_codification_bureau: None | int = field(
        default=None,
        metadata={
            "name": "natoCodificationBureau",
            "type": "Attribute",
        },
    )
    nato_item_ident_number_core: None | int = field(
        default=None,
        metadata={
            "name": "natoItemIdentNumberCore",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "fullNatoStockNumber",
                    "type": FullNatoStockNumber,
                },
                {
                    "name": "refs",
                    "type": Refs,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class PartRefElemType:
    class Meta:
        name = "partRefElemType"

    refs: None | Refs = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    part_number_value: str = field(
        metadata={
            "name": "partNumberValue",
            "type": "Attribute",
        }
    )
    manufacturer_code_value: str = field(
        metadata={
            "name": "manufacturerCodeValue",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class SpecDocumentElemType:
    class Meta:
        name = "specDocumentElemType"

    refs: None | Refs = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    manufacturer_code_value: None | str = field(
        default=None,
        metadata={
            "name": "manufacturerCodeValue",
            "type": "Attribute",
        },
    )
    country_iso_code: None | str = field(
        default=None,
        metadata={
            "name": "countryIsoCode",
            "type": "Attribute",
            "pattern": r"[A-Z]{2}",
        },
    )
    spec_document_number: None | str = field(
        default=None,
        metadata={
            "name": "specDocumentNumber",
            "type": "Attribute",
        },
    )
    spec_document_type: None | str = field(
        default=None,
        metadata={
            "name": "specDocumentType",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class SupplyRefElemType:
    class Meta:
        name = "supplyRefElemType"

    name: None | Name = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    short_name: None | ShortName = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
        },
    )
    refs: None | Refs = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    supply_number: str = field(
        metadata={
            "name": "supplyNumber",
            "type": "Attribute",
        }
    )
    supply_number_type: SupplyNumberTypeAttType = field(
        metadata={
            "name": "supplyNumberType",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class SupplyRqmtRefElemType:
    class Meta:
        name = "supplyRqmtRefElemType"

    refs: None | Refs = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    material_category: None | str = field(
        default=None,
        metadata={
            "name": "materialCategory",
            "type": "Attribute",
        },
    )
    vendor_flag: None | str = field(
        default=None,
        metadata={
            "name": "vendorFlag",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    supply_rqmt_number: str = field(
        metadata={
            "name": "supplyRqmtNumber",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ToolElemType:
    class Meta:
        name = "toolElemType"

    item_descr: ItemDescr = field(
        metadata={
            "name": "itemDescr",
            "type": "Element",
        }
    )
    functional_physical_area_ref: None | FunctionalPhysicalAreaRef = field(
        default=None,
        metadata={
            "name": "functionalPhysicalAreaRef",
            "type": "Element",
        },
    )
    rcmd_quantity: None | RcmdQuantity = field(
        default=None,
        metadata={
            "name": "rcmdQuantity",
            "type": "Element",
        },
    )
    packaging: None | Packaging = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    task_category: None | TaskCategory = field(
        default=None,
        metadata={
            "name": "taskCategory",
            "type": "Element",
        },
    )
    simple_remark: None | SimpleRemark = field(
        default=None,
        metadata={
            "name": "simpleRemark",
            "type": "Element",
        },
    )
    internal_ref: None | InternalRef = field(
        default=None,
        metadata={
            "name": "internalRef",
            "type": "Element",
        },
    )
    refs: list[Refs] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    alt_number: None | str = field(
        default=None,
        metadata={
            "name": "altNumber",
            "type": "Attribute",
        },
    )
    delivered_specification_flag: None | str = field(
        default=None,
        metadata={
            "name": "deliveredSpecificationFlag",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ToolRefElemType:
    class Meta:
        name = "toolRefElemType"

    refs: None | Refs = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    tool_number: str = field(
        metadata={
            "name": "toolNumber",
            "type": "Attribute",
        }
    )
    manufacturer_code_value: None | str = field(
        default=None,
        metadata={
            "name": "manufacturerCodeValue",
            "type": "Attribute",
        },
    )
    specific: str = field(
        default="1",
        metadata={
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    tool_alt_flag: str = field(
        default="0",
        metadata={
            "name": "toolAltFlag",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ZoneRefElemType:
    class Meta:
        name = "zoneRefElemType"

    name: None | Name = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    short_name: None | ShortName = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
        },
    )
    refs: None | Refs = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    zone_number: None | str = field(
        default=None,
        metadata={
            "name": "zoneNumber",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lsar_data: str = field(
        default="0",
        metadata={
            "name": "lsarData",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class AccessPointRef(AccessPointRefElemType):
    class Meta:
        name = "accessPointRef"


@dataclass(kw_only=True)
class ApplicSpec(ApplicSpecElemType):
    class Meta:
        name = "applicSpec"


@dataclass(kw_only=True)
class CatalogSeqNumberRef(CatalogSeqNumberRefElemType):
    class Meta:
        name = "catalogSeqNumberRef"


@dataclass(kw_only=True)
class CircuitBreakerRef(CircuitBreakerRefElemType):
    class Meta:
        name = "circuitBreakerRef"


@dataclass(kw_only=True)
class ControlIndicatorRef(ControlIndicatorRefElemType):
    class Meta:
        name = "controlIndicatorRef"


@dataclass(kw_only=True)
class EnterpriseSpec(EnterpriseSpecElemType):
    class Meta:
        name = "enterpriseSpec"


@dataclass(kw_only=True)
class FunctionalItemRef(FunctionalItemRefElemType):
    class Meta:
        name = "functionalItemRef"


@dataclass(kw_only=True)
class FunctionalPhysicalAreaRepository(
    FunctionalPhysicalAreaRepositoryElemType
):
    class Meta:
        name = "functionalPhysicalAreaRepository"


@dataclass(kw_only=True)
class NatoStockNumber(NatoStockNumberElemType):
    class Meta:
        name = "natoStockNumber"


@dataclass(kw_only=True)
class PartRef(PartRefElemType):
    class Meta:
        name = "partRef"


@dataclass(kw_only=True)
class SpecDocument(SpecDocumentElemType):
    class Meta:
        name = "specDocument"


@dataclass(kw_only=True)
class SupplyRef(SupplyRefElemType):
    class Meta:
        name = "supplyRef"


@dataclass(kw_only=True)
class SupplyRqmtRef(SupplyRqmtRefElemType):
    class Meta:
        name = "supplyRqmtRef"


@dataclass(kw_only=True)
class Tool(ToolElemType):
    class Meta:
        name = "tool"


@dataclass(kw_only=True)
class ToolRef(ToolRefElemType):
    class Meta:
        name = "toolRef"


@dataclass(kw_only=True)
class ZoneRef(ZoneRefElemType):
    class Meta:
        name = "zoneRef"


@dataclass(kw_only=True)
class AccessFromElemType:
    class Meta:
        name = "accessFromElemType"

    zone_ref: list[ZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "zoneRef",
            "type": "Element",
        },
    )
    access_point_ref: list[AccessPointRef] = field(
        default_factory=list,
        metadata={
            "name": "accessPointRef",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class AccessPointRefGroupElemType:
    class Meta:
        name = "accessPointRefGroupElemType"

    access_point_ref: list[AccessPointRef] = field(
        default_factory=list,
        metadata={
            "name": "accessPointRef",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    access_point_ref_type: str = field(
        metadata={
            "name": "accessPointRefType",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class AccessToElemType:
    class Meta:
        name = "accessToElemType"

    functional_item_ref: list[FunctionalItemRef] = field(
        default_factory=list,
        metadata={
            "name": "functionalItemRef",
            "type": "Element",
        },
    )
    other_items: None | OtherItems = field(
        default=None,
        metadata={
            "name": "otherItems",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class AlteredFromPartElemType:
    class Meta:
        name = "alteredFromPartElemType"

    part_ref: list[PartRef] = field(
        default_factory=list,
        metadata={
            "name": "partRef",
            "type": "Element",
        },
    )
    catalog_seq_number_ref: list[CatalogSeqNumberRef] = field(
        default_factory=list,
        metadata={
            "name": "catalogSeqNumberRef",
            "type": "Element",
        },
    )
    altered_from_part_descr: None | AlteredFromPartDescr = field(
        default=None,
        metadata={
            "name": "alteredFromPartDescr",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ApplicRepositoryElemType:
    class Meta:
        name = "applicRepositoryElemType"

    applic_spec: list[ApplicSpec] = field(
        default_factory=list,
        metadata={
            "name": "applicSpec",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ChangeInlineElemType:
    class Meta:
        name = "changeInlineElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "functionalItemRef",
                    "type": FunctionalItemRef,
                },
                {
                    "name": "circuitBreakerRef",
                    "type": CircuitBreakerRef,
                },
                {
                    "name": "controlIndicatorRef",
                    "type": ControlIndicatorRef,
                },
                {
                    "name": "inlineSignificantData",
                    "type": InlineSignificantData,
                },
                {
                    "name": "quantity",
                    "type": Quantity,
                },
                {
                    "name": "internalRef",
                    "type": InternalRef,
                },
                {
                    "name": "changeInline",
                    "type": ForwardRef("ChangeInline"),
                },
                {
                    "name": "emphasis",
                    "type": ForwardRef("Emphasis"),
                },
                {
                    "name": "symbol",
                    "type": Symbol,
                },
                {
                    "name": "subScript",
                    "type": SubScript,
                },
                {
                    "name": "superScript",
                    "type": SuperScript,
                },
                {
                    "name": "dmRef",
                    "type": DmRef,
                },
                {
                    "name": "pmRef",
                    "type": PmRef,
                },
                {
                    "name": "externalPubRef",
                    "type": ExternalPubRef,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
                {
                    "name": "acronymTerm",
                    "type": AcronymTerm,
                },
                {
                    "name": "verbatimText",
                    "type": VerbatimText,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class CircuitBreakerRefGroupElemType:
    class Meta:
        name = "circuitBreakerRefGroupElemType"

    circuit_breaker_ref: list[CircuitBreakerRef] = field(
        default_factory=list,
        metadata={
            "name": "circuitBreakerRef",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    circuit_breaker_ref_type: CircuitBreakerRefTypeAttType = field(
        metadata={
            "name": "circuitBreakerRefType",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class EnterpriseRepositoryElemType:
    class Meta:
        name = "enterpriseRepositoryElemType"

    enterprise_spec: list[EnterpriseSpec] = field(
        default_factory=list,
        metadata={
            "name": "enterpriseSpec",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class FunctionalItemRefGroupElemType:
    class Meta:
        name = "functionalItemRefGroupElemType"

    functional_item_ref: list[FunctionalItemRef] = field(
        default_factory=list,
        metadata={
            "name": "functionalItemRef",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    functional_item_ref_type: FunctionalItemRefTypeAttType = field(
        metadata={
            "name": "functionalItemRefType",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class HotspotElemType:
    class Meta:
        name = "hotspotElemType"

    hotspot: list[Hotspot] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    internal_ref: list[InternalRef] = field(
        default_factory=list,
        metadata={
            "name": "internalRef",
            "type": "Element",
        },
    )
    dm_ref: list[DmRef] = field(
        default_factory=list,
        metadata={
            "name": "dmRef",
            "type": "Element",
        },
    )
    catalog_seq_number_ref: list[CatalogSeqNumberRef] = field(
        default_factory=list,
        metadata={
            "name": "catalogSeqNumberRef",
            "type": "Element",
        },
    )
    application_structure_ident: None | str = field(
        default=None,
        metadata={
            "name": "applicationStructureIdent",
            "type": "Attribute",
        },
    )
    application_structure_name: None | str = field(
        default=None,
        metadata={
            "name": "applicationStructureName",
            "type": "Attribute",
        },
    )
    hotspot_type: None | str = field(
        default=None,
        metadata={
            "name": "hotspotType",
            "type": "Attribute",
        },
    )
    hotspot_title: None | str = field(
        default=None,
        metadata={
            "name": "hotspotTitle",
            "type": "Attribute",
        },
    )
    object_descr: None | str = field(
        default=None,
        metadata={
            "name": "objectDescr",
            "type": "Attribute",
        },
    )
    object_coordinates: None | str = field(
        default=None,
        metadata={
            "name": "objectCoordinates",
            "type": "Attribute",
        },
    )
    visibility: VisibilityAttType = field(
        default=VisibilityAttType.VISIBLE,
        metadata={
            "type": "Attribute",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ItemIdentDataElemType:
    class Meta:
        name = "itemIdentDataElemType"

    descr_for_part: DescrForPart = field(
        metadata={
            "name": "descrForPart",
            "type": "Element",
        }
    )
    part_keyword: None | PartKeyword = field(
        default=None,
        metadata={
            "name": "partKeyword",
            "type": "Element",
        },
    )
    short_name: None | ShortName = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
        },
    )
    over_length_part_number: None | OverLengthPartNumber = field(
        default=None,
        metadata={
            "name": "overLengthPartNumber",
            "type": "Element",
        },
    )
    limited_part_number: None | LimitedPartNumber = field(
        default=None,
        metadata={
            "name": "limitedPartNumber",
            "type": "Element",
        },
    )
    customer_stock_number: list[CustomerStockNumber] = field(
        default_factory=list,
        metadata={
            "name": "customerStockNumber",
            "type": "Element",
        },
    )
    nato_stock_number: None | NatoStockNumber = field(
        default=None,
        metadata={
            "name": "natoStockNumber",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class LocalFabricationMaterialElemType:
    class Meta:
        name = "localFabricationMaterialElemType"

    part_ref: list[PartRef] = field(
        default_factory=list,
        metadata={
            "name": "partRef",
            "type": "Element",
        },
    )
    catalog_seq_number_ref: list[CatalogSeqNumberRef] = field(
        default_factory=list,
        metadata={
            "name": "catalogSeqNumberRef",
            "type": "Element",
        },
    )
    quantity: None | Quantity = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class LocationElemType:
    class Meta:
        name = "locationElemType"

    zone_ref: list[ZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "zoneRef",
            "type": "Element",
        },
    )
    access_point_ref: list[AccessPointRef] = field(
        default_factory=list,
        metadata={
            "name": "accessPointRef",
            "type": "Element",
            "sequence": 1,
        },
    )
    quantity: list[Quantity] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 1,
        },
    )
    installation_location: list[InstallationLocation] = field(
        default_factory=list,
        metadata={
            "name": "installationLocation",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class OptionalPartElemType:
    class Meta:
        name = "optionalPartElemType"

    part_ref: list[PartRef] = field(
        default_factory=list,
        metadata={
            "name": "partRef",
            "type": "Element",
        },
    )
    catalog_seq_number_ref: list[CatalogSeqNumberRef] = field(
        default_factory=list,
        metadata={
            "name": "catalogSeqNumberRef",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class PreferredSparePartElemType:
    class Meta:
        name = "preferredSparePartElemType"

    part_ref: list[PartRef] = field(
        default_factory=list,
        metadata={
            "name": "partRef",
            "type": "Element",
        },
    )
    catalog_seq_number_ref: list[CatalogSeqNumberRef] = field(
        default_factory=list,
        metadata={
            "name": "catalogSeqNumberRef",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ReplacedByElemType:
    class Meta:
        name = "replacedByElemType"

    part_ref: None | PartRef = field(
        default=None,
        metadata={
            "name": "partRef",
            "type": "Element",
        },
    )
    catalog_seq_number_ref: None | CatalogSeqNumberRef = field(
        default=None,
        metadata={
            "name": "catalogSeqNumberRef",
            "type": "Element",
        },
    )
    functional_item_ref: list[FunctionalItemRef] = field(
        default_factory=list,
        metadata={
            "name": "functionalItemRef",
            "type": "Element",
        },
    )
    replacement_cond: None | ReplacementCond = field(
        default=None,
        metadata={
            "name": "replacementCond",
            "type": "Element",
        },
    )
    replacement_code: str = field(
        metadata={
            "name": "replacementCode",
            "type": "Attribute",
        }
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class SpecGroupElemType:
    class Meta:
        name = "specGroupElemType"

    spec_document: list[SpecDocument] = field(
        default_factory=list,
        metadata={
            "name": "specDocument",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    vendor_flag: None | str = field(
        default=None,
        metadata={
            "name": "vendorFlag",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class SupplyRqmtAltStatusElemType:
    class Meta:
        name = "supplyRqmtAltStatusElemType"

    authorization_status: AuthorizationStatus = field(
        metadata={
            "name": "authorizationStatus",
            "type": "Element",
        }
    )
    supply_rqmt_ref: list[SupplyRqmtRef] = field(
        default_factory=list,
        metadata={
            "name": "supplyRqmtRef",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class SupplyRqmtStatusElemType:
    class Meta:
        name = "supplyRqmtStatusElemType"

    supply_rqmt_ref: list[SupplyRqmtRef] = field(
        default_factory=list,
        metadata={
            "name": "supplyRqmtRef",
            "type": "Element",
        },
    )
    supply_rqmt_status_value: None | str = field(
        default=None,
        metadata={
            "name": "supplyRqmtStatusValue",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class SupplySetElemType:
    class Meta:
        name = "supplySetElemType"

    supply_ref: list[SupplyRef] = field(
        default_factory=list,
        metadata={
            "name": "supplyRef",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ToolAltsElemType:
    class Meta:
        name = "toolAltsElemType"

    tool: list[Tool] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ToolRefGroupElemType:
    class Meta:
        name = "toolRefGroupElemType"

    tool_ref: list[ToolRef] = field(
        default_factory=list,
        metadata={
            "name": "toolRef",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    tool_ref_type: str = field(
        metadata={
            "name": "toolRefType",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ZoneRefGroupElemType:
    class Meta:
        name = "zoneRefGroupElemType"

    zone_ref: list[ZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "zoneRef",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    zone_ref_type: str = field(
        metadata={
            "name": "zoneRefType",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class AccessFrom(AccessFromElemType):
    class Meta:
        name = "accessFrom"


@dataclass(kw_only=True)
class AccessPointRefGroup(AccessPointRefGroupElemType):
    class Meta:
        name = "accessPointRefGroup"


@dataclass(kw_only=True)
class AccessTo(AccessToElemType):
    class Meta:
        name = "accessTo"


@dataclass(kw_only=True)
class AlteredFromPart(AlteredFromPartElemType):
    class Meta:
        name = "alteredFromPart"


@dataclass(kw_only=True)
class ApplicRepository(ApplicRepositoryElemType):
    class Meta:
        name = "applicRepository"


@dataclass(kw_only=True)
class ChangeInline(ChangeInlineElemType):
    class Meta:
        name = "changeInline"


@dataclass(kw_only=True)
class CircuitBreakerRefGroup(CircuitBreakerRefGroupElemType):
    class Meta:
        name = "circuitBreakerRefGroup"


@dataclass(kw_only=True)
class EnterpriseRepository(EnterpriseRepositoryElemType):
    class Meta:
        name = "enterpriseRepository"


@dataclass(kw_only=True)
class FunctionalItemRefGroup(FunctionalItemRefGroupElemType):
    class Meta:
        name = "functionalItemRefGroup"


@dataclass(kw_only=True)
class Hotspot(HotspotElemType):
    class Meta:
        name = "hotspot"


@dataclass(kw_only=True)
class ItemIdentData(ItemIdentDataElemType):
    class Meta:
        name = "itemIdentData"


@dataclass(kw_only=True)
class LocalFabricationMaterial(LocalFabricationMaterialElemType):
    class Meta:
        name = "localFabricationMaterial"


@dataclass(kw_only=True)
class Location(LocationElemType):
    class Meta:
        name = "location"


@dataclass(kw_only=True)
class OptionalPart(OptionalPartElemType):
    class Meta:
        name = "optionalPart"


@dataclass(kw_only=True)
class PreferredSparePart(PreferredSparePartElemType):
    class Meta:
        name = "preferredSparePart"


@dataclass(kw_only=True)
class ReplacedBy(ReplacedByElemType):
    class Meta:
        name = "replacedBy"


@dataclass(kw_only=True)
class SpecGroup(SpecGroupElemType):
    class Meta:
        name = "specGroup"


@dataclass(kw_only=True)
class SupplyRqmtAltStatus(SupplyRqmtAltStatusElemType):
    class Meta:
        name = "supplyRqmtAltStatus"


@dataclass(kw_only=True)
class SupplyRqmtStatus(SupplyRqmtStatusElemType):
    class Meta:
        name = "supplyRqmtStatus"


@dataclass(kw_only=True)
class SupplySet(SupplySetElemType):
    class Meta:
        name = "supplySet"


@dataclass(kw_only=True)
class ToolAlts(ToolAltsElemType):
    class Meta:
        name = "toolAlts"


@dataclass(kw_only=True)
class ToolRefGroup(ToolRefGroupElemType):
    class Meta:
        name = "toolRefGroup"


@dataclass(kw_only=True)
class ZoneRefGroup(ZoneRefGroupElemType):
    class Meta:
        name = "zoneRefGroup"


@dataclass(kw_only=True)
class AccessPointElemType:
    class Meta:
        name = "accessPointElemType"

    name: None | Name = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    short_name: None | ShortName = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
        },
    )
    access_point_type: AccessPointType = field(
        metadata={
            "name": "accessPointType",
            "type": "Element",
        }
    )
    zone_ref: ZoneRef = field(
        metadata={
            "name": "zoneRef",
            "type": "Element",
        }
    )
    access_to: None | AccessTo = field(
        default=None,
        metadata={
            "name": "accessTo",
            "type": "Element",
        },
    )
    access_point_ref_group: list[AccessPointRefGroup] = field(
        default_factory=list,
        metadata={
            "name": "accessPointRefGroup",
            "type": "Element",
        },
    )
    fastener: list[Fastener] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    quantity: list[Quantity] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    hours_to_close: None | HoursToClose = field(
        default=None,
        metadata={
            "name": "hoursToClose",
            "type": "Element",
        },
    )
    hours_to_open: None | HoursToOpen = field(
        default=None,
        metadata={
            "name": "hoursToOpen",
            "type": "Element",
        },
    )
    internal_ref: list[InternalRef] = field(
        default_factory=list,
        metadata={
            "name": "internalRef",
            "type": "Element",
        },
    )
    alt_number: None | str = field(
        default=None,
        metadata={
            "name": "altNumber",
            "type": "Attribute",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class CircuitBreakerElemType:
    class Meta:
        name = "circuitBreakerElemType"

    name: None | Name = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    short_name: None | ShortName = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
        },
    )
    circuit_breaker_class: CircuitBreakerClass = field(
        metadata={
            "name": "circuitBreakerClass",
            "type": "Element",
        }
    )
    location: None | Location = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    functional_physical_area_ref: None | FunctionalPhysicalAreaRef = field(
        default=None,
        metadata={
            "name": "functionalPhysicalAreaRef",
            "type": "Element",
        },
    )
    functional_item_ref_group: list[FunctionalItemRefGroup] = field(
        default_factory=list,
        metadata={
            "name": "functionalItemRefGroup",
            "type": "Element",
        },
    )
    circuit_breaker_ref_group: list[CircuitBreakerRefGroup] = field(
        default_factory=list,
        metadata={
            "name": "circuitBreakerRefGroup",
            "type": "Element",
        },
    )
    amperage: None | Amperage = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    alt_number: None | str = field(
        default=None,
        metadata={
            "name": "altNumber",
            "type": "Attribute",
        },
    )
    monitored_flag: None | str = field(
        default=None,
        metadata={
            "name": "monitoredFlag",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    collared_circuit_breaker_flag: None | str = field(
        default=None,
        metadata={
            "name": "collaredCircuitBreakerFlag",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    provisioned_flag: None | str = field(
        default=None,
        metadata={
            "name": "provisionedFlag",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class EmphasisElemType:
    class Meta:
        name = "emphasisElemType"

    emphasis_type: EmphasisTypeAttType = field(
        default=EmphasisTypeAttType.EM01,
        metadata={
            "name": "emphasisType",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "functionalItemRef",
                    "type": FunctionalItemRef,
                },
                {
                    "name": "circuitBreakerRef",
                    "type": CircuitBreakerRef,
                },
                {
                    "name": "controlIndicatorRef",
                    "type": ControlIndicatorRef,
                },
                {
                    "name": "inlineSignificantData",
                    "type": InlineSignificantData,
                },
                {
                    "name": "quantity",
                    "type": Quantity,
                },
                {
                    "name": "internalRef",
                    "type": InternalRef,
                },
                {
                    "name": "changeInline",
                    "type": ChangeInline,
                },
                {
                    "name": "emphasis",
                    "type": ForwardRef("Emphasis"),
                },
                {
                    "name": "symbol",
                    "type": Symbol,
                },
                {
                    "name": "subScript",
                    "type": SubScript,
                },
                {
                    "name": "superScript",
                    "type": SuperScript,
                },
                {
                    "name": "dmRef",
                    "type": DmRef,
                },
                {
                    "name": "pmRef",
                    "type": PmRef,
                },
                {
                    "name": "externalPubRef",
                    "type": ExternalPubRef,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
                {
                    "name": "acronymTerm",
                    "type": AcronymTerm,
                },
                {
                    "name": "verbatimText",
                    "type": VerbatimText,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class FunctionalItemElemType:
    class Meta:
        name = "functionalItemElemType"

    name: None | Name = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    short_name: None | ShortName = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
        },
    )
    location: None | Location = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    access_from: None | AccessFrom = field(
        default=None,
        metadata={
            "name": "accessFrom",
            "type": "Element",
        },
    )
    functional_physical_area_ref: None | FunctionalPhysicalAreaRef = field(
        default=None,
        metadata={
            "name": "functionalPhysicalAreaRef",
            "type": "Element",
        },
    )
    req_quantity: None | ReqQuantity = field(
        default=None,
        metadata={
            "name": "reqQuantity",
            "type": "Element",
        },
    )
    functional_item_family: None | FunctionalItemFamily = field(
        default=None,
        metadata={
            "name": "functionalItemFamily",
            "type": "Element",
        },
    )
    grounding_type: None | GroundingType = field(
        default=None,
        metadata={
            "name": "groundingType",
            "type": "Element",
        },
    )
    functional_item_ref_group: list[FunctionalItemRefGroup] = field(
        default_factory=list,
        metadata={
            "name": "functionalItemRefGroup",
            "type": "Element",
        },
    )
    internal_ref: list[InternalRef] = field(
        default_factory=list,
        metadata={
            "name": "internalRef",
            "type": "Element",
        },
    )
    alt_number: None | str = field(
        default=None,
        metadata={
            "name": "altNumber",
            "type": "Attribute",
        },
    )
    normative_component_flag: str = field(
        default="0",
        metadata={
            "name": "normativeComponentFlag",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    sealed_flag: str = field(
        default="0",
        metadata={
            "name": "sealedFlag",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class PartRefGroupElemType:
    class Meta:
        name = "partRefGroupElemType"

    replaced_by: list[ReplacedBy] = field(
        default_factory=list,
        metadata={
            "name": "replacedBy",
            "type": "Element",
        },
    )
    optional_part: list[OptionalPart] = field(
        default_factory=list,
        metadata={
            "name": "optionalPart",
            "type": "Element",
        },
    )
    preferred_spare_part: list[PreferredSparePart] = field(
        default_factory=list,
        metadata={
            "name": "preferredSparePart",
            "type": "Element",
        },
    )
    altered_from_part: list[AlteredFromPart] = field(
        default_factory=list,
        metadata={
            "name": "alteredFromPart",
            "type": "Element",
        },
    )
    local_fabrication_material: list[LocalFabricationMaterial] = field(
        default_factory=list,
        metadata={
            "name": "localFabricationMaterial",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class SupplySetGroupElemType:
    class Meta:
        name = "supplySetGroupElemType"

    supply_set: list[SupplySet] = field(
        default_factory=list,
        metadata={
            "name": "supplySet",
            "type": "Element",
        },
    )
    supply_ref: list[SupplyRef] = field(
        default_factory=list,
        metadata={
            "name": "supplyRef",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ZoneElemType:
    class Meta:
        name = "zoneElemType"

    item_descr: ItemDescr = field(
        metadata={
            "name": "itemDescr",
            "type": "Element",
        }
    )
    short_name: None | ShortName = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
        },
    )
    zone_side: None | ZoneSide = field(
        default=None,
        metadata={
            "name": "zoneSide",
            "type": "Element",
        },
    )
    boundary_from: None | BoundaryFrom = field(
        default=None,
        metadata={
            "name": "boundaryFrom",
            "type": "Element",
        },
    )
    boundary_to: None | BoundaryTo = field(
        default=None,
        metadata={
            "name": "boundaryTo",
            "type": "Element",
        },
    )
    zone_ref_group: list[ZoneRefGroup] = field(
        default_factory=list,
        metadata={
            "name": "zoneRefGroup",
            "type": "Element",
        },
    )
    internal_ref: list[InternalRef] = field(
        default_factory=list,
        metadata={
            "name": "internalRef",
            "type": "Element",
        },
    )
    alt_number: None | str = field(
        default=None,
        metadata={
            "name": "altNumber",
            "type": "Attribute",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class AccessPoint(AccessPointElemType):
    class Meta:
        name = "accessPoint"


@dataclass(kw_only=True)
class CircuitBreaker(CircuitBreakerElemType):
    class Meta:
        name = "circuitBreaker"


@dataclass(kw_only=True)
class Emphasis(EmphasisElemType):
    class Meta:
        name = "emphasis"


@dataclass(kw_only=True)
class FunctionalItem(FunctionalItemElemType):
    class Meta:
        name = "functionalItem"


@dataclass(kw_only=True)
class PartRefGroup(PartRefGroupElemType):
    class Meta:
        name = "partRefGroup"


@dataclass(kw_only=True)
class SupplySetGroup(SupplySetGroupElemType):
    class Meta:
        name = "supplySetGroup"


@dataclass(kw_only=True)
class Zone(ZoneElemType):
    class Meta:
        name = "zone"


@dataclass(kw_only=True)
class AccessPointAltsElemType:
    class Meta:
        name = "accessPointAltsElemType"

    access_point: list[AccessPoint] = field(
        default_factory=list,
        metadata={
            "name": "accessPoint",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class AttentionListItemParaElemType:
    class Meta:
        name = "attentionListItemParaElemType"

    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "functionalItemRef",
                    "type": FunctionalItemRef,
                },
                {
                    "name": "circuitBreakerRef",
                    "type": CircuitBreakerRef,
                },
                {
                    "name": "controlIndicatorRef",
                    "type": ControlIndicatorRef,
                },
                {
                    "name": "supplyRef",
                    "type": SupplyRef,
                },
                {
                    "name": "inlineSignificantData",
                    "type": InlineSignificantData,
                },
                {
                    "name": "quantity",
                    "type": Quantity,
                },
                {
                    "name": "internalRef",
                    "type": InternalRef,
                },
                {
                    "name": "changeInline",
                    "type": ChangeInline,
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                },
                {
                    "name": "symbol",
                    "type": Symbol,
                },
                {
                    "name": "subScript",
                    "type": SubScript,
                },
                {
                    "name": "superScript",
                    "type": SuperScript,
                },
                {
                    "name": "dmRef",
                    "type": DmRef,
                },
                {
                    "name": "pmRef",
                    "type": PmRef,
                },
                {
                    "name": "externalPubRef",
                    "type": ExternalPubRef,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
                {
                    "name": "acronymTerm",
                    "type": AcronymTerm,
                },
                {
                    "name": "verbatimText",
                    "type": VerbatimText,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class CircuitBreakerAltsElemType:
    class Meta:
        name = "circuitBreakerAltsElemType"

    circuit_breaker: list[CircuitBreaker] = field(
        default_factory=list,
        metadata={
            "name": "circuitBreaker",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class FunctionalItemAltsElemType:
    class Meta:
        name = "functionalItemAltsElemType"

    functional_item: list[FunctionalItem] = field(
        default_factory=list,
        metadata={
            "name": "functionalItem",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ListItemTermElemType:
    class Meta:
        name = "listItemTermElemType"

    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "functionalItemRef",
                    "type": FunctionalItemRef,
                },
                {
                    "name": "circuitBreakerRef",
                    "type": CircuitBreakerRef,
                },
                {
                    "name": "controlIndicatorRef",
                    "type": ControlIndicatorRef,
                },
                {
                    "name": "inlineSignificantData",
                    "type": InlineSignificantData,
                },
                {
                    "name": "quantity",
                    "type": Quantity,
                },
                {
                    "name": "internalRef",
                    "type": InternalRef,
                },
                {
                    "name": "changeInline",
                    "type": ChangeInline,
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                },
                {
                    "name": "symbol",
                    "type": Symbol,
                },
                {
                    "name": "subScript",
                    "type": SubScript,
                },
                {
                    "name": "superScript",
                    "type": SuperScript,
                },
                {
                    "name": "dmRef",
                    "type": DmRef,
                },
                {
                    "name": "pmRef",
                    "type": PmRef,
                },
                {
                    "name": "externalPubRef",
                    "type": ExternalPubRef,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
                {
                    "name": "acronymTerm",
                    "type": AcronymTerm,
                },
                {
                    "name": "verbatimText",
                    "type": VerbatimText,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class ParaElemType:
    class Meta:
        name = "paraElemType"

    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "functionalItemRef",
                    "type": FunctionalItemRef,
                },
                {
                    "name": "circuitBreakerRef",
                    "type": CircuitBreakerRef,
                },
                {
                    "name": "controlIndicatorRef",
                    "type": ControlIndicatorRef,
                },
                {
                    "name": "inlineSignificantData",
                    "type": InlineSignificantData,
                },
                {
                    "name": "quantity",
                    "type": Quantity,
                },
                {
                    "name": "internalRef",
                    "type": InternalRef,
                },
                {
                    "name": "changeInline",
                    "type": ChangeInline,
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                },
                {
                    "name": "symbol",
                    "type": Symbol,
                },
                {
                    "name": "subScript",
                    "type": SubScript,
                },
                {
                    "name": "superScript",
                    "type": SuperScript,
                },
                {
                    "name": "dmRef",
                    "type": DmRef,
                },
                {
                    "name": "pmRef",
                    "type": PmRef,
                },
                {
                    "name": "externalPubRef",
                    "type": ExternalPubRef,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
                {
                    "name": "acronymTerm",
                    "type": AcronymTerm,
                },
                {
                    "name": "verbatimText",
                    "type": VerbatimText,
                },
                {
                    "name": "sequentialList",
                    "type": ForwardRef("SequentialList"),
                },
                {
                    "name": "randomList",
                    "type": ForwardRef("RandomList"),
                },
                {
                    "name": "definitionList",
                    "type": ForwardRef("DefinitionList"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class ReasonForAmendmentElemType:
    class Meta:
        name = "reasonForAmendmentElemType"

    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "functionalItemRef",
                    "type": FunctionalItemRef,
                },
                {
                    "name": "circuitBreakerRef",
                    "type": CircuitBreakerRef,
                },
                {
                    "name": "controlIndicatorRef",
                    "type": ControlIndicatorRef,
                },
                {
                    "name": "inlineSignificantData",
                    "type": InlineSignificantData,
                },
                {
                    "name": "quantity",
                    "type": Quantity,
                },
                {
                    "name": "internalRef",
                    "type": InternalRef,
                },
                {
                    "name": "changeInline",
                    "type": ChangeInline,
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                },
                {
                    "name": "symbol",
                    "type": Symbol,
                },
                {
                    "name": "subScript",
                    "type": SubScript,
                },
                {
                    "name": "superScript",
                    "type": SuperScript,
                },
                {
                    "name": "dmRef",
                    "type": DmRef,
                },
                {
                    "name": "pmRef",
                    "type": PmRef,
                },
                {
                    "name": "externalPubRef",
                    "type": ExternalPubRef,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
                {
                    "name": "acronymTerm",
                    "type": AcronymTerm,
                },
                {
                    "name": "verbatimText",
                    "type": VerbatimText,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class SimpleRefParaElemType:
    class Meta:
        name = "simpleRefParaElemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "subScript",
                    "type": SubScript,
                },
                {
                    "name": "superScript",
                    "type": SuperScript,
                },
                {
                    "name": "verbatimText",
                    "type": VerbatimText,
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                },
                {
                    "name": "inlineSignificantData",
                    "type": InlineSignificantData,
                },
                {
                    "name": "dmRef",
                    "type": DmRef,
                },
                {
                    "name": "pmRef",
                    "type": PmRef,
                },
                {
                    "name": "externalPubRef",
                    "type": ExternalPubRef,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class SupplyRqmtElemType:
    class Meta:
        name = "supplyRqmtElemType"

    supply_rqmt_alt_ident: SupplyRqmtAltIdent = field(
        metadata={
            "name": "supplyRqmtAltIdent",
            "type": "Element",
        }
    )
    supply_set_group: SupplySetGroup = field(
        metadata={
            "name": "supplySetGroup",
            "type": "Element",
        }
    )
    supply_rqmt_alt_status: None | SupplyRqmtAltStatus = field(
        default=None,
        metadata={
            "name": "supplyRqmtAltStatus",
            "type": "Element",
        },
    )
    enterprise_ref: None | EnterpriseRef = field(
        default=None,
        metadata={
            "name": "enterpriseRef",
            "type": "Element",
        },
    )
    supply_classification: None | SupplyClassification = field(
        default=None,
        metadata={
            "name": "supplyClassification",
            "type": "Element",
        },
    )
    spec_group: list[SpecGroup] = field(
        default_factory=list,
        metadata={
            "name": "specGroup",
            "type": "Element",
        },
    )
    name: Name = field(
        metadata={
            "type": "Element",
        }
    )
    short_name: None | ShortName = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
        },
    )
    safety_category: None | SafetyCategory = field(
        default=None,
        metadata={
            "name": "safetyCategory",
            "type": "Element",
        },
    )
    usage: None | Usage = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    rcmd: None | Rcmd = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    refs: None | Refs = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    product_category: None | ProductCategoryAttType = field(
        default=None,
        metadata={
            "name": "productCategory",
            "type": "Attribute",
        },
    )
    supply_rqmt_type: None | str = field(
        default=None,
        metadata={
            "name": "supplyRqmtType",
            "type": "Attribute",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class TitleElemType:
    class Meta:
        name = "titleElemType"

    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "functionalItemRef",
                    "type": FunctionalItemRef,
                },
                {
                    "name": "circuitBreakerRef",
                    "type": CircuitBreakerRef,
                },
                {
                    "name": "controlIndicatorRef",
                    "type": ControlIndicatorRef,
                },
                {
                    "name": "inlineSignificantData",
                    "type": InlineSignificantData,
                },
                {
                    "name": "quantity",
                    "type": Quantity,
                },
                {
                    "name": "internalRef",
                    "type": InternalRef,
                },
                {
                    "name": "changeInline",
                    "type": ChangeInline,
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                },
                {
                    "name": "symbol",
                    "type": Symbol,
                },
                {
                    "name": "subScript",
                    "type": SubScript,
                },
                {
                    "name": "superScript",
                    "type": SuperScript,
                },
                {
                    "name": "dmRef",
                    "type": DmRef,
                },
                {
                    "name": "pmRef",
                    "type": PmRef,
                },
                {
                    "name": "externalPubRef",
                    "type": ExternalPubRef,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
                {
                    "name": "acronymTerm",
                    "type": AcronymTerm,
                },
                {
                    "name": "verbatimText",
                    "type": VerbatimText,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class ZoneAltsElemType:
    class Meta:
        name = "zoneAltsElemType"

    zone: list[Zone] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class AccessPointAlts(AccessPointAltsElemType):
    class Meta:
        name = "accessPointAlts"


@dataclass(kw_only=True)
class AttentionListItemPara(AttentionListItemParaElemType):
    class Meta:
        name = "attentionListItemPara"


@dataclass(kw_only=True)
class CircuitBreakerAlts(CircuitBreakerAltsElemType):
    class Meta:
        name = "circuitBreakerAlts"


@dataclass(kw_only=True)
class DefinitionTitle(TitleElemType):
    class Meta:
        name = "definitionTitle"


@dataclass(kw_only=True)
class FunctionalItemAlts(FunctionalItemAltsElemType):
    class Meta:
        name = "functionalItemAlts"


@dataclass(kw_only=True)
class ListItemTerm(ListItemTermElemType):
    class Meta:
        name = "listItemTerm"


@dataclass(kw_only=True)
class Para(ParaElemType):
    class Meta:
        name = "para"


@dataclass(kw_only=True)
class ReasonForAmendment(ReasonForAmendmentElemType):
    class Meta:
        name = "reasonForAmendment"


@dataclass(kw_only=True)
class SimpleRefPara(SimpleRefParaElemType):
    class Meta:
        name = "simpleRefPara"


@dataclass(kw_only=True)
class SupplyRqmt(SupplyRqmtElemType):
    class Meta:
        name = "supplyRqmt"


@dataclass(kw_only=True)
class TermTitle(TitleElemType):
    class Meta:
        name = "termTitle"


@dataclass(kw_only=True)
class Title(TitleElemType):
    class Meta:
        name = "title"


@dataclass(kw_only=True)
class ZoneAlts(ZoneAltsElemType):
    class Meta:
        name = "zoneAlts"


@dataclass(kw_only=True)
class AccessPointSpecElemType:
    class Meta:
        name = "accessPointSpecElemType"

    access_point_ident: AccessPointIdent = field(
        metadata={
            "name": "accessPointIdent",
            "type": "Element",
        }
    )
    access_point_ref_group: list[AccessPointRefGroup] = field(
        default_factory=list,
        metadata={
            "name": "accessPointRefGroup",
            "type": "Element",
        },
    )
    access_point_alts: AccessPointAlts = field(
        metadata={
            "name": "accessPointAlts",
            "type": "Element",
        }
    )
    refs: None | Refs = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class AttentionRandomListItemElemType:
    class Meta:
        name = "attentionRandomListItemElemType"

    attention_list_item_para: list[AttentionListItemPara] = field(
        default_factory=list,
        metadata={
            "name": "attentionListItemPara",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class CircuitBreakerSpecElemType:
    class Meta:
        name = "circuitBreakerSpecElemType"

    circuit_breaker_ident: CircuitBreakerIdent = field(
        metadata={
            "name": "circuitBreakerIdent",
            "type": "Element",
        }
    )
    name: Name = field(
        metadata={
            "type": "Element",
        }
    )
    short_name: None | ShortName = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
        },
    )
    functional_physical_area_ref: None | FunctionalPhysicalAreaRef = field(
        default=None,
        metadata={
            "name": "functionalPhysicalAreaRef",
            "type": "Element",
        },
    )
    circuit_breaker_ref_group: list[CircuitBreakerRefGroup] = field(
        default_factory=list,
        metadata={
            "name": "circuitBreakerRefGroup",
            "type": "Element",
        },
    )
    circuit_breaker_alts: CircuitBreakerAlts = field(
        metadata={
            "name": "circuitBreakerAlts",
            "type": "Element",
        }
    )
    refs: None | Refs = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ControlAuthorityTextElemType:
    class Meta:
        name = "controlAuthorityTextElemType"

    para: Para = field(
        metadata={
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class DefinitionListHeaderElemType:
    class Meta:
        name = "definitionListHeaderElemType"

    term_title: TermTitle = field(
        metadata={
            "name": "termTitle",
            "type": "Element",
        }
    )
    definition_title: DefinitionTitle = field(
        metadata={
            "name": "definitionTitle",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class FunctionalItemSpecElemType:
    class Meta:
        name = "functionalItemSpecElemType"

    functional_item_ident: FunctionalItemIdent = field(
        metadata={
            "name": "functionalItemIdent",
            "type": "Element",
        }
    )
    name: Name = field(
        metadata={
            "type": "Element",
        }
    )
    short_name: None | ShortName = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
        },
    )
    functional_physical_area_ref: None | FunctionalPhysicalAreaRef = field(
        default=None,
        metadata={
            "name": "functionalPhysicalAreaRef",
            "type": "Element",
        },
    )
    software_classification: None | SoftwareClassification = field(
        default=None,
        metadata={
            "name": "softwareClassification",
            "type": "Element",
        },
    )
    software_customization_status: None | SoftwareCustomizationStatus = field(
        default=None,
        metadata={
            "name": "softwareCustomizationStatus",
            "type": "Element",
        },
    )
    functional_item_ref_group: list[FunctionalItemRefGroup] = field(
        default_factory=list,
        metadata={
            "name": "functionalItemRefGroup",
            "type": "Element",
        },
    )
    functional_item_alts: FunctionalItemAlts = field(
        metadata={
            "name": "functionalItemAlts",
            "type": "Element",
        }
    )
    refs: None | Refs = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class GraphicElemType:
    class Meta:
        name = "graphicElemType"

    hotspot: list[Hotspot] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    reason_for_amendment: list[ReasonForAmendment] = field(
        default_factory=list,
        metadata={
            "name": "reasonForAmendment",
            "type": "Element",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    info_entity_ident: str = field(
        metadata={
            "name": "infoEntityIdent",
            "type": "Attribute",
        }
    )
    reproduction_width: None | str = field(
        default=None,
        metadata={
            "name": "reproductionWidth",
            "type": "Attribute",
            "pattern": r"\d+(\.\d+)?\s*(cm|in|mm|pc|pt)",
        },
    )
    reproduction_height: None | str = field(
        default=None,
        metadata={
            "name": "reproductionHeight",
            "type": "Attribute",
            "pattern": r"\d+(\.\d+)?\s*(cm|in|mm|pc|pt)",
        },
    )
    reproduction_scale: None | int = field(
        default=None,
        metadata={
            "name": "reproductionScale",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    type_value: TypeValue = field(
        init=False,
        default=TypeValue.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: None | ShowValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: None | ActuateValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ListItemDefinitionElemType:
    class Meta:
        name = "listItemDefinitionElemType"

    para: list[Para] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class MultimediaObjectElemType:
    class Meta:
        name = "multimediaObjectElemType"

    parameter: list[Parameter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    reason_for_amendment: list[ReasonForAmendment] = field(
        default_factory=list,
        metadata={
            "name": "reasonForAmendment",
            "type": "Element",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    auto_play: None | str = field(
        default=None,
        metadata={
            "name": "autoPlay",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    full_screen: None | str = field(
        default=None,
        metadata={
            "name": "fullScreen",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    info_entity_ident: str = field(
        metadata={
            "name": "infoEntityIdent",
            "type": "Attribute",
        }
    )
    multimedia_object_height: None | str = field(
        default=None,
        metadata={
            "name": "multimediaObjectHeight",
            "type": "Attribute",
        },
    )
    multimedia_object_width: None | str = field(
        default=None,
        metadata={
            "name": "multimediaObjectWidth",
            "type": "Attribute",
        },
    )
    multimedia_type: MultimediaTypeAttType = field(
        metadata={
            "name": "multimediaType",
            "type": "Attribute",
        }
    )
    run_time_duration: None | int = field(
        default=None,
        metadata={
            "name": "runTimeDuration",
            "type": "Attribute",
        },
    )
    show_plugin_controls: None | ShowPluginControlsAttType = field(
        default=None,
        metadata={
            "name": "showPluginControls",
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    type_value: TypeValue = field(
        init=False,
        default=TypeValue.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: None | ShowValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: None | ActuateValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ReasonForUpdateElemType:
    class Meta:
        name = "reasonForUpdateElemType"

    simple_para: list[SimplePara] = field(
        default_factory=list,
        metadata={
            "name": "simplePara",
            "type": "Element",
        },
    )
    simple_ref_para: list[SimpleRefPara] = field(
        default_factory=list,
        metadata={
            "name": "simpleRefPara",
            "type": "Element",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    update_reason_type: None | UpdateReasonTypeAttType = field(
        default=None,
        metadata={
            "name": "updateReasonType",
            "type": "Attribute",
        },
    )
    update_highlight: None | str = field(
        default=None,
        metadata={
            "name": "updateHighlight",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class SupplyRqmtAltsElemType:
    class Meta:
        name = "supplyRqmtAltsElemType"

    supply_rqmt: list[SupplyRqmt] = field(
        default_factory=list,
        metadata={
            "name": "supplyRqmt",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ZoneSpecElemType:
    class Meta:
        name = "zoneSpecElemType"

    zone_ident: ZoneIdent = field(
        metadata={
            "name": "zoneIdent",
            "type": "Element",
        }
    )
    zone_ref_group: list[ZoneRefGroup] = field(
        default_factory=list,
        metadata={
            "name": "zoneRefGroup",
            "type": "Element",
        },
    )
    zone_alts: ZoneAlts = field(
        metadata={
            "name": "zoneAlts",
            "type": "Element",
        }
    )
    refs: None | Refs = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    zone_type: None | str = field(
        default=None,
        metadata={
            "name": "zoneType",
            "type": "Attribute",
            "pattern": r"majorzone|subzone|specifzone",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class AccessPointSpec(AccessPointSpecElemType):
    class Meta:
        name = "accessPointSpec"


@dataclass(kw_only=True)
class AttentionRandomListItem(AttentionRandomListItemElemType):
    class Meta:
        name = "attentionRandomListItem"


@dataclass(kw_only=True)
class CircuitBreakerSpec(CircuitBreakerSpecElemType):
    class Meta:
        name = "circuitBreakerSpec"


@dataclass(kw_only=True)
class ControlAuthorityText(ControlAuthorityTextElemType):
    class Meta:
        name = "controlAuthorityText"


@dataclass(kw_only=True)
class DefinitionListHeader(DefinitionListHeaderElemType):
    class Meta:
        name = "definitionListHeader"


@dataclass(kw_only=True)
class FunctionalItemSpec(FunctionalItemSpecElemType):
    class Meta:
        name = "functionalItemSpec"


@dataclass(kw_only=True)
class Graphic(GraphicElemType):
    class Meta:
        name = "graphic"


@dataclass(kw_only=True)
class ListItemDefinition(ListItemDefinitionElemType):
    class Meta:
        name = "listItemDefinition"


@dataclass(kw_only=True)
class MultimediaObject(MultimediaObjectElemType):
    class Meta:
        name = "multimediaObject"


@dataclass(kw_only=True)
class ReasonForUpdate(ReasonForUpdateElemType):
    class Meta:
        name = "reasonForUpdate"


@dataclass(kw_only=True)
class SupplyRqmtAlts(SupplyRqmtAltsElemType):
    class Meta:
        name = "supplyRqmtAlts"


@dataclass(kw_only=True)
class ZoneSpec(ZoneSpecElemType):
    class Meta:
        name = "zoneSpec"


@dataclass(kw_only=True)
class AccessPointRepositoryElemType:
    class Meta:
        name = "accessPointRepositoryElemType"

    access_point_spec: list[AccessPointSpec] = field(
        default_factory=list,
        metadata={
            "name": "accessPointSpec",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class AttentionRandomListElemType:
    class Meta:
        name = "attentionRandomListElemType"

    attention_random_list_item: list[AttentionRandomListItem] = field(
        default_factory=list,
        metadata={
            "name": "attentionRandomListItem",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    list_item_prefix: ListItemPrefixAttType = field(
        default=ListItemPrefixAttType.PF02,
        metadata={
            "name": "listItemPrefix",
            "type": "Attribute",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class CircuitBreakerRepositoryElemType:
    class Meta:
        name = "circuitBreakerRepositoryElemType"

    circuit_breaker_spec: list[CircuitBreakerSpec] = field(
        default_factory=list,
        metadata={
            "name": "circuitBreakerSpec",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ControlAuthorityElemType:
    class Meta:
        name = "controlAuthorityElemType"

    control_authority_text: None | ControlAuthorityText = field(
        default=None,
        metadata={
            "name": "controlAuthorityText",
            "type": "Element",
        },
    )
    dm_ref: None | DmRef = field(
        default=None,
        metadata={
            "name": "dmRef",
            "type": "Element",
        },
    )
    symbol: list[Symbol] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_type: ControlAuthorityTypeAttType = field(
        metadata={
            "name": "controlAuthorityType",
            "type": "Attribute",
        }
    )
    control_authority_source: None | str = field(
        default=None,
        metadata={
            "name": "controlAuthoritySource",
            "type": "Attribute",
        },
    )
    control_authority_value: None | str = field(
        default=None,
        metadata={
            "name": "controlAuthorityValue",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DefinitionListItemElemType:
    class Meta:
        name = "definitionListItemElemType"

    list_item_term: ListItemTerm = field(
        metadata={
            "name": "listItemTerm",
            "type": "Element",
        }
    )
    list_item_definition: ListItemDefinition = field(
        metadata={
            "name": "listItemDefinition",
            "type": "Element",
        }
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class FunctionalItemRepositoryElemType:
    class Meta:
        name = "functionalItemRepositoryElemType"

    functional_item_spec: list[FunctionalItemSpec] = field(
        default_factory=list,
        metadata={
            "name": "functionalItemSpec",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class MultimediaElemType:
    class Meta:
        name = "multimediaElemType"

    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    multimedia_object: list[MultimediaObject] = field(
        default_factory=list,
        metadata={
            "name": "multimediaObject",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class SupplyRqmtSpecElemType:
    class Meta:
        name = "supplyRqmtSpecElemType"

    supply_rqmt_ident: SupplyRqmtIdent = field(
        metadata={
            "name": "supplyRqmtIdent",
            "type": "Element",
        }
    )
    physical_chemical_descr: None | PhysicalChemicalDescr = field(
        default=None,
        metadata={
            "name": "physicalChemicalDescr",
            "type": "Element",
        },
    )
    usage: None | Usage = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    compliance_category: None | ComplianceCategory = field(
        default=None,
        metadata={
            "name": "complianceCategory",
            "type": "Element",
        },
    )
    process_category: list[ProcessCategory] = field(
        default_factory=list,
        metadata={
            "name": "processCategory",
            "type": "Element",
        },
    )
    supply_rqmt_status: None | SupplyRqmtStatus = field(
        default=None,
        metadata={
            "name": "supplyRqmtStatus",
            "type": "Element",
        },
    )
    spec_group: list[SpecGroup] = field(
        default_factory=list,
        metadata={
            "name": "specGroup",
            "type": "Element",
        },
    )
    supply_rqmt_alts: SupplyRqmtAlts = field(
        metadata={
            "name": "supplyRqmtAlts",
            "type": "Element",
        }
    )
    rcmd: None | Rcmd = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    refs: None | Refs = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    supply_category: None | SupplyCategoryAttType = field(
        default=None,
        metadata={
            "name": "supplyCategory",
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ZoneRepositoryElemType:
    class Meta:
        name = "zoneRepositoryElemType"

    zone_spec: list[ZoneSpec] = field(
        default_factory=list,
        metadata={
            "name": "zoneSpec",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class AccessPointRepository(AccessPointRepositoryElemType):
    class Meta:
        name = "accessPointRepository"


@dataclass(kw_only=True)
class AttentionRandomList(AttentionRandomListElemType):
    class Meta:
        name = "attentionRandomList"


@dataclass(kw_only=True)
class CircuitBreakerRepository(CircuitBreakerRepositoryElemType):
    class Meta:
        name = "circuitBreakerRepository"


@dataclass(kw_only=True)
class ControlAuthority(ControlAuthorityElemType):
    class Meta:
        name = "controlAuthority"


@dataclass(kw_only=True)
class DefinitionListItem(DefinitionListItemElemType):
    class Meta:
        name = "definitionListItem"


@dataclass(kw_only=True)
class FunctionalItemRepository(FunctionalItemRepositoryElemType):
    class Meta:
        name = "functionalItemRepository"


@dataclass(kw_only=True)
class Multimedia(MultimediaElemType):
    class Meta:
        name = "multimedia"


@dataclass(kw_only=True)
class SupplyRqmtSpec(SupplyRqmtSpecElemType):
    class Meta:
        name = "supplyRqmtSpec"


@dataclass(kw_only=True)
class ZoneRepository(ZoneRepositoryElemType):
    class Meta:
        name = "zoneRepository"


@dataclass(kw_only=True)
class AttentionSequentialListItemElemType:
    class Meta:
        name = "attentionSequentialListItemElemType"

    attention_list_item_para: list[AttentionListItemPara] = field(
        default_factory=list,
        metadata={
            "name": "attentionListItemPara",
            "type": "Element",
        },
    )
    attention_random_list: list[AttentionRandomList] = field(
        default_factory=list,
        metadata={
            "name": "attentionRandomList",
            "type": "Element",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ControlAuthorityGroupElemType:
    class Meta:
        name = "controlAuthorityGroupElemType"

    control_authority: list[ControlAuthority] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthority",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DefinitionListElemType:
    class Meta:
        name = "definitionListElemType"

    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    definition_list_header: None | DefinitionListHeader = field(
        default=None,
        metadata={
            "name": "definitionListHeader",
            "type": "Element",
        },
    )
    definition_list_item: list[DefinitionListItem] = field(
        default_factory=list,
        metadata={
            "name": "definitionListItem",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class MultimediaAltsElemType:
    class Meta:
        name = "multimediaAltsElemType"

    multimedia: list[Multimedia] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class SafetyInformationElemType:
    class Meta:
        name = "safetyInformationElemType"

    supplemental_safety_category: SupplementalSafetyCategoryAttType = field(
        default=SupplementalSafetyCategoryAttType.SSC01,
        metadata={
            "name": "supplementalSafetyCategory",
            "type": "Attribute",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "functionalItemRef",
                    "type": FunctionalItemRef,
                },
                {
                    "name": "circuitBreakerRef",
                    "type": CircuitBreakerRef,
                },
                {
                    "name": "controlIndicatorRef",
                    "type": ControlIndicatorRef,
                },
                {
                    "name": "supplyRef",
                    "type": SupplyRef,
                },
                {
                    "name": "inlineSignificantData",
                    "type": InlineSignificantData,
                },
                {
                    "name": "quantity",
                    "type": Quantity,
                },
                {
                    "name": "internalRef",
                    "type": InternalRef,
                },
                {
                    "name": "changeInline",
                    "type": ChangeInline,
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                },
                {
                    "name": "symbol",
                    "type": Symbol,
                },
                {
                    "name": "subScript",
                    "type": SubScript,
                },
                {
                    "name": "superScript",
                    "type": SuperScript,
                },
                {
                    "name": "dmRef",
                    "type": DmRef,
                },
                {
                    "name": "pmRef",
                    "type": PmRef,
                },
                {
                    "name": "externalPubRef",
                    "type": ExternalPubRef,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
                {
                    "name": "acronymTerm",
                    "type": AcronymTerm,
                },
                {
                    "name": "verbatimText",
                    "type": VerbatimText,
                },
                {
                    "name": "attentionRandomList",
                    "type": AttentionRandomList,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class SupplyRqmtRepositoryElemType:
    class Meta:
        name = "supplyRqmtRepositoryElemType"

    supply_rqmt_spec: list[SupplyRqmtSpec] = field(
        default_factory=list,
        metadata={
            "name": "supplyRqmtSpec",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class WarningAndCautionParaElemType:
    class Meta:
        name = "warningAndCautionParaElemType"

    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "functionalItemRef",
                    "type": FunctionalItemRef,
                },
                {
                    "name": "circuitBreakerRef",
                    "type": CircuitBreakerRef,
                },
                {
                    "name": "controlIndicatorRef",
                    "type": ControlIndicatorRef,
                },
                {
                    "name": "supplyRef",
                    "type": SupplyRef,
                },
                {
                    "name": "inlineSignificantData",
                    "type": InlineSignificantData,
                },
                {
                    "name": "quantity",
                    "type": Quantity,
                },
                {
                    "name": "internalRef",
                    "type": InternalRef,
                },
                {
                    "name": "changeInline",
                    "type": ChangeInline,
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                },
                {
                    "name": "symbol",
                    "type": Symbol,
                },
                {
                    "name": "subScript",
                    "type": SubScript,
                },
                {
                    "name": "superScript",
                    "type": SuperScript,
                },
                {
                    "name": "dmRef",
                    "type": DmRef,
                },
                {
                    "name": "pmRef",
                    "type": PmRef,
                },
                {
                    "name": "externalPubRef",
                    "type": ExternalPubRef,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
                {
                    "name": "acronymTerm",
                    "type": AcronymTerm,
                },
                {
                    "name": "verbatimText",
                    "type": VerbatimText,
                },
                {
                    "name": "attentionRandomList",
                    "type": AttentionRandomList,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class AttentionSequentialListItem(AttentionSequentialListItemElemType):
    class Meta:
        name = "attentionSequentialListItem"


@dataclass(kw_only=True)
class ControlAuthorityGroup(ControlAuthorityGroupElemType):
    class Meta:
        name = "controlAuthorityGroup"


@dataclass(kw_only=True)
class DefinitionList(DefinitionListElemType):
    class Meta:
        name = "definitionList"


@dataclass(kw_only=True)
class MultimediaAlts(MultimediaAltsElemType):
    class Meta:
        name = "multimediaAlts"


@dataclass(kw_only=True)
class SafetyInformation(SafetyInformationElemType):
    class Meta:
        name = "safetyInformation"


@dataclass(kw_only=True)
class SupplyRqmtRepository(SupplyRqmtRepositoryElemType):
    class Meta:
        name = "supplyRqmtRepository"


@dataclass(kw_only=True)
class WarningAndCautionPara(WarningAndCautionParaElemType):
    class Meta:
        name = "warningAndCautionPara"


@dataclass(kw_only=True)
class AttentionSequentialListElemType:
    class Meta:
        name = "attentionSequentialListElemType"

    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    attention_sequential_list_item: list[AttentionSequentialListItem] = field(
        default_factory=list,
        metadata={
            "name": "attentionSequentialListItem",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class CautionElemType:
    class Meta:
        name = "cautionElemType"

    symbol: list[Symbol] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    warning_and_caution_para: list[WarningAndCautionPara] = field(
        default_factory=list,
        metadata={
            "name": "warningAndCautionPara",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    caution_type: None | str = field(
        default=None,
        metadata={
            "name": "cautionType",
            "type": "Attribute",
        },
    )
    internal_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "internalRefId",
            "type": "Attribute",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class CautionSpecElemType:
    class Meta:
        name = "cautionSpecElemType"

    caution_ident: CautionIdent = field(
        metadata={
            "name": "cautionIdent",
            "type": "Element",
        }
    )
    symbol: list[Symbol] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    warning_and_caution_para: list[WarningAndCautionPara] = field(
        default_factory=list,
        metadata={
            "name": "warningAndCautionPara",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class HazardElemType:
    class Meta:
        name = "hazardElemType"

    symbol: list[Symbol] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    hazardous_class: list[HazardousClass] = field(
        default_factory=list,
        metadata={
            "name": "hazardousClass",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    safety_information: list[SafetyInformation] = field(
        default_factory=list,
        metadata={
            "name": "safetyInformation",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class HazardSpecElemType:
    class Meta:
        name = "hazardSpecElemType"

    hazard_ident: HazardIdent = field(
        metadata={
            "name": "hazardIdent",
            "type": "Element",
        }
    )
    symbol: list[Symbol] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    hazardous_class: list[HazardousClass] = field(
        default_factory=list,
        metadata={
            "name": "hazardousClass",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    safety_information: list[SafetyInformation] = field(
        default_factory=list,
        metadata={
            "name": "safetyInformation",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class LegendElemType:
    class Meta:
        name = "legendElemType"

    definition_list: DefinitionList = field(
        metadata={
            "name": "definitionList",
            "type": "Element",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class WarningElemType:
    class Meta:
        name = "warningElemType"

    symbol: list[Symbol] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    warning_and_caution_para: list[WarningAndCautionPara] = field(
        default_factory=list,
        metadata={
            "name": "warningAndCautionPara",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    warning_type: None | str = field(
        default=None,
        metadata={
            "name": "warningType",
            "type": "Attribute",
        },
    )
    internal_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "internalRefId",
            "type": "Attribute",
        },
    )
    vital_warning_flag: None | str = field(
        default=None,
        metadata={
            "name": "vitalWarningFlag",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class WarningSpecElemType:
    class Meta:
        name = "warningSpecElemType"

    warning_ident: WarningIdent = field(
        metadata={
            "name": "warningIdent",
            "type": "Element",
        }
    )
    symbol: list[Symbol] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    warning_and_caution_para: list[WarningAndCautionPara] = field(
        default_factory=list,
        metadata={
            "name": "warningAndCautionPara",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class AttentionSequentialList(AttentionSequentialListElemType):
    class Meta:
        name = "attentionSequentialList"


@dataclass(kw_only=True)
class Caution(CautionElemType):
    class Meta:
        name = "caution"


@dataclass(kw_only=True)
class CautionSpec(CautionSpecElemType):
    class Meta:
        name = "cautionSpec"


@dataclass(kw_only=True)
class Hazard(HazardElemType):
    class Meta:
        name = "hazard"


@dataclass(kw_only=True)
class HazardSpec(HazardSpecElemType):
    class Meta:
        name = "hazardSpec"


@dataclass(kw_only=True)
class Legend(LegendElemType):
    class Meta:
        name = "legend"


@dataclass(kw_only=True)
class Warning(WarningElemType):
    class Meta:
        name = "warning"


@dataclass(kw_only=True)
class WarningSpec(WarningSpecElemType):
    class Meta:
        name = "warningSpec"


@dataclass(kw_only=True)
class CautionRepositoryElemType:
    class Meta:
        name = "cautionRepositoryElemType"

    caution_spec: list[CautionSpec] = field(
        default_factory=list,
        metadata={
            "name": "cautionSpec",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class FigureElemType:
    class Meta:
        name = "figureElemType"

    title: Title = field(
        metadata={
            "type": "Element",
        }
    )
    graphic: list[Graphic] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    legend: None | Legend = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class HazardRepositoryElemType:
    class Meta:
        name = "hazardRepositoryElemType"

    hazard_spec: list[HazardSpec] = field(
        default_factory=list,
        metadata={
            "name": "hazardSpec",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class HazardsElemType:
    class Meta:
        name = "hazardsElemType"

    hazard_ref: list[HazardRef] = field(
        default_factory=list,
        metadata={
            "name": "hazardRef",
            "type": "Element",
        },
    )
    hazard: list[Hazard] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class NoteParaElemType:
    class Meta:
        name = "noteParaElemType"

    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "functionalItemRef",
                    "type": FunctionalItemRef,
                },
                {
                    "name": "circuitBreakerRef",
                    "type": CircuitBreakerRef,
                },
                {
                    "name": "controlIndicatorRef",
                    "type": ControlIndicatorRef,
                },
                {
                    "name": "supplyRef",
                    "type": SupplyRef,
                },
                {
                    "name": "inlineSignificantData",
                    "type": InlineSignificantData,
                },
                {
                    "name": "quantity",
                    "type": Quantity,
                },
                {
                    "name": "internalRef",
                    "type": InternalRef,
                },
                {
                    "name": "changeInline",
                    "type": ChangeInline,
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                },
                {
                    "name": "symbol",
                    "type": Symbol,
                },
                {
                    "name": "subScript",
                    "type": SubScript,
                },
                {
                    "name": "superScript",
                    "type": SuperScript,
                },
                {
                    "name": "dmRef",
                    "type": DmRef,
                },
                {
                    "name": "pmRef",
                    "type": PmRef,
                },
                {
                    "name": "externalPubRef",
                    "type": ExternalPubRef,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
                {
                    "name": "acronymTerm",
                    "type": AcronymTerm,
                },
                {
                    "name": "verbatimText",
                    "type": VerbatimText,
                },
                {
                    "name": "attentionSequentialList",
                    "type": AttentionSequentialList,
                },
                {
                    "name": "attentionRandomList",
                    "type": AttentionRandomList,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class WarningRepositoryElemType:
    class Meta:
        name = "warningRepositoryElemType"

    warning_spec: list[WarningSpec] = field(
        default_factory=list,
        metadata={
            "name": "warningSpec",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class CautionRepository(CautionRepositoryElemType):
    class Meta:
        name = "cautionRepository"


@dataclass(kw_only=True)
class Figure(FigureElemType):
    class Meta:
        name = "figure"


@dataclass(kw_only=True)
class HazardRepository(HazardRepositoryElemType):
    class Meta:
        name = "hazardRepository"


@dataclass(kw_only=True)
class Hazards(HazardsElemType):
    class Meta:
        name = "hazards"


@dataclass(kw_only=True)
class NotePara(NoteParaElemType):
    class Meta:
        name = "notePara"


@dataclass(kw_only=True)
class WarningRepository(WarningRepositoryElemType):
    class Meta:
        name = "warningRepository"


@dataclass(kw_only=True)
class FigureAltsElemType:
    class Meta:
        name = "figureAltsElemType"

    figure: list[Figure] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class NoteElemType:
    class Meta:
        name = "noteElemType"

    symbol: list[Symbol] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    note_para: list[NotePara] = field(
        default_factory=list,
        metadata={
            "name": "notePara",
            "type": "Element",
        },
    )
    attention_sequential_list: list[AttentionSequentialList] = field(
        default_factory=list,
        metadata={
            "name": "attentionSequentialList",
            "type": "Element",
        },
    )
    attention_random_list: list[AttentionRandomList] = field(
        default_factory=list,
        metadata={
            "name": "attentionRandomList",
            "type": "Element",
        },
    )
    note_type: None | str = field(
        default=None,
        metadata={
            "name": "noteType",
            "type": "Attribute",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    internal_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "internalRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class SupplySpecElemType:
    class Meta:
        name = "supplySpecElemType"

    supply_ident: SupplyIdent = field(
        metadata={
            "name": "supplyIdent",
            "type": "Element",
        }
    )
    supply_set_group: None | SupplySetGroup = field(
        default=None,
        metadata={
            "name": "supplySetGroup",
            "type": "Element",
        },
    )
    supply_classification: None | SupplyClassification = field(
        default=None,
        metadata={
            "name": "supplyClassification",
            "type": "Element",
        },
    )
    name: None | Name = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    short_name: None | ShortName = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
        },
    )
    spec_group: list[SpecGroup] = field(
        default_factory=list,
        metadata={
            "name": "specGroup",
            "type": "Element",
        },
    )
    enterprise_group: None | EnterpriseGroup = field(
        default=None,
        metadata={
            "name": "enterpriseGroup",
            "type": "Element",
        },
    )
    nato_stock_number: None | NatoStockNumber = field(
        default=None,
        metadata={
            "name": "natoStockNumber",
            "type": "Element",
        },
    )
    quantity: list[Quantity] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    rcmd: None | Rcmd = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    refs: list[Refs] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    lowest_authorized_level_group: None | LowestAuthorizedLevelGroup = field(
        default=None,
        metadata={
            "name": "lowestAuthorizedLevelGroup",
            "type": "Element",
        },
    )
    hazards: None | Hazards = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    manufactured_flag: str = field(
        default="1",
        metadata={
            "name": "manufacturedFlag",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    obsolete_flag: None | str = field(
        default=None,
        metadata={
            "name": "obsoleteFlag",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    special_label_flag: None | str = field(
        default=None,
        metadata={
            "name": "specialLabelFlag",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    supply_category: None | SupplyCategoryAttType = field(
        default=None,
        metadata={
            "name": "supplyCategory",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class TechDataElemType:
    class Meta:
        name = "techDataElemType"

    spare_part_class: None | SparePartClass = field(
        default=None,
        metadata={
            "name": "sparePartClass",
            "type": "Element",
        },
    )
    part_usage: None | PartUsage = field(
        default=None,
        metadata={
            "name": "partUsage",
            "type": "Element",
        },
    )
    spec_document: list[SpecDocument] = field(
        default_factory=list,
        metadata={
            "name": "specDocument",
            "type": "Element",
        },
    )
    quantity: list[Quantity] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    physical_security_pilferage_code: None | PhysicalSecurityPilferageCode = (
        field(
            default=None,
            metadata={
                "name": "physicalSecurityPilferageCode",
                "type": "Element",
            },
        )
    )
    fitment_code: None | FitmentCode = field(
        default=None,
        metadata={
            "name": "fitmentCode",
            "type": "Element",
        },
    )
    unit_of_issue: None | UnitOfIssue = field(
        default=None,
        metadata={
            "name": "unitOfIssue",
            "type": "Element",
        },
    )
    unit_of_issue_qualification_segment: (
        None | UnitOfIssueQualificationSegment
    ) = field(
        default=None,
        metadata={
            "name": "unitOfIssueQualificationSegment",
            "type": "Element",
        },
    )
    special_storage: None | SpecialStorage = field(
        default=None,
        metadata={
            "name": "specialStorage",
            "type": "Element",
        },
    )
    calibration_marker: None | CalibrationMarker = field(
        default=None,
        metadata={
            "name": "calibrationMarker",
            "type": "Element",
        },
    )
    placard_text: None | PlacardText = field(
        default=None,
        metadata={
            "name": "placardText",
            "type": "Element",
        },
    )
    hazardous_class: None | HazardousClass = field(
        default=None,
        metadata={
            "name": "hazardousClass",
            "type": "Element",
        },
    )
    hazards: None | Hazards = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    etops_flag: None | str = field(
        default=None,
        metadata={
            "name": "etopsFlag",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class FigureAlts(FigureAltsElemType):
    class Meta:
        name = "figureAlts"


@dataclass(kw_only=True)
class Note(NoteElemType):
    class Meta:
        name = "note"


@dataclass(kw_only=True)
class SupplySpec(SupplySpecElemType):
    class Meta:
        name = "supplySpec"


@dataclass(kw_only=True)
class TechData(TechDataElemType):
    class Meta:
        name = "techData"


@dataclass(kw_only=True)
class ControlIndicatorDescrElemType:
    class Meta:
        name = "controlIndicatorDescrElemType"

    note: None | Note = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    control_indicator_function: list[ControlIndicatorFunction] = field(
        default_factory=list,
        metadata={
            "name": "controlIndicatorFunction",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class EntryElemType:
    class Meta:
        name = "entryElemType"

    para: list[Para] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    warning: list[Warning] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    caution: list[Caution] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    note: list[Note] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    legend: list[Legend] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    colname: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    namest: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    nameend: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    spanname: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    morerows: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        },
    )
    colsep: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    rowsep: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    rotate: str = field(
        default="0",
        metadata={
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    valign: None | ValignAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    align: None | AlignAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charoff: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    warning_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "warningRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    caution_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "cautionRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ListItemElemType:
    class Meta:
        name = "listItemElemType"

    note: list[Note] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    para: list[Para] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class PartSpecElemType:
    class Meta:
        name = "partSpecElemType"

    part_ident: PartIdent = field(
        metadata={
            "name": "partIdent",
            "type": "Element",
        }
    )
    item_ident_data: ItemIdentData = field(
        metadata={
            "name": "itemIdentData",
            "type": "Element",
        }
    )
    procurement_data: None | ProcurementData = field(
        default=None,
        metadata={
            "name": "procurementData",
            "type": "Element",
        },
    )
    tech_data: None | TechData = field(
        default=None,
        metadata={
            "name": "techData",
            "type": "Element",
        },
    )
    part_ref_group: None | PartRefGroup = field(
        default=None,
        metadata={
            "name": "partRefGroup",
            "type": "Element",
        },
    )
    refs: None | Refs = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    part_number_unavailable_flag: str = field(
        default="0",
        metadata={
            "name": "partNumberUnavailableFlag",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class SupplyRepositoryElemType:
    class Meta:
        name = "supplyRepositoryElemType"

    supply_spec: list[SupplySpec] = field(
        default_factory=list,
        metadata={
            "name": "supplySpec",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ToolSpecElemType:
    class Meta:
        name = "toolSpecElemType"

    tool_ident: ToolIdent = field(
        metadata={
            "name": "toolIdent",
            "type": "Element",
        }
    )
    item_ident_data: ItemIdentData = field(
        metadata={
            "name": "itemIdentData",
            "type": "Element",
        }
    )
    procurement_data: ProcurementData = field(
        metadata={
            "name": "procurementData",
            "type": "Element",
        }
    )
    tech_data: TechData = field(
        metadata={
            "name": "techData",
            "type": "Element",
        }
    )
    tool_ref_group: list[ToolRefGroup] = field(
        default_factory=list,
        metadata={
            "name": "toolRefGroup",
            "type": "Element",
        },
    )
    tool_alts: None | ToolAlts = field(
        default=None,
        metadata={
            "name": "toolAlts",
            "type": "Element",
        },
    )
    refs: list[Refs] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ControlIndicatorDescr(ControlIndicatorDescrElemType):
    class Meta:
        name = "controlIndicatorDescr"


@dataclass(kw_only=True)
class Entry(EntryElemType):
    class Meta:
        name = "entry"


@dataclass(kw_only=True)
class ListItem(ListItemElemType):
    class Meta:
        name = "listItem"


@dataclass(kw_only=True)
class PartSpec(PartSpecElemType):
    class Meta:
        name = "partSpec"


@dataclass(kw_only=True)
class SupplyRepository(SupplyRepositoryElemType):
    class Meta:
        name = "supplyRepository"


@dataclass(kw_only=True)
class ToolSpec(ToolSpecElemType):
    class Meta:
        name = "toolSpec"


@dataclass(kw_only=True)
class ControlIndicatorSpecElemType:
    class Meta:
        name = "controlIndicatorSpecElemType"

    control_indicator_key: ControlIndicatorKey = field(
        metadata={
            "name": "controlIndicatorKey",
            "type": "Element",
        }
    )
    control_indicator_name: ControlIndicatorName = field(
        metadata={
            "name": "controlIndicatorName",
            "type": "Element",
        }
    )
    short_name: None | ShortName = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
        },
    )
    control_indicator_descr: ControlIndicatorDescr = field(
        metadata={
            "name": "controlIndicatorDescr",
            "type": "Element",
        }
    )
    control_indicator_number: str = field(
        metadata={
            "name": "controlIndicatorNumber",
            "type": "Attribute",
        }
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class PartRepositoryElemType:
    class Meta:
        name = "partRepositoryElemType"

    part_spec: list[PartSpec] = field(
        default_factory=list,
        metadata={
            "name": "partSpec",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class RandomListElemType:
    class Meta:
        name = "randomListElemType"

    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    list_item: list[ListItem] = field(
        default_factory=list,
        metadata={
            "name": "listItem",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    list_item_prefix: ListItemPrefixAttType = field(
        default=ListItemPrefixAttType.PF02,
        metadata={
            "name": "listItemPrefix",
            "type": "Attribute",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class RowElemType:
    class Meta:
        name = "rowElemType"

    entry: list[Entry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    rowsep: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class SequentialListElemType:
    class Meta:
        name = "sequentialListElemType"

    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    list_item: list[ListItem] = field(
        default_factory=list,
        metadata={
            "name": "listItem",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ToolRepositoryElemType:
    class Meta:
        name = "toolRepositoryElemType"

    tool_spec: list[ToolSpec] = field(
        default_factory=list,
        metadata={
            "name": "toolSpec",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ControlIndicatorSpec(ControlIndicatorSpecElemType):
    class Meta:
        name = "controlIndicatorSpec"


@dataclass(kw_only=True)
class PartRepository(PartRepositoryElemType):
    class Meta:
        name = "partRepository"


@dataclass(kw_only=True)
class RandomList(RandomListElemType):
    class Meta:
        name = "randomList"


@dataclass(kw_only=True)
class Row(RowElemType):
    class Meta:
        name = "row"


@dataclass(kw_only=True)
class SequentialList(SequentialListElemType):
    class Meta:
        name = "sequentialList"


@dataclass(kw_only=True)
class ToolRepository(ToolRepositoryElemType):
    class Meta:
        name = "toolRepository"


@dataclass(kw_only=True)
class ControlIndicatorGroupElemType:
    class Meta:
        name = "controlIndicatorGroupElemType"

    internal_ref: list[InternalRef] = field(
        default_factory=list,
        metadata={
            "name": "internalRef",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    control_indicator_spec: list[ControlIndicatorSpec] = field(
        default_factory=list,
        metadata={
            "name": "controlIndicatorSpec",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class CopyrightParaElemType:
    class Meta:
        name = "copyrightParaElemType"

    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "emphasis",
                    "type": Emphasis,
                },
                {
                    "name": "subScript",
                    "type": SubScript,
                },
                {
                    "name": "superScript",
                    "type": SuperScript,
                },
                {
                    "name": "dmRef",
                    "type": DmRef,
                },
                {
                    "name": "randomList",
                    "type": RandomList,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class TbodyElemType:
    class Meta:
        name = "tbodyElemType"

    row: list[Row] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    valign: ValignAttType = field(
        default=ValignAttType.TOP,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class TerminologyParaElemType:
    class Meta:
        name = "terminologyParaElemType"

    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "inlineSignificantData",
                    "type": InlineSignificantData,
                },
                {
                    "name": "changeInline",
                    "type": ChangeInline,
                },
                {
                    "name": "symbol",
                    "type": Symbol,
                },
                {
                    "name": "verbatimText",
                    "type": VerbatimText,
                },
                {
                    "name": "subScript",
                    "type": SubScript,
                },
                {
                    "name": "superScript",
                    "type": SuperScript,
                },
                {
                    "name": "dmRef",
                    "type": DmRef,
                },
                {
                    "name": "randomList",
                    "type": RandomList,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class TfootElemType:
    class Meta:
        name = "tfootElemType"

    colspec: list[Colspec] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    row: list[Row] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    valign: ValignAttType = field(
        default=ValignAttType.TOP,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class TheadElemType:
    class Meta:
        name = "theadElemType"

    colspec: list[Colspec] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    row: list[Row] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    valign: ValignAttType = field(
        default=ValignAttType.BOTTOM,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ControlIndicatorGroup(ControlIndicatorGroupElemType):
    class Meta:
        name = "controlIndicatorGroup"


@dataclass(kw_only=True)
class CopyrightPara(CopyrightParaElemType):
    class Meta:
        name = "copyrightPara"


@dataclass(kw_only=True)
class Tbody(TbodyElemType):
    class Meta:
        name = "tbody"


@dataclass(kw_only=True)
class TerminologyPara(TerminologyParaElemType):
    class Meta:
        name = "terminologyPara"


@dataclass(kw_only=True)
class Tfoot(TfootElemType):
    class Meta:
        name = "tfoot"


@dataclass(kw_only=True)
class Thead(TheadElemType):
    class Meta:
        name = "thead"


@dataclass(kw_only=True)
class ControlIndicatorRepositoryElemType:
    class Meta:
        name = "controlIndicatorRepositoryElemType"

    control_indicator_group: list[ControlIndicatorGroup] = field(
        default_factory=list,
        metadata={
            "name": "controlIndicatorGroup",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class CopyrightElemType:
    class Meta:
        name = "copyrightElemType"

    copyright_para: list[CopyrightPara] = field(
        default_factory=list,
        metadata={
            "name": "copyrightPara",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class TerminologyDefinitionElemType:
    class Meta:
        name = "terminologyDefinitionElemType"

    terminology_para: list[TerminologyPara] = field(
        default_factory=list,
        metadata={
            "name": "terminologyPara",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class TgroupElemType:
    class Meta:
        name = "tgroupElemType"

    colspec: list[Colspec] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    spanspec: list[Spanspec] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    thead: None | Thead = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    tfoot: None | Tfoot = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    tbody: Tbody = field(
        metadata={
            "type": "Element",
        }
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    cols: int = field(
        metadata={
            "type": "Attribute",
        }
    )
    tgstyle: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    colsep: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    rowsep: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    align: AlignAttType = field(
        default=AlignAttType.LEFT,
        metadata={
            "type": "Attribute",
        },
    )
    charoff: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ControlIndicatorRepository(ControlIndicatorRepositoryElemType):
    class Meta:
        name = "controlIndicatorRepository"


@dataclass(kw_only=True)
class Copyright(CopyrightElemType):
    class Meta:
        name = "copyright"


@dataclass(kw_only=True)
class TerminologyDefinition(TerminologyDefinitionElemType):
    class Meta:
        name = "terminologyDefinition"


@dataclass(kw_only=True)
class Tgroup(TgroupElemType):
    class Meta:
        name = "tgroup"


@dataclass(kw_only=True)
class RestrictionInfoElemType:
    class Meta:
        name = "restrictionInfoElemType"

    copyright: None | Copyright = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    policy_statement: None | PolicyStatement = field(
        default=None,
        metadata={
            "name": "policyStatement",
            "type": "Element",
        },
    )
    data_conds: None | DataConds = field(
        default=None,
        metadata={
            "name": "dataConds",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class TableElemType:
    class Meta:
        name = "tableElemType"

    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    tgroup: list[Tgroup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    graphic: list[Graphic] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    tabstyle: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    tocentry: str = field(
        default="1",
        metadata={
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    frame: None | FrameAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    colsep: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    rowsep: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    orient: None | OrientAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    pgwide: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class TerminologySpecElemType:
    class Meta:
        name = "terminologySpecElemType"

    terminology_ident: TerminologyIdent = field(
        metadata={
            "name": "terminologyIdent",
            "type": "Element",
        }
    )
    terminology_term: TerminologyTerm = field(
        metadata={
            "name": "terminologyTerm",
            "type": "Element",
        }
    )
    terminology_definition: TerminologyDefinition = field(
        metadata={
            "name": "terminologyDefinition",
            "type": "Element",
        }
    )
    refs: None | Refs = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    term_type: TermTypeAttType = field(
        metadata={
            "name": "termType",
            "type": "Attribute",
        }
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class RestrictionInfo(RestrictionInfoElemType):
    class Meta:
        name = "restrictionInfo"


@dataclass(kw_only=True)
class Table(TableElemType):
    class Meta:
        name = "table"


@dataclass(kw_only=True)
class TerminologySpec(TerminologySpecElemType):
    class Meta:
        name = "terminologySpec"


@dataclass(kw_only=True)
class DataRestrictionsElemType:
    class Meta:
        name = "dataRestrictionsElemType"

    restriction_instructions: RestrictionInstructions = field(
        metadata={
            "name": "restrictionInstructions",
            "type": "Element",
        }
    )
    restriction_info: None | RestrictionInfo = field(
        default=None,
        metadata={
            "name": "restrictionInfo",
            "type": "Element",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class FoldoutElemType:
    class Meta:
        name = "foldoutElemType"

    figure: list[Figure] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    figure_alts: list[FigureAlts] = field(
        default_factory=list,
        metadata={
            "name": "figureAlts",
            "type": "Element",
        },
    )
    table: None | Table = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class TerminologyRepositoryElemType:
    class Meta:
        name = "terminologyRepositoryElemType"

    terminology_spec: list[TerminologySpec] = field(
        default_factory=list,
        metadata={
            "name": "terminologySpec",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class DataRestrictions(DataRestrictionsElemType):
    class Meta:
        name = "dataRestrictions"


@dataclass(kw_only=True)
class Foldout(FoldoutElemType):
    class Meta:
        name = "foldout"


@dataclass(kw_only=True)
class TerminologyRepository(TerminologyRepositoryElemType):
    class Meta:
        name = "terminologyRepository"


@dataclass(kw_only=True)
class CommonInfoDescrParaElemType:
    class Meta:
        name = "commonInfoDescrParaElemType"

    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    note: list[Note] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    para: list[Para] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    figure: list[Figure] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    figure_alts: list[FigureAlts] = field(
        default_factory=list,
        metadata={
            "name": "figureAlts",
            "type": "Element",
        },
    )
    multimedia: list[Multimedia] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    multimedia_alts: list[MultimediaAlts] = field(
        default_factory=list,
        metadata={
            "name": "multimediaAlts",
            "type": "Element",
        },
    )
    foldout: list[Foldout] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    table: list[Table] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    common_info_descr_para: list[CommonInfoDescrPara] = field(
        default_factory=list,
        metadata={
            "name": "commonInfoDescrPara",
            "type": "Element",
        },
    )
    common_info_descr_para_alts: list[CommonInfoDescrParaAlts] = field(
        default_factory=list,
        metadata={
            "name": "commonInfoDescrParaAlts",
            "type": "Element",
        },
    )
    applic_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "applicRefId",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class DmStatusGenericElemType:
    class Meta:
        name = "dmStatusGenericElemType"

    source_dm_ident: None | SourceDmIdent = field(
        default=None,
        metadata={
            "name": "sourceDmIdent",
            "type": "Element",
        },
    )
    repository_source_dm_ident: list[RepositorySourceDmIdent] = field(
        default_factory=list,
        metadata={
            "name": "repositorySourceDmIdent",
            "type": "Element",
        },
    )
    security: Security = field(
        metadata={
            "type": "Element",
        }
    )
    derivative_classification: None | DerivativeClassification = field(
        default=None,
        metadata={
            "name": "derivativeClassification",
            "type": "Element",
        },
    )
    control_authority_group: None | ControlAuthorityGroup = field(
        default=None,
        metadata={
            "name": "controlAuthorityGroup",
            "type": "Element",
        },
    )
    data_restrictions: list[DataRestrictions] = field(
        default_factory=list,
        metadata={
            "name": "dataRestrictions",
            "type": "Element",
        },
    )
    logo: None | Logo = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    responsible_partner_company: ResponsiblePartnerCompany = field(
        metadata={
            "name": "responsiblePartnerCompany",
            "type": "Element",
        }
    )
    originator: Originator = field(
        metadata={
            "type": "Element",
        }
    )
    applic_cross_ref_table_ref: None | ApplicCrossRefTableRef = field(
        default=None,
        metadata={
            "name": "applicCrossRefTableRef",
            "type": "Element",
        },
    )
    applic: None | Applic = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    applic_ref: None | ApplicRef = field(
        default=None,
        metadata={
            "name": "applicRef",
            "type": "Element",
        },
    )
    tech_standard: None | TechStandard = field(
        default=None,
        metadata={
            "name": "techStandard",
            "type": "Element",
        },
    )
    brex_dm_ref: BrexDmRef = field(
        metadata={
            "name": "brexDmRef",
            "type": "Element",
        }
    )
    quality_assurance: list[QualityAssurance] = field(
        default_factory=list,
        metadata={
            "name": "qualityAssurance",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    system_breakdown_code: list[SystemBreakdownCode] = field(
        default_factory=list,
        metadata={
            "name": "systemBreakdownCode",
            "type": "Element",
        },
    )
    functional_item_code: list[FunctionalItemCode] = field(
        default_factory=list,
        metadata={
            "name": "functionalItemCode",
            "type": "Element",
        },
    )
    functional_item_ref: list[FunctionalItemRef] = field(
        default_factory=list,
        metadata={
            "name": "functionalItemRef",
            "type": "Element",
        },
    )
    skill_level: None | SkillLevel = field(
        default=None,
        metadata={
            "name": "skillLevel",
            "type": "Element",
        },
    )
    reason_for_update: list[ReasonForUpdate] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdate",
            "type": "Element",
        },
    )
    product_safety: None | ProductSafety = field(
        default=None,
        metadata={
            "name": "productSafety",
            "type": "Element",
        },
    )
    remarks: list[Remarks] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    issue_type: IssueTypeAttType = field(
        default=IssueTypeAttType.NEW,
        metadata={
            "name": "issueType",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class CommonInfoDescrPara(CommonInfoDescrParaElemType):
    class Meta:
        name = "commonInfoDescrPara"


@dataclass(kw_only=True)
class DmStatus(DmStatusGenericElemType):
    class Meta:
        name = "dmStatus"


@dataclass(kw_only=True)
class CommonInfoDescrParaAltsElemType:
    class Meta:
        name = "commonInfoDescrParaAltsElemType"

    common_info_descr_para: list[CommonInfoDescrPara] = field(
        default_factory=list,
        metadata={
            "name": "commonInfoDescrPara",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class IdentAndStatusSectionElemType:
    class Meta:
        name = "identAndStatusSectionElemType"

    dm_address: DmAddress = field(
        metadata={
            "name": "dmAddress",
            "type": "Element",
        }
    )
    dm_status: DmStatus = field(
        metadata={
            "name": "dmStatus",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class CommonInfoDescrParaAlts(CommonInfoDescrParaAltsElemType):
    class Meta:
        name = "commonInfoDescrParaAlts"


@dataclass(kw_only=True)
class IdentAndStatusSection(IdentAndStatusSectionElemType):
    class Meta:
        name = "identAndStatusSection"


@dataclass(kw_only=True)
class CommonInfoElemType:
    class Meta:
        name = "commonInfoElemType"

    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    figure: list[Figure] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    figure_alts: list[FigureAlts] = field(
        default_factory=list,
        metadata={
            "name": "figureAlts",
            "type": "Element",
        },
    )
    note: list[Note] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    para: list[Para] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    common_info_descr_para: list[CommonInfoDescrPara] = field(
        default_factory=list,
        metadata={
            "name": "commonInfoDescrPara",
            "type": "Element",
        },
    )
    common_info_descr_para_alts: list[CommonInfoDescrParaAlts] = field(
        default_factory=list,
        metadata={
            "name": "commonInfoDescrParaAlts",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class CommonInfo(CommonInfoElemType):
    class Meta:
        name = "commonInfo"


@dataclass(kw_only=True)
class CommonRepositoryElemType:
    class Meta:
        name = "commonRepositoryElemType"

    common_info: None | CommonInfo = field(
        default=None,
        metadata={
            "name": "commonInfo",
            "type": "Element",
        },
    )
    figure: list[Figure] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    figure_alts: list[FigureAlts] = field(
        default_factory=list,
        metadata={
            "name": "figureAlts",
            "type": "Element",
        },
    )
    multimedia: list[Multimedia] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    multimedia_alts: list[MultimediaAlts] = field(
        default_factory=list,
        metadata={
            "name": "multimediaAlts",
            "type": "Element",
        },
    )
    functional_item_repository: None | FunctionalItemRepository = field(
        default=None,
        metadata={
            "name": "functionalItemRepository",
            "type": "Element",
        },
    )
    circuit_breaker_repository: None | CircuitBreakerRepository = field(
        default=None,
        metadata={
            "name": "circuitBreakerRepository",
            "type": "Element",
        },
    )
    part_repository: None | PartRepository = field(
        default=None,
        metadata={
            "name": "partRepository",
            "type": "Element",
        },
    )
    zone_repository: None | ZoneRepository = field(
        default=None,
        metadata={
            "name": "zoneRepository",
            "type": "Element",
        },
    )
    access_point_repository: None | AccessPointRepository = field(
        default=None,
        metadata={
            "name": "accessPointRepository",
            "type": "Element",
        },
    )
    tool_repository: None | ToolRepository = field(
        default=None,
        metadata={
            "name": "toolRepository",
            "type": "Element",
        },
    )
    enterprise_repository: None | EnterpriseRepository = field(
        default=None,
        metadata={
            "name": "enterpriseRepository",
            "type": "Element",
        },
    )
    supply_repository: None | SupplyRepository = field(
        default=None,
        metadata={
            "name": "supplyRepository",
            "type": "Element",
        },
    )
    supply_rqmt_repository: None | SupplyRqmtRepository = field(
        default=None,
        metadata={
            "name": "supplyRqmtRepository",
            "type": "Element",
        },
    )
    functional_physical_area_repository: (
        None | FunctionalPhysicalAreaRepository
    ) = field(
        default=None,
        metadata={
            "name": "functionalPhysicalAreaRepository",
            "type": "Element",
        },
    )
    control_indicator_repository: None | ControlIndicatorRepository = field(
        default=None,
        metadata={
            "name": "controlIndicatorRepository",
            "type": "Element",
        },
    )
    applic_repository: None | ApplicRepository = field(
        default=None,
        metadata={
            "name": "applicRepository",
            "type": "Element",
        },
    )
    warning_repository: None | WarningRepository = field(
        default=None,
        metadata={
            "name": "warningRepository",
            "type": "Element",
        },
    )
    caution_repository: None | CautionRepository = field(
        default=None,
        metadata={
            "name": "cautionRepository",
            "type": "Element",
        },
    )
    hazard_repository: None | HazardRepository = field(
        default=None,
        metadata={
            "name": "hazardRepository",
            "type": "Element",
        },
    )
    terminology_repository: None | TerminologyRepository = field(
        default=None,
        metadata={
            "name": "terminologyRepository",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    change_type: None | ChangeTypeAttType = field(
        default=None,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_mark: None | str = field(
        default=None,
        metadata={
            "name": "changeMark",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    reason_for_update_ref_ids: list[str] = field(
        default_factory=list,
        metadata={
            "name": "reasonForUpdateRefIds",
            "type": "Attribute",
            "tokens": True,
        },
    )
    security_classification: None | SecurityClassificationAttType = field(
        default=None,
        metadata={
            "name": "securityClassification",
            "type": "Attribute",
        },
    )
    commercial_classification: None | CommercialClassificationAttType = field(
        default=None,
        metadata={
            "name": "commercialClassification",
            "type": "Attribute",
        },
    )
    caveat: None | CaveatAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    derivative_classification_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "derivativeClassificationRefId",
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class CommonRepository(CommonRepositoryElemType):
    class Meta:
        name = "commonRepository"


@dataclass(kw_only=True)
class ContentElemType:
    class Meta:
        name = "contentElemType"

    refs: None | Refs = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    referenced_applic_group: None | ReferencedApplicGroup = field(
        default=None,
        metadata={
            "name": "referencedApplicGroup",
            "type": "Element",
        },
    )
    referenced_applic_group_ref: None | ReferencedApplicGroupRef = field(
        default=None,
        metadata={
            "name": "referencedApplicGroupRef",
            "type": "Element",
        },
    )
    common_repository: CommonRepository = field(
        metadata={
            "name": "commonRepository",
            "type": "Element",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class Content(ContentElemType):
    class Meta:
        name = "content"


@dataclass(kw_only=True)
class DmoduleElemType:
    class Meta:
        name = "dmoduleElemType"

    description: None | Description = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        },
    )
    ident_and_status_section: IdentAndStatusSection = field(
        metadata={
            "name": "identAndStatusSection",
            "type": "Element",
        }
    )
    content: Content = field(
        metadata={
            "type": "Element",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class Dmodule(DmoduleElemType):
    class Meta:
        name = "dmodule"
