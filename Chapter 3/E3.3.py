try :
    Score = input("Enter Score : ")
    Score = float(Score)

    if Score >= 0 and Score < 0.6  :
        print("F")
    elif Score < 0.7 :
        print("D")
    elif Score < 0.8 :
        print("C")
    elif Score < 0.9 :
        print("B")
    elif Score <= 1 :
        print("A")
    else :
        print("Bad Score")
        
except :
    print("Bad Score")

