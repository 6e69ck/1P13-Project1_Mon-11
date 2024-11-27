def fleet_data():
    '''Reads fleet data file. Returns 2-D list with fleet data'''
    f_data = []
    with open("../fleet_data.txt", 'r') as file:
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