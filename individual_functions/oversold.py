"""
Author: Nick Ly
MacID: lyn10 (400589650)

This function computes how many oversold seats there are for every flight on a
certain day using the daily data.
"""


def oversold(flight_data, daily_data):
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