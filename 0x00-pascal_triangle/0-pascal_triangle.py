#!/usr/bin/python3
""" pascal triangle
"""


def pascal_triangle(n):
    """ returns pascal triangle
    """
    if n <= 0:
        return []

    pt = []

    for i in range(n):
        # first element
        my_List = [1]
        if i == 0:
            pt.append(my_List)
            continue

        k = i - 1
        for j in range(len(pt[k])):
            if j + 1 == len(pt[k]):
                # last element
                my_List.append(1)
                break
            # Add two previous values to get current next value
            nextVal = pt[k][j] + pt[k][j + 1]
            my_List.append(nextVal)
        pt.append(my_List)

    return pt
