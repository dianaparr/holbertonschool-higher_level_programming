#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        tuple_two = (len(sentence), None)
    else:
        # other form represents position 0 of the string with splice
        tuple_two = len(sentence), sentence[:1]
    return tuple_two
