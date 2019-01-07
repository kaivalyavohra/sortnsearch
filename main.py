print("DISCLAIMER: Only merge sort works with string arrays.")

#import statements
import time
from generate import gen
from importing import importlist
from msort import mergesort
from bubble import bubblesort
from insertion import insertionsort
from linearsearch import linearsearch
from binarysearchtree import btsearch
from binarysearch import binsearch

# generate/import array
startingarrgen = input(
    '''\nEnter 1 if you want to generate an array of number.\nEnter 2 if you want to import numbers from a text file: ''')
# validation
while startingarrgen not in ["1", "2"]:
    print("Invalid")
    startingarrgen = input(
        '''\nEnter 1 if you want the program to generate an array of number.\nEnter 2 if you want to import numbers from a text file: ''')
listtype = "int"
startarray = []
if startingarrgen == "1":
    n = input("\nHow many integers would you like to generate: ")
    x = input("What is the minimum value of integers: ")
    y = input("What is the maximum value of integers: ")
    while not n.isdigit() or not x.isdigit or not y.isdigit() or int(n) < 0 or y < x:
        print("\nInvalid input")
        n = input("\nHow many integers would you like to generate: ")
        x = input("What is the minimum value of integers: ")
        y = input("What is the maximum value of integers: ")
    startarray = gen(int(n), int(x), int(y))
else:
    print("\nYou can import txt or csv files. Please see README for formatting.")
    filename = input("\nEnter the file name please: ")
    while ".txt" not in filename and ".csv" not in filename:
        print("\nInvalid extension.")
        filename = input("\nEnter the file name please: ")
    listtype = input(
        "\nEnter str if the list is of string. Enter int if list is of numbers: ")
    while listtype not in ["int", "str"]:
        print("Invalid")
        listtype = input(
            "\nEnter str if the list is of string. Enter int if list is of numbers: ")

    try:
        startarray = importlist(filename, listtype)
    except FileNotFoundError:
        print("Sorry. No such file. Goodbye")
        exit(1)


# Sorting functions
def sort(arr):
    sortedarr = []
    starttime = time.time()
    whichsort = input(
        "Enter 1 for bubblesort or 2 for insertion sort 3 for mergesort: ")
    while whichsort not in ["1", "2","3"]:
        print("Invalid")
        whichsort = input(
            "Enter 1 for bubblesort or 2 for insertion sort 3 for mergesort: ")
    if whichsort == "1":
        if listtype == "int":
            starttime = time.time()
            sortedarr = bubblesort(startarray)
            print("Time taken for bubblesort: ", round(
                (time.time() - starttime) * 1000, 2), "milliseconds. Comparisons:", sortedarr[1], "Big O: n squared. Omega: n.")
        else:
            print("Sorry bubble sort only works with integers")
            sortedarr=[0,0]
    elif whichsort == "2":
        if listtype == "int":
            starttime = time.time()
            sortedarr = insertionsort(startarray)
            print("Time taken for insertion sort: ", round(
                (time.time() - starttime) * 1000, 2), "milliseconds. Comparisons:", sortedarr[1], "Big O: n squared. Omega: n.")
        else:
            print("Sorry insertion sort only works with integers")
            sortedarr=[0,0]
    else:
        starttime = time.time()
        sortedarr = mergesort(startarray)
        print("Time taken for mergesort: ", round(
            (time.time() - starttime) * 1000, 2), "milliseconds. Comparisons:", sortedarr[1], "Big O: n log n. Omega: n log n.")
    
    z = input("Enter anything if you want to see the array. Enter nothing if you do not.")
    if z == "":
        return sortedarr[0]
    else:
        print(sortedarr[0])
        return sortedarr[0]

# Searching functions
def search(arr):
    starttime = time.time()
    whichsearch = input(
        "Enter 1 for linear search or 2 for binary search or 3 for binary tree search: ")
    while whichsearch not in ["1", "2", "3"]:
        print("Invalid")
        whichsearch = input(
            "Enter 1 for linear search or 2 for binary search or 3 for binary tree search: ")
    if whichsearch == "1":
        comparisons = linearsearch(arr, listtype)

    elif whichsearch == "2":
        print("The list must be sorted first.")
        arr = sort(arr)
        binsearch(arr, listtype)

    else:
        btsearch(arr, listtype)

#keep asking for sort/search
choice = "0"
while choice != "3":
    choice = input("\nEnter 1 to sort.\nEnter 2 to search.\nEnter 3 to quit: ")
    while choice not in ["1", "2", "3"]:
        print("Invalid")
        choice = input(
            "\nEnter 1 to sort.\nEnter 2 to search.\nEnter 3 to quit: ")

    if choice == "1":
        sort(startarray)
    elif choice == "2":
        search(startarray)
