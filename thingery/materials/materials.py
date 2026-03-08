# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Thingery Materials
	description: >
		Complete materials database - metals, alloys, polymers, ceramics, semiconductors
		Data loaded from materials.yaml for easy updates.
	version: 0.1.0.0.0
	authority: filesystem
	security: seclvl2
	<(WT)>: -32
"""
# -*- coding: utf-8 -*
from typing import Any, Dict, List, Optional

from thingery._loader import load_yaml
from thingery.models import Material, MaterialCategory


# ============================================================================
# Data Loading
# ============================================================================


def _load_materials() -> Dict[str, List[Dict]]:
    """Load all materials from YAML."""
    data = load_yaml('materials.yaml')
    return data.get('materials', {})


# ============================================================================
# Material Access Functions
# ============================================================================


def get_material(name: str) -> Optional[Dict[str, Any]]:
    """
    Get a material by name (case-insensitive).
    
    Args:
        name: Material name to search for
        
    Returns:
        Material dictionary or None if not found
    """
    materials_data = _load_materials()
    name_lower = name.lower()
    
    for category, items in materials_data.items():
        for material in items:
            if material.get('name', '').lower() == name_lower:
                return material
    
    return None


def get_material_or_raise(name: str) -> Dict[str, Any]:
    """Get material by name or raise KeyError."""
    material = get_material(name)
    if material is None:
        raise KeyError(f"Material not found: {name}")
    return material


def list_materials(category: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    List all materials, optionally filtered by category.
    
    Args:
        category: Optional category filter (metal, alloy, polymer, etc.)
        
    Returns:
        List of material dictionaries
    """
    materials_data = _load_materials()
    
    if category is None:
        # Return all materials
        all_materials = []
        for items in materials_data.values():
            all_materials.extend(items)
        return all_materials
    
    category = category.lower()
    return materials_data.get(category, [])


def list_categories() -> List[str]:
    """List all material categories."""
    materials_data = _load_materials()
    return list(materials_data.keys())


def get_materials_by_property(property_name: str, value: Any) -> List[Dict[str, Any]]:
    """
    Find materials by a specific property value.
    
    Args:
        property_name: Name of the property to search
        value: Value to match
        
    Returns:
        List of matching materials
    """
    all_materials = list_materials()
    results = []
    
    for material in all_materials:
        props = material.get('properties', {})
        if material.get(property_name) == value or props.get(property_name) == value:
            results.append(material)
    
    return results


def search_materials(query: str) -> List[Dict[str, Any]]:
    """
    Search materials by name or formula.
    
    Args:
        query: Search query (case-insensitive)
        
    Returns:
        List of matching materials
    """
    all_materials = list_materials()
    query_lower = query.lower()
    results = []
    
    for material in all_materials:
        name = material.get('name', '').lower()
        formula = material.get('formula', '').lower()
        
        if query_lower in name or query_lower in formula:
            results.append(material)
    
    return results


# ============================================================================
# Dataclass Factory Functions (for backward compatibility)
# ============================================================================


def create_material_dataclass(data: Dict[str, Any]) -> Material:
    """Create a Material dataclass from YAML data."""
    return Material(
        name=data.get('name', ''),
        formula=data.get('formula'),
        category=data.get('category', 'MATERIAL'),
        density=data.get('density', 0.0),
        melting_point=data.get('melting_point'),
        boiling_point=data.get('boiling_point'),
        hardness=data.get('hardness'),
        tensile_strength=data.get('tensile_strength'),
        thermal_conductivity=data.get('thermal_conductivity'),
        electrical_resistivity=data.get('electrical_resistivity'),
        properties=data.get('properties', {})
    )


# ============================================================================
# Backward Compatibility Exports
# ============================================================================


# For backward compatibility, provide class-like access
# These wrap the YAML data in dataclass form on demand
class _MaterialProxy:
    """Lazy-loading material proxy for backward compatibility."""
    
    def __init__(self, name: str):
        self._name = name
        self._data = None
    
    def _load(self):
        if self._data is None:
            self._data = get_material_or_raise(self._name)
        return self._data
    
    def __getattr__(self, name):
        data = self._load()
        return data.get(name)
    
    def __repr__(self):
        data = self._load()
        return f"<Material: {data.get('name')}>"


# Create module-level exports for backward compatibility
def __getattr__(name):
    """Lazy-load materials for backward compatibility."""
    try:
        return _MaterialProxy(name)
    except KeyError:
        raise AttributeError(f"Module has no attribute '{name}'")


__all__ = [
    'get_material',
    'get_material_or_raise', 
    'list_materials',
    'list_categories',
    'get_materials_by_property',
    'search_materials',
    'create_material_dataclass',
    'Material',
]
