# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for kata in fh :
    katain = kata.upper()
    kataini = katain.rstrip()
    print(kataini)


