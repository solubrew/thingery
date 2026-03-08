# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Thingery Colors
	description: >
		Complete color database with web colors, natural colors, and paint colors
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


# ===========================WEB COLORS===============================================================================||
# ====================================================================================================================||

# Reds
@dataclass
class Red:
    name: str = "Red"
    hex_code: str = "#FF0000"
    rgb: Tuple[int, int, int] = (255, 0, 0)
    category: str = "web"


@dataclass
class Maroon:
    name: str = "Maroon"
    hex_code: str = "#800000"
    rgb: Tuple[int, int, int] = (128, 0, 0)
    category: str = "web"


@dataclass
class Crimson:
    name: str = "Crimson"
    hex_code: str = "#DC143C"
    rgb: Tuple[int, int, int] = (220, 20, 60)
    category: str = "web"


@dataclass
class Coral:
    name: str = "Coral"
    hex_code: str = "#FF7F50"
    rgb: Tuple[int, int, int] = (255, 127, 80)
    category: str = "web"


@dataclass
class Tomato:
    name: str = "Tomato"
    hex_code: str = "#FF6347"
    rgb: Tuple[int, int, int] = (255, 99, 71)
    category: str = "web"


@dataclass
class FireBrick:
    name: str = "FireBrick"
    hex_code: str = "#B22222"
    rgb: Tuple[int, int, int] = (178, 34, 34)
    category: str = "web"


# Oranges & Yellows
@dataclass
class Orange:
    name: str = "Orange"
    hex_code: str = "#FFA500"
    rgb: Tuple[int, int, int] = (255, 165, 0)
    category: str = "web"


@dataclass
class DarkOrange:
    name: str = "DarkOrange"
    hex_code: str = "#FF8C00"
    rgb: Tuple[int, int, int] = (255, 140, 0)
    category: str = "web"


@dataclass
class Yellow:
    name: str = "Yellow"
    hex_code: str = "#FFFF00"
    rgb: Tuple[int, int, int] = (255, 255, 0)
    category: str = "web"


@dataclass
class Gold:
    name: str = "Gold"
    hex_code: str = "#FFD700"
    rgb: Tuple[int, int, int] = (255, 215, 0)
    category: str = "web"


@dataclass
class LemonChiffon:
    name: str = "LemonChiffon"
    hex_code: str = "#FFFACD"
    rgb: Tuple[int, int, int] = (255, 250, 205)
    category: str = "web"


# Greens
@dataclass
class Green:
    name: str = "Green"
    hex_code: str = "#008000"
    rgb: Tuple[int, int, int] = (0, 128, 0)
    category: str = "web"


@dataclass
class Lime:
    name: str = "Lime"
    hex_code: str = "#00FF00"
    rgb: Tuple[int, int, int] = (0, 255, 0)
    category: str = "web"


@dataclass
class ForestGreen:
    name: str = "ForestGreen"
    hex_code: str = "#228B22"
    rgb: Tuple[int, int, int] = (34, 139, 34)
    category: str = "web"


@dataclass
class SeaGreen:
    name: str = "SeaGreen"
    hex_code: str = "#2E8B57"
    rgb: Tuple[int, int, int] = (46, 139, 87)
    category: str = "web"


@dataclass
class Olive:
    name: str = "Olive"
    hex_code: str = "#808000"
    rgb: Tuple[int, int, int] = (128, 128, 0)
    category: str = "web"


@dataclass
class DarkGreen:
    name: str = "DarkGreen"
    hex_code: str = "#006400"
    rgb: Tuple[int, int, int] = (0, 100, 0)
    category: str = "web"


@dataclass
class LawnGreen:
    name: str = "LawnGreen"
    hex_code: str = "#7CFC00"
    rgb: Tuple[int, int, int] = (124, 252, 0)
    category: str = "web"


# Blues
@dataclass
class Blue:
    name: str = "Blue"
    hex_code: str = "#0000FF"
    rgb: Tuple[int, int, int] = (0, 0, 255)
    category: str = "web"


@dataclass
class Navy:
    name: str = "Navy"
    hex_code: str = "#000080"
    rgb: Tuple[int, int, int] = (0, 0, 128)
    category: str = "web"


@dataclass
class RoyalBlue:
    name: str = "RoyalBlue"
    hex_code: str = "#4169E1"
    rgb: Tuple[int, int, int] = (65, 105, 225)
    category: str = "web"


@dataclass
class SkyBlue:
    name: str = "SkyBlue"
    hex_code: str = "#87CEEB"
    rgb: Tuple[int, int, int] = (135, 206, 235)
    category: str = "web"


@dataclass
class Cyan:
    name: str = "Cyan"
    hex_code: str = "#00FFFF"
    rgb: Tuple[int, int, int] = (0, 255, 255)
    category: str = "web"


@dataclass
class Teal:
    name: str = "Teal"
    hex_code: str = "#008080"
    rgb: Tuple[int, int, int] = (0, 128, 128)
    category: str = "web"


@dataclass
class DodgerBlue:
    name: str = "DodgerBlue"
    hex_code: str = "#1E90FF"
    rgb: Tuple[int, int, int] = (30, 144, 255)
    category: str = "web"


@dataclass
class SteelBlue:
    name: str = "SteelBlue"
    hex_code: str = "#4682B4"
    rgb: Tuple[int, int, int] = (70, 130, 180)
    category: str = "web"


# Purples & Pinks
@dataclass
class Purple:
    name: str = "Purple"
    hex_code: str = "#800080"
    rgb: Tuple[int, int, int] = (128, 0, 128)
    category: str = "web"


@dataclass
class Violet:
    name: str = "Violet"
    hex_code: str = "#EE82EE"
    rgb: Tuple[int, int, int] = (238, 130, 238)
    category: str = "web"


@dataclass
class Indigo:
    name: str = "Indigo"
    hex_code: str = "#4B0082"
    rgb: Tuple[int, int, int] = (75, 0, 130)
    category: str = "web"


@dataclass
class Magenta:
    name: str = "Magenta"
    hex_code: str = "#FF00FF"
    rgb: Tuple[int, int, int] = (255, 0, 255)
    category: str = "web"


@dataclass
class Pink:
    name: str = "Pink"
    hex_code: str = "#FFC0CB"
    rgb: Tuple[int, int, int] = (255, 192, 203)
    category: str = "web"


@dataclass
class HotPink:
    name: str = "HotPink"
    hex_code: str = "#FF69B4"
    rgb: Tuple[int, int, int] = (255, 105, 180)
    category: str = "web"


@dataclass
class DeepPink:
    name: str = "DeepPink"
    hex_code: str = "#FF1493"
    rgb: Tuple[int, int, int] = (255, 20, 147)
    category: str = "web"


@dataclass
class Lavender:
    name: str = "Lavender"
    hex_code: str = "#E6E6FA"
    rgb: Tuple[int, int, int] = (230, 230, 250)
    category: str = "web"


# Browns
@dataclass
class Brown:
    name: str = "Brown"
    hex_code: str = "#A52A2A"
    rgb: Tuple[int, int, int] = (165, 42, 42)
    category: str = "web"


@dataclass
class SaddleBrown:
    name: str = "SaddleBrown"
    hex_code: str = "#8B4513"
    rgb: Tuple[int, int, int] = (139, 69, 19)
    category: str = "web"


@dataclass
class Sienna:
    name: str = "Sienna"
    hex_code: str = "#A0522D"
    rgb: Tuple[int, int, int] = (160, 82, 45)
    category: str = "web"


@dataclass
class Chocolate:
    name: str = "Chocolate"
    hex_code: str = "#D2691E"
    rgb: Tuple[int, int, int] = (210, 105, 30)
    category: str = "web"


@dataclass
class Peru:
    name: str = "Peru"
    hex_code: str = "#CD853F"
    rgb: Tuple[int, int, int] = (205, 133, 63)
    category: str = "web"


# Grays & Neutrals
@dataclass
class White:
    name: str = "White"
    hex_code: str = "#FFFFFF"
    rgb: Tuple[int, int, int] = (255, 255, 255)
    category: str = "web"


@dataclass
class Black:
    name: str = "Black"
    hex_code: str = "#000000"
    rgb: Tuple[int, int, int] = (0, 0, 0)
    category: str = "web"


@dataclass
class Gray:
    name: str = "Gray"
    hex_code: str = "#808080"
    rgb: Tuple[int, int, int] = (128, 128, 128)
    category: str = "web"


@dataclass
class Silver:
    name: str = "Silver"
    hex_code: str = "#C0C0C0"
    rgb: Tuple[int, int, int] = (192, 192, 192)
    category: str = "web"


@dataclass
class LightGray:
    name: str = "LightGray"
    hex_code: str = "#D3D3D3"
    rgb: Tuple[int, int, int] = (211, 211, 211)
    category: str = "web"


@dataclass
class DarkGray:
    name: str = "DarkGray"
    hex_code: str = "#A9A9A9"
    rgb: Tuple[int, int, int] = (169, 169, 169)
    category: str = "web"


# ===========================NATURAL COLORS==========================================================================||
# ====================================================================================================================||


@dataclass
class SkyBlueNatural:
    name: str = "Sky Blue"
    hex_code: str = "#87CEEB"
    rgb: Tuple[int, int, int] = (135, 206, 235)
    category: str = "natural"


@dataclass
class ForestGreenNatural:
    name: str = "Forest Green"
    hex_code: str = "#228B22"
    rgb: Tuple[int, int, int] = (34, 139, 34)
    category: str = "natural"


@dataclass
class OceanBlue:
    name: str = "Ocean Blue"
    hex_code: str = "#006994"
    rgb: Tuple[int, int, int] = (0, 105, 148)
    category: str = "natural"


@dataclass
class Sand:
    name: str = "Sand"
    hex_code: str = "#C2B280"
    rgb: Tuple[int, int, int] = (194, 178, 128)
    category: str = "natural"


@dataclass
class EarthBrown:
    name: str = "Earth Brown"
    hex_code: str = "#8B4513"
    rgb: Tuple[int, int, int] = (139, 69, 19)
    category: str = "natural"


@dataclass
class LeafGreen:
    name: str = "Leaf Green"
    hex_code: str = "#4CAF50"
    rgb: Tuple[int, int, int] = (76, 175, 80)
    category: str = "natural"


@dataclass
class SunsetOrange:
    name: str = "Sunset Orange"
    hex_code: str = "#FD5E53"
    rgb: Tuple[int, int, int] = (253, 94, 83)
    category: str = "natural"


@dataclass
class RosePink:
    name: str = "Rose Pink"
    hex_code: str = "#FF006E"
    rgb: Tuple[int, int, int] = (255, 0, 110)
    category: str = "natural"


@dataclass
class LavenderNatural:
    name: str = "Lavender"
    hex_code: str = "#E6E6FA"
    rgb: Tuple[int, int, int] = (230, 230, 250)
    category: str = "natural"


@dataclass
class MintGreen:
    name: str = "Mint Green"
    hex_code: str = "#98FF98"
    rgb: Tuple[int, int, int] = (152, 255, 152)
    category: str = "natural"


# ===========================PAINT COLORS=============================================================================||
# ====================================================================================================================||


@dataclass
class CadmiumYellow:
    name: str = "Cadmium Yellow"
    hex_code: str = "#FFE600"
    rgb: Tuple[int, int, int] = (255, 230, 0)
    category: str = "paint"


@dataclass
class CadmiumRed:
    name: str = "Cadmium Red"
    hex_code: str = "#E30022"
    rgb: Tuple[int, int, int] = (227, 0, 34)
    category: str = "paint"


@dataclass
class CobaltBlue:
    name: str = "Cobalt Blue"
    hex_code: str = "#0047AB"
    rgb: Tuple[int, int, int] = (0, 71, 171)
    category: str = "paint"


@dataclass
class TitaniumWhite:
    name: str = "Titanium White"
    hex_code: str = "#FFFFFF"
    rgb: Tuple[int, int, int] = (255, 255, 255)
    category: str = "paint"


@dataclass
class IvoryBlack:
    name: str = "Ivory Black"
    hex_code: str = "#0D0D0D"
    rgb: Tuple[int, int, int] = (13, 13, 13)
    category: str = "paint"


@dataclass
class Viridian:
    name: str = "Viridian"
    hex_code: str = "#40826D"
    rgb: Tuple[int, int, int] = (64, 130, 109)
    category: str = "paint"


@dataclass
class RawUmber:
    name: str = "Raw Umber"
    hex_code: str = "#6A4C13"
    rgb: Tuple[int, int, int] = (106, 76, 19)
    category: str = "paint"


@dataclass
class BurntSienna:
    name: str = "Burnt Sienna"
    hex_code: str = "#E97451"
    rgb: Tuple[int, int, int] = (233, 116, 81)
    category: str = "paint"


@dataclass
class Ultramarine:
    name: str = "Ultramarine"
    hex_code: str = "#120A8F"
    rgb: Tuple[int, int, int] = (18, 10, 143)
    category: str = "paint"


@dataclass
class PhthaloBlue:
    name: str = "Phthalo Blue"
    hex_code: str = "#000F89"
    rgb: Tuple[int, int, int] = (0, 15, 137)
    category: str = "paint"


# ===========================EXPORTS===================================================================================||
# ====================================================================================================================||


__all__ = [
    # Web Colors - Reds
    'Red', 'Maroon', 'Crimson', 'Coral', 'Tomato', 'FireBrick',
    # Web Colors - Oranges & Yellows
    'Orange', 'DarkOrange', 'Yellow', 'Gold', 'LemonChiffon',
    # Web Colors - Greens
    'Green', 'Lime', 'ForestGreen', 'SeaGreen', 'Olive', 'DarkGreen', 'LawnGreen',
    # Web Colors - Blues
    'Blue', 'Navy', 'RoyalBlue', 'SkyBlue', 'Cyan', 'Teal', 'DodgerBlue', 'SteelBlue',
    # Web Colors - Purples & Pinks
    'Purple', 'Violet', 'Indigo', 'Magenta', 'Pink', 'HotPink', 'DeepPink', 'Lavender',
    # Web Colors - Browns
    'Brown', 'SaddleBrown', 'Sienna', 'Chocolate', 'Peru',
    # Web Colors - Grays & Neutrals
    'White', 'Black', 'Gray', 'Silver', 'LightGray', 'DarkGray',
    # Natural Colors
    'SkyBlueNatural', 'ForestGreenNatural', 'OceanBlue', 'Sand', 'EarthBrown',
    'LeafGreen', 'SunsetOrange', 'RosePink', 'LavenderNatural', 'MintGreen',
    # Paint Colors
    'CadmiumYellow', 'CadmiumRed', 'CobaltBlue', 'TitaniumWhite', 'IvoryBlack',
    'Viridian', 'RawUmber', 'BurntSienna', 'Ultramarine', 'PhthaloBlue',
]
