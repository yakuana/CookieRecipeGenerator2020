""" 
Authors: Orlando Coyoy, Ya'Kuana Davis, Roger Trejo
Course Name: CSCI 3725
Assignment Name: PQ1
Date: September 25, 2020
Description: This document can be used to run our modified version of PIERRE. The files classes.py, get_methods.py, reading_files.py and mutations are all imported into this file and utilized as necessary. Use `python3 main.py` in the terminal to explore our code.  

*** Disclaimer *** 

Sept. 25: change_ingredient_name function occasionally gets stuck in a loop. Recipe total amounts do not add up to 100. Some exceed and others are way below. 

Sept. 30: change_ingredient_name function has not broken the code after 30 runs. Recipe total amounts add up to 100. Decimal points can be 9 digits long. 

"""

import random
from read_files import read_files, file_names
from classes import Recipe, Ingredient

def main():
    #prepping first generation from the inspiring set
    recipe_names = file_names()
    parent = read_files(recipe_names)
   
    #creating n number of generations
    num_of_generations = 2
    num_of_offspring = 0 

   
    print("\n", "---------------------")
    print("\n", "* Final Recipes *")

    for recipe in parent:
        print("\n", recipe.name)
        recipe.print_ingredients()

    print("--------------")
    print("ENJOY :)", "\n")


main()
