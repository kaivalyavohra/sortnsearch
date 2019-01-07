def bubblesort(arr):
    #initialze variables (comparisons, swaps)
    comps, swaps = 0,1    
    #keep bubbling until no swaps
    while swaps > 0:
        comps += 1
        #reset swaps to 0
        swaps = 0
        #loop through arr
        for i in range(0, len(arr) - 1):
            comps += 1
            #swap if required
            if arr[i] > arr[i + 1]:
                temp = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = temp
                swaps += 1
    #return sorted array and number of comparisons
    return (arr, comps)
