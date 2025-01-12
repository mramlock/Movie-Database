"""
-------------------------------------------------------
Tests various array-based sorting functions.
-------------------------------------------------------
Author:  Ahmed Maher
ID:      169037984
Email:   mahe7984@mylaurier.ca
__updated__ = "2023-03-29"
-------------------------------------------------------
"""
# Imports
import random
from Number import Number
from Sorts_array import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
    ('Bin. Ins. Sort', Sorts.binary_insert_sort),
    ('BST Sort', Sorts.bst_sort),
    ('Cocktail Sort', Sorts.cocktail_sort),
    ('Comb Sort', Sorts.comb_sort),
    ('Heap Sort', Sorts.heap_sort),
    ('Shell Sort', Sorts.shell_sort)
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted list of SIZE Number objects with values
        from 0 up to SIZE-1.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """

    # your code here
    values = []
    for i in range(SIZE):
        values.append(Number(i))

    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed list of SIZE Number objects with values
        from SIZE-1 down to 0.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """

    # your code here
    values = []
    for i in range(SIZE - 1, -1, -1):
        values.append(Number(i))
    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TESTS rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        arrays - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of list of Number)
    -------------------------------------------------------
    """

    # your code here
    arrays = []
    for i in range(TESTS):
        a = []
        for i in range(SIZE):
            b = random.randint(0, XRANGE)
            a.append(Number(b))
        arrays.append(a)
    return arrays


def test_sort(title, func):
    """
    -------------------------------------------------------
    Test a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of arrays in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """

    # your code here
    a = create_sorted()
    b = create_reversed()
    c = create_randoms()
    func(a)
    a_c = round(Number.comparisons, 0)
    a_s = round(Sorts.swaps, 0)
    Number.comparisons = 0
    Sorts.swaps = 0
    func(b)
    b_c = round(Number.comparisons, 0)
    b_s = round(Sorts.swaps, 0)
    Number.comparisons = 0
    Sorts.swaps = 0
    for a in c:
        func(a)
    c_c = round(Number.comparisons // TESTS, 0)
    c_s = round(Sorts.swaps // TESTS, 0)
    Number.comparisons = 0
    Sorts.swaps = 0
    print("{:14} {:8} {:8} {:8} {:8} {:8} {:8}".format(
        title, a_c, b_c, c_c, a_s, b_s, c_s))
    return
