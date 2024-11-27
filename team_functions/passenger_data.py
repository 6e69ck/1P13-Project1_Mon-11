def passenger_data():
    '''Reads passenger data file. Returns 2-D list containing passenger data.'''
    file = open("../passenger_data_v2.txt", "r")
    passenger_data = []
    for line in file:
        line = line.split(",")
        line[-1] = line[-1].strip() # stripping newline at the end of each line
        line[6] = float(line[6]) # turning baggage weight from str to float
        passenger_data.append(line)
    file.close()
    return passenger_data
