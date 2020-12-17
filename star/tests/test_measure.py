"""
Tests for the measure module
"""

import star
import numpy as np
import math
import pytest

def test_calculate_distance():
	r1 = np.array([0, 0, 0])
	r2 = np.array([0, 1, 0])

	expected_distance = 1

	calculated_distance = star.calculate_distance(r1, r2)

	assert expected_distance == calculated_distance	
	##assert 1 == 2	

def test_calculate_angle():
	r1 = np.array([0, 0, -1])
	r2 = np.array([0, 0, 0])
	r3 = np.array([1, 0, 0])

	expected_angle = math.pi/2

	calculated_angle = star.calculate_angle(r1, r2, r3)

	assert pytest.approx(expected_angle) == calculated_angle	
	##assert 1 == 2	

@pytest.mark.parametrize("p1, p2, p3, expected_angle",[ 
(np.array([np.sqrt(2)/2,np.sqrt(2)/2,0]),np.array([0,0,0]),np.array([1,0,0]),math.pi/4),
(np.array([0,0,-1]),np.array([0,1,0]),np.array([1,0,0]),math.pi/3)
])
def test_calculate_angle_many(p1, p2, p3, expected_angle):
	calculated_value = star.calculate_angle(p1,p2,p3)
	assert pytest.approx(expected_angle) == calculated_value
