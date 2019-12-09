from dec_1.data import dec_1_data_set
from dec_1.dec_1_calcs import basic_fuel_sum, complex_fuel_calc


if __name__ == "__main__":

    # Day one part one:
    print("Dec 1 part 1 answer:", basic_fuel_sum(dec_1_data_set), "units of fuel.")

    # Day one part two:
    print("Dec 1 part 2 answer:", complex_fuel_calc(dec_1_data_set), "units of fuel.")
