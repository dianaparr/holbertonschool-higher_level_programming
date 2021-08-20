#!/usr/bin/python3
""" Module that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ Function based in algorithm of binary search
        Source: https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/
    """
    lengthArr = len(list_of_integers)
    if not lengthArr:
        return None
    return recursionPeak(list_of_integers, 0, lengthArr - 1, lengthArr)


def recursionPeak(arr, low, high, lengthArr):
    """ Function recursive """
    numberMid = int(low + (high - low)/2)

    if ((numberMid == 0 or arr[numberMid - 1] <= arr[numberMid]) and
       (numberMid == lengthArr - 1 or arr[numberMid + 1] <= arr[numberMid])):
            return arr[numberMid]

    elif (numberMid > 0 and arr[numberMid - 1] > arr[numberMid]):
        return recursionPeak(arr, low, (numberMid - 1), lengthArr)

    else:
        return recursionPeak(arr, (numberMid + 1), high, lengthArr)
