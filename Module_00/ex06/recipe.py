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
		print(cookbook[recipe]["prep_time"], "min\n")
	else:
		print("Could not find recipe of", recipe)

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
	while True:
		try:
			prep_time = int (input("Enter a preparation time:\n"))
			break
		except:
			print("Invalid meal time")

	cookbook[recipe] = dict(ingredients = ingredients, meal = meal_type, prep_time = prep_time)
	print_recipe(recipe)


print("Welcome to the Python Cookbook !")

while 1:
	print("""List of available option:
	1: Add a recipe
	2: Delete a recipe
	3: Print a recipe
	4: Print the cookbook
	5: Quit
	""")
	try:
		choice = input("Select an option:\n")
	except:
		break

	print("")
	if choice == "1":
		add_recipe()
	elif choice == "2":
		recipe = input("Enter recipe name to remove:\n")
		if recipe in cookbook:
			remove_recipe(recipe)
	elif choice  == "3":
		recipe = input("Enter recipe name to get its details:\n")
		print_recipe(recipe)
	elif choice == "4":
		print_all_recipe()
	elif choice == "5":
		print("Cookbook closed. Goodbye !")
		break
	else:
		print("Wrong option :c")