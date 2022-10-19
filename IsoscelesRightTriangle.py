import math


class IsoscelesRightTriangle:
    def __init__(self, element_number, element_value):
        self.element_number = element_number
        self.element_value = element_value
        self.array_of_elements = []

    def zero_error(self, a, c, h, s):
        temp_list = [a, c, h, s]
        for i in temp_list:
            if i < 0:
                raise ZeroDivisionError

    def the_value_of_the_leg(self):
        a = self.element_value
        c = math.sqrt(2) * a
        h = c / 2
        s = c * h / 2
        return self.add_to_array(a, c, h, s)

    def the_value_of_the_hypotenuse(self):
        c = self.element_value
        a = c / math.sqrt(2)
        h = c / 2
        s = c * h / 2
        return self.add_to_array(a, c, h, s)

    def the_value_of_the_height(self):
        h = self.element_value
        c = 2 * h
        a = c / math.sqrt(2)
        s = c * h / 2
        return self.add_to_array(a, c, h, s)

    def the_value_of_the_area(self):
        s = self.element_value
        c = math.sqrt(s * 4)
        a = c / math.sqrt(2)
        h = c / 2
        return self.add_to_array(a, c, h, s)

    def counting_from_element_number(self):
        if self.element_number == 1:
            elements_value = self.the_value_of_the_leg()
        elif self.element_number == 2:
            elements_value = self.the_value_of_the_hypotenuse()
        elif self.element_number == 3:
            elements_value = self.the_value_of_the_height()
        elif self.element_number == 4:
            elements_value = self.the_value_of_the_area()
        else:
            raise Exception('Incorrect element number')
        return elements_value

    def add_to_array(self, a, c, h, s):
        self.zero_error(a, c, h, s)
        self.array_of_elements.append(a)
        self.array_of_elements.append(c)
        self.array_of_elements.append(h)
        self.array_of_elements.append(s)
        return self.array_of_elements

# triangle = IsoscelesRightTriangle(1, 0.2348)
# print(triangle.counting_from_element_number())
