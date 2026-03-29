# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name:
	description: >
	version: 0.0.0.0.0.0
	authority: filesystem
	security: seclvl2
	<(WT)>: -32
"""
# -*- coding: utf-8 -*
# ======================================Standard Library Modules======================================================||
from os.path import abspath, dirname, join
import datetime as dt
import random
import inspect
# ======================================3rd Party Library Modules=====================================================||

# ======================================Solutions Brewer Library Modules==============================================||
from condor import condor
from ogma.logma import Logma

# ====================================================================================================================||
here = join(dirname(__file__), '')  # ||
log = True
logma = Logma(__name__)

# ====================================================================================================================||
pxcfg = join(here, '_data_', '.yaml')

# ====================================================================================================================||
def _get_all_words():
    """Collect all available words from different modules."""
    words = set()
    
    # Get elements
    try:
        from thingery.elements import elements
        for name, obj in inspect.getmembers(elements):
            if inspect.isclass(obj) and hasattr(obj, '__init__') and name != 'Element':
                words.add(name)
    except (ImportError, FileNotFoundError):
        pass
            
    # Get foods
    try:
        from thingery.food import foods
        food_list = foods.list_foods()
        for food in food_list:
            if isinstance(food, dict) and 'name' in food:
                words.add(food['name'])
    except (ImportError, FileNotFoundError):
        pass
            
    # Get materials
    try:
        from thingery.materials import materials
        material_list = materials.list_materials()
        for mat in material_list:
            if isinstance(mat, dict) and 'name' in mat:
                words.add(mat['name'])
    except (ImportError, FileNotFoundError):
        pass

    # Get pantone colors
    try:
        from thingery import pantone
        for name, obj in inspect.getmembers(pantone):
            if inspect.isclass(obj) and name.startswith('Pantone'):
                words.add(name)
    except (ImportError, FileNotFoundError):
        pass
            
    return sorted(list(words))

def random_name_generator(words=2):
    """
    Generates a random name consisting of a specified number of words.
    
    Args:
        words (int): Number of words to include in the generated name.
        
    Returns:
        str: A space-separated string of random words in Title Case.
    """
    all_words = _get_all_words()
    
    # Fallback words if no data could be loaded
    if not all_words:
        all_words = ["Thing", "Object", "Item", "Element", "Component", "Device", "Artifact", "Entity"]
        
    selected = [random.choice(all_words) for _ in range(words)]
    return " ".join(word.title() for word in selected)
    

# ====================================================================================================================||

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
