def op_code_processor(input_list, reverse_value=False):
    new_dict = {}
    counter = 0
    output = input_list
    operational_values = [1, 2]
    termination_value = 99

    for opcode in input_list:
        new_dict[counter] = opcode
        counter += 1

    for key, value in new_dict.items():

        if key % 4 == 0:
            if value in operational_values:
                if reverse_value is True:
                    new_dict[new_dict[key + 3]] = reverse_value_analysis(key, value, new_dict)
                else:
                    new_dict[new_dict[key + 3]] = value_analysis(key, value, new_dict)
            elif value == termination_value:
                new_dict[key] = "PROGRAM TERMINATED"
                final_values = list(new_dict.values())
                return final_values[:key + 1]
            else:
                new_dict[key] = "1202 PROGRAM ALARM"
                final_values = list(new_dict.values())
                return final_values[:key]

    return output


def value_analysis(key, value, new_dict):
    new_value = 0
    if value == 1:
        new_value = new_dict[new_dict[key + 1]] + new_dict[new_dict[key + 2]]
    elif value == 2:
        new_value = new_dict[new_dict[key + 1]] * new_dict[new_dict[key + 2]]

    return new_value


def reverse_program(data_input: list):
    reversed_data_as_lists = []
    reversed_data_list = []
    new_dict = {}
    counter = 0

    for opcode in data_input:
        new_dict[counter] = opcode
        counter += 1

    for key, value in new_dict.items():
        if key % 4 == 0:
            reversed_data_as_lists.append(data_input[key:key + 4])

    reversed_data_as_lists = reversed_data_as_lists[::-1]
    reversed_data_as_lists = reversed_data_as_lists[1:]

    for element in reversed_data_as_lists:
        for data in element:
            reversed_data_list.append(data)

    initial_code = op_code_processor(input_list=reversed_data_list, reverse_value=True)
    reverse_engineered_first_group = initial_code[len(initial_code) - 4:]

    return reverse_engineered_first_group


def reverse_value_analysis(key, value, new_dict):
    new_value = 0
    if value == 1:
        new_value = new_dict[new_dict[key + 1]] - new_dict[new_dict[key + 2]]
    elif value == 2:
        new_value = new_dict[new_dict[key + 1]] / new_dict[new_dict[key + 2]]

    return new_value
