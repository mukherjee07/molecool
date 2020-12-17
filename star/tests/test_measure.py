"""
Tests for the measure module
"""

import star
import numpy as np

def test_calculate_distance():
	r1 = np.array([0, 0, 0])
	r2 = np.array([0, 1, 0])

	expected_distance = 2

	calculated_distance = star.calculate_distance(r1, r2)

	assert expected_distance == calculated_distance	
	##assert 1 == 2	

