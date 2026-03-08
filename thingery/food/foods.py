# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Thingery Foods
	description: >
		Complete food database with nutritional information
	version: 0.0.0.0.0.0
	authority: filesystem
	security: seclvl2
	<(WT)>: -32
"""
# -*- coding: utf-8 -*
from dataclasses import dataclass
from typing import Dict
from thingery.models import Food, Nutrition


# ======================================Standard Library Modules======================================================||
# ======================================3rd Party Library Modules=====================================================||
# ======================================Solutions Brewer Library Modules=============================================||
# ====================================================================================================================||


# ===========================FRUITS==================================================================================||
# ====================================================================================================================||


@dataclass
class Apple(Food):
    def __init__(self):
        super().__init__(
            name="Apple",
            category="fruit",
            serving_size=182.0,
            nutrition=Nutrition(
                calories=95.0,
                protein=0.5,
                carbohydrates=25.0,
                fat=0.3,
                fiber=4.4,
                sugar=19.0,
                sodium=2.0,
                cholesterol=0.0,
                vitamins={"C": 8.4, "A": 14.0},
                minerals={"potassium": 195.0, "calcium": 11.0}
            )
        )


@dataclass
class Banana(Food):
    def __init__(self):
        super().__init__(
            name="Banana",
            category="fruit",
            serving_size=118.0,
            nutrition=Nutrition(
                calories=105.0,
                protein=1.3,
                carbohydrates=27.0,
                fat=0.4,
                fiber=3.1,
                sugar=14.0,
                sodium=1.0,
                cholesterol=0.0,
                vitamins={"C": 10.3, "B6": 0.4},
                minerals={"potassium": 422.0, "magnesium": 32.0}
            )
        )


@dataclass
class Orange(Food):
    def __init__(self):
        super().__init__(
            name="Orange",
            category="fruit",
            serving_size=131.0,
            nutrition=Nutrition(
                calories=62.0,
                protein=1.2,
                carbohydrates=15.0,
                fat=0.2,
                fiber=3.1,
                sugar=12.0,
                sodium=0.0,
                cholesterol=0.0,
                vitamins={"C": 69.7, "B1": 0.1},
                minerals={"potassium": 237.0, "calcium": 52.0}
            )
        )


@dataclass
class Strawberry(Food):
    def __init__(self):
        super().__init__(
            name="Strawberry",
            category="fruit",
            serving_size=144.0,
            nutrition=Nutrition(
                calories=46.0,
                protein=1.0,
                carbohydrates=11.0,
                fat=0.4,
                fiber=2.9,
                sugar=7.0,
                sodium=1.0,
                cholesterol=0.0,
                vitamins={"C": 84.7, "B9": 35.0},
                minerals={"potassium": 220.0, "manganese": 0.6}
            )
        )


@dataclass
class Blueberry(Food):
    def __init__(self):
        super().__init__(
            name="Blueberry",
            category="fruit",
            serving_size=148.0,
            nutrition=Nutrition(
                calories=84.0,
                protein=1.1,
                carbohydrates=21.0,
                fat=0.5,
                fiber=3.6,
                sugar=15.0,
                sodium=1.0,
                cholesterol=0.0,
                vitamins={"C": 14.4, "K": 28.6},
                minerals={"potassium": 114.0, "manganese": 0.5}
            )
        )


@dataclass
class Grape(Food):
    def __init__(self):
        super().__init__(
            name="Grape",
            category="fruit",
            serving_size=151.0,
            nutrition=Nutrition(
                calories=104.0,
                protein=1.1,
                carbohydrates=27.0,
                fat=0.2,
                fiber=1.4,
                sugar=23.0,
                sodium=3.0,
                cholesterol=0.0,
                vitamins={"C": 4.8, "K": 22.0},
                minerals={"potassium": 288.0, "copper": 0.2}
            )
        )


@dataclass
class Watermelon(Food):
    def __init__(self):
        super().__init__(
            name="Watermelon",
            category="fruit",
            serving_size=286.0,
            nutrition=Nutrition(
                calories=86.0,
                protein=1.8,
                carbohydrates=22.0,
                fat=0.4,
                fiber=1.1,
                sugar=18.0,
                sodium=3.0,
                cholesterol=0.0,
                vitamins={"C": 24.1, "A": 1066.0},
                minerals={"potassium": 320.0, "magnesium": 32.0}
            )
        )


@dataclass
class Mango(Food):
    def __init__(self):
        super().__init__(
            name="Mango",
            category="fruit",
            serving_size=165.0,
            nutrition=Nutrition(
                calories=99.0,
                protein=1.4,
                carbohydrates=25.0,
                fat=0.6,
                fiber=2.6,
                sugar=23.0,
                sodium=2.0,
                cholesterol=0.0,
                vitamins={"C": 60.1, "A": 1492.0},
                minerals={"potassium": 277.0, "copper": 0.2}
            )
        )


# ===========================VEGETABLES===============================================================================||
# ====================================================================================================================||


@dataclass
class Broccoli(Food):
    def __init__(self):
        super().__init__(
            name="Broccoli",
            category="vegetable",
            serving_size=156.0,
            nutrition=Nutrition(
                calories=55.0,
                protein=3.7,
                carbohydrates=11.0,
                fat=0.6,
                fiber=5.1,
                sugar=2.2,
                sodium=64.0,
                cholesterol=0.0,
                vitamins={"C": 135.1, "K": 220.0},
                minerals={"potassium": 479.0, "calcium": 62.0}
            )
        )


@dataclass
class Carrot(Food):
    def __init__(self):
        super().__init__(
            name="Carrot",
            category="vegetable",
            serving_size=128.0,
            nutrition=Nutrition(
                calories=52.0,
                protein=1.2,
                carbohydrates=12.0,
                fat=0.3,
                fiber=3.6,
                sugar=6.0,
                sodium=88.0,
                cholesterol=0.0,
                vitamins={"A": 21383.0, "K": 19.0},
                minerals={"potassium": 410.0, "calcium": 42.0}
            )
        )


@dataclass
class Spinach(Food):
    def __init__(self):
        super().__init__(
            name="Spinach",
            category="vegetable",
            serving_size=30.0,
            nutrition=Nutrition(
                calories=7.0,
                protein=0.9,
                carbohydrates=1.1,
                fat=0.1,
                fiber=0.7,
                sugar=0.1,
                sodium=24.0,
                cholesterol=0.0,
                vitamins={"A": 2813.0, "K": 145.0},
                minerals={"potassium": 167.0, "iron": 0.8}
            )
        )


@dataclass
class Tomato(Food):
    def __init__(self):
        super().__init__(
            name="Tomato",
            category="vegetable",
            serving_size=123.0,
            nutrition=Nutrition(
                calories=22.0,
                protein=1.1,
                carbohydrates=4.8,
                fat=0.2,
                fiber=1.5,
                sugar=3.2,
                sodium=6.0,
                cholesterol=0.0,
                vitamins={"C": 16.9, "A": 1025.0},
                minerals={"potassium": 292.0, "copper": 0.1}
            )
        )


@dataclass
class Potato(Food):
    def __init__(self):
        super().__init__(
            name="Potato",
            category="vegetable",
            serving_size=213.0,
            nutrition=Nutrition(
                calories=163.0,
                protein=4.3,
                carbohydrates=37.0,
                fat=0.2,
                fiber=3.6,
                sugar=1.7,
                sodium=13.0,
                cholesterol=0.0,
                vitamins={"C": 19.6, "B6": 0.4},
                minerals={"potassium": 926.0, "manganese": 0.3}
            )
        )


@dataclass
class Onion(Food):
    def __init__(self):
        super().__init__(
            name="Onion",
            category="vegetable",
            serving_size=110.0,
            nutrition=Nutrition(
                calories=44.0,
                protein=1.2,
                carbohydrates=10.0,
                fat=0.1,
                fiber=1.9,
                sugar=4.7,
                sodium=4.0,
                cholesterol=0.0,
                vitamins={"C": 7.4, "B6": 0.2},
                minerals={"potassium": 161.0, "manganese": 0.2}
            )
        )


# ===========================PROTEINS=================================================================================||
# ====================================================================================================================||


@dataclass
class ChickenBreast(Food):
    def __init__(self):
        super().__init__(
            name="Chicken Breast",
            category="protein",
            serving_size=174.0,
            nutrition=Nutrition(
                calories=284.0,
                protein=52.0,
                carbohydrates=0.0,
                fat=6.2,
                fiber=0.0,
                sugar=0.0,
                sodium=104.0,
                cholesterol=146.0,
                vitamins={"B3": 13.7, "B6": 0.9},
                minerals={"phosphorus": 251.0, "selenium": 37.5}
            )
        )


@dataclass
class Beef(Food):
    def __init__(self):
        super().__init__(
            name="Beef",
            category="protein",
            serving_size=170.0,
            nutrition=Nutrition(
                calories=271.0,
                protein=48.0,
                carbohydrates=0.0,
                fat=8.8,
                fiber=0.0,
                sugar=0.0,
                sodium=76.0,
                cholesterol=140.0,
                vitamins={"B12": 3.4, "B3": 9.2},
                minerals={"zinc": 8.5, "phosphorus": 248.0}
            )
        )


@dataclass
class Salmon(Food):
    def __init__(self):
        super().__init__(
            name="Salmon",
            category="protein",
            serving_size=178.0,
            nutrition=Nutrition(
                calories=415.0,
                protein=46.0,
                carbohydrates=0.0,
                fat=23.0,
                fiber=0.0,
                sugar=0.0,
                sodium=99.0,
                cholesterol=117.0,
                vitamins={"D": 669.0, "B12": 5.2},
                minerals={"selenium": 64.0, "phosphorus": 363.0}
            )
        )


@dataclass
class Egg(Food):
    def __init__(self):
        super().__init__(
            name="Egg",
            category="protein",
            serving_size=50.0,
            nutrition=Nutrition(
                calories=78.0,
                protein=6.3,
                carbohydrates=0.6,
                fat=5.3,
                fiber=0.0,
                sugar=0.6,
                sodium=62.0,
                cholesterol=186.0,
                vitamins={"A": 270.0, "D": 41.0},
                minerals={"selenium": 15.4, "phosphorus": 99.0}
            )
        )


@dataclass
class Tofu(Food):
    def __init__(self):
        super().__init__(
            name="Tofu",
            category="protein",
            serving_size=126.0,
            nutrition=Nutrition(
                calories=94.0,
                protein=10.0,
                carbohydrates=2.3,
                fat=5.3,
                fiber=0.4,
                sugar=0.6,
                sodium=8.0,
                cholesterol=0.0,
                vitamins={"K": 2.4, "B1": 0.1},
                minerals={"calcium": 353.0, "iron": 5.4}
            )
        )


# ===========================GRAINS===================================================================================||
# ====================================================================================================================||


@dataclass
class Rice(Food):
    def __init__(self):
        super().__init__(
            name="Rice",
            category="grain",
            serving_size=158.0,
            nutrition=Nutrition(
                calories=206.0,
                protein=4.3,
                carbohydrates=45.0,
                fat=0.4,
                fiber=0.6,
                sugar=0.1,
                sodium=2.0,
                cholesterol=0.0,
                vitamins={"B1": 0.1, "B3": 2.0},
                minerals={"manganese": 1.9, "magnesium": 24.0}
            )
        )


@dataclass
class Wheat(Food):
    def __init__(self):
        super().__init__(
            name="Wheat",
            category="grain",
            serving_size=30.0,
            nutrition=Nutrition(
                calories=102.0,
                protein=4.0,
                carbohydrates=21.0,
                fat=0.6,
                fiber=3.0,
                sugar=0.2,
                sodium=1.0,
                cholesterol=0.0,
                vitamins={"B1": 0.2, "B3": 1.4},
                minerals={"manganese": 0.7, "phosphorus": 71.0}
            )
        )


@dataclass
class Oatmeal(Food):
    def __init__(self):
        super().__init__(
            name="Oatmeal",
            category="grain",
            serving_size=40.0,
            nutrition=Nutrition(
                calories=150.0,
                protein=5.0,
                carbohydrates=27.0,
                fat=3.0,
                fiber=4.0,
                sugar=1.0,
                sodium=65.0,
                cholesterol=0.0,
                vitamins={"B1": 0.2, "B5": 0.4},
                minerals={"manganese": 0.8, "phosphorus": 77.0}
            )
        )


# ===========================DAIRY====================================================================================||
# ====================================================================================================================||


@dataclass
class Milk(Food):
    def __init__(self):
        super().__init__(
            name="Milk",
            category="dairy",
            serving_size=244.0,
            nutrition=Nutrition(
                calories=149.0,
                protein=8.0,
                carbohydrates=12.0,
                fat=8.0,
                fiber=0.0,
                sugar=12.0,
                sodium=105.0,
                cholesterol=24.0,
                vitamins={"D": 3.2, "A": 162.0},
                minerals={"calcium": 293.0, "phosphorus": 228.0}
            )
        )


@dataclass
class Cheese(Food):
    def __init__(self):
        super().__init__(
            name="Cheese",
            category="dairy",
            serving_size=28.0,
            nutrition=Nutrition(
                calories=113.0,
                protein=7.0,
                carbohydrates=0.4,
                fat=9.0,
                fiber=0.0,
                sugar=0.1,
                sodium=174.0,
                cholesterol=28.0,
                vitamins={"A": 249.0, "B12": 0.2},
                minerals={"calcium": 204.0, "phosphorus": 145.0}
            )
        )


@dataclass
class Yogurt(Food):
    def __init__(self):
        super().__init__(
            name="Yogurt",
            category="dairy",
            serving_size=170.0,
            nutrition=Nutrition(
                calories=100.0,
                protein=17.0,
                carbohydrates=6.0,
                fat=0.7,
                fiber=0.0,
                sugar=6.0,
                sodium=65.0,
                cholesterol=10.0,
                vitamins={"B2": 0.3, "B12": 0.8},
                minerals={"calcium": 200.0, "phosphorus": 160.0}
            )
        )


# ===========================BEVERAGES=================================================================================||
# ====================================================================================================================||


@dataclass
class Coffee(Food):
    def __init__(self):
        super().__init__(
            name="Coffee",
            category="beverage",
            serving_size=237.0,
            nutrition=Nutrition(
                calories=2.0,
                protein=0.3,
                carbohydrates=0.0,
                fat=0.0,
                fiber=0.0,
                sugar=0.0,
                sodium=5.0,
                cholesterol=0.0,
                vitamins={"B2": 0.3, "B3": 0.5},
                minerals={"potassium": 116.0, "magnesium": 7.0}
            )
        )


@dataclass
class Tea(Food):
    def __init__(self):
        super().__init__(
            name="Tea",
            category="beverage",
            serving_size=237.0,
            nutrition=Nutrition(
                calories=2.0,
                protein=0.0,
                carbohydrates=0.7,
                fat=0.0,
                fiber=0.0,
                sugar=0.0,
                sodium=7.0,
                cholesterol=0.0,
                vitamins={"C": 0.0, "K": 0.0},
                minerals={"potassium": 88.0, "manganese": 0.4}
            )
        )


@dataclass
class OrangeJuice(Food):
    def __init__(self):
        super().__init__(
            name="Orange Juice",
            category="beverage",
            serving_size=248.0,
            nutrition=Nutrition(
                calories=112.0,
                protein=1.7,
                carbohydrates=26.0,
                fat=0.5,
                fiber=0.5,
                sugar=21.0,
                sodium=2.0,
                cholesterol=0.0,
                vitamins={"C": 124.0, "B1": 0.2},
                minerals={"potassium": 496.0, "calcium": 27.0}
            )
        )


@dataclass
class OliveOil(Food):
    def __init__(self):
        super().__init__(
            name="Olive Oil",
            category="beverage",
            serving_size=14.0,
            nutrition=Nutrition(
                calories=119.0,
                protein=0.0,
                carbohydrates=0.0,
                fat=13.5,
                fiber=0.0,
                sugar=0.0,
                sodium=0.0,
                cholesterol=0.0,
                vitamins={"E": 1.9, "K": 8.1},
                minerals={"iron": 0.1, "calcium": 0.1}
            )
        )


# ===========================ADDITIONAL FRUITS=======================================================================||


@dataclass
class Pear(Food):
    def __init__(self):
        super().__init__(
            name="Pear",
            category="fruit",
            serving_size=178.0,
            nutrition=Nutrition(
                calories=102.0, protein=0.6, carbohydrates=27.0, fat=0.2,
                fiber=5.5, sugar=17.0, sodium=2.0, cholesterol=0.0,
                vitamins={"C": 7.5, "K": 4.0}, minerals={"potassium": 212.0, "copper": 0.2}
            )
        )


@dataclass
class Peach(Food):
    def __init__(self):
        super().__init__(
            name="Peach", category="fruit", serving_size=150.0,
            nutrition=Nutrition(calories=59.0, protein=1.4, carbohydrates=14.0, fat=0.4,
                fiber=2.3, sugar=13.0, sodium=0.0, cholesterol=0.0,
                vitamins={"C": 10.0, "A": 489.0}, minerals={"potassium": 285.0})
        )


@dataclass
class Kiwi(Food):
    def __init__(self):
        super().__init__(
            name="Kiwi", category="fruit", serving_size=69.0,
            nutrition=Nutrition(calories=42.0, protein=0.8, carbohydrates=10.0, fat=0.4,
                fiber=2.1, sugar=6.0, sodium=2.0, cholesterol=0.0,
                vitamins={"C": 64.0, "K": 40.0}, minerals={"potassium": 252.0})
        )


@dataclass
class Pineapple(Food):
    def __init__(self):
        super().__init__(
            name="Pineapple", category="fruit", serving_size=165.0,
            nutrition=Nutrition(calories=82.0, protein=0.9, carbohydrates=22.0, fat=0.2,
                fiber=2.3, sugar=16.0, sodium=2.0, cholesterol=0.0,
                vitamins={"C": 78.0}, minerals={"potassium": 180.0})
        )


# ===========================ADDITIONAL VEGETABLES===================================================================||


@dataclass
class Celery(Food):
    def __init__(self):
        super().__init__(
            name="Celery", category="vegetable", serving_size=101.0,
            nutrition=Nutrition(calories=16.0, protein=0.7, carbohydrates=3.0, fat=0.2,
                fiber=1.6, sugar=1.3, sodium=88.0, cholesterol=0.0,
                vitamins={"K": 29.0}, minerals={"potassium": 260.0})
        )


@dataclass
class BellPepper(Food):
    def __init__(self):
        super().__init__(
            name="Bell Pepper", category="vegetable", serving_size=119.0,
            nutrition=Nutrition(calories=31.0, protein=1.0, carbohydrates=6.0, fat=0.3,
                fiber=2.1, sugar=4.2, sodium=4.0, cholesterol=0.0,
                vitamins={"C": 152.0, "A": 3131.0}, minerals={"potassium": 211.0})
        )


@dataclass
class Kale(Food):
    def __init__(self):
        super().__init__(
            name="Kale", category="vegetable", serving_size=67.0,
            nutrition=Nutrition(calories=33.0, protein=2.2, carbohydrates=6.0, fat=0.5,
                fiber=2.6, sugar=1.3, sodium=25.0, cholesterol=0.0,
                vitamins={"C": 90.0, "K": 499.0}, minerals={"potassium": 329.0})
        )


@dataclass
class Mushroom(Food):
    def __init__(self):
        super().__init__(
            name="Mushroom", category="vegetable", serving_size=96.0,
            nutrition=Nutrition(calories=21.0, protein=3.0, carbohydrates=3.3, fat=0.3,
                fiber=1.0, sugar=2.0, sodium=5.0, cholesterol=0.0,
                vitamins={"D": 7.0}, minerals={"potassium": 318.0})
        )


# ===========================ADDITIONAL PROTEINS=====================================================================||
# ====================================================================================================================||


@dataclass
class Turkey(Food):
    def __init__(self):
        super().__init__(
            name="Turkey", category="protein", serving_size=170.0,
            nutrition=Nutrition(calories=189.0, protein=41.0, carbohydrates=0.0, fat=2.0,
                fiber=0.0, sugar=0.0, sodium=74.0, cholesterol=99.0,
                vitamins={"B3": 10.0, "B6": 0.7}, minerals={"selenium": 36.0})
        )


@dataclass
class Pork(Food):
    def __init__(self):
        super().__init__(
            name="Pork", category="protein", serving_size=170.0,
            nutrition=Nutrition(calories=243.0, protein=33.0, carbohydrates=0.0, fat=11.0,
                fiber=0.0, sugar=0.0, sodium=86.0, cholesterol=94.0,
                vitamins={"B1": 0.9, "B6": 0.5}, minerals={"selenium": 36.0})
        )


@dataclass
class Shrimp(Food):
    def __init__(self):
        super().__init__(
            name="Shrimp", category="protein", serving_size=85.0,
            nutrition=Nutrition(calories=84.0, protein=18.0, carbohydrates=0.2, fat=0.9,
                fiber=0.0, sugar=0.0, sodium=805.0, cholesterol=189.0,
                vitamins={"B12": 1.3, "D": 2.0}, minerals={"selenium": 34.0})
        )


@dataclass
class Tuna(Food):
    def __init__(self):
        super().__init__(
            name="Tuna", category="protein", serving_size=85.0,
            nutrition=Nutrition(calories=110.0, protein=22.0, carbohydrates=0.0, fat=2.0,
                fiber=0.0, sugar=0.0, sodium=301.0, cholesterol=36.0,
                vitamins={"B12": 2.2, "D": 1.8}, minerals={"selenium": 62.0})
        )


# ===========================ADDITIONAL GRAINS=======================================================================||


@dataclass
class Quinoa(Food):
    def __init__(self):
        super().__init__(
            name="Quinoa", category="grain", serving_size=185.0,
            nutrition=Nutrition(calories=222.0, protein=8.0, carbohydrates=39.0, fat=4.0,
                fiber=5.0, sugar=0.0, sodium=13.0, cholesterol=0.0,
                vitamins={"B1": 0.2, "B6": 0.2}, minerals={"magnesium": 118.0})
        )


@dataclass
class Barley(Food):
    def __init__(self):
        super().__init__(
            name="Barley", category="grain", serving_size=157.0,
            nutrition=Nutrition(calories=193.0, protein=4.0, carbohydrates=44.0, fat=1.0,
                fiber=6.0, sugar=0.4, sodium=5.0, cholesterol=0.0,
                vitamins={"B1": 0.2, "B3": 3.0}, minerals={"selenium": 17.0})
        )


# ===========================NUTS & SEEDS=============================================================================||
# ====================================================================================================================||


@dataclass
class Almonds(Food):
    def __init__(self):
        super().__init__(
            name="Almonds", category="nuts", serving_size=28.0,
            nutrition=Nutrition(calories=164.0, protein=6.0, carbohydrates=6.0, fat=14.0,
                fiber=3.5, sugar=1.2, sodium=0.0, cholesterol=0.0,
                vitamins={"E": 7.3, "B2": 0.3}, minerals={"magnesium": 76.0})
        )


@dataclass
class Walnuts(Food):
    def __init__(self):
        super().__init__(
            name="Walnuts", category="nuts", serving_size=28.0,
            nutrition=Nutrition(calories=185.0, protein=4.3, carbohydrates=4.0, fat=18.0,
                fiber=1.9, sugar=0.7, sodium=1.0, cholesterol=0.0,
                vitamins={"B6": 0.2, "E": 0.2}, minerals={"magnesium": 45.0})
        )


@dataclass
class ChiaSeeds(Food):
    def __init__(self):
        super().__init__(
            name="Chia Seeds", category="seeds", serving_size=28.0,
            nutrition=Nutrition(calories=138.0, protein=5.0, carbohydrates=12.0, fat=9.0,
                fiber=10.0, sugar=0.0, sodium=5.0, cholesterol=0.0,
                vitamins={"B3": 2.5, "B1": 0.2}, minerals={"calcium": 179.0})
        )


# ===========================LEGUMES=================================================================================||
# ====================================================================================================================||


@dataclass
class BlackBeans(Food):
    def __init__(self):
        super().__init__(
            name="Black Beans", category="legumes", serving_size=172.0,
            nutrition=Nutrition(calories=227.0, protein=15.0, carbohydrates=41.0, fat=0.9,
                fiber=15.0, sugar=0.6, sodium=1.0, cholesterol=0.0,
                vitamins={"B1": 0.4, "B9": 64.0}, minerals={"magnesium": 70.0})
        )


@dataclass
class Chickpeas(Food):
    def __init__(self):
        super().__init__(
            name="Chickpeas", category="legumes", serving_size=164.0,
            nutrition=Nutrition(calories=269.0, protein=15.0, carbohydrates=45.0, fat=4.0,
                fiber=12.0, sugar=8.0, sodium=11.0, cholesterol=0.0,
                vitamins={"B6": 0.4, "B9": 141.0}, minerals={"manganese": 1.7})
        )


@dataclass
class Lentils(Food):
    def __init__(self):
        super().__init__(
            name="Lentils", category="legumes", serving_size=198.0,
            nutrition=Nutrition(calories=230.0, protein=18.0, carbohydrates=40.0, fat=0.8,
                fiber=16.0, sugar=3.6, sodium=4.0, cholesterol=0.0,
                vitamins={"B9": 134.0, "B1": 0.5}, minerals={"iron": 6.6})
        )


# ===========================OILS & FATS=============================================================================||
# ====================================================================================================================||


@dataclass
class CoconutOil(Food):
    def __init__(self):
        super().__init__(
            name="Coconut Oil", category="oils", serving_size=14.0,
            nutrition=Nutrition(calories=121.0, protein=0.0, carbohydrates=0.0, fat=13.5,
                fiber=0.0, sugar=0.0, sodium=0.0, cholesterol=0.0,
                vitamins={"E": 0.1, "K": 0.1}, minerals={"iron": 0.0})
        )


# ===========================HERBS==================================================================================||
# ====================================================================================================================||


@dataclass
class Basil(Food):
    def __init__(self):
        super().__init__(
            name="Basil", category="herbs", serving_size=2.0,
            nutrition=Nutrition(calories=1.0, protein=0.1, carbohydrates=0.1, fat=0.0,
                fiber=0.0, sugar=0.0, sodium=0.0, cholesterol=0.0,
                vitamins={"K": 4.3, "A": 43.0}, minerals={"potassium": 5.0})
        )


# ===========================CONDIMENTS==============================================================================||
# ====================================================================================================================||


@dataclass
class Honey(Food):
    def __init__(self):
        super().__init__(
            name="Honey", category="condiments", serving_size=21.0,
            nutrition=Nutrition(calories=64.0, protein=0.1, carbohydrates=17.0, fat=0.0,
                fiber=0.0, sugar=17.0, sodium=1.0, cholesterol=0.0,
                vitamins={"B2": 0.0, "C": 0.1}, minerals={"potassium": 11.0})
        )


@dataclass
class Ketchup(Food):
    def __init__(self):
        super().__init__(
            name="Ketchup", category="condiments", serving_size=17.0,
            nutrition=Nutrition(calories=19.0, protein=0.2, carbohydrates=5.0, fat=0.0,
                fiber=0.1, sugar=4.0, sodium=154.0, cholesterol=0.0,
                vitamins={"A": 28.0, "C": 1.7}, minerals={"potassium": 67.0})
        )


@dataclass
class Mustard(Food):
    def __init__(self):
        super().__init__(
            name="Mustard", category="condiments", serving_size=5.0,
            nutrition=Nutrition(calories=3.0, protein=0.2, carbohydrates=0.3, fat=0.2,
                fiber=0.2, sugar=0.1, sodium=57.0, cholesterol=0.0,
                vitamins={"K": 0.3}, minerals={"manganese": 0.1})
        )


# ===========================EXPORTS===================================================================================||
# ====================================================================================================================||


__all__ = [
    # Fruits
    'Apple', 'Banana', 'Orange', 'Strawberry', 'Blueberry', 'Grape', 'Watermelon', 'Mango',
    'Pear', 'Peach', 'Plum', 'Cherry', 'Kiwi', 'Pineapple', 'Papaya', 'Cantaloupe', 
    'Honeydew', 'Grapefruit', 'Lemon', 'Lime', 'Pomegranate', 'Avocado', 'Coconut',
    # Vegetables
    'Broccoli', 'Carrot', 'Spinach', 'Tomato', 'Potato', 'Onion', 'Celery', 'BellPepper',
    'Cucumber', 'Lettuce', 'Kale', 'Cabbage', 'Cauliflower', 'BrusselsSprouts', 'Asparagus',
    'GreenBeans', 'Peas', 'Corn', 'SweetPotato', 'Beet', 'Radish', 'Zucchini', 'Eggplant',
    'Mushroom', 'Garlic', 'Ginger', 'Scallion', 'Leek', 'Artichoke',
    # Proteins
    'ChickenBreast', 'Beef', 'Salmon', 'Egg', 'Tofu', 'Turkey', 'Pork', 'Lamb', 'Duck',
    'Shrimp', 'Crab', 'Lobster', 'Tuna', 'Cod', 'Tilapia', 'Halibut', 'Sardines',
    'TurkeyBreast', 'GroundBeef', 'Bacon', 'Ham', 'TofuFirm', 'Tempeh', 'Seitan',
    'Venison', 'Bison', 'Rabbit', 'Anchovies',
    # Grains
    'Rice', 'Wheat', 'Oatmeal', 'Quinoa', 'Barley', 'Couscous', 'Farro', 'Bulgur',
    'Millet', 'Buckwheat', 'Amaranth', 'Sorghum', 'Spelt', 'Rye', 'Cornmeal',
    'Pasta', 'BreadWholeWheat', 'BreadWhite', 'Bagel', 'EnglishMuffin', 'Tortilla',
    # Dairy
    'Milk', 'Cheese', 'Yogurt', 'Butter', 'CreamCheese', 'SourCream', 'CottageCheese',
    'HeavyCream', 'HalfAndHalf', 'EvaporatedMilk', 'CondensedMilk', 'Ghee',
    # Beverages
    'Coffee', 'Tea', 'OrangeJuice', 'OliveOil', 'AppleJuice', 'CranberryJuice', 
    'GrapeJuice', 'Lemonade', 'AlmondMilk', 'SoyMilk', 'CoconutMilk', 'RiceMilk',
    'ProteinShake', 'Smoothie', 'Cola', 'LemonLimeSoda', 'EnergyDrink', 'SportsDrink',
    # Nuts & Seeds
    'Almonds', 'Walnuts', 'Cashews', 'Peanuts', 'Pistachios', 'Hazelnuts', 'Macadamia',
    'BrazilNuts', 'Pecans', 'ChiaSeeds', 'FlaxSeeds', 'SunflowerSeeds', 'PumpkinSeeds',
    'SesameSeeds', 'HempSeeds', 'PoppySeeds',
    # Legumes
    'BlackBeans', 'KidneyBeans', 'Chickpeas', 'Lentils', 'NavyBeans', 'PintoBeans',
    'LimaBeans', 'BlackEyedPeas', 'Soybeans', 'AdzukiBeans', 'CannelliniBeans',
    # Condiments & Sauces
    'Ketchup', 'Mustard', 'Mayonnaise', 'SoySauce', 'HotSauce', 'BarbecueSauce',
    'Salsa', 'Guacamole', 'Hummus', 'Tahini', 'PeanutButter', 'AlmondButter',
    'Jam', 'Jelly', 'Honey', 'MapleSyrup', 'Agave', 'Molasses',
    # Oils & Fats
    'OliveOil', 'CoconutOil', 'SesameOil', 'VegetableOil', 'CanolaOil', 'FlaxseedOil',
    'WalnutOil', 'AvocadoOil', 'GrapeseedOil', 'SunflowerOil', 'PalmOil', 'Lard',
    # Herbs & Spices
    'Basil', 'Oregano', 'Thyme', 'Rosemary', 'Parsley', 'Cilantro', 'Mint', 'Dill',
    'Sage', 'Tarragon', 'BayLeaves', 'Cumin', 'Coriander', 'Paprika', 'Cayenne',
    'BlackPepper', 'Salt', 'Cinnamon', 'Nutmeg', 'GingerSpice', 'Turmeric', 'Saffron',
    'Cardamom', 'Cloves', 'AllSpice', 'MustardSeed', 'Fennel', 'Caraway',
    # Sweets & Desserts
    'ChocolateDark', 'ChocolateMilk', 'WhiteChocolate', 'CocoaPowder', 'VanillaExtract',
    'BakingPowder', 'BakingSoda', 'CornStarch', 'Gelatin', 'WhippedCream', 'IceCream',
    'FrozenYogurt', 'Sherbet', 'Sorbet', 'Candy', 'GummyBears', 'HardCandy',
    # Prepared Foods
    'Pizza', 'Burger', 'Sandwich', 'HotDog', 'FrenchFries', 'OnionRings', 'Nachos',
    'Taco', 'Burrito', 'Sushi', 'Ramen', 'FriedRice', 'PadThai', ' Curry',
    'Chili', 'Stew', 'Soup', 'Salad', 'Coleslaw', 'PotatoSalad', 'MacAndCheese',
]
