# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Thingery Materials
	description: >
		Materials module - metals, alloys, polymers, ceramics, semiconductors
	version: 0.1.0.0.0
	authority: filesystem
	security: seclvl2
	<(WT)>: -32
"""
# -*- coding: utf-8 -*
# Re-export from materials.py for backward compatibility
from thingery.materials.materials import (
	get_material,
	get_material_or_raise,
	list_materials,
	list_categories,
	get_materials_by_property,
	search_materials,
	create_material_dataclass,
	Material,
)

# Also expose common materials directly for convenience
# These use lazy loading via __getattr__
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
