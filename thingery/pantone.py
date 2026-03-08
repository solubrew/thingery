# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Thingery Pantone Colors
	description: >
		Pantone color matching system colors
	version: 0.0.0.0.0.0
	authority: filesystem
	security: seclvl2
	<(WT)>: -32
"""
# -*- coding: utf-8 -*
from dataclasses import dataclass
from typing import Tuple


# ======================================Standard Library Modules======================================================||
# ======================================3rd Party Library Modules=====================================================||
# ======================================Solutions Brewer Library Modules=============================================||
# ====================================================================================================================||


# ===========================PANTONE CLASSIC COLORS=================================================================||
# ====================================================================================================================||

# Pantone Yellows
@dataclass
class PantoneYellow:
    name: str = "Pantone Yellow"
    pantone_code: str = "PMS 100 C"
    hex_code: str = "#F4ED7C"
    rgb: Tuple[int, int, int] = (244, 237, 124)
    category: str = "pantone"


@dataclass
class PantoneGoldenYellow:
    name: str = "Pantone Golden Yellow"
    pantone_code: str = "PMS 109 C"
    hex_code: str = "#FFD100"
    rgb: Tuple[int, int, int] = (255, 209, 0)
    category: str = "pantone"


@dataclass
class PantoneOrange:
    name: str = "Pantone Orange"
    pantone_code: str = "PMS 021 C"
    hex_code: str = "#FE5000"
    rgb: Tuple[int, int, int] = (254, 80, 0)
    category: str = "pantone"


@dataclass
class PantoneWarmRed:
    name: str = "Pantone Warm Red"
    pantone_code: str = "PMS 179 C"
    hex_code: str = "#E35205"
    rgb: Tuple[int, int, int] = (227, 82, 5)
    category: str = "pantone"


@dataclass
class PantoneRed:
    name: str = "Pantone Red"
    pantone_code: str = "PMS 186 C"
    hex_code: str = "#C8102E"
    rgb: Tuple[int, int, int] = (200, 16, 46)
    category: str = "pantone"


@dataclass
class PantoneRubineRed:
    name: str = "Pantone Rubine Red"
    pantone_code: str = "PMS 199 C"
    hex_code: str = "#D50032"
    rgb: Tuple[int, int, int] = (213, 0, 50)
    category: str = "pantone"


@dataclass
class PantoneRhodamineRed:
    name: str = "Pantone Rhodamine Red"
    pantone_code: str = "PMS Red"
    hex_code: str = "#E10098"
    rgb: Tuple[int, int, int] = (225, 0, 152)
    category: str = "pantone"


@dataclass
class PantoneMagenta:
    name: str = "Pantone Magenta"
    pantone_code: str = "PMS 260 C"
    hex_code: str = "#7B3F9D"
    rgb: Tuple[int, int, int] = (123, 63, 157)
    category: str = "pantone"


@dataclass
class PantoneViolet:
    name: str = "Pantone Violet"
    pantone_code: str = "PMS 268 C"
    hex_code: str = "#440099"
    rgb: Tuple[int, int, int] = (68, 0, 153)
    category: str = "pantone"


@dataclass
class PantoneBlue:
    name: str = "Pantone Blue"
    pantone_code: str = "PMS 072 C"
    hex_code: str = "#0047BB"
    rgb: Tuple[int, int, int] = (0, 71, 187)
    category: str = "pantone"


@dataclass
class PantoneProcessBlue:
    name: str = "Pantone Process Blue"
    pantone_code: str = "PMS 299 C"
    hex_code: str = "#00A3E0"
    rgb: Tuple[int, int, int] = (0, 163, 224)
    category: str = "pantone"


@dataclass
class PantoneGreen:
    name: str = "Pantone Green"
    pantone_code: str = "PMS 354 C"
    hex_code: str = "#00B140"
    rgb: Tuple[int, int, int] = (0, 177, 64)
    category: str = "pantone"


@dataclass
class PantoneBlack:
    name: str = "Pantone Black"
    pantone_code: str = "PMS Black C"
    hex_code: str = "#2D2926"
    rgb: Tuple[int, int, int] = (45, 41, 38)
    category: str = "pantone"


@dataclass
class PantoneCoolGray1:
    name: str = "Pantone Cool Gray 1"
    pantone_code: str = "PMS Cool Gray 1 C"
    hex_code: str = "#D9D9D6"
    rgb: Tuple[int, int, int] = (217, 217, 214)
    category: str = "pantone"


@dataclass
class PantoneCoolGray5:
    name: str = "Pantone Cool Gray 5"
    pantone_code: str = "PMS Cool Gray 5 C"
    hex_code: str = "#B1B3B3"
    rgb: Tuple[int, int, int] = (177, 179, 179)
    category: str = "pantone"


@dataclass
class PantoneCoolGray10:
    name: str = "Pantone Cool Gray 10"
    pantone_code: str = "PMS Cool Gray 10 C"
    hex_code: str = "#53565A"
    rgb: Tuple[int, int, int] = (83, 86, 90)
    category: str = "pantone"


# ===========================PANTONE PLUS COLORS===================================================================||
# ====================================================================================================================||

# Pantone Plus Yellows
@dataclass
class PantonePlusYellow:
    name: str = "Pantone Plus Yellow"
    pantone_code: str = "PMS 106 C"
    hex_code: str = "#F9E547"
    rgb: Tuple[int, int, int] = (249, 229, 71)
    category: str = "pantone_plus"


@dataclass
class PantonePlusOrange021:
    name: str = "Pantone Plus Orange 021"
    pantone_code: str = "PMS Orange 021 C"
    hex_code: str = "#FE7800"
    rgb: Tuple[int, int, int] = (254, 120, 0)
    category: str = "pantone_plus"


@dataclass
class PantonePlusWarmRed:
    name: str = "Pantone Plus Warm Red"
    pantone_code: str = "PMS Warm Red C"
    hex_code: str = "#F94144"
    rgb: Tuple[int, int, int] = (249, 65, 68)
    category: str = "pantone_plus"


@dataclass
class PantonePlusRed:
    name: str = "Pantone Plus Red"
    pantone_code: str = "PMS Red 032 C"
    hex_code: str = "#EF3340"
    rgb: Tuple[int, int, int] = (239, 51, 64)
    category: str = "pantone_plus"


@dataclass
class PantonePlusPink:
    name: str = "Pantone Plus Pink"
    pantone_code: str = "PMS Pink C"
    hex_code: str = "#FFCDD6"
    rgb: Tuple[int, int, int] = (255, 205, 214)
    category: str = "pantone_plus"


@dataclass
class PantonePlusRhodamineRed:
    name: str = "Pantone Plus Rhodamine Red"
    pantone_code: str = "PMS Rhodamine Red C"
    hex_code: str = "#FF00CC"
    rgb: Tuple[int, int, int] = (255, 0, 204)
    category: str = "pantone_plus"


@dataclass
class PantonePlusPurple:
    name: str = "Pantone Plus Purple"
    pantone_code: str = "PMS Purple C"
    hex_code: str = "#BB29BB"
    rgb: Tuple[int, int, int] = (187, 41, 187)
    category: str = "pantone_plus"


@dataclass
class PantonePlusViolet:
    name: str = "Pantone Plus Violet"
    pantone_code: str = "PMS Violet C"
    hex_code: str = "#440099"
    rgb: Tuple[int, int, int] = (68, 0, 153)
    category: str = "pantone_plus"


@dataclass
class PantonePlusBlue072:
    name: str = "Pantone Plus Blue 072"
    pantone_code: str = "PMS Blue 072 C"
    hex_code: str = "#0033A0"
    rgb: Tuple[int, int, int] = (0, 51, 160)
    category: str = "pantone_plus"


@dataclass
class PantonePlusProcessBlue:
    name: str = "Pantone Plus Process Blue"
    pantone_code: str = "PMS Process Cyan C"
    hex_code: str = "#00A3E0"
    rgb: Tuple[int, int, int] = (0, 163, 224)
    category: str = "pantone_plus"


@dataclass
class PantonePlusGreen:
    name: str = "Pantone Plus Green"
    pantone_code: str = "PMS Green C"
    hex_code: str = "#00AB84"
    rgb: Tuple[int, int, int] = (0, 171, 132)
    category: str = "pantone_plus"


@dataclass
class PantonePlusBlack:
    name: str = "Pantone Plus Black"
    pantone_code: str = "PMS Process Black C"
    hex_code: str = "#2D2926"
    rgb: Tuple[int, int, int] = (45, 41, 38)
    category: str = "pantone_plus"


# ===========================PANTONE METALLICS======================================================================||
# ====================================================================================================================||


@dataclass
class PantoneMetallicGold:
    name: str = "Pantone Metallic Gold"
    pantone_code: str = "PMS 871 C"
    hex_code: str = "#85714D"
    rgb: Tuple[int, int, int] = (133, 113, 77)
    category: str = "pantone_metallic"


@dataclass
class PantoneMetallicSilver:
    name: str = "Pantone Metallic Silver"
    pantone_code: str = "PMS 877 C"
    hex_code: str = "#8A8D8F"
    rgb: Tuple[int, int, int] = (138, 141, 143)
    category: str = "pantone_metallic"


# ===========================PANTONE SKINTONE=======================================================================||
# ====================================================================================================================||


@dataclass
class PantoneSkintoneLight:
    name: str = "Pantone Skintone Light"
    pantone_code: str = "PMS 7527 C"
    hex_code: str = "#E4C3A8"
    rgb: Tuple[int, int, int] = (228, 195, 168)
    category: str = "pantone_skintone"


@dataclass
class PantoneSkintoneMedium:
    name: str = "Pantone Skintone Medium"
    pantone_code: str = "PMS 7526 C"
    hex_code: str = "#C48A69"
    rgb: Tuple[int, int, int] = (196, 138, 105)
    category: str = "pantone_skintone"


@dataclass
class PantoneSkintoneDark:
    name: str = "Pantone Skintone Dark"
    pantone_code: str = "PMS 722 C"
    hex_code: str = "#8D5524"
    rgb: Tuple[int, int, int] = (141, 85, 36)
    category: str = "pantone_skintone"


# ===========================PANTONE FASHION COLORS===============================================================||
# ====================================================================================================================||


@dataclass
class PantoneFashionLilac:
    name: str = "Pantone Fashion Lilac"
    pantone_code: str = "PMS 15-3817 TPG"
    hex_code: str = "#9BB7D4"
    rgb: Tuple[int, int, int] = (155, 183, 212)
    category: str = "pantone_fashion"


@dataclass
class PantoneFashionBlue:
    name: str = "Pantone Fashion Blue"
    pantone_code: str = "PMS 15-4020 TPG"
    hex_code: str = "#B4C6D9"
    rgb: Tuple[int, int, int] = (180, 198, 217)
    category: str = "pantone_fashion"


@dataclass
class PantoneFashionFuchsia:
    name: str = "Pantone Fashion Fuchsia"
    pantone_code: str = "PMS 17-3020 TPG"
    hex_code: str = "#B94E78"
    rgb: Tuple[int, int, int] = (185, 78, 120)
    category: str = "pantone_fashion"


@dataclass
class PantoneFashionEmerald:
    name: str = "Pantone Fashion Emerald"
    pantone_code: str = "PMS 17-5024 TPG"
    hex_code: str = "#358477"
    rgb: Tuple[int, int, int] = (53, 132, 119)
    category: str = "pantone_fashion"


@dataclass
class PantoneFashionTangerine:
    name: str = "Pantone Fashion Tangerine"
    pantone_code: str = "PMS 16-1356 TPG"
    hex_code: str = "#E8762E"
    rgb: Tuple[int, int, int] = (232, 118, 46)
    category: str = "pantone_fashion"


# ===========================EXPORTS=================================================================================||
# ====================================================================================================================||


__all__ = [
    # Classic Pantone Colors
    'PantoneYellow', 'PantoneGoldenYellow', 'PantoneOrange', 'PantoneWarmRed',
    'PantoneRed', 'PantoneRubineRed', 'PantoneRhodamineRed', 'PantoneMagenta',
    'PantoneViolet', 'PantoneBlue', 'PantoneProcessBlue', 'PantoneGreen',
    'PantoneBlack', 'PantoneCoolGray1', 'PantoneCoolGray5', 'PantoneCoolGray10',
    # Pantone Plus Colors
    'PantonePlusYellow', 'PantonePlusOrange021', 'PantonePlusWarmRed',
    'PantonePlusRed', 'PantonePlusPink', 'PantonePlusRhodamineRed',
    'PantonePlusPurple', 'PantonePlusViolet', 'PantonePlusBlue072',
    'PantonePlusProcessBlue', 'PantonePlusGreen', 'PantonePlusBlack',
    # Pantone Metallics
    'PantoneMetallicGold', 'PantoneMetallicSilver',
    # Pantone Skintone
    'PantoneSkintoneLight', 'PantoneSkintoneMedium', 'PantoneSkintoneDark',
    # Pantone Fashion Colors
    'PantoneFashionLilac', 'PantoneFashionBlue', 'PantoneFashionFuchsia',
    'PantoneFashionEmerald', 'PantoneFashionTangerine',
]
