"""
Unit and regression test for the star package.
"""

# Import package, test suite, and other packages as needed
import star
import pytest
import sys

def test_star_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "star" in sys.modules
