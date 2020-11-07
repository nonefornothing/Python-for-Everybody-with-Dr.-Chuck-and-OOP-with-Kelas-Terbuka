lst = list()
number = 0

while number != "done" :
    number = input("Enter a Number : ")
    if number == "done" :
        break
    number = int(number)
    lst.append(number)
    
X = max(lst)
Y = min(lst)

print("Maximum: ", X)
print("Minimum: ", Y)




