def daily_data(passenger_data):
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

