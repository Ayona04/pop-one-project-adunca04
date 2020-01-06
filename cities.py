from math import *
import random

def distance(lat1degrees, long1degrees, lat2degrees, long2degrees):
    earth_radius = 3956  # miles
    lat1 = radians(lat1degrees)
    long1 = radians(long1degrees)
    lat2 = radians(lat2degrees)
    long2 = radians(long2degrees)
    lat_difference = lat2 - lat1
    long_difference = long2 - long1
    sin_half_lat = sin(lat_difference / 2)
    sin_half_long = sin(long_difference / 2)
    a = sin_half_lat ** 2 + cos(lat1) * cos(lat2) * sin_half_long ** 2
    c = 2 * atan2(sqrt(a), sqrt(1.0 - a))
    return earth_radius * c

def read_cities('city-data.txt'):
    file = open('city-data.txt','r')
    road_map = []
    for line in file:
        road_map.append(tuple(line.strip().split('\t')))
    file.close()
    return road_map
    """
    Read in the cities from the given `file_name`, and return 
    them as a list of four-tuples: 

      [(state, city, latitude, longitude), ...] 

    Use this as your initial `road_map`, that is, the cycle 

      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """
    pass
  
def print_cities(road_map):
    print_map = []
    for city in road_map:
        print_map.append((city[0], city[1], (round(float(city[2]), 1), round(float(city[3]), 1))))
    print (print_map)
    """
    Prints a list of cities, along with their locations. 
    Print only one or two digits after the decimal point.
    """ 
    pass

def compute_total_distance(road_map):
    total_distance = 0.0
    r = road_map
    i = -1
    while i < len(r) - 1: 
        total_distance += distance(float(r[i][2]), float(r[i][3]), float(r[i + 1][2]), float(r[i + 1][3]),float(road_map[(i+1)%len(road_map)][2]), float(road_map[(i+1)%len(road_map)][3])))
        i += 1
    return total_distance
    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    
    pass


def swap_cities(road_map, index):
    new_road_map = road_map[:]
    new_road_map[index] = road_map[(index+1) % len(road_map)]
    new_road_map[(index+1) % len(road_map)] = road_map[index]
    new_total_distance = compute_total_distance(new_road_map)
    return (new_road_map, new_total_distance)
    
    """
    Take the city at location `index` in the `road_map`, and the 
    city at location `index2`, swap their positions in the `road_map`, 
    compute the new total distance, and return the tuple 

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """
    pass

def shift_cities(road_map):
    for i in road_map:
        i = road_map[-1:] + road_map[:-1] 
    return (road_map)
    new_road_map = road_map[:]
     for city in road_map:
        city += 1
        new_road_map.append((city[0], city[1], round(float(city[2]), 1),round(float(city[3]), 1)))
    return new_road_map
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map. 
    """
    pass

def find_best_cycle(road_map):
    shortest_distance = None
    best_cycle = road_map[:]
    for n in range(0, 10000):
        index1 = random.randint(0, len(road_map) - 1)
        index2 = random.randint(0, len(road_map) - 1)
        (new_cycle1, distance1) = swap_cities(best_cycle, index1, index2)  
        if shortest_distance is None or distance1 < shortest_distance:
            shortest_distance = distance1
            best_cycle = new_cycle1
    for n in range(0, 10000):
        index = random.randint(0, len(road_map) - 1)
        (new_cycle2, distance2) = swap_adjacent_cities(best_cycle, index)
        if distance2 < shortest_distance:
            shortest_distance = distance2
            best_cycle = new_cycle2
    return best_cycle
            
    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """
    pass

def print_map(road_map):
    for i in range(0, len(road_map)):
        print ("From", road_map[i][0], "to", road_map[(i + 1) % len(road_map)][0], "is", distance(float(road_map[i][2]), float(road_map[i][3]), float(road_map[(i + 1) % len(road_map)][2]), float(road_map[(i + 1) % len(road_map)][3])))
    print ("\nThe total cost is:", compute_total_distance(road_map))
    
    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """
    pass

def main():
    road_map = read_cities("city-data.txt")
    print_cities(road_map)
    compute_total_distance(road_map)
    find_best_cycle(road_map)
    print_map(road_map)
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    pass

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(‘city-data.txt’)
def visualise(road_map):
    

if __name__ == "__main__": #keep this in
    main()
