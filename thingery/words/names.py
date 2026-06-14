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
from kahndor import kahndor
from kahndor.logma import Logma

# ====================================================================================================================||
here = join(dirname(__file__), "")  # ||
log = True
logma = Logma(__name__)

# ====================================================================================================================||
pxcfg = join(here, "_data_", ".yaml")


# ====================================================================================================================||
def _get_all_words():
    """Collect all available words from different modules."""
    words = set()

    # Get elements
    try:
        from thingery.elements import elements

        for name, obj in inspect.getmembers(elements):
            if inspect.isclass(obj) and hasattr(obj, "__init__") and name != "Element":
                words.add(name)
    except (ImportError, FileNotFoundError):
        pass

    # Get foods
    try:
        from thingery.food import foods

        food_list = foods.list_foods()
        for food in food_list:
            if isinstance(food, dict) and "name" in food:
                words.add(food["name"])
    except (ImportError, FileNotFoundError):
        pass

    # Get materials
    try:
        from thingery.materials import materials

        material_list = materials.list_materials()
        for mat in material_list:
            if isinstance(mat, dict) and "name" in mat:
                words.add(mat["name"])
    except (ImportError, FileNotFoundError):
        pass

    # Get pantone colors
    try:
        from thingery.materials import pantone

        for name, obj in inspect.getmembers(pantone):
            if inspect.isclass(obj) and name.startswith("Pantone"):
                words.add(name)
    except (ImportError, FileNotFoundError):
        pass

    return sorted(list(words))


def random_name_generator(words=2, max_letters=None, min_letters=None):
    """
    Generates a random name consisting of a specified number of words.

    Args:
        words (int): Number of words to include in the generated name.

    Returns:
        str: A space-separated string of random words in Title Case.
    """
    all_words = _get_all_words()
    if not all_words:
        raise ValueError("No words could be loaded from the available sources.")
    # if letters:
    # restrict to words of the specified length
    selected = [random.choice(all_words) for _ in range(words)]
    return " ".join(word.title() for word in selected)

def random_english_name_of_person():
    """
    Generates a random English name of a person."""
    names = kahndor.Instruct(join(HERE, "..", "_data_", "names.yaml")).load()
    first_names = names.get("first", [])
    last_names = names.get("last", [])
    selected = [random.choice(first_names), random.choice(last_names)]
    return f"{selected[0]} {selected[1]}"

def random_english_name_of_place():
    """
    Generates a random English name of a place."""
    all_words = _get_all_words()
    if not all_words:
        raise ValueError("No words could be loaded from the available sources.")
    selected = [random.choice(all_words) for _ in range(2)]
    return " ".join(word.title() for word in selected)


# ====================================================================================================================||

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
