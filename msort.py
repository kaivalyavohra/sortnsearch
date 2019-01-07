#initialize comparsions
comps = 0

#helper function that joins two sorted arrays
def join(arr1, arr2):
    global comps
    if len(arr1) == 0:
        return(arr2)
    if len(arr2) == 0:
        return(arr1)

    x = []
    counter1, counter2 = 0, 0
    while counter1 < len(arr1) and counter2 < len(arr2):
        comps += 1
        if arr1[counter1] < arr2[counter2]:
            x.append(arr1[counter1])
            counter1 += 1

        else:
            x.append(arr2[counter2])
            counter2 += 1
    #add left over values 
    x.extend(arr1[counter1:])
    x.extend(arr2[counter2:])

    return(x)

#main merge sort function
def main(arr):
    global comps
    comps += 1
    if len(arr) <= 1:
        return arr
    #run recursive merge sort
    leftarr, rightarr = main(arr[:len(arr) // 2]), main(arr[len(arr) // 2:])

    return join(leftarr, rightarr)

#return sorted array and number of compaprisons
def mergesort(arr):
    return(main(arr),comps)


