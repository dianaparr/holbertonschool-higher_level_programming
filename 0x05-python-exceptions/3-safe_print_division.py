#!/usr/bin/python3
def safe_print_division(a, b):
    result_div = 0
    try:
        result_div = a / b
        return result_div
    except ZeroDivisionError:
        result_div = None
        return None
    finally:
        print("Inside result: {}".format(result_div))
