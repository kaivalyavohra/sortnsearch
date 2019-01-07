import time
def linearsearch(thelist,typeof):
    comparisons = 0
    #get search item
    if typeof == "int":
        searchitem = int(input("What number would you like to search for: "))
    else:
        searchitem = input("What would you like to search for: ")

    starttime = time.time()
    #iterate through the list while checking
    for i in thelist:
        comparisons += 1
        if i == searchitem:
            print("Found")
            print("Time taken for linear search: ", round(
            (time.time() - starttime) * 1000, 2), "milliseconds. Comparisons:", comparisons, "Big O: n. Omega: 1.")
            #break out if found
            return True
    print("Not Found")
    print("Time taken for linear search: ", round(
            (time.time() - starttime) * 1000, 2), "milliseconds. Comparisons:", comparisons, "Big O: n. Omega: 1.")
    return False
