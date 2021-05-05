#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) is None:
        tuple_two = len(sentence), None
        return tuple_two
    else:
        # other form represents position 0 of the string with splice
        tuple_two = len(sentence), sentence[:1]
        return tuple_two
