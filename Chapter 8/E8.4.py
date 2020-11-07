fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh :
    word = line.rstrip()
    word = line.split()
    for lines in word :
        if lines in lst :
            continue
        else :
            lst.append(lines)
lst.sort()
print (lst)
    
