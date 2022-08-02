
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





co_resturaunts = ["Casa Bonita", "Beau Joes", "Buckhorn Exchange","The Mint", "The Fort"]
co_rest_select = random.choice(co_resturaunts)

def rand_co_rest (co_rest_select):
    for resturaunt in co_resturaunts:
        print(co_rest_select)
        user_rest_input = input("Is this choice acceptable? yes/no: ")
        if user_rest_input =="yes":
            print("We will see you in there")
            return co_rest_select
        else:
            print ("We will select another location")

resturaunt = co_rest_select


co_activities =["Garden of the Gods","Cave of the Winds","Hike a 14er", "Sports Game","Denver Mint"]
co_act_select = random.choice(co_activities)
def rand_co_act (co_act_select):
    for activity in co_activities:
        print(co_act_select)
        user_act_input = input("Is this choice acceptable? yes/no: ")
        if user_act_input =="yes":
            print("We will see you in there")
            return co_act_select
        else:
            print ("We will select another location")

activity = co_act_select


fl_resturaunts  =["McGuires Irish Pub","Peg Leg Petes","Flounders","The Coffee Cup", "The District"]
fl_rest_select = random.choice(fl_resturaunts)

def rand_fl_rest (fl_rest_select):
    for resturaunt in fl_resturaunts:
        print(fl_rest_select)
        user_rest_input = input("Is this choice acceptable? yes/no: ")
        if user_rest_input =="yes":
            print("We will see you in there")
            return fl_rest_select
        else:
            print ("We will select another location")

resturaunt = fl_rest_select

fl_activities  =["Jet Ski", "Lay out on the Beach", "Naval Aviation Museum", "Disney World", "Universal Studios"]
fl_act_select = random.choice(fl_activities)

def rand_fl_act (fl_act_select):
    for activity in fl_activities:
        print(fl_act_select)
        user_act_input = input("Is this choice acceptable? yes/no: ")
        if user_act_input =="yes":
            print("We will see you in there")
            return fl_act_select
        else:
            print ("We will select another location")


activity = fl_act_select


tx_resturaunts =["Hutchins","Contigo","BCN Taste & Tradition","The Village Bakery","Blue Bonnet Cafe"]
tx_rest_select =random.choice(tx_resturaunts)

def rand_tx_rest (tx_rest_select):
    for resturaunt in tx_resturaunts:
        print(tx_rest_select)
        user_rest_input = input("Is this choice acceptable? yes/no: ")
        if user_rest_input =="yes":
            print("We will see you in there")
            return tx_rest_select
        else:
            print ("We will select another location")

resturaunt = tx_rest_select

tx_activities =["San Antonio River Walk","The Alamo","Space Center Houston","Guadalupe Mountains National Park","The Fort Worth Stockyards"]
tx_act_select =random.choice(tx_activities)

def rand_tx_act (tx_act_select):
    for activity in tx_activities:
        print(tx_act_select)
        user_act_input = input("Is this choice acceptable? yes/no: ")
        if user_act_input =="yes":
            print("We will see you in there")
            return tx_act_select
        else:
            print ("We will select another location")

activity = tx_act_select


ny_resturaunts =["Tavern on the Green","Nathans Famous","Peter Luger Steak House","Hudson Smokehouse","Playground"]
ny_rest_select =random.choice(ny_resturaunts)

def rand_ny_rest (ny_rest_select):
    for resturaunt in ny_resturaunts:
        print(ny_rest_select)
        user_rest_input = input("Is this choice acceptable? yes/no: ")
        if user_rest_input =="yes":
            print("We will see you in there")
            return ny_rest_select
        else:
            print ("We will select another location")
resturaunt = ny_rest_select

ny_activities =["Central Park", "Metropolitan Museum of Art","Empire State Building","Ellis Island","Broadway Show"]
ny_act_select =random.choice(ny_activities)

def rand_ny_act (ny_act_select):
    for activity in ny_activities:
        print(ny_act_select)
        user_act_input = input("Is this choice acceptable? yes/no: ")
        if user_act_input =="yes":
            print("We will see you in there")
            return ny_act_select
        else:
            print ("We will select another location")

activity = ny_act_select



p_resturaunts =["Le Fouquets","Le Relais Plaza","Café de Flore","Tour d Argent","L As du Fallafel"]
p_rest_select = random.choice(p_resturaunts)

def rand_p_rest (p_rest_select):
    for resturaunt in p_resturaunts:
        print(p_rest_select)
        user_rest_input = input("Is this choice acceptable? yes/no: ")
        if user_rest_input =="yes":
            print("We will see you in there")
            return p_rest_select
        else:
            print ("We will select another location")

resturaunt = p_rest_select

p_activities =["Eiffel Tower","Musée du Louvre","Palais Garnier, Opéra National de Paris", "Arc de Triomphe", "Seine River Cruises"]
p_act_select = random.choice(p_activities)

def rand_p_act (p_act_select):
    for activity in p_activities:
        print(p_act_select)
        user_act_input = input("Is this choice acceptable? yes/no: ")
        if user_act_input =="yes":
            print("We will see you in there")
            return p_act_select
        else:
            print ("We will select another location")


activity = p_act_select


if destination == "Colorado":
    rand_co_rest (co_rest_select)
elif destination == "Florida":
    rand_fl_rest (fl_rest_select)
elif destination =="Texas":
    rand_tx_rest (tx_rest_select)
elif destination == "New York":
    rand_ny_rest (ny_rest_select)
else:
    rand_p_rest (p_rest_select)





