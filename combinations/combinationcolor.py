from enum import Enum


def get_template_color(number):
    return "TEMPLATE_COLOR_" + str(number + 1)


class CombinationColor(Enum):
    SOLUTION_COLOR = "SOLUTION_COLOR"
    TEMPLATE_COLOR = "TEMPLATE_COLOR_"
