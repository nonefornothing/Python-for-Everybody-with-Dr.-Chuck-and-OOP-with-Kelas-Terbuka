fname = input("Enter file name: ")
fh = open(fname)
lst = list()                       # list for the desired output
for line in fh:                    # to read every line of file romeo.txt
    word= line.rstrip().split()    # to eliminate the unwanted blanks and turn the line into a list of words
    lst.append(word)    # append     
lst.sort()                         # sort the list (de-indent indicates that you sort when the loop ends)
print (lst)                        # print the list
