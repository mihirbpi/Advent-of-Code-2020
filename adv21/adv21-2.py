from aocd import get_data

my_list = get_data(day=21).split("\n")

allergens_dict = {}
allergens_toingredient_dict = {}
all_ingredients = []

for i in range(0, len(my_list)):
    entry = my_list[i]
    ingredients = entry.split("(contains")[0].strip(" ").split(" ")

    for ing in ingredients:
        all_ingredients.append(ing)

    allergens = entry.split("(contains")[1].strip(")").strip(" ").split(", ")

    for allergen in allergens:

        if(allergen not in allergens_dict.keys()):
            allergens_dict[allergen] = ingredients

        else:
            ingredients_list_check = allergens_dict[allergen].copy()

            for ingredient in allergens_dict[allergen].copy():

                if(ingredient not in ingredients):
                    ingredients_list_check.remove(ingredient)

            allergens_dict[allergen] = ingredients_list_check

allergens_dict_copy = allergens_dict.copy()

while(len(allergens_dict_copy.keys()) > 0):

    for allergen in allergens_dict.keys():

        if(len(allergens_dict[allergen]) == 1):
            allergens_toingredient_dict[allergen] = allergens_dict[allergen][0]
            ingredient_to_remove = allergens_dict[allergen][0]

            allergens_dict_copy.pop(allergen, None)

            for other_allergen in allergens_dict_copy.keys():

                if(ingredient_to_remove in allergens_dict[other_allergen]):
                    x = allergens_dict[other_allergen]
                    x.remove(ingredient_to_remove)
                    allergens_dict[other_allergen] = x

for allergen in allergens_dict.keys():
    allergens_dict[allergen] = allergens_dict[allergen][0]

allergens_list = list(allergens_dict.keys())
allergens_list.sort()

danger_list = ""

for allergen in allergens_list:
        danger_list += allergens_dict[allergen] + ","

print(danger_list.strip(","))
