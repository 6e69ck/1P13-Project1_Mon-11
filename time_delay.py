from team_functions.fleet_data import fleet_data
from team_functions.passenger_data import passenger_data

def time_delay(passenger_data, fleet_data):
    late_layover_data = []

    # go over data
    for flight in fleet_data:
        plane_model, _, _, _, gate, destination, status, _ = flight
        
        # process delayed flight
        if status.strip() == "Late":
            layover_count = 0
            
            # go over passenger data
            for passenger in passenger_data:
                _, _, passenger_gate, _, passenger_destination, passenger_status, _, layover = passenger
                
                # see if there's any delayed passenger and layover
                if (passenger_gate.strip() == gate.strip() and
                    passenger_destination.strip() == destination.strip() and
                    passenger_status.strip() == "Late" and
                    layover.strip() == "Layover"):
                    layover_count += 1
            
            # show flight only if it has layover passengers
            if layover_count > 0:
                late_layover_data.append([plane_model.strip(), layover_count])

    return late_layover_data


# Load data
fleet_data = fleet_data()
passenger_data = passenger_data()

print(time_delay(passenger_data, fleet_data))
