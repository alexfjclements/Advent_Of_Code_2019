import math


def basic_fuel_sum(input_list):
    total_mass = sum(input_list)
    basic_fuel_requirement = math.floor(total_mass/3) - 2

    return basic_fuel_requirement


def complex_fuel_calc(input_list):
    list_of_fuel_requirements = [recursive_fuel_sum(input_mass=mass) for mass in input_list]
    total_fuel_requirements = sum(list_of_fuel_requirements)

    return total_fuel_requirements


def recursive_fuel_sum(input_mass=None, current_fuel=None, total_fuel=0):
    if current_fuel is None:
        current_fuel = math.floor(input_mass/3) - 2
        return recursive_fuel_sum(current_fuel=current_fuel)
    else:
        if current_fuel > 0:
            total_fuel = total_fuel + current_fuel
            current_fuel = math.floor(current_fuel/3) - 2
            return recursive_fuel_sum(current_fuel=current_fuel, total_fuel=total_fuel)
        return total_fuel

