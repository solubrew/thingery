# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Thingery Protocols
	description: >
		Laboratory and measurement protocols.
		Data loaded from protocols.yaml for easy updates.
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


def _load_protocols() -> Dict[str, List[Dict]]:
    """Load all protocols from YAML."""
    data = load_yaml('protocols.yaml')
    return data.get('protocols', {})


_PROTOCOLS_DATA: Dict[str, List[Dict]] = _load_protocols()


# ============================================================================
# Access Functions
# ============================================================================


def get_protocol(name: str) -> Optional[Dict]:
    """Get a protocol by name from any category."""
    for protocols in _PROTOCOLS_DATA.values():
        for p in protocols:
            if p.get('name', '').lower() == name.lower():
                return p
    return None


def get_protocols_by_category(category: str) -> List[Dict]:
    """Get all protocols in a category."""
    return _PROTOCOLS_DATA.get(category, [])


def list_categories() -> List[str]:
    """List all protocol categories."""
    return list(_PROTOCOLS_DATA.keys())


def list_protocols(category: Optional[str] = None) -> List[str]:
    """List all protocol names."""
    if category:
        return [p['name'] for p in _PROTOCOLS_DATA.get(category, [])]
    result = []
    for protocols in _PROTOCOLS_DATA.values():
        result.extend([p['name'] for p in protocols])
    return result


# ============================================================================
# Protocol Dataclass for type safety
# ============================================================================


class Protocol:
    """Represents a laboratory or measurement protocol."""
    
    def __init__(self, data: Dict):
        self.name = data.get('name', '')
        self.category = data.get('category', '')
        self.description = data.get('description', '')
        self.steps = data.get('steps', [])
        self.equipment = data.get('equipment', [])
        self.safety_notes = data.get('safety_notes', [])
        self.duration = data.get('duration', '')
    
    def __repr__(self):
        return f"<Protocol: {self.name} ({self.category})>"
    
    def to_dict(self) -> Dict:
        return {
            'name': self.name,
            'category': self.category,
            'description': self.description,
            'steps': self.steps,
            'equipment': self.equipment,
            'safety_notes': self.safety_notes,
            'duration': self.duration,
        }


def get_Protocol(name: str) -> Optional[Protocol]:
    """Get a Protocol object by name."""
    data = get_protocol(name)
    return Protocol(data) if data else None


# ============================================================================
# Backward Compatibility
# ============================================================================


class _ProtocolAccessor:
    """Provides class-like access to protocol data."""
    
    def __getattr__(self, name: str) -> Protocol:
        data = get_protocol(name)
        if data:
            return Protocol(data)
        raise AttributeError(f"module has no protocol '{name}'")


_Protocol = _ProtocolAccessor()


def __getattr__(name: str):
    """Module-level attribute access for backward compatibility."""
    return getattr(_Protocol, name)


# ============================================================================
# Exports
# ============================================================================


__all__ = [
    'Protocol', 'get_protocol', 'get_Protocol', 'get_protocols_by_category',
    'list_categories', 'list_protocols',
]
