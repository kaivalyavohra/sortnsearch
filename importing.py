from csv import reader


def importlist(filename, typeof):
    contents = []

    if ".txt" in filename:
        #read file and put values into an array
        file = open(filename, "r")
        contents = file.read().split(",")
    
    elif ".csv" in filename:
        with open(filename, newline='') as file:
            csvreader = reader(file, delimiter=' ', quotechar='|')
            #read file and put values into an array
            for row in csvreader:
                contents = row[0].split(",")
    else:
        print("Sorry invalid file")
        return 1

    file.close()
    #if integers, cast strings imported to int
    if typeof == "int":
        contents = [int(i) for i in contents]
    return contents
