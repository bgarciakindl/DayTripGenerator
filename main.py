
from importlib.abc import Traversable
from logging.config import valid_ident
from math import fabs
import random


destinations = ["Colorado","Florida", "Texas", "New York", "Paris"]
location_select= random.choice(destinations)

def rand_location (location_select):
    
    for location in destinations:
        print (location_select)
        user_input = input("Is this choice acceptable? yes/no: ")

        if user_input =="yes":
            print ("We will see you in there")
            return location_select
        else:
            print ("We will select another location")

rand_location(location_select)
destination = location_select
#print(destination)