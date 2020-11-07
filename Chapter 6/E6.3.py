word = 'banana'

def counting (word):
    counter = 0
    for letter in word :
        if letter == 'b':
            counter = counter + 1
    print(counter)

counting(word) 
