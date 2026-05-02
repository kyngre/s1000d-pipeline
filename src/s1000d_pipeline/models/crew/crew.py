from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import ForwardRef

from s1000d_pipeline.models.crew.rdf import Description
from s1000d_pipeline.models.crew.xlink import (
    ActuateValue,
    ShowValue,
    TypeValue,
)
from s1000d_pipeline.models.crew.xml import SpaceValue


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


class ActionResponsibilityAttType(Enum):
    ALL = "all"
    ANY = "any"


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


class AlignCaptionAttType(Enum):
    LEFT = "left"
    RIGHT = "right"
    CENTER = "center"


class AlignCaptionEntryAttType(Enum):
    LEFT = "left"
    RIGHT = "right"
    CENTER = "center"
    JUSTIFY = "justify"


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
class Building:
    class Meta:
        name = "building"

    value: str = field(default="")


@dataclass(kw_only=True)
class BusinessUnitName:
    class Meta:
        name = "businessUnitName"

    value: str = field(default="")


class CaptionTypeAttType(Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"


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


class ColorAttType(Enum):
    CO00 = "co00"
    CO01 = "co01"
    CO02 = "co02"
    CO03 = "co03"
    CO04 = "co04"
    CO05 = "co05"
    CO06 = "co06"
    CO07 = "co07"
    CO08 = "co08"
    CO09 = "co09"
    CO10 = "co10"
    CO11 = "co11"
    CO12 = "co12"
    CO13 = "co13"
    CO14 = "co14"
    CO15 = "co15"
    CO16 = "co16"
    CO17 = "co17"
    CO18 = "co18"
    CO19 = "co19"
    CO20 = "co20"
    CO21 = "co21"
    CO22 = "co22"
    CO23 = "co23"
    CO24 = "co24"
    CO25 = "co25"
    CO26 = "co26"
    CO27 = "co27"
    CO28 = "co28"
    CO29 = "co29"
    CO30 = "co30"
    CO31 = "co31"
    CO32 = "co32"
    CO33 = "co33"
    CO34 = "co34"
    CO35 = "co35"
    CO36 = "co36"
    CO37 = "co37"
    CO38 = "co38"
    CO39 = "co39"
    CO40 = "co40"
    CO41 = "co41"
    CO42 = "co42"
    CO43 = "co43"
    CO44 = "co44"
    CO45 = "co45"
    CO46 = "co46"
    CO47 = "co47"
    CO48 = "co48"
    CO49 = "co49"
    CO50 = "co50"
    CO51 = "co51"
    CO52 = "co52"
    CO53 = "co53"
    CO54 = "co54"
    CO55 = "co55"
    CO56 = "co56"
    CO57 = "co57"
    CO58 = "co58"
    CO59 = "co59"
    CO60 = "co60"
    CO61 = "co61"
    CO62 = "co62"
    CO63 = "co63"
    CO64 = "co64"
    CO65 = "co65"
    CO66 = "co66"
    CO67 = "co67"
    CO68 = "co68"
    CO69 = "co69"
    CO70 = "co70"
    CO71 = "co71"
    CO72 = "co72"
    CO73 = "co73"
    CO74 = "co74"
    CO75 = "co75"
    CO76 = "co76"
    CO77 = "co77"
    CO78 = "co78"
    CO79 = "co79"
    CO80 = "co80"
    CO81 = "co81"
    CO82 = "co82"
    CO83 = "co83"
    CO84 = "co84"
    CO85 = "co85"
    CO86 = "co86"
    CO87 = "co87"
    CO88 = "co88"
    CO89 = "co89"
    CO90 = "co90"
    CO91 = "co91"
    CO92 = "co92"
    CO93 = "co93"
    CO94 = "co94"
    CO95 = "co95"
    CO96 = "co96"
    CO97 = "co97"
    CO98 = "co98"
    CO99 = "co99"


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


class CrewMemberTypeAttType(Enum):
    CM01 = "cm01"
    CM02 = "cm02"
    CM03 = "cm03"
    CM04 = "cm04"
    CM05 = "cm05"
    CM06 = "cm06"
    CM07 = "cm07"
    CM08 = "cm08"
    CM09 = "cm09"
    CM10 = "cm10"
    CM11 = "cm11"
    CM12 = "cm12"
    CM13 = "cm13"
    CM14 = "cm14"
    CM15 = "cm15"
    CM16 = "cm16"
    CM17 = "cm17"
    CM18 = "cm18"
    CM19 = "cm19"
    CM20 = "cm20"
    CM21 = "cm21"
    CM22 = "cm22"
    CM23 = "cm23"
    CM24 = "cm24"
    CM25 = "cm25"
    CM26 = "cm26"
    CM27 = "cm27"
    CM28 = "cm28"
    CM29 = "cm29"
    CM30 = "cm30"
    CM31 = "cm31"
    CM32 = "cm32"
    CM33 = "cm33"
    CM34 = "cm34"
    CM35 = "cm35"
    CM36 = "cm36"
    CM37 = "cm37"
    CM38 = "cm38"
    CM39 = "cm39"
    CM40 = "cm40"
    CM41 = "cm41"
    CM42 = "cm42"
    CM43 = "cm43"
    CM44 = "cm44"
    CM45 = "cm45"
    CM46 = "cm46"
    CM47 = "cm47"
    CM48 = "cm48"
    CM49 = "cm49"
    CM50 = "cm50"
    CM51 = "cm51"
    CM52 = "cm52"
    CM53 = "cm53"
    CM54 = "cm54"
    CM55 = "cm55"
    CM56 = "cm56"
    CM57 = "cm57"
    CM58 = "cm58"
    CM59 = "cm59"
    CM60 = "cm60"
    CM61 = "cm61"
    CM62 = "cm62"
    CM63 = "cm63"
    CM64 = "cm64"
    CM65 = "cm65"
    CM66 = "cm66"
    CM67 = "cm67"
    CM68 = "cm68"
    CM69 = "cm69"
    CM70 = "cm70"
    CM71 = "cm71"
    CM72 = "cm72"
    CM73 = "cm73"
    CM74 = "cm74"
    CM75 = "cm75"
    CM76 = "cm76"
    CM77 = "cm77"
    CM78 = "cm78"
    CM79 = "cm79"
    CM80 = "cm80"
    CM81 = "cm81"
    CM82 = "cm82"
    CM83 = "cm83"
    CM84 = "cm84"
    CM85 = "cm85"
    CM86 = "cm86"
    CM87 = "cm87"
    CM88 = "cm88"
    CM89 = "cm89"
    CM90 = "cm90"
    CM91 = "cm91"
    CM92 = "cm92"
    CM93 = "cm93"
    CM94 = "cm94"
    CM95 = "cm95"
    CM96 = "cm96"
    CM97 = "cm97"
    CM98 = "cm98"
    CM99 = "cm99"


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


class DrillTypeAttType(Enum):
    DT00 = "dt00"
    DT01 = "dt01"
    DT02 = "dt02"
    DT03 = "dt03"
    DT04 = "dt04"
    DT05 = "dt05"
    DT06 = "dt06"
    DT07 = "dt07"
    DT08 = "dt08"
    DT09 = "dt09"
    DT10 = "dt10"
    DT11 = "dt11"
    DT12 = "dt12"
    DT13 = "dt13"
    DT14 = "dt14"
    DT15 = "dt15"
    DT16 = "dt16"
    DT17 = "dt17"
    DT18 = "dt18"
    DT19 = "dt19"
    DT20 = "dt20"
    DT21 = "dt21"
    DT22 = "dt22"
    DT23 = "dt23"
    DT24 = "dt24"
    DT25 = "dt25"
    DT26 = "dt26"
    DT27 = "dt27"
    DT28 = "dt28"
    DT29 = "dt29"
    DT30 = "dt30"
    DT31 = "dt31"
    DT32 = "dt32"
    DT33 = "dt33"
    DT34 = "dt34"
    DT35 = "dt35"
    DT36 = "dt36"
    DT37 = "dt37"
    DT38 = "dt38"
    DT39 = "dt39"
    DT40 = "dt40"
    DT41 = "dt41"
    DT42 = "dt42"
    DT43 = "dt43"
    DT44 = "dt44"
    DT45 = "dt45"
    DT46 = "dt46"
    DT47 = "dt47"
    DT48 = "dt48"
    DT49 = "dt49"
    DT50 = "dt50"
    DT51 = "dt51"
    DT52 = "dt52"
    DT53 = "dt53"
    DT54 = "dt54"
    DT55 = "dt55"
    DT56 = "dt56"
    DT57 = "dt57"
    DT58 = "dt58"
    DT59 = "dt59"
    DT60 = "dt60"
    DT61 = "dt61"
    DT62 = "dt62"
    DT63 = "dt63"
    DT64 = "dt64"
    DT65 = "dt65"
    DT66 = "dt66"
    DT67 = "dt67"
    DT68 = "dt68"
    DT69 = "dt69"
    DT70 = "dt70"
    DT71 = "dt71"
    DT72 = "dt72"
    DT73 = "dt73"
    DT74 = "dt74"
    DT75 = "dt75"
    DT76 = "dt76"
    DT77 = "dt77"
    DT78 = "dt78"
    DT79 = "dt79"
    DT80 = "dt80"
    DT81 = "dt81"
    DT82 = "dt82"
    DT83 = "dt83"
    DT84 = "dt84"
    DT85 = "dt85"
    DT86 = "dt86"
    DT87 = "dt87"
    DT88 = "dt88"
    DT89 = "dt89"
    DT90 = "dt90"
    DT91 = "dt91"
    DT92 = "dt92"
    DT93 = "dt93"
    DT94 = "dt94"
    DT95 = "dt95"
    DT96 = "dt96"
    DT97 = "dt97"
    DT98 = "dt98"
    DT99 = "dt99"


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


class FootnoteMarkAttType(Enum):
    NUM = "num"
    SYM = "sym"
    ALPHA = "alpha"


class FrameAttType(Enum):
    TOP = "top"
    BOTTOM = "bottom"
    TOPBOT = "topbot"
    ALL = "all"
    SIDES = "sides"
    NONE = "none"


@dataclass(kw_only=True)
class FunctionalItemCode:
    class Meta:
        name = "functionalItemCode"

    value: str = field(default="")


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


class SeparatorStyleAttType(Enum):
    DOT = "dot"
    LINE = "line"
    NONE = "none"


class SerialNumberFormAttType(Enum):
    SINGLE = "single"
    RANGE = "range"


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


@dataclass(kw_only=True)
class SubScript:
    class Meta:
        name = "subScript"

    value: str = field(default="")


@dataclass(kw_only=True)
class SuperScript:
    class Meta:
        name = "superScript"

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


class TableOfContentTypeAttType(Enum):
    NONE = "none"
    REDTOC = "redtoc"
    COMDTOC = "comdtoc"
    AMBERTOC = "ambertoc"
    GREENTOC = "greentoc"
    YELOWTOC = "yelowtoc"


@dataclass(kw_only=True)
class TechPubBase:
    class Meta:
        name = "techPubBase"

    value: str = field(default="")


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
class CrewMemberElemType:
    class Meta:
        name = "crewMemberElemType"

    crew_member_type: CrewMemberTypeAttType = field(
        metadata={
            "name": "crewMemberType",
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
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
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
class ExportRegistrationCode(ExportRegistrationCodeElemType):
    class Meta:
        name = "exportRegistrationCode"


@dataclass(kw_only=True)
class ExternalPubIssueDate(ExternalPubIssueDateElemType):
    class Meta:
        name = "externalPubIssueDate"


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
class FootnoteRefElemType:
    class Meta:
        name = "footnoteRefElemType"

    internal_ref_id: None | str = field(
        default=None,
        metadata={
            "name": "internalRefId",
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
class Language(LanguageElemType):
    class Meta:
        name = "language"


@dataclass(kw_only=True)
class ManufacturerCodeElemType:
    class Meta:
        name = "manufacturerCodeElemType"

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
class Parameter(ParameterElemType):
    class Meta:
        name = "parameter"


@dataclass(kw_only=True)
class PartNumberElemType:
    class Meta:
        name = "partNumberElemType"

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
class PhoneNumber(PhoneNumberElemType):
    class Meta:
        name = "phoneNumber"


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
class SerialNumberElemType:
    class Meta:
        name = "serialNumberElemType"

    serial_number_form: SerialNumberFormAttType = field(
        metadata={
            "name": "serialNumberForm",
            "type": "Attribute",
        }
    )
    serial_number_value: str = field(
        metadata={
            "name": "serialNumberValue",
            "type": "Attribute",
        }
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
class Unverified(UnverifiedElemType):
    class Meta:
        name = "unverified"


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
class Colspec(ColspecElemType):
    class Meta:
        name = "colspec"


@dataclass(kw_only=True)
class CrewMember(CrewMemberElemType):
    class Meta:
        name = "crewMember"


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
class DmCode(DmCodeElemType):
    class Meta:
        name = "dmCode"


@dataclass(kw_only=True)
class FirstVerification(FirstVerificationElemType):
    class Meta:
        name = "firstVerification"


@dataclass(kw_only=True)
class FootnoteRef(FootnoteRefElemType):
    class Meta:
        name = "footnoteRef"


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
class InternalRef(InternalRefElemType):
    class Meta:
        name = "internalRef"


@dataclass(kw_only=True)
class ManufacturerCode(ManufacturerCodeElemType):
    class Meta:
        name = "manufacturerCode"


@dataclass(kw_only=True)
class Modification(ModificationElemType):
    class Meta:
        name = "modification"


@dataclass(kw_only=True)
class Name(NameElemType):
    class Meta:
        name = "name"


@dataclass(kw_only=True)
class Originator(OriginatorElemType):
    class Meta:
        name = "originator"


@dataclass(kw_only=True)
class PartNumber(PartNumberElemType):
    class Meta:
        name = "partNumber"


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
class ResponsiblePartnerCompany(ResponsiblePartnerCompanyElemType):
    class Meta:
        name = "responsiblePartnerCompany"


@dataclass(kw_only=True)
class SecondVerification(SecondVerificationElemType):
    class Meta:
        name = "secondVerification"


@dataclass(kw_only=True)
class Security(SecurityElemType):
    class Meta:
        name = "security"


@dataclass(kw_only=True)
class SerialNumber(SerialNumberElemType):
    class Meta:
        name = "serialNumber"


@dataclass(kw_only=True)
class ShortName(ShortNameElemType):
    class Meta:
        name = "shortName"


@dataclass(kw_only=True)
class SimplePara(SimpleParaElemType):
    class Meta:
        name = "simplePara"


@dataclass(kw_only=True)
class SkillLevel(SkillLevelElemType):
    class Meta:
        name = "skillLevel"


@dataclass(kw_only=True)
class Spanspec(SpanspecElemType):
    class Meta:
        name = "spanspec"


@dataclass(kw_only=True)
class Supersedure(SupersedureElemType):
    class Meta:
        name = "supersedure"


@dataclass(kw_only=True)
class Symbol(SymbolElemType):
    class Meta:
        name = "symbol"


@dataclass(kw_only=True)
class TechName(TechNameElemType):
    class Meta:
        name = "techName"


@dataclass(kw_only=True)
class ValueAfterAction(ValueAfterActionElemType):
    class Meta:
        name = "valueAfterAction"


@dataclass(kw_only=True)
class VerbatimText(VerbatimTextElemType):
    class Meta:
        name = "verbatimText"


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
class BusinessUnitAddress(AddressElemType):
    class Meta:
        name = "businessUnitAddress"


@dataclass(kw_only=True)
class CaptionLineElemType:
    class Meta:
        name = "captionLineElemType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "acronymTerm",
                    "type": AcronymTerm,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class ContactPersonAddress(AddressElemType):
    class Meta:
        name = "contactPersonAddress"


@dataclass(kw_only=True)
class CrewMemberGroupElemType:
    class Meta:
        name = "crewMemberGroupElemType"

    crew_member: list[CrewMember] = field(
        default_factory=list,
        metadata={
            "name": "crewMember",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    action_responsibility: ActionResponsibilityAttType = field(
        default=ActionResponsibilityAttType.ALL,
        metadata={
            "name": "actionResponsibility",
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
class PartAndSerialNumberElemType:
    class Meta:
        name = "partAndSerialNumberElemType"

    part_number: PartNumber = field(
        metadata={
            "name": "partNumber",
            "type": "Element",
        }
    )
    serial_number: list[SerialNumber] = field(
        default_factory=list,
        metadata={
            "name": "serialNumber",
            "type": "Element",
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
class Acronym(AcronymElemType):
    class Meta:
        name = "acronym"


@dataclass(kw_only=True)
class CaptionLine(CaptionLineElemType):
    class Meta:
        name = "captionLine"


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
class CrewMemberGroup(CrewMemberGroupElemType):
    class Meta:
        name = "crewMemberGroup"


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
class Logo(LogoElemType):
    class Meta:
        name = "logo"


@dataclass(kw_only=True)
class PartAndSerialNumber(PartAndSerialNumberElemType):
    class Meta:
        name = "partAndSerialNumber"


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
class SourceDmIdent(SourceDmIdentGenericElemType):
    class Meta:
        name = "sourceDmIdent"


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
class CaptionElemType:
    class Meta:
        name = "captionElemType"

    caption_line: list[CaptionLine] = field(
        default_factory=list,
        metadata={
            "name": "captionLine",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    color: ColorAttType = field(
        default=ColorAttType.CO09,
        metadata={
            "type": "Attribute",
        },
    )
    caption_width: None | str = field(
        default=None,
        metadata={
            "name": "captionWidth",
            "type": "Attribute",
        },
    )
    caption_height: None | str = field(
        default=None,
        metadata={
            "name": "captionHeight",
            "type": "Attribute",
        },
    )
    system_ident_code: None | str = field(
        default=None,
        metadata={
            "name": "systemIdentCode",
            "type": "Attribute",
        },
    )
    align_caption: AlignCaptionAttType = field(
        default=AlignCaptionAttType.LEFT,
        metadata={
            "name": "alignCaption",
            "type": "Attribute",
        },
    )
    table_of_content_type: TableOfContentTypeAttType = field(
        default=TableOfContentTypeAttType.NONE,
        metadata={
            "name": "tableOfContentType",
            "type": "Attribute",
        },
    )
    caption_type: CaptionTypeAttType = field(
        default=CaptionTypeAttType.PRIMARY,
        metadata={
            "name": "captionType",
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
class Applic(ApplicElemType):
    class Meta:
        name = "applic"


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
class Caption(CaptionElemType):
    class Meta:
        name = "caption"


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
class ReferencedApplicGroup(ReferencedApplicGroupElemType):
    class Meta:
        name = "referencedApplicGroup"


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
class CautionRefElemType:
    class Meta:
        name = "cautionRefElemType"

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
    caution_ident_number: str = field(
        metadata={
            "name": "cautionIdentNumber",
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
class ClassificationAction(ClassificationActionElemType):
    class Meta:
        name = "classificationAction"


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
class TerminologyRefElemType:
    class Meta:
        name = "terminologyRefElemType"

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
    terminology_ident_number: str = field(
        metadata={
            "name": "terminologyIdentNumber",
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
class WarningRefElemType:
    class Meta:
        name = "warningRefElemType"

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
    warning_ident_number: str = field(
        metadata={
            "name": "warningIdentNumber",
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
class ApplicCrossRefTableRef(ApplicCrossRefTableRefElemType):
    class Meta:
        name = "applicCrossRefTableRef"


@dataclass(kw_only=True)
class ApplicRef(ApplicRefElemType):
    class Meta:
        name = "applicRef"


@dataclass(kw_only=True)
class BrexDmRef(BrexDmRefElemType):
    class Meta:
        name = "brexDmRef"


@dataclass(kw_only=True)
class CautionRef(CautionRefElemType):
    class Meta:
        name = "cautionRef"


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
class ExportRegistrationStmt(ExportRegistrationStmtElemType):
    class Meta:
        name = "exportRegistrationStmt"


@dataclass(kw_only=True)
class ExternalPubRefIdent(ExternalPubRefIdentElemType):
    class Meta:
        name = "externalPubRefIdent"


@dataclass(kw_only=True)
class TerminologyRef(TerminologyRefElemType):
    class Meta:
        name = "terminologyRef"


@dataclass(kw_only=True)
class WarningRef(WarningRefElemType):
    class Meta:
        name = "warningRef"


@dataclass(kw_only=True)
class ClassificationActionGroup(ClassificationActionGroupElemType):
    class Meta:
        name = "classificationActionGroup"


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
class WarningsAndCautionsRefElemType:
    class Meta:
        name = "warningsAndCautionsRefElemType"

    warning_ref: list[WarningRef] = field(
        default_factory=list,
        metadata={
            "name": "warningRef",
            "type": "Element",
        },
    )
    caution_ref: list[CautionRef] = field(
        default_factory=list,
        metadata={
            "name": "cautionRef",
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
class ExportControl(ExportControlElemType):
    class Meta:
        name = "exportControl"


@dataclass(kw_only=True)
class ExternalPubRef(ExternalPubRefElemType):
    class Meta:
        name = "externalPubRef"


@dataclass(kw_only=True)
class ReferencedApplicGroupRef(ReferencedApplicGroupRefElemType):
    class Meta:
        name = "referencedApplicGroupRef"


@dataclass(kw_only=True)
class WarningsAndCautionsRef(WarningsAndCautionsRefElemType):
    class Meta:
        name = "warningsAndCautionsRef"


@dataclass(kw_only=True)
class DerivativeClassification(DerivativeClassificationElemType):
    class Meta:
        name = "derivativeClassification"


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
class IdentNumberElemType:
    class Meta:
        name = "identNumberElemType"

    manufacturer_code: ManufacturerCode = field(
        metadata={
            "name": "manufacturerCode",
            "type": "Element",
        }
    )
    part_and_serial_number: list[PartAndSerialNumber] = field(
        default_factory=list,
        metadata={
            "name": "partAndSerialNumber",
            "type": "Element",
        },
    )
    refs: None | Refs = field(
        default=None,
        metadata={
            "type": "Element",
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
class FunctionalItemRef(FunctionalItemRefElemType):
    class Meta:
        name = "functionalItemRef"


@dataclass(kw_only=True)
class IdentNumber(IdentNumberElemType):
    class Meta:
        name = "identNumber"


@dataclass(kw_only=True)
class SupplyRef(SupplyRefElemType):
    class Meta:
        name = "supplyRef"


@dataclass(kw_only=True)
class ZoneRef(ZoneRefElemType):
    class Meta:
        name = "zoneRef"


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
                    "name": "indexFlag",
                    "type": IndexFlag,
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
                    "name": "terminologyRef",
                    "type": TerminologyRef,
                },
                {
                    "name": "footnote",
                    "type": ForwardRef("Footnote"),
                },
                {
                    "name": "footnoteRef",
                    "type": FootnoteRef,
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
                    "name": "captionGroup",
                    "type": ForwardRef("CaptionGroup"),
                },
                {
                    "name": "caption",
                    "type": Caption,
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
class Hotspot(HotspotElemType):
    class Meta:
        name = "hotspot"


@dataclass(kw_only=True)
class Para(ParaElemType):
    class Meta:
        name = "para"


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
class FootnoteElemType:
    class Meta:
        name = "footnoteElemType"

    para: list[Para] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    footnote_mark: FootnoteMarkAttType = field(
        default=FootnoteMarkAttType.NUM,
        metadata={
            "name": "footnoteMark",
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
class ControlAuthorityText(ControlAuthorityTextElemType):
    class Meta:
        name = "controlAuthorityText"


@dataclass(kw_only=True)
class Footnote(FootnoteElemType):
    class Meta:
        name = "footnote"


@dataclass(kw_only=True)
class ListItemDefinition(ListItemDefinitionElemType):
    class Meta:
        name = "listItemDefinition"


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
                    "name": "indexFlag",
                    "type": IndexFlag,
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
                    "name": "terminologyRef",
                    "type": TerminologyRef,
                },
                {
                    "name": "footnote",
                    "type": Footnote,
                },
                {
                    "name": "footnoteRef",
                    "type": FootnoteRef,
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
                    "name": "captionGroup",
                    "type": ForwardRef("CaptionGroup"),
                },
                {
                    "name": "caption",
                    "type": Caption,
                },
            ),
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
class ChangeInline(ChangeInlineElemType):
    class Meta:
        name = "changeInline"


@dataclass(kw_only=True)
class ControlAuthority(ControlAuthorityElemType):
    class Meta:
        name = "controlAuthority"


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
                    "name": "indexFlag",
                    "type": IndexFlag,
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
                    "name": "terminologyRef",
                    "type": TerminologyRef,
                },
                {
                    "name": "footnote",
                    "type": Footnote,
                },
                {
                    "name": "footnoteRef",
                    "type": FootnoteRef,
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
                    "name": "captionGroup",
                    "type": ForwardRef("CaptionGroup"),
                },
                {
                    "name": "caption",
                    "type": Caption,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class ControlAuthorityGroup(ControlAuthorityGroupElemType):
    class Meta:
        name = "controlAuthorityGroup"


@dataclass(kw_only=True)
class Emphasis(EmphasisElemType):
    class Meta:
        name = "emphasis"


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
                    "name": "zoneRef",
                    "type": ZoneRef,
                },
                {
                    "name": "accessPointRef",
                    "type": AccessPointRef,
                },
                {
                    "name": "identNumber",
                    "type": IdentNumber,
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
                    "name": "terminologyRef",
                    "type": TerminologyRef,
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
                    "name": "caption",
                    "type": Caption,
                },
                {
                    "name": "verbatimText",
                    "type": VerbatimText,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class CaptionTextElemType:
    class Meta:
        name = "captionTextElemType"

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
                    "name": "internalRef",
                    "type": InternalRef,
                },
                {
                    "name": "indexFlag",
                    "type": IndexFlag,
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
class AttentionListItemPara(AttentionListItemParaElemType):
    class Meta:
        name = "attentionListItemPara"


@dataclass(kw_only=True)
class CaptionText(CaptionTextElemType):
    class Meta:
        name = "captionText"


@dataclass(kw_only=True)
class SimpleRefPara(SimpleRefParaElemType):
    class Meta:
        name = "simpleRefPara"


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
class CaptionEntryElemType:
    class Meta:
        name = "captionEntryElemType"

    caption: None | Caption = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    caption_text: None | CaptionText = field(
        default=None,
        metadata={
            "name": "captionText",
            "type": "Element",
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
    valign: None | ValignAttType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    align_caption_entry: None | AlignCaptionEntryAttType = field(
        default=None,
        metadata={
            "name": "alignCaptionEntry",
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
class AttentionRandomListItem(AttentionRandomListItemElemType):
    class Meta:
        name = "attentionRandomListItem"


@dataclass(kw_only=True)
class CaptionEntry(CaptionEntryElemType):
    class Meta:
        name = "captionEntry"


@dataclass(kw_only=True)
class ReasonForUpdate(ReasonForUpdateElemType):
    class Meta:
        name = "reasonForUpdate"


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
class CaptionRowElemType:
    class Meta:
        name = "captionRowElemType"

    caption_entry: list[CaptionEntry] = field(
        default_factory=list,
        metadata={
            "name": "captionEntry",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    rowsep: None | str = field(
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
class AttentionRandomList(AttentionRandomListElemType):
    class Meta:
        name = "attentionRandomList"


@dataclass(kw_only=True)
class CaptionRow(CaptionRowElemType):
    class Meta:
        name = "captionRow"


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
class CaptionBodyElemType:
    class Meta:
        name = "captionBodyElemType"

    caption_row: list[CaptionRow] = field(
        default_factory=list,
        metadata={
            "name": "captionRow",
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
                    "name": "zoneRef",
                    "type": ZoneRef,
                },
                {
                    "name": "accessPointRef",
                    "type": AccessPointRef,
                },
                {
                    "name": "identNumber",
                    "type": IdentNumber,
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
                    "name": "terminologyRef",
                    "type": TerminologyRef,
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
                    "name": "caption",
                    "type": Caption,
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
class CaptionBody(CaptionBodyElemType):
    class Meta:
        name = "captionBody"


@dataclass(kw_only=True)
class WarningAndCautionPara(WarningAndCautionParaElemType):
    class Meta:
        name = "warningAndCautionPara"


@dataclass(kw_only=True)
class CaptionGroupElemType:
    class Meta:
        name = "captionGroupElemType"

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
    caption_body: CaptionBody = field(
        metadata={
            "name": "captionBody",
            "type": "Element",
        }
    )
    cols: int = field(
        metadata={
            "type": "Attribute",
        }
    )
    align_caption: AlignCaptionAttType = field(
        default=AlignCaptionAttType.LEFT,
        metadata={
            "name": "alignCaption",
            "type": "Attribute",
        },
    )
    table_of_content_type: TableOfContentTypeAttType = field(
        default=TableOfContentTypeAttType.NONE,
        metadata={
            "name": "tableOfContentType",
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
class CaptionGroup(CaptionGroupElemType):
    class Meta:
        name = "captionGroup"


@dataclass(kw_only=True)
class Caution(CautionElemType):
    class Meta:
        name = "caution"


@dataclass(kw_only=True)
class Warning(WarningElemType):
    class Meta:
        name = "warning"


@dataclass(kw_only=True)
class CaseCondElemType:
    class Meta:
        name = "caseCondElemType"

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
                    "name": "indexFlag",
                    "type": IndexFlag,
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
                    "name": "terminologyRef",
                    "type": TerminologyRef,
                },
                {
                    "name": "footnote",
                    "type": Footnote,
                },
                {
                    "name": "footnoteRef",
                    "type": FootnoteRef,
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
                    "name": "captionGroup",
                    "type": CaptionGroup,
                },
                {
                    "name": "caption",
                    "type": Caption,
                },
            ),
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
                    "name": "indexFlag",
                    "type": IndexFlag,
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
                    "name": "terminologyRef",
                    "type": TerminologyRef,
                },
                {
                    "name": "footnote",
                    "type": Footnote,
                },
                {
                    "name": "footnoteRef",
                    "type": FootnoteRef,
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
                    "name": "captionGroup",
                    "type": CaptionGroup,
                },
                {
                    "name": "caption",
                    "type": Caption,
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
                    "name": "indexFlag",
                    "type": IndexFlag,
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
                    "name": "terminologyRef",
                    "type": TerminologyRef,
                },
                {
                    "name": "footnote",
                    "type": Footnote,
                },
                {
                    "name": "footnoteRef",
                    "type": FootnoteRef,
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
                    "name": "captionGroup",
                    "type": CaptionGroup,
                },
                {
                    "name": "caption",
                    "type": Caption,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class ThumbTabTextElemType:
    class Meta:
        name = "thumbTabTextElemType"

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
                    "name": "internalRef",
                    "type": InternalRef,
                },
                {
                    "name": "indexFlag",
                    "type": IndexFlag,
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
                    "name": "footnoteRef",
                    "type": FootnoteRef,
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
                    "name": "captionGroup",
                    "type": CaptionGroup,
                },
                {
                    "name": "caption",
                    "type": Caption,
                },
                {
                    "name": "terminologyRef",
                    "type": TerminologyRef,
                },
            ),
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
                    "name": "indexFlag",
                    "type": IndexFlag,
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
                    "name": "terminologyRef",
                    "type": TerminologyRef,
                },
                {
                    "name": "footnote",
                    "type": Footnote,
                },
                {
                    "name": "footnoteRef",
                    "type": FootnoteRef,
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
                    "name": "captionGroup",
                    "type": CaptionGroup,
                },
                {
                    "name": "caption",
                    "type": Caption,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class WarningsAndCautionsElemType:
    class Meta:
        name = "warningsAndCautionsElemType"

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
class CaseCond(CaseCondElemType):
    class Meta:
        name = "caseCond"


@dataclass(kw_only=True)
class DefinitionTitle(TitleElemType):
    class Meta:
        name = "definitionTitle"


@dataclass(kw_only=True)
class ListItemTerm(ListItemTermElemType):
    class Meta:
        name = "listItemTerm"


@dataclass(kw_only=True)
class ReasonForAmendment(ReasonForAmendmentElemType):
    class Meta:
        name = "reasonForAmendment"


@dataclass(kw_only=True)
class TermTitle(TitleElemType):
    class Meta:
        name = "termTitle"


@dataclass(kw_only=True)
class ThumbTabText(ThumbTabTextElemType):
    class Meta:
        name = "thumbTabText"


@dataclass(kw_only=True)
class Title(TitleElemType):
    class Meta:
        name = "title"


@dataclass(kw_only=True)
class WarningsAndCautions(WarningsAndCautionsElemType):
    class Meta:
        name = "warningsAndCautions"


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
class AttentionSequentialList(AttentionSequentialListElemType):
    class Meta:
        name = "attentionSequentialList"


@dataclass(kw_only=True)
class DefinitionListHeader(DefinitionListHeaderElemType):
    class Meta:
        name = "definitionListHeader"


@dataclass(kw_only=True)
class DefinitionListItem(DefinitionListItemElemType):
    class Meta:
        name = "definitionListItem"


@dataclass(kw_only=True)
class Graphic(GraphicElemType):
    class Meta:
        name = "graphic"


@dataclass(kw_only=True)
class MultimediaObject(MultimediaObjectElemType):
    class Meta:
        name = "multimediaObject"


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
                    "name": "zoneRef",
                    "type": ZoneRef,
                },
                {
                    "name": "accessPointRef",
                    "type": AccessPointRef,
                },
                {
                    "name": "identNumber",
                    "type": IdentNumber,
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
                    "name": "terminologyRef",
                    "type": TerminologyRef,
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
                    "name": "caption",
                    "type": Caption,
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
class DefinitionList(DefinitionListElemType):
    class Meta:
        name = "definitionList"


@dataclass(kw_only=True)
class Multimedia(MultimediaElemType):
    class Meta:
        name = "multimedia"


@dataclass(kw_only=True)
class NotePara(NoteParaElemType):
    class Meta:
        name = "notePara"


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
class Legend(LegendElemType):
    class Meta:
        name = "legend"


@dataclass(kw_only=True)
class MultimediaAlts(MultimediaAltsElemType):
    class Meta:
        name = "multimediaAlts"


@dataclass(kw_only=True)
class Note(NoteElemType):
    class Meta:
        name = "note"


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
class Entry(EntryElemType):
    class Meta:
        name = "entry"


@dataclass(kw_only=True)
class Figure(FigureElemType):
    class Meta:
        name = "figure"


@dataclass(kw_only=True)
class ListItem(ListItemElemType):
    class Meta:
        name = "listItem"


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
class FigureAlts(FigureAltsElemType):
    class Meta:
        name = "figureAlts"


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
class CopyrightPara(CopyrightParaElemType):
    class Meta:
        name = "copyrightPara"


@dataclass(kw_only=True)
class Tbody(TbodyElemType):
    class Meta:
        name = "tbody"


@dataclass(kw_only=True)
class Tfoot(TfootElemType):
    class Meta:
        name = "tfoot"


@dataclass(kw_only=True)
class Thead(TheadElemType):
    class Meta:
        name = "thead"


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
class Copyright(CopyrightElemType):
    class Meta:
        name = "copyright"


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
class RestrictionInfo(RestrictionInfoElemType):
    class Meta:
        name = "restrictionInfo"


@dataclass(kw_only=True)
class Table(TableElemType):
    class Meta:
        name = "table"


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
class DataRestrictions(DataRestrictionsElemType):
    class Meta:
        name = "dataRestrictions"


@dataclass(kw_only=True)
class Foldout(FoldoutElemType):
    class Meta:
        name = "foldout"


@dataclass(kw_only=True)
class ChallengeElemType:
    class Meta:
        name = "challengeElemType"

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
class CrewProcedureNameElemType:
    class Meta:
        name = "crewProcedureNameElemType"

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
class EndMatterElemType:
    class Meta:
        name = "endMatterElemType"

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
class ResponseElemType:
    class Meta:
        name = "responseElemType"

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
class Challenge(ChallengeElemType):
    class Meta:
        name = "challenge"


@dataclass(kw_only=True)
class CrewProcedureName(CrewProcedureNameElemType):
    class Meta:
        name = "crewProcedureName"


@dataclass(kw_only=True)
class DmStatus(DmStatusGenericElemType):
    class Meta:
        name = "dmStatus"


@dataclass(kw_only=True)
class EndMatter(EndMatterElemType):
    class Meta:
        name = "endMatter"


@dataclass(kw_only=True)
class Response(ResponseElemType):
    class Meta:
        name = "response"


@dataclass(kw_only=True)
class ChallengeAndResponseElemType:
    class Meta:
        name = "challengeAndResponseElemType"

    challenge: Challenge = field(
        metadata={
            "type": "Element",
        }
    )
    crew_member_group: list[CrewMemberGroup] = field(
        default_factory=list,
        metadata={
            "name": "crewMemberGroup",
            "type": "Element",
        },
    )
    response: list[Response] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
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
class ChallengeAndResponse(ChallengeAndResponseElemType):
    class Meta:
        name = "challengeAndResponse"


@dataclass(kw_only=True)
class IdentAndStatusSection(IdentAndStatusSectionElemType):
    class Meta:
        name = "identAndStatusSection"


@dataclass(kw_only=True)
class CrewDrillStepElemType:
    class Meta:
        name = "crewDrillStepElemType"

    title: None | Title = field(
        default=None,
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
    caption: list[Caption] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    crew_member_group: list[CrewMemberGroup] = field(
        default_factory=list,
        metadata={
            "name": "crewMemberGroup",
            "type": "Element",
        },
    )
    crew_procedure_name: list[CrewProcedureName] = field(
        default_factory=list,
        metadata={
            "name": "crewProcedureName",
            "type": "Element",
        },
    )
    challenge_and_response: list[ChallengeAndResponse] = field(
        default_factory=list,
        metadata={
            "name": "challengeAndResponse",
            "type": "Element",
        },
    )
    crew_drill_step: list[CrewDrillStep] = field(
        default_factory=list,
        metadata={
            "name": "crewDrillStep",
            "type": "Element",
        },
    )
    if_value: list[If] = field(
        default_factory=list,
        metadata={
            "name": "if",
            "type": "Element",
        },
    )
    else_if: list[ElseIf] = field(
        default_factory=list,
        metadata={
            "name": "elseIf",
            "type": "Element",
        },
    )
    case: list[Case] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    step_label: None | str = field(
        default=None,
        metadata={
            "name": "stepLabel",
            "type": "Attribute",
        },
    )
    keep_with_next: str = field(
        default="0",
        metadata={
            "name": "keepWithNext",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    memorize_steps_flag: str = field(
        default="0",
        metadata={
            "name": "memorizeStepsFlag",
            "type": "Attribute",
            "pattern": r"[01]",
        },
    )
    separator_style: SeparatorStyleAttType = field(
        default=SeparatorStyleAttType.DOT,
        metadata={
            "name": "separatorStyle",
            "type": "Attribute",
        },
    )
    ordered_steps_flag: str = field(
        default="1",
        metadata={
            "name": "orderedStepsFlag",
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
    crew_step_condition: list[str] = field(
        default_factory=list,
        metadata={
            "name": "crewStepCondition",
            "type": "Attribute",
            "pattern": r"csc\d{2}( csc\d{2})*",
            "tokens": True,
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
    independent_check: None | str = field(
        default=None,
        metadata={
            "name": "independentCheck",
            "type": "Attribute",
        },
    )
    skill_level_code: None | SkillLevelCodeAttType = field(
        default=None,
        metadata={
            "name": "skillLevelCode",
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
class CrewDrillStep(CrewDrillStepElemType):
    class Meta:
        name = "crewDrillStep"


@dataclass(kw_only=True)
class IfElemType:
    class Meta:
        name = "ifElemType"

    case_cond: CaseCond = field(
        metadata={
            "name": "caseCond",
            "type": "Element",
        }
    )
    crew_drill_step: list[CrewDrillStep] = field(
        default_factory=list,
        metadata={
            "name": "crewDrillStep",
            "type": "Element",
        },
    )
    if_value: list[If] = field(
        default_factory=list,
        metadata={
            "name": "if",
            "type": "Element",
        },
    )
    else_if: list[ElseIf] = field(
        default_factory=list,
        metadata={
            "name": "elseIf",
            "type": "Element",
        },
    )
    case: list[Case] = field(
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
class If(IfElemType):
    class Meta:
        name = "if"


@dataclass(kw_only=True)
class ElseIfElemType:
    class Meta:
        name = "elseIfElemType"

    case_cond: CaseCond = field(
        metadata={
            "name": "caseCond",
            "type": "Element",
        }
    )
    crew_drill_step: list[CrewDrillStep] = field(
        default_factory=list,
        metadata={
            "name": "crewDrillStep",
            "type": "Element",
        },
    )
    if_value: list[If] = field(
        default_factory=list,
        metadata={
            "name": "if",
            "type": "Element",
        },
    )
    else_if: list[ElseIf] = field(
        default_factory=list,
        metadata={
            "name": "elseIf",
            "type": "Element",
        },
    )
    case: list[Case] = field(
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
class ElseIf(ElseIfElemType):
    class Meta:
        name = "elseIf"


@dataclass(kw_only=True)
class CaseElemType:
    class Meta:
        name = "caseElemType"

    case_cond: CaseCond = field(
        metadata={
            "name": "caseCond",
            "type": "Element",
        }
    )
    crew_drill_step: list[CrewDrillStep] = field(
        default_factory=list,
        metadata={
            "name": "crewDrillStep",
            "type": "Element",
        },
    )
    if_value: list[If] = field(
        default_factory=list,
        metadata={
            "name": "if",
            "type": "Element",
        },
    )
    else_if: list[ElseIf] = field(
        default_factory=list,
        metadata={
            "name": "elseIf",
            "type": "Element",
        },
    )
    case: list[Case] = field(
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
class Case(CaseElemType):
    class Meta:
        name = "case"


@dataclass(kw_only=True)
class SubCrewDrillElemType:
    class Meta:
        name = "subCrewDrillElemType"

    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    thumb_tab_text: None | ThumbTabText = field(
        default=None,
        metadata={
            "name": "thumbTabText",
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
    crew_member_group: list[CrewMemberGroup] = field(
        default_factory=list,
        metadata={
            "name": "crewMemberGroup",
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
    crew_drill_step: list[CrewDrillStep] = field(
        default_factory=list,
        metadata={
            "name": "crewDrillStep",
            "type": "Element",
        },
    )
    if_value: list[If] = field(
        default_factory=list,
        metadata={
            "name": "if",
            "type": "Element",
        },
    )
    else_if: list[ElseIf] = field(
        default_factory=list,
        metadata={
            "name": "elseIf",
            "type": "Element",
        },
    )
    case: list[Case] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ordered_steps_flag: str = field(
        default="1",
        metadata={
            "name": "orderedStepsFlag",
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
    independent_check: None | str = field(
        default=None,
        metadata={
            "name": "independentCheck",
            "type": "Attribute",
        },
    )
    skill_level_code: None | SkillLevelCodeAttType = field(
        default=None,
        metadata={
            "name": "skillLevelCode",
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
    control_authority_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthorityRefs",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class SubCrewDrill(SubCrewDrillElemType):
    class Meta:
        name = "subCrewDrill"


@dataclass(kw_only=True)
class CrewDrillElemType:
    class Meta:
        name = "crewDrillElemType"

    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    thumb_tab_text: None | ThumbTabText = field(
        default=None,
        metadata={
            "name": "thumbTabText",
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
    crew_member_group: list[CrewMemberGroup] = field(
        default_factory=list,
        metadata={
            "name": "crewMemberGroup",
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
    crew_drill_step: list[CrewDrillStep] = field(
        default_factory=list,
        metadata={
            "name": "crewDrillStep",
            "type": "Element",
        },
    )
    if_value: list[If] = field(
        default_factory=list,
        metadata={
            "name": "if",
            "type": "Element",
        },
    )
    else_if: list[ElseIf] = field(
        default_factory=list,
        metadata={
            "name": "elseIf",
            "type": "Element",
        },
    )
    case: list[Case] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    sub_crew_drill: list[SubCrewDrill] = field(
        default_factory=list,
        metadata={
            "name": "subCrewDrill",
            "type": "Element",
        },
    )
    end_matter: None | EndMatter = field(
        default=None,
        metadata={
            "name": "endMatter",
            "type": "Element",
        },
    )
    drill_type: DrillTypeAttType = field(
        default=DrillTypeAttType.DT00,
        metadata={
            "name": "drillType",
            "type": "Attribute",
        },
    )
    ordered_steps_flag: str = field(
        default="1",
        metadata={
            "name": "orderedStepsFlag",
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
    crew_step_condition: list[str] = field(
        default_factory=list,
        metadata={
            "name": "crewStepCondition",
            "type": "Attribute",
            "pattern": r"csc\d{2}( csc\d{2})*",
            "tokens": True,
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
    independent_check: None | str = field(
        default=None,
        metadata={
            "name": "independentCheck",
            "type": "Attribute",
        },
    )
    skill_level_code: None | SkillLevelCodeAttType = field(
        default=None,
        metadata={
            "name": "skillLevelCode",
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
class CrewDrill(CrewDrillElemType):
    class Meta:
        name = "crewDrill"


@dataclass(kw_only=True)
class CrewRefCardElemType:
    class Meta:
        name = "crewRefCardElemType"

    title: list[Title] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 1,
        },
    )
    warning: list[Warning] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 1,
        },
    )
    caution: list[Caution] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 1,
        },
    )
    note: list[Note] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 1,
        },
    )
    para: list[Para] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 1,
        },
    )
    crew_drill: list[CrewDrill] = field(
        default_factory=list,
        metadata={
            "name": "crewDrill",
            "type": "Element",
            "sequence": 1,
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
class LevelledParaElemType:
    class Meta:
        name = "levelledParaElemType"

    title: None | Title = field(
        default=None,
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
    caption: list[Caption] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    crew_drill: None | CrewDrill = field(
        default=None,
        metadata={
            "name": "crewDrill",
            "type": "Element",
        },
    )
    levelled_para: list[LevelledPara] = field(
        default_factory=list,
        metadata={
            "name": "levelledPara",
            "type": "Element",
        },
    )
    levelled_para_alts: list[LevelledParaAlts] = field(
        default_factory=list,
        metadata={
            "name": "levelledParaAlts",
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
class CrewRefCard(CrewRefCardElemType):
    class Meta:
        name = "crewRefCard"


@dataclass(kw_only=True)
class LevelledPara(LevelledParaElemType):
    class Meta:
        name = "levelledPara"


@dataclass(kw_only=True)
class DescrCrewElemType:
    class Meta:
        name = "descrCrewElemType"

    warning: list[Warning] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 1,
        },
    )
    caution: list[Caution] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 1,
        },
    )
    note: list[Note] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 1,
        },
    )
    levelled_para: list[LevelledPara] = field(
        default_factory=list,
        metadata={
            "name": "levelledPara",
            "type": "Element",
            "sequence": 1,
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
class LevelledParaAltsElemType:
    class Meta:
        name = "levelledParaAltsElemType"

    levelled_para: list[LevelledPara] = field(
        default_factory=list,
        metadata={
            "name": "levelledPara",
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
class DescrCrew(DescrCrewElemType):
    class Meta:
        name = "descrCrew"


@dataclass(kw_only=True)
class LevelledParaAlts(LevelledParaAltsElemType):
    class Meta:
        name = "levelledParaAlts"


@dataclass(kw_only=True)
class CrewElemType:
    class Meta:
        name = "crewElemType"

    crew_ref_card: None | CrewRefCard = field(
        default=None,
        metadata={
            "name": "crewRefCard",
            "type": "Element",
        },
    )
    descr_crew: None | DescrCrew = field(
        default=None,
        metadata={
            "name": "descrCrew",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
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


@dataclass(kw_only=True)
class Crew(CrewElemType):
    class Meta:
        name = "crew"


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
    warnings_and_cautions: None | WarningsAndCautions = field(
        default=None,
        metadata={
            "name": "warningsAndCautions",
            "type": "Element",
        },
    )
    warnings_and_cautions_ref: None | WarningsAndCautionsRef = field(
        default=None,
        metadata={
            "name": "warningsAndCautionsRef",
            "type": "Element",
        },
    )
    crew: Crew = field(
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
