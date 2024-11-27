'''
Karl Matta
'''


def layover(plane_list, passenger_list):
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