import time
comps = 0
found = False

#comparison checker
#normally would not use global variable but in this case potentially the best
#http://wiki.c2.com/?GlobalVariablesAreBad
def compsIncrement():
    global comps
    comps += 1


def binsearch(arr,typeof):
    
    #get search item
    if typeof == "int":
        x = int(input("What number would you like to search for: "))
    else:
        x = input("What would you like to search for: ")
    starttime = time.time()
    #recursive definition of find func
    def find(arr, n):
        global found
        middle = (len(arr) - 1) // 2
        #base case
        if n != arr[middle] and len(arr) == 1:
            print("Not Found")
            compsIncrement()
            return 0
        compsIncrement()
        if n == arr[middle]:
            print("Found")
            found = True
            return 0
        #call find on half of the array each time
        if n < arr[middle]:
            find(arr[:middle], n)
        elif n > arr[middle]:
            find(arr[middle + 1:], n)

    find(arr, x)
    print("Time taken for binary search: ", round(
            (time.time() - starttime) * 1000, 2), "milliseconds. Comparisons:", comps, "Big O: log n. Omega: 1.")
    return found
