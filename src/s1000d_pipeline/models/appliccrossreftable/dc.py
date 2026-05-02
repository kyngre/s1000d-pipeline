from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.purl.org/dc/elements/1.1/"


@dataclass(kw_only=True)
class Contributor:
    class Meta:
        name = "contributor"
        namespace = "http://www.purl.org/dc/elements/1.1/"

    value: str = field(default="")


@dataclass(kw_only=True)
class Creator:
    class Meta:
        name = "creator"
        namespace = "http://www.purl.org/dc/elements/1.1/"

    value: str = field(default="")


@dataclass(kw_only=True)
class Date:
    class Meta:
        name = "date"
        namespace = "http://www.purl.org/dc/elements/1.1/"

    value: XmlDate = field()


@dataclass(kw_only=True)
class Format:
    class Meta:
        name = "format"
        namespace = "http://www.purl.org/dc/elements/1.1/"

    value: str = field(init=False, default="text/xml")


@dataclass(kw_only=True)
class Identifier:
    class Meta:
        name = "identifier"
        namespace = "http://www.purl.org/dc/elements/1.1/"

    value: str = field(default="")


@dataclass(kw_only=True)
class Language:
    class Meta:
        name = "language"
        namespace = "http://www.purl.org/dc/elements/1.1/"

    value: str = field(
        default="",
        metadata={
            "pattern": r"[a-z]{2,3}(-[A-Z]{2})?",
        },
    )


@dataclass(kw_only=True)
class Publisher:
    class Meta:
        name = "publisher"
        namespace = "http://www.purl.org/dc/elements/1.1/"

    value: str = field(default="")


@dataclass(kw_only=True)
class Rights:
    class Meta:
        name = "rights"
        namespace = "http://www.purl.org/dc/elements/1.1/"

    value: str = field(
        default="",
        metadata={
            "pattern": r"[0-9]{1,2}((_cc[0-9]{2})?(_cv[0-9]{2})?(_ai[0-9]{2}_[0-9]{4}_[0-1][0-9]_[0-3][0-9])*)?",
        },
    )


@dataclass(kw_only=True)
class Source:
    class Meta:
        name = "source"
        namespace = "http://www.purl.org/dc/elements/1.1/"

    value: str = field(default="")


@dataclass(kw_only=True)
class Subject:
    class Meta:
        name = "subject"
        namespace = "http://www.purl.org/dc/elements/1.1/"

    value: str = field(default="")


@dataclass(kw_only=True)
class Title:
    class Meta:
        name = "title"
        namespace = "http://www.purl.org/dc/elements/1.1/"

    value: str = field(default="")


@dataclass(kw_only=True)
class Type:
    class Meta:
        name = "type"
        namespace = "http://www.purl.org/dc/elements/1.1/"

    value: str = field(init=False, default="text")
