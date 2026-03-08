# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Thingery Foods
	description: >
		Complete food database - fruits, vegetables, proteins, grains, dairy, beverages
		Data loaded from foods.yaml for easy updates.
	version: 0.1.0.0.0
	authority: filesystem
	security: seclvl2
	<(WT)>: -32
"""
# -*- coding: utf-8 -*
from typing import Any, Dict, List, Optional

from thingery._loader import load_yaml
from thingery.models import Food


# ============================================================================
# Data Loading
# ============================================================================


def _load_foods() -> Dict[str, List[Dict]]:
    """Load all foods from YAML."""
    data = load_yaml('foods.yaml')
    return data.get('foods', {})


# ============================================================================
# Food Access Functions
# ============================================================================


def get_food(name: str) -> Optional[Dict[str, Any]]:
    """
    Get a food by name (case-insensitive).
    
    Args:
        name: Food name to search for
        
    Returns:
        Food dictionary or None if not found
    """
    foods_data = _load_foods()
    name_lower = name.lower()
    
    for category, items in foods_data.items():
        for food in items:
            if food.get('name', '').lower() == name_lower:
                return food
    
    return None


def get_food_or_raise(name: str) -> Dict[str, Any]:
    """Get food by name or raise KeyError."""
    food = get_food(name)
    if food is None:
        raise KeyError(f"Food not found: {name}")
    return food


def list_foods(category: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    List all foods, optionally filtered by category.
    
    Args:
        category: Optional category filter (fruit, vegetable, protein, etc.)
        
    Returns:
        List of food dictionaries
    """
    foods_data = _load_foods()
    
    if category is None:
        # Return all foods
        all_foods = []
        for items in foods_data.values():
            all_foods.extend(items)
        return all_foods
    
    category = category.lower()
    return foods_data.get(category, [])


def list_food_categories() -> List[str]:
    """List all food categories."""
    foods_data = _load_foods()
    return list(foods_data.keys())


def search_foods(query: str) -> List[Dict[str, Any]]:
    """
    Search foods by name.
    
    Args:
        query: Search query (case-insensitive)
        
    Returns:
        List of matching foods
    """
    all_foods = list_foods()
    query_lower = query.lower()
    results = []
    
    for food in all_foods:
        name = food.get('name', '').lower()
        if query_lower in name:
            results.append(food)
    
    return results


def get_foods_by_nutrition(property_name: str, min_value: float = None, max_value: float = None) -> List[Dict[str, Any]]:
    """
    Find foods by nutritional values.
    
    Args:
        property_name: Nutrition property (calories, protein, carbohydrates, fat, etc.)
        min_value: Minimum value (optional)
        max_value: Maximum value (optional)
        
    Returns:
        List of matching foods
    """
    all_foods = list_foods()
    results = []
    
    for food in all_foods:
        nutrition = food.get('nutrition', {})
        value = nutrition.get(property_name)
        
        if value is not None:
            if min_value is not None and value < min_value:
                continue
            if max_value is not None and value > max_value:
                continue
            results.append(food)
    
    return results


# ============================================================================
# Dataclass Factory Functions (for backward compatibility)
# ============================================================================


def create_food_dataclass(data: Dict[str, Any]) -> Food:
    """Create a Food dataclass from YAML data."""
    nutrition_data = data.get('nutrition', {})
    
    return Food(
        name=data.get('name', ''),
        category=data.get('category', 'FOOD'),
        serving_size=data.get('serving_size', 100.0),
        nutrition=nutrition_data,
        amino_acids=data.get('amino_acids'),
        fatty_acids=data.get('fatty_acids')
    )


# ============================================================================
# Backward Compatibility Exports
# ============================================================================


class _FoodProxy:
    """Lazy-loading food proxy for backward compatibility."""
    
    def __init__(self, name: str):
        self._name = name
        self._data = None
    
    def _load(self):
        if self._data is None:
            self._data = get_food_or_raise(self._name)
        return self._data
    
    def __getattr__(self, name):
        data = self._load()
        return data.get(name)
    
    def __repr__(self):
        data = self._load()
        return f"<Food: {data.get('name')}>"


def __getattr__(name):
    """Lazy-load foods for backward compatibility."""
    try:
        return _FoodProxy(name)
    except KeyError:
        raise AttributeError(f"Module has no attribute '{name}'")


__all__ = [
    'get_food',
    'get_food_or_raise',
    'list_foods',
    'list_food_categories',
    'search_foods',
    'get_foods_by_nutrition',
    'create_food_dataclass',
    'Food',
]
