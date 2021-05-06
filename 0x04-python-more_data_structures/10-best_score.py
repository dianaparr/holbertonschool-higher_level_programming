#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        # For return key as a string with the name of key
        key = ""
        best_s = 0
        for v in a_dictionary:
            if a_dictionary.get(v) > best_s:
                key = v
                best_s = a_dictionary.get(v)
        return key
    else:
        return None
