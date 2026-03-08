# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Food Module
	description: >
		Food data models and implementations
	version: 0.0.0.0.0.0
	authority: filesystem
	security: seclvl2
	<(WT)>: -32
"""
# -*- coding: utf-8 -*
# ======================================Standard Library Modules======================================================||
from dataclasses import dataclass
# ======================================3rd Party Library Modules=====================================================||
# ======================================Solutions Brewer Library Modules=============================================||
from thingery.models import Food, NutritionInfo, FoodCategory

# ====================================================================================================================||

# Fruits
Apple = Food(
	name="Apple",
	category=FoodCategory.FRUIT.value,
	nutrition=NutritionInfo(
		calories=52,
		protein=0.3,
		carbohydrates=14,
		fat=0.2,
		fiber=2.4,
		sugar=10,
		sodium=1,
		vitamin_a=54,
		vitamin_c=4.6,
		calcium=6,
		iron=0.12,
		potassium=107,
	),
	description="A sweet, edible fruit produced by an apple tree.",
)

Banana = Food(
	name="Banana",
	category=FoodCategory.FRUIT.value,
	nutrition=NutritionInfo(
		calories=89,
		protein=1.1,
		carbohydrates=23,
		fat=0.3,
		fiber=2.6,
		sugar=12,
		sodium=1,
		vitamin_a=64,
		vitamin_c=8.7,
		calcium=5,
		iron=0.26,
		potassium=358,
	),
	description="A long, curved fruit with yellow skin.",
)

Orange = Food(
	name="Orange",
	category=FoodCategory.FRUIT.value,
	nutrition=NutritionInfo(
		calories=47,
		protein=0.9,
		carbohydrates=12,
		fat=0.1,
		fiber=2.4,
		sugar=9,
		sodium=0,
		vitamin_a=225,
		vitamin_c=53,
		calcium=40,
		iron=0.1,
		potassium=181,
	),
	description="A round, orange-colored citrus fruit.",
)

# Proteins
Beef = Food(
	name="Beef",
	category=FoodCategory.PROTEIN.value,
	nutrition=NutritionInfo(
		calories=250,
		protein=26,
		carbohydrates=0,
		fat=15,
		fiber=0,
		sugar=0,
		sodium=72,
		cholesterol=90,
		vitamin_a=0,
		vitamin_c=0,
		calcium=18,
		iron=2.6,
		potassium=318,
	),
	is_raw=False,
	description="The meat of cattle.",
)

Pork = Food(
	name="Pork",
	category=FoodCategory.PROTEIN.value,
	nutrition=NutritionInfo(
		calories=242,
		protein=27,
		carbohydrates=0,
		fat=14,
		fiber=0,
		sugar=0,
		sodium=62,
		cholesterol=80,
		vitamin_a=7,
		vitamin_c=0.6,
		calcium=19,
		iron=1.0,
		potassium=356,
	),
	is_raw=False,
	description="The meat of domestic pigs.",
)

Chicken = Food(
	name="Chicken",
	category=FoodCategory.PROTEIN.value,
	nutrition=NutritionInfo(
		calories=239,
		protein=27,
		carbohydrates=0,
		fat=14,
		fiber=0,
		sugar=0,
		sodium=74,
		cholesterol=85,
		vitamin_a=68,
		vitamin_c=0,
		calcium=15,
		iron=1.0,
		potassium=256,
	),
	is_raw=False,
	description="The meat of chickens.",
)

Eggs = Food(
	name="Eggs",
	category=FoodCategory.PROTEIN.value,
	nutrition=NutritionInfo(
		calories=155,
		protein=13,
		carbohydrates=1.1,
		fat=11,
		fiber=0,
		sugar=1.1,
		sodium=124,
		cholesterol=373,
		vitamin_a=520,
		vitamin_c=0,
		calcium=50,
		iron=1.2,
		potassium=126,
	),
	description="An egg laid by female birds, typically chicken.",
)

# Grains
Rice = Food(
	name="Rice",
	category=FoodCategory.GRAIN.value,
	nutrition=NutritionInfo(
		calories=130,
		protein=2.7,
		carbohydrates=28,
		fat=0.3,
		fiber=0.4,
		sugar=0,
		sodium=1,
		cholesterol=0,
		vitamin_a=0,
		vitamin_c=0,
		calcium=10,
		iron=0.2,
		potassium=35,
	),
	is_raw=False,
	description="The edible seed of the rice plant.",
)

Wheat = Food(
	name="Wheat",
	category=FoodCategory.GRAIN.value,
	nutrition=NutritionInfo(
		protein=13,
		carbohydrates=71,
		fat=2.5,
		fiber=10,
		sugar=0.3,
		sodium=2,
		calcium=34,
		iron=3.6,
		potassium=363,
	),
	description="A cereal grain, a member of the grass family.",
)

Bread = Food(
	name="Bread",
	category=FoodCategory.GRAIN.value,
	nutrition=NutritionInfo(
		calories=265,
		protein=9,
		carbohydrates=49,
		fat=3.2,
		fiber=2.7,
		sugar=5,
		sodium=491,
		cholesterol=0,
		vitamin_a=0,
		vitamin_c=0,
		calcium=260,
		iron=3.6,
		potassium=117,
	),
	is_raw=False,
	description="A staple food made from flour and water.",
)

# Dairy
Milk = Food(
	name="Milk",
	category=FoodCategory.DAIRY.value,
	nutrition=NutritionInfo(
		calories=42,
		protein=3.4,
		carbohydrates=5,
		fat=1,
		fiber=0,
		sugar=5,
		sodium=44,
		cholesterol=5,
		vitamin_a=162,
		vitamin_c=0,
		calcium=125,
		iron=0.03,
		potassium=132,
	),
	description="A nutrient-rich liquid produced by mammals.",
)

# Condiments & Other
Sugar = Food(
	name="Sugar",
	category=FoodCategory.CONDIMENT.value,
	nutrition=NutritionInfo(
		calories=387,
		protein=0,
		carbohydrates=100,
		fat=0,
		fiber=0,
		sugar=100,
		sodium=1,
		calcium=1,
		iron=0.1,
		potassium=2,
	),
	description="A sweet crystalline substance obtained from various plants.",
)

Almonds = Food(
	name="Almonds",
	category=FoodCategory.PROTEIN.value,
	nutrition=NutritionInfo(
		calories=579,
		protein=21,
		carbohydrates=22,
		fat=50,
		fiber=12,
		sugar=4.4,
		sodium=1,
		cholesterol=0,
		vitamin_a=2,
		vitamin_c=0,
		calcium=269,
		iron=3.7,
		potassium=733,
	),
	description="An edible seed of the almond tree.",
)

OrangeJuice = Food(
	name="Orange Juice",
	category=FoodCategory.BEVERAGE.value,
	nutrition=NutritionInfo(
		calories=45,
		protein=0.7,
		carbohydrates=10,
		fat=0.2,
		fiber=0.2,
		sugar=8,
		sodium=1,
		cholesterol=0,
		vitamin_a=200,
		vitamin_c=50,
		calcium=11,
		iron=0.2,
		potassium=200,
	),
	description="A liquid extract of the orange tree fruit.",
)

# Export all foods
__all__ = [
	'Apple', 'Banana', 'Orange',
	'Beef', 'Pork', 'Chicken', 'Eggs',
	'Rice', 'Wheat', 'Bread',
	'Milk', 'Sugar', 'Almonds', 'OrangeJuice',
]
