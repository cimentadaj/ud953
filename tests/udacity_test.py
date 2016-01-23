# -*- coding: utf-8 -*-
# Author: github.com/madhavajay
"""
This is a test that answers the Udacity Quizzes for ud953
https://www.udacity.com/course/linear-algebra-refresher-course--ud953
"""
from decimal import Decimal, getcontext
from vector import Vector

# set the decimal precision
getcontext().prec = 30


def test_plus_minus_scalar_multiply():
    """Quiz 1 addition, subtraction and multiplication with Vectors"""
    vector1 = Vector([8.218, -9.341])
    vector2 = Vector([-1.129, 2.111])
    answer1 = Vector([7.089, -7.23]).round_coords(3)
    assert (vector1 + vector2).round_coords(3) == answer1

    vector3 = Vector([7.119, 8.215])
    vector4 = Vector([-8.223, 0.878])
    answer2 = Vector([15.342, 7.337]).round_coords(3)
    assert (vector3 - vector4).round_coords(3) == answer2

    scalar1 = 7.41
    vector5 = Vector([1.671, -1.012, -0.318])
    answer3 = Vector([12.382, -7.499, -2.356]).round_coords(3)
    assert (vector5 * scalar1).round_coords(3) == answer3


def test_magnitude_and_normalize():
    """Quiz 2 calculating magnitude and normalization of Vectors"""
    vector1 = Vector([-0.221, 7.437])
    answer1 = Decimal('7.440')
    assert round(vector1.magnitude(), 3) == answer1

    vector2 = Vector([8.813, -1.331, -6.247])
    answer2 = Decimal('10.884')
    assert round(vector2.magnitude(), 3) == answer2

    vector3 = Vector([5.581, -2.136])
    answer3 = Vector([0.934, -0.357]).round_coords(3)
    assert vector3.normalize().round_coords(3) == answer3

    vector4 = Vector([1.996, 3.108, -4.554])
    answer4 = Vector([0.340, 0.530, -0.777]).round_coords(3)
    assert vector4.normalize().round_coords(3) == answer4


def test_dot_product_and_angle():
    """Quiz 3 calculating the dot product and angle of two Vectors"""
    vector1 = Vector([7.887, 4.138])
    vector2 = Vector([-8.802, 6.776])
    answer1 = Decimal('-41.382')
    assert round(vector1.dot_product(vector2), 3) == answer1

    vector3 = Vector([-5.955, -4.904, -1.874])
    vector4 = Vector([-4.496, -8.755, 7.103])
    answer2 = Decimal('56.397')
    assert round(vector3.dot_product(vector4), 3) == answer2

    vector5 = Vector([3.183, -7.627])
    vector6 = Vector([-2.668, 5.319])
    answer3 = 3.072
    assert round(vector5.angle_radians(vector6), 3) == answer3

    vector7 = Vector([7.35, 0.221, 5.188])
    vector8 = Vector([2.751, 8.259, 3.985])
    answer4 = 60.276
    assert round(vector7.angle_degrees(vector8), 3) == answer4


def test_parallel_or_orthogonal():
    """Quiz 4 checking for parallelism and orthogonality"""
    vector1 = Vector([-7.579, -7.88])
    vector2 = Vector([22.737, 23.64])
    assert vector1.is_parallel(vector2) is True
    assert vector1.is_orthogonal(vector2) is False

    vector3 = Vector([-2.029, 9.97, 4.172])
    vector4 = Vector([-9.231, -6.639, -7.245])
    assert vector3.is_parallel(vector4) is False
    assert vector3.is_orthogonal(vector4) is False

    vector5 = Vector([-2.328, -7.284, -1.214])
    vector6 = Vector([-1.821, 1.072, -2.94])
    assert vector5.is_parallel(vector6) is False
    assert vector5.is_orthogonal(vector6) is True

    vector7 = Vector([2.118, 4.827])
    vector8 = Vector([0, 0])
    assert vector7.is_parallel(vector8) is True
    assert vector7.is_orthogonal(vector8) is True