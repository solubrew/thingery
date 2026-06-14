# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Thingery Colors
	description: >
		Complete color database with web colors, natural colors, and paint colors.
		Data loaded from colors.yaml for easy updates.
	version: 0.0.0.0.0.0
	authority: filesystem
	security: seclvl2
	<(WT)>: -32
"""
# -*- coding: utf-8 -*
from typing import Any, Dict, List, Optional, Tuple

from thingery._loader import load_yaml


# ============================================================================
# Data Loading
# ============================================================================


def _load_colors() -> Dict[str, Any]:
    """Load all colors from YAML."""
    data = load_yaml('colors.yaml')
    return data.get('colors', {})


_COLORS_DATA: Dict[str, Any] = _load_colors()


# ============================================================================
# Access Functions
# ============================================================================


def get_color(name: str) -> Optional[Dict]:
    """Get a color by name from any category."""
    # Check web colors
    for subcategory, colors in _COLORS_DATA.get('web', {}).items():
        for c in colors:
            if c.get('name', '').lower() == name.lower():
                return c
    
    # Check natural colors
    for c in _COLORS_DATA.get('natural', []):
        if c.get('name', '').lower() == name.lower():
            return c
    
    # Check paint colors
    for c in _COLORS_DATA.get('paint', []):
        if c.get('name', '').lower() == name.lower():
            return c
    
    return None


def get_colors_by_category(category: str) -> List[Dict]:
    """Get all colors in a category."""
    if category == 'web':
        # Web colors are nested by subcategory
        result = []
        for subcategory in _COLORS_DATA.get('web', {}).values():
            result.extend(subcategory)
        return result
    return _COLORS_DATA.get(category, [])


def list_categories() -> List[str]:
    """List all color categories."""
    return list(_COLORS_DATA.keys())


def list_colors(category: Optional[str] = None) -> List[str]:
    """List all color names."""
    if category == 'web':
        result = []
        for subcategory in _COLORS_DATA.get('web', {}).values():
            result.extend([c['name'] for c in subcategory])
        return result
    if category:
        return [c['name'] for c in _COLORS_DATA.get(category, [])]
    
    # All colors
    result = list_colors('web')
    result.extend([c['name'] for c in _COLORS_DATA.get('natural', [])])
    result.extend([c['name'] for c in _COLORS_DATA.get('paint', [])])
    return result


# ============================================================================
# Dataclass-like Color class for backward compatibility
# ============================================================================


class Color:
    """Represents a color with name, hex, rgb, and category."""
    
    def __init__(self, data: Dict):
        self.name = data.get('name', '')
        self.hex_code = data.get('hex_code', '')
        self.rgb = tuple(data.get('rgb', [0, 0, 0]))
        self.category = data.get('category', '')
    
    def __repr__(self):
        return f"<Color: {self.name} ({self.hex_code})>"
    
    def to_dict(self) -> Dict:
        return {
            'name': self.name,
            'hex_code': self.hex_code,
            'rgb': self.rgb,
            'category': self.category,
        }


def get_Color(name: str) -> Optional[Color]:
    """Get a Color object by name."""
    data = get_color(name)
    return Color(data) if data else None


# ============================================================================
# Backward Compatibility
# ============================================================================


# For backward compatibility, provide a way to access colors like:
# from thingery.colors import Red
# red = Red()

class _ColorAccessor:
    """Provides class-like access to color data."""
    
    def __getattr__(self, name: str) -> Color:
        data = get_color(name)
        if data:
            return Color(data)
        raise AttributeError(f"module has no color '{name}'")


_Color = _ColorAccessor()


def __getattr__(name: str):
    """Module-level attribute access for backward compatibility."""
    return getattr(_Color, name)


# Also import pantone colors


# ============================================================================
# Exports
# ============================================================================


__all__ = [
    'Color', 'get_color', 'get_Color', 'get_colors_by_category',
    'list_categories', 'list_colors',
]
