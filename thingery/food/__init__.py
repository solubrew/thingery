# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Thingery Foods
	description: >
		Foods module - fruits, vegetables, meats, grains, dairy, beverages
	version: 0.1.0.0.0
	authority: filesystem
	security: seclvl2
	<(WT)>: -32
"""
# -*- coding: utf-8 -*
# Re-export from foods.py for backward compatibility
from thingery.food.foods import (
	get_food,
	get_food_or_raise,
	list_foods,
	list_categories,
	get_foods_by_category,
	search_foods,
	create_food_dataclass,
	Food,
)

__all__ = [
	'get_food',
	'get_food_or_raise',
	'list_foods',
	'list_categories',
	'get_foods_by_category',
	'search_foods',
	'create_food_dataclass',
	'Food',
]
