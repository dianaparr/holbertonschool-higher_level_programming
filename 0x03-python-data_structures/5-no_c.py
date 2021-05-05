#!/usr/bin/python3
def no_c(my_string):
    # Create a string empty
    string_two = ""
    len_my_string = len(my_string)
    for c in range(0, len(my_string)):
        # If the condition is met, fill in the empty string created
        if my_string[c] != 'c' and my_string[c] != 'C':
            string_two += my_string[c]
    return string_two
