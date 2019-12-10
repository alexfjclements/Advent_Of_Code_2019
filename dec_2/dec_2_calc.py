def op_code_processor(input_list):
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
    elif value == 99:
        new_value = "PROGRAM TERMINATED"

    return new_value
