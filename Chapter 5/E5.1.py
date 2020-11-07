Total = 0
Count = 0
Average = 0
Masukan = 123

while Masukan != 'done' :
    Masukan = input("Number = ")
    try :
        Masukan = float(Masukan)

        Total = Total + Masukan
        Count = Count + 1
    
    except :
        if Masukan == 'done' :
            break
        print("error")

Average = Total/Count
print(Total , Count , Average)
    
