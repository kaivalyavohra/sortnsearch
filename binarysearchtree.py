import time
comps = 0
found = False
#comparison checker
#normally would not use global variable but in this case potentially the best
#http://wiki.c2.com/?GlobalVariablesAreBad
def compsIncrement():
    global comps
    comps+=1
#OOP implementation of a binary search tree
class Node:
    def __init__(self, value):
        self.val = value
        self.rn = None
        self.ln = None
    #insert new node
    def insert(self, n):
        if n < self.val:
            if self.ln != None:
                self.ln.insert(n)
            else:
                self.ln = Node(n)
        elif n > self.val:
            if self.rn != None:
                self.rn.insert(n)
            else:
                self.rn = Node(n)
    #pre order traversal
    def display(self):
        print(self.val)
        if self.ln != None:
            self.ln.display()
        if self.rn != None:
            self.rn.display()
    #traverse down tree to find item
    def find(self, n):
        compsIncrement()
        if n < self.val:
            if self.ln != None:
                self.ln.find(n)
            else:
                print("Not Found")
        elif n > self.val:
            if self.rn != None:
                self.rn.find(n)
            else:
                print("Not Found")
        elif n == self.val:
            global found
            found = True
            print("Found")
        

def btsearch(arr,typeof):
    #initialise new tree root node
    node1 = Node(arr[0])
    #iterate through rest of the array inserting into tree
    for i in range(1, len(arr)):
        node1.insert(arr[i])
    #get search item
    if typeof == "int":
        searchitem = int(input("What number would you like to search for: "))
    else:
        searchitem = input("What would you like to search for: ")
    starttime = time.time()
    found = node1.find(searchitem)
    print("Time taken for binary tree search: ", round(
            (time.time() - starttime) * 1000, 2), "milliseconds. Comparisons:", comps, "Big O: n log n. Omega: n log n.")
    return found



