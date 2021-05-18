#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    result_div = 0
    for i in range(0, list_length):
        try:
            result_div = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            result_div = 0
            print("division by 0")
        except TypeError:
            result_div = 0
            print("wrong type")
        except IndexError:
            result_div = 0
            print("out of range")
        finally:
            new_list.append(result_div)
    return new_list
