def computepay(Hours,Rate):
    if Hours > 40 :
       Pay = 40*Rate + (Hours-40)*1.5*Rate
    else :
       Pay = Hours*Rate
    return Pay

Hours = input("Enter Hours : ")
Hours = float(Hours)
Rate = input("Enter Rate : ")
Rate = float(Rate)

p = computepay(Hours,Rate)
print(p)
