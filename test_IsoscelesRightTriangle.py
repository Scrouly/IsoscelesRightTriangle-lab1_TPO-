import pytest

from IsoscelesRightTriangle import IsoscelesRightTriangle


# @pytest.fixture()
# def class_init():
#     return IsoscelesRightTriangle(1, 11.31370849898476)


@pytest.mark.parametrize(
    "number, value, result",
    [
        (1, 11.31370849898476, [11.31370849898476, 16.0, 8.0, 64.0]),
        (2, 16, [11.31370849898476, 16.0, 8.0, 64.0]),
        (3, 8, [11.31370849898476, 16.0, 8.0, 64.0]),
        (4, 64, [11.31370849898476, 16.0, 8.0, 64.0]),
        (1, 0.2348, [0.2348, 0.33205734444520274, 0.16602867222260137, 0.027565520000000003]),
        (2, 0.33205734444520274, [0.2348, 0.33205734444520274, 0.16602867222260137, 0.027565520000000003]),
        (3, 0.16602867222260137, [0.2348, 0.33205734444520274, 0.16602867222260137, 0.027565520000000003]),
        (4, 0.027565520000000003, [0.2348, 0.33205734444520274, 0.16602867222260137, 0.027565520000000003]),
    ]
)
def test_result(number, value, result):
    triangle = IsoscelesRightTriangle(number, value)
    assert triangle.counting_from_element_number() == result


@pytest.mark.parametrize(
    "number, value",
    [
        (0, -5),
        (-2, 540),
        (3.33, 68),
        (-3.000015, 2.24),
    ]
)
def test_incorrect_number(number, value):
    triangle = IsoscelesRightTriangle(number, value)
    with pytest.raises(Exception):
        triangle.counting_from_element_number()


@pytest.mark.parametrize(
    "number, value",
    [
        (1, -5),
        (2, -2.542),
        (3, -0.5474),
        (4, -4454121),
    ]
)
def test_incorrect_number(number, value):
    triangle = IsoscelesRightTriangle(number, value)
    with pytest.raises(Exception):
        triangle.counting_from_element_number()