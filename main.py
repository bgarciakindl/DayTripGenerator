
from importlib.abc import Traversable
from logging.config import valid_ident
from math import fabs
import random
from tkinter.messagebox import YES


destinations = ["Colorado","Florida", "Texas", "New York", "Paris"]
location_select= random.choice(destinations)

def rand_location (initial_location_select):
    for location in destinations:
        print (initial_location_select)
        user_input = input("Is this choice acceptable? yes/no: ")

        if user_input =="yes":
            print ("We will see you in there")
            return initial_location_select
        else:
            print ("We will select another location")
            initial_location_select= random.choice(destinations)

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
            co_rest_select = random.choice(co_resturaunts)




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
            co_act_select = random.choice(co_activities)




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
            fl_rest_select = random.choice(fl_resturaunts)



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
            fl_act_select = random.choice(fl_activities)




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
            tx_rest_select =random.choice(tx_resturaunts)



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
            tx_act_select = random.choice(tx_activities)




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
            ny_rest_select = random.choice(ny_resturaunts)


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
            ny_act_select = random.choice(ny_activities)




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
            p_rest_select = random.choice(p_resturaunts)
            



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
            p_act_select = random.choice(p_resturaunts)
            


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

if destination == "Colorado":
    rand_co_act (co_act_select)
elif destination == "Florida":
    rand_fl_act (fl_act_select)
elif destination =="Texas":
    rand_tx_act (tx_act_select)
elif destination == "New York":
    rand_ny_act (ny_act_select)
else:
    rand_p_act (p_act_select)


if destination == "Colorado":
    activity = co_act_select
    resturaunt = co_rest_select
elif destination == "Florida":
     activity = fl_act_select
     resturaunt = fl_rest_select
elif destination =="Texas":
    activity = tx_act_select
    resturaunt = tx_rest_select
elif destination == "New York":
    activity = ny_act_select
    resturaunt = ny_rest_select
else:
    activity = p_act_select
    resturaunt = p_rest_select
   



transportation_list = ["Rental Car", "Train", "Bus", "Bike", "Ride Share"]
transport_select = random.choice(transportation_list)

def rand_transport (transport_select):
    
    for transport in transportation_list:
        print (transport_select)
        user_transport_input = input("Is this choice acceptable? yes/no: ")
        if user_transport_input=="yes":
            print ("Thank you for selecting this transportation method")
            return transport_select
        else:
            print ("We will choose another transport")
            transport_select = random.choice(transportation_list)


rand_transport(transport_select)
transport = transport_select

final_input = input (f"It appears that you have selected to go to {destination} and planned {activity}, and to eat at {resturaunt}, and travel by {transport} is this correct? yes/no: ")

