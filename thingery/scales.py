# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Thingery Scales
	description: >
		Complete measurement scales database - temperature, pressure, length, mass, electrical, radiation.
		Data loaded from scales.yaml for easy updates.
	version: 0.0.0.0.0.0
	authority: filesystem
	security: seclvl2
	<(WT)>: -32
"""
# -*- coding: utf-8 -*
from typing import Any, Dict, List, Optional

from thingery._loader import load_yaml


# ============================================================================
# Data Loading
# ============================================================================


def _load_scales() -> Dict[str, List[Dict]]:
    """Load all scales from YAML."""
    data = load_yaml('scales.yaml')
    return data.get('scales', {})


_SCALES_DATA: Dict[str, List[Dict]] = _load_scales()


# ============================================================================
# Access Functions
# ============================================================================


def get_scale(name: str) -> Optional[Dict]:
    """Get a scale by name from any category."""
    for scales in _SCALES_DATA.values():
        for s in scales:
            if s.get('name', '').lower() == name.lower():
                return s
    return None


def get_scales_by_category(category: str) -> List[Dict]:
    """Get all scales in a category."""
    return _SCALES_DATA.get(category, [])


def list_categories() -> List[str]:
    """List all scale categories."""
    return list(_SCALES_DATA.keys())


def list_scales(category: Optional[str] = None) -> List[str]:
    """List all scale names."""
    if category:
        return [s['name'] for s in _SCALES_DATA.get(category, [])]
    result = []
    for scales in _SCALES_DATA.values():
        result.extend([s['name'] for s in scales])
    return result


# ============================================================================
# Backward Compatible Class-like Access via __getattr__
# ============================================================================


class _ScaleAccessor:
    """Provides class-like access to scale data."""
    
    _scales = _SCALES_DATA
    
    def __getattr__(self, name: str) -> Any:
        # Try to find a scale with this name
        for scales in self._scales.values():
            for s in scales:
                # Create class name from scale name
                class_name = s['name'].replace(' ', '').replace('/', '').replace('-', '')
                if class_name == name:
                    # Return a namespace with the scale's properties
                    return _ScaleProperties(s)
        raise AttributeError(f"module has no scale '{name}'")


class _ScaleProperties:
    """Provides property access to scale data."""
    
    def __init__(self, data: Dict):
        self._data = data
    
    def __getattr__(self, name: str) -> Any:
        if name in self._data:
            return self._data[name]
        # Handle conversion_X -> conversion_to_X
        if name.startswith('conversion_'):
            return self._data.get(f'conversion_to_{name.split("_", 1)[1]}')
        raise AttributeError(f"scale has no attribute '{name}'")
    
    def __repr__(self):
        return f"<Scale: {self._data.get('name', 'unknown')}>"


# Singleton accessor for backward compatibility
_Scale = _ScaleAccessor()


# ============================================================================
# Define commonly used scales as module-level accessors
# ============================================================================


def __getattr__(name: str) -> Any:
    """Module-level attribute access for backward compatibility."""
    return getattr(_Scale, name)


# ============================================================================
# Exports
# ============================================================================


__all__ = [
    'get_scale', 'get_scales_by_category', 'list_categories', 'list_scales',
]
