from upstart.solver import func
from numpy.testing import assert_almost_equal
import numpy as np


def test_flat_case():
    savings = [5, 5, 5, 5, 5]
    assert func(savings) == [5, 5, 5, 5, 5]


def test_increaing_case():
    savings = [5, 5, 5, 10, 10]
    assert func(savings) == [5, 5, 5, 10, 10]


def test_decreasing_case():
    savings = [10, 10, 5, 5, 5]
    assert func(savings) == [7, 7, 7, 7, 7]


def test_oscillation_case():
    savings = [10, 5, 10, 5, 10]
    assert_almost_equal(
        np.array(func(savings)),
        np.array([8, 7, 8.3333, 6.6667, 10]),
        decimal=4,
    )


def test_spike_case():
    savings = [2.5, 5, 100, 5, 2.5]
    assert_almost_equal(
        np.array(func(savings)),
        np.array([2.5, 5, 35.8333, 35.8333, 35.8333]),
        decimal=4,
    )
