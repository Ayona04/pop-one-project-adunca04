import pytest
from cities import *

def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    assert compute_total_distance(road_map1)==\
           pytest.approx(9.386+18.496+10.646, 0.01)

    assert compute_total_distance(road_map1)==\
                               distance(38.197274, -84.86311, 39.161921, -75.526755) + \
                               distance(39.161921, -75.526755, 44.95, -93.094) + \
                               distance( 44.95, -93.094, 38.197274, -84.86311), "should be 38.24 "  
    assert compute_total_distance(road_map1)((9.386+18.496+10.646)) == 38, "should be 38.524 "
    assert compute_total_distance(road_map1)((9.386+18.496+10.646)) == 59.543,"should be 38.524 "
    assert compute_total_distance(road_map1)((9.386+18.496+10.646)) == 60,"should be 38.524 "
    assert compute_total_distance(road_map1)((9.386+18.496+44.95+-93.094)) == 38.524,"should be 38.524"

if __name__ == "__main__":
    test_compute_total_distance()
    print("Everything passed")

def test_swap_cities():
    road_map1 =  [('Colorado', 'Denver', '39.7391667', '-104.984167'),\
                  ('Connecticut', 'Hartford', '41.767', '-72.677'),\
                  ('Delaware', 'Dover', '39.161921', '-75.526755'),\
                  ('Florida', 'Tallahassee', '30.4518', '-84.27277')]
    new_road_map1 = [('Colorado', 'Denver', '39.7391667', '-104.984167'),\
		     ('Connecticut', 'Hartford', '41.767', '-72.677'),\
		     ('Florida', 'Tallahassee', '30.4518', '-84.27277'),\
		     ('Delaware', 'Dover', '39.161921', '-75.526755')]
	new_total_distance1 = compute_total_distance(new_road_map1)
	assert (swap_cities(road_map1,1,3)),\
	(new_road_map1, new_total_distance1)
	
    assert (swap_cities
    assert (swap_cities
    assert (swap_cities
    assert (swap_cities

def test_shift_cities():
	
    '''add your tests'''


