
import turtle 
def passenger_data():
    '''Reads passenger data file. Returns 2-D list containing passenger data.'''
    file = open("passenger_data_v2.txt", "r")
    passenger_data = []
    for line in file:
        line = line.split(",")
        # stripping newline at the end of each line 
        line[-1] = line[-1].strip()
        # turning baggage weight from str to float
        line[6] = float(line[6])
        passenger_data.append(line)
    file.close()
    return passenger_data

def fleet_data():
    '''Reads fleet data file. Returns 2-D list with fleet data'''
    f_data = []
    with open("fleet_data.txt", 'r') as file:
        for line in file:
            data = line.strip().split(',')
            # changes certain items from str to int 
            plane_model = data[0].strip()
            business_seats = int(data[1].strip())
            economy_seats = int(data[2].strip())
            total_seats = int(data[3].strip())
            gate = data[4].strip()
            destination = data[5].strip()
            arrival_status = data[6].strip()
            max_baggage_weight = int(data[7].strip())
            
            f_data.append([plane_model, business_seats, economy_seats, total_seats, gate, destination, 
                           arrival_status, max_baggage_weight])
    return f_data

def daily_data(passenger_data): #Anannya Pandit
    '''Accepts 2D list of passenger data. Extracts gate number, number of people flying business and 
    number of people flying economy. Returns 2D daily_data list containing sublists of each gate number 
    and their respective number of business and economy seats'''
    daily_data = []
    # Initialize gate list, this will contain each unique gate from passenger data
    gate_list = []
    for passenger in passenger_data:
        # If that gate from the passenger sublist has not already been added to gate_list, append gate to gate_list
        if passenger[2] not in gate_list:
            gate_list.append(passenger[2])
    for gate in gate_list:
        # Initialize sub list for each gate, set initial economy and business seats to zero
        current_list = [gate, 0, 0]
        for list in passenger_data:
            # If the passenger's gate is the same as the current gate iteration
            if list[2] == gate:
                # Checks if passenger is flying business
                if list[4] == "B":
                    current_list[1] += 1
                # Passenger is flying economy
                else:
                    current_list[2] +=1
        daily_data.append(current_list)
    return daily_data

def oversold(flight_data, daily_data): # Nick Ly
    """
    Passenger data is omitted because daily data is derived from passenger data
    :param list flight_data: flight data
    :param list daily_data: daily data
    """
    os_business_seats = []
    os_economy_seats = []

    for f in flight_data:
        model = f[0]
        # Number of total seats on plane
        business_seats = f[1]
        eco_seats = f[2]
        gate = f[4]

        # Filter data for gate only, convert the filtered data to a list
        filter_d_data = list(filter(lambda x: x[0] == gate, daily_data))
        # make sure the filtered data actually has an item
        if len(filter_d_data) != 0:
            # Grab the element
            # it is assumed there will be only one plane at the gate, should only be one plane
            d = filter_d_data[0]
            # Get number of sold seats
            sold_bs = d[1]
            sold_es = d[2]

            # compute oversold count (if < 0, it means there is a surplus of seats, not oversold)
            # max to clamp down to be >= 0
            oversold_b = max(0, sold_bs - business_seats )
            oversold_e = max(0, sold_es - eco_seats)

            # Add data to the results
            os_business_seats.append([model, oversold_b])
            os_economy_seats.append([model, oversold_e])

        else:
            # Data does not line up, one of the flights isnt in departures
            raise ValueError("Departure data does not match flight data!")


    return os_business_seats, os_economy_seats

def overweight(fleet_data, passenger_data): # Mattea Bessette
    general_list = [] #will contain each plane model and how many passengers have overweight bags on each plane
    specific_list  = []  #for every passenger who has an overweight bag, this list will have their name, gate number, and how much their bag exceeds the maximum weight
    for item in fleet_data:
        general_sublist = [item[0], 0] #item[0] is the plane model
        for row in passenger_data:
            if row[2] == item[4]: #comparing gate numbers
                if row[6] > item[7]: #if the bag weight exceeds the maximum
                    specific_sublist = [row[0], row[1], row[2], round(row[6] - item[7],2)] #last item is the amount the bag exceeds the maximum
                    general_sublist[1] = general_sublist[1] + 1 #running counter of how many people per plane   type have an overwight bag
                    specific_list.append(specific_sublist)
        general_list.append(general_sublist)
    return general_list, specific_list

def layover(plane_list, passenger_list): #Karl Matta
    '''
    This function takes 2D lists containing plane information and passenger information.

    Parameters
    ----------
    plane_list : list
        A 2D list containing the data from fleet_data.txt.
    passenger_list : list
        A 2D list containing the data from fleet_data.txt.

    Returns
    -------
    list
        A tuple containing two, 2D lists. The first contains passengers who have layovers, and the second contains a flight model and the numver of passengers it has who have layovers.

    '''
    
    # Initiallizing lists
    passenger_layover_list = []
    plane_layover_list = []
    
    # Iterating through the passenger list
    for passenger in passenger_list:
        
        # If the passenger has a layover
        if passenger[7]:
            
            # Adding the passenger to the passenger_layover_list
            passenger_layover_list.append([passenger[0], passenger[1], passenger[2]])
            
            # Checking for a plane with a matching destination
            for plane in plane_list:
                found = False
                
                # If a matching plane is found, see if it has already been added to the plane_layover_list
                if plane[5] == passenger[3]:
                    for layover in plane_layover_list:
                        
                        # If the plane has already been added, add one passenger to the number of layovers
                        if plane[0] == layover[0]:
                            found = True
                            layover[1] += 1
                            break
                        
                    # If the plane has not been added, add it to the list with 1 layover
                    if not(found):
                        plane_layover_list.append([plane[0], 1])
                        break
                    
    # Return the two lists as a tuple
    return passenger_layover_list, plane_layover_list

def graphical_Mon11(oversold, overweight, layover):
    '''Accepts 2-D lists oversold, overweight, layover and time delay. Displays flight and passenger 
    information organized by flight model. '''
    turtle.setup(1000, 450)
    t = turtle.Turtle()
    screen = turtle.Screen()
    x = -450
    t.pu()
    
    for os_b in oversold[0]: # oversold business list
        t.goto(x,60)
        t.color("lightpink")
        t.begin_fill()
        t.pd()
		# Draw background square
        for i in range (4):
            t.forward(120)
            t.right(90)
        t.end_fill()
        # draws header rectangle
        t.color("lightblue")
        t.pu()
        t.begin_fill()
        t.forward(120)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(120)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.end_fill()
        t.color("black")
        t.goto(x+60,40)
        # Writes flight model in header
        t.write(os_b[0], align = 'center')
        
        t.goto(x+60,20)
        t.write(f"Oversold business:{os_b[1]}", align = 'center') # oversold business seats
        for os_e in oversold[1]: # oversold economy list
            if os_e[0] == os_b[0]:
                t.goto(x+60,0)
                t.write(f"Oversold economy:{os_e[1]}", align = 'center') # oversold economy seats
        for overweight_list in overweight[0]: # plane overweight list
            if overweight_list[0] == os_b[0]:
                t.goto(x+60,-20)
                t.write(f"Overweight bags:{overweight_list[1]}", align = 'center') 
        for layover_list in layover[1]: # plane layover list
            if layover_list[0] == os_b[0]:
                t.goto(x+60,-40)
                t.write(f"Late Layover:{layover_list[1]}", align = 'center') # amount of passengers that have late layover
        # x-coordinate for next rectangle
        x += 130
    t.hideturtle()
    screen.exitonclick()
    turtle.done()

# Main code
Daily_data = daily_data(passenger_data())
Oversold = oversold(fleet_data(), Daily_data)
Overweight = overweight(fleet_data(), passenger_data())
Layover = layover(fleet_data(), passenger_data())
graphical_Mon11(Oversold,Overweight,Layover)