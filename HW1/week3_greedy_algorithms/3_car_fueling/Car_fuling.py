# %%

fuel_station_locations = list(
    map(int, input('Enter the distance between the fuel stations').split()))
tank_capacity = int(input('Enter your tank capacity'))
distance = int(input('Enter the distance from source to destination'))

fuel_station_locations = [0]+fuel_station_locations+[distance]

# %%
def fuel_car_automation(fuel_station_locations, tank_capacity, distance):
    total_capacity = tank_capacity
    for i in range(1, len(fuel_station_locations)-1):
        tank_capacity = tank_capacity - \
            (fuel_station_locations[i] - fuel_station_locations[i-1])
        print('reached to station {}. tank: {}, distance to next station: {}'
              .format(i, tank_capacity, fuel_station_locations[i+1]-fuel_station_locations[i]))
        if tank_capacity < fuel_station_locations[i+1]-fuel_station_locations[i]:
            print('Refuel the car at {}'.format(fuel_station_locations[i]))
            tank_capacity = total_capacity
        else:
            print('Please continue to the next station')
# %%
fuel_car_automation(fuel_station_locations, tank_capacity, distance)
