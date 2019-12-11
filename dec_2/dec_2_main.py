from dec_2.data import data, test_data
from dec_2.dec_2_calc import op_code_processor, reverse_program


if __name__ == "__main__":
    dec_2_part_1 = op_code_processor(data)
    print("Completed opcode:", dec_2_part_1)

    target_value = 19690720

    initial_set = reverse_program(dec_2_part_1)
    print("Initial set for target value", target_value, "is", initial_set)
