Maximum = None
Minimum = None
Masukan = 123

while Masukan != 'done' :
    Masukan = input("Number = ")
    try :
        Masukan = int(Masukan)
        if Maximum is None or Masukan > Maximum :
            Maximum = Masukan
        if Minimum is None or Masukan < Minimum :
            Minimum = Masukan
           
    except :
        if Masukan == 'done' :
            break
        print("Invalid input")

print("Maximum is" , Maximum)
print("Minimum is" , Minimum)
    
