#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        # For return key as a string with the name of key
        key = ""
        best_s = 0
        for v in a_dictionary:
            # If the value is bigger that the score, the variables key
            # and best_s take their corresponding values
            if a_dictionary.get(v) > best_s:
                key = v
                best_s = a_dictionary.get(v)
        return key
    else:
        return None
