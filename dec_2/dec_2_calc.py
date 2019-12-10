

def op_code_processor(input_list):
    new_dict = {}
    counter = 1
    output = []
    allowed_values = [1, 2, 99]

    for opcode in input_list:
        new_dict[counter] = opcode
        counter += 1

    for key, value in new_dict.items():

        if key % 4 == 0 and value in allowed_values:  # TODO fix to pick out correct keys
            output.append(value_analysis(key, value, new_dict))
        else:
            output.append("1202 PROGRAM ALARM")

    return output


def value_analysis(key, value, new_dict):
    sublist = [value, new_dict[key + 1], new_dict[key + 2]]
    if value == 1:
        sublist.append(new_dict[key + 1] + new_dict[key + 2])
    elif value == 2:
        sublist.append(new_dict[key + 1] * new_dict[key + 2])
    elif value == 99:
        sublist.append("PROGRAM TERMINATED")

    return sublist
