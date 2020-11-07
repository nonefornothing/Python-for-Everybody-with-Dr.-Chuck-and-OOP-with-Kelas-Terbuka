def chop (lst) :
    X = lst.pop(0) ##chop first element
    Y = lst.pop(-1) ## acces last element directly
    #Y = lst.pop(len(lst)-1)
    print (lst)

def middle (lst) :
    new = lst[1:((-1)-1)]
    print (lst)
lst = list()
number = 0
while number != "done" :
    number = input("Input a Number : ")
    if number == "done" :
        break
    lst.append(number)

chop(lst)
middle(lst)



