cookbook = {
    "Sandwich" : {
        "ingredients" : ["ham", "bread", "cheese", "tomatoes"],
        "meal" : "lunch",
        "prep_time" : 10
	},
    "Cake" : {
        "ingredients" : ["floor", "sugar", "eggs"],
        "meal" : "dessert",
        "prep_time" : 60
	},
	"Salad" : {
        "ingredients" : ["avocado", "arugula", "tomatoes", "spinach"],
        "meal" : "lunch",
        "prep_time" : 15
	}
}

def print_all_recipe():
	print("Current recipe in the cookbook:", *cookbook.keys(), sep="\n")

def print_recipe(recipe):
	if recipe in cookbook:
		print("Recipe for", recipe)
		print("Ingredients are: ", end="")
		print(*cookbook[recipe]["ingredients"], sep=", ")
		print("Meal is for: ", end="")
		print(cookbook[recipe]["meal"])
		print("Prep time is: ", end="")
		print(cookbook[recipe]["prep_time"], "min")
	else:
		print("Could not find this recipe of", recipe)

def remove_recipe(recipe):
	cookbook.pop(recipe)

def add_recipe():
	recipe = input("Enter a recipe name:\n")
	ingredients = []
	while 1:
		ing = input("Enter next ingredient:\n")
		if ing:
			ingredients.append(ing)
		else:
			break

	meal_type = input("Enter a meal type:\n")
	try:
		prep_time = int (input("Enter a preparation time:\n"))
	except:
		print("Invalid meal time")
		prep_time = 42

	cookbook[recipe] = dict(ingredients = ingredients, meal = meal_type, prep_time = prep_time)
	print_recipe(recipe)


print_all_recipe()
print_recipe("Sandwich")
remove_recipe("Sandwich")
print_all_recipe()
add_recipe()