import pytest
from cithara.core.interval import Interval


def test_interval_initialisation():
    interval = Interval(3)
    assert interval.semitones == 3
    assert interval.interval_name == "Minor Third"

def test_invalid_interval_raises():
    with pytest.raises(ValueError):
        Interval("hello")
    
    with pytest.raises(ValueError):
        Interval([5])

def test_handle_large_interval():
    interval = Interval(77)
    assert interval.semitones == 5
    assert interval.interval_name == "Perfect Fourth"

def test_handle_negative_interval():
    with pytest.raises(ValueError):
        Interval(-1)
