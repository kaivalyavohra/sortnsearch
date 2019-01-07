def insertionsort(arr):
    #initialize comparisons
    comps = 0
    #initialize new array with a value that is bigger than any in the start array
    finalarr = [max(arr) + 1]
    #loop through and insert at the right place
    for i in range(0, len(arr)):
        comps += 1
        counter = 0
        while arr[i] > finalarr[counter]:
            comps += 1
            counter += 1
        finalarr.insert(counter, arr[i])
    #remove final value that we added at the start
    finalarr.pop()
    return (finalarr, comps)
