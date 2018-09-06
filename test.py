#/usr/bin/env python

import unittest
from numpy.testing import assert_array_almost_equal

from assignment3 import *

class TestSolution(unittest.TestCase):
    
	def test_water_rel_perm(self):
	    
	    assert_array_almost_equal(water_rel_perm(0.6, 0.2, 0.2, 3), (0.0, 0.07499999999999994, 0.6), decimal=1)


	def test_add_well_activity(self):
	    
	    well_list1 = add_well_activity([['well1', 'producing', '0']], 'well2', 'shut-in', '100')
	    well_list2 = add_well_activity(well_list1, 'well3', 'injecting', '10')
	    
	    
	    assert well_list2 == [['well1', 'producing', '0'], 
				  ['well3', 'injecting', '10'], 
				  ['well2', 'shut-in', '100']] 



	def test_add_well_activity_from_file(self):
	    
	    well_list = add_well_activity_from_file('well_activity.csv', 'well4', 'injecting', '1000')
	    
	    assert well_list == [['well1', 'producing', '0'], 
				 ['well2', 'shut-in', '0'], 
				 ['well3', 'shut-in', '0'],
				 ['well4', 'injecting', '1000'],
				 ['well2', 'injecting', '2000'],
				 ['well3', 'producing', '3000'],
				 ['well1', 'injecting', '3000'],
				 ['well1', 'shut-in', '7000'],
				 ['well2', 'shut-in', '7000'],
				 ['well3', 'shut-in', '7000']] 


	def test_get_bhp_well_values(self):

	    assert abs(get_bhp_well_values({'wells': {'bhp': {'values': 10.0}}}) - 10.0) < 1e-6


	def test_get_bhp_well_values_from_file(self):
	    
	    assert_array_almost_equal(get_bhp_well_values_from_file('wells.yml'), [2200.0, 2000.0], decimal=1)


if __name__ == '__main__':
    unittest.main()

