""" 
Authors: Orlando Coyoy, Ya'Kuana Davis, Roger Trejo
Course Name: CSCI 3725
Assignment Name: PQ1
Date: September 25, 2020
Description: This file includes a collection of functions that will either assist or cause mutations on given recipe objects 
"""

import random
from classes import Recipe, Ingredient


def ingredient_from_set(file_list, ingredient_names):
    """Returns an ingredient from the inspiring set"""
    # Finds the random file
    if(len(file_list) == 1):
        afile = file_list
    else:
        afile = file_list[random.randint(0, (len(file_list)-1))]
    
    # This while loop ensures that the chosen ingredient from the i
    # nspiring set does not match an ingredient in the curent 
    # list of ingredients
    while(True):
        # Chooses a random line from the random file
        lines = open(afile).read().splitlines()
        my_line = random.choice(lines)
        print(my_line)
        # ingredient_name = my_line.split(' g ')[1]
        if (my_line.find(" g ") != -1):
            ingredient_name = my_line.split(' g ')[1]
        else:
            ingredient_name = " ".join(my_line.split()[1:])

        if(ingredient_names.count(ingredient_name) == 0):
            return ingredient_name

def change_ingredient_amount(recipe_obj):
    """Changes the ingredient amount of a  random selected ingredient."""
    # gets a random ingredient to change
    ingredient = random.choice(recipe_obj.ingredients)

    previous_amount = ingredient.amount 
    new_amount = random.randrange(0,10) + recipe_obj.fitness

    # this if statement makes sure that 
    # there will always be a change in the amount
    if previous_amount == new_amount: 
        new_amount += 1 
    ingredient.amount = new_amount
    
    # Calculates the new total ounces of ingredients
    # in the recipe and then normalizes each quantity for
    # the final total to equal 100


def change_ingredient_name(recipe_obj, file_list):
    """An ingredient is selected uniformly at random from the recipe. 
    Its name is changed to that of another ingredient that is chosen at random 
    from the ones in the inspiring set."""
    ingredient = random.choice(recipe_obj.ingredients)
    new_name = ingredient_from_set(file_list, recipe_obj.ingredients)

    #This is where the ingredient name is changed
    ingredient.name = new_name

    # Calculates the new total ounces of ingredients
    # in the recipe and then normalizes each quantity for
    # the final total to equal 100



def add_ingredient(recipe_obj, file_list):
    """An ingredient is selected uniformly at random from the inspiring set 
    and added to the recipe."""
    ingredient_name = ingredient_from_set(file_list, recipe_obj.ingredients)
    
    # The amount of the new ingredient will be an int ,i, such that 
    # 1<=1<10
    ingredient_amount = random.randrange(1, 10)
    recipe_obj.ingredients.append(Ingredient(ingredient_name, ingredient_amount))

    # The fitness increases by one because a new ingredient is added
    recipe_obj.fitness += 1

    # Calculates the new total ounces of ingredients
    # in the recipe and then normalizes each quantity for
    # the final total to equal 100


def delete_ingredient(recipe_obj):
    """An ingredient is selected uniformly at random from the recipe, 
    and removed from the recipe."""

    #random ingredient index is chosen
    choose_ingredient = random.randint(0, len(recipe_obj.ingredients) - 1)
    
    #removes the ingredient from the recipe object
    recipe_obj.ingredients.pop(choose_ingredient)

    #since one ingredient is removed, the fitness is one less
    recipe_obj.fitness -= 1
    
    # Calculates the new total ounces of ingredients
    # in the recipe and then normalizes each quantity for
    # the final total to equal 100