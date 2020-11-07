counter = 0
#fname = input("Enter file name: ")
fh = open("mbox-short.txt")
for line in fh :
    word = line.rstrip()
    word = line.split()
    for lines in word :
        if lines.startswith('From:') :
            continue
        elif lines.startswith('From') :
            print (word[1])
            counter = counter + 1
print("There were", counter, "lines in the file with From as the first word")
    
