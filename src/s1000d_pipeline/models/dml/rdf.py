from __future__ import annotations

from dataclasses import dataclass, field

from s1000d_pipeline.models.dml.dc import (
    Contributor,
    Creator,
    Date,
    Format,
    Identifier,
    Language,
    Publisher,
    Rights,
    Source,
    Subject,
    Title,
    Type,
)

__NAMESPACE__ = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"


@dataclass(kw_only=True)
class Description:
    class Meta:
        namespace = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"

    title: list[Title] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.purl.org/dc/elements/1.1/",
        },
    )
    creator: list[Creator] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.purl.org/dc/elements/1.1/",
        },
    )
    subject: list[Subject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.purl.org/dc/elements/1.1/",
        },
    )
    publisher: list[Publisher] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.purl.org/dc/elements/1.1/",
        },
    )
    contributor: list[Contributor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.purl.org/dc/elements/1.1/",
        },
    )
    source: list[Source] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.purl.org/dc/elements/1.1/",
        },
    )
    date: list[Date] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.purl.org/dc/elements/1.1/",
        },
    )
    type_value: list[Type] = field(
        default_factory=list,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.purl.org/dc/elements/1.1/",
        },
    )
    format: list[Format] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.purl.org/dc/elements/1.1/",
        },
    )
    identifier: list[Identifier] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.purl.org/dc/elements/1.1/",
        },
    )
    language: list[Language] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.purl.org/dc/elements/1.1/",
        },
    )
    rights: list[Rights] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.purl.org/dc/elements/1.1/",
        },
    )
