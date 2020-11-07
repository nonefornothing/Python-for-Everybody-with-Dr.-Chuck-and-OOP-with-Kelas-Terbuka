# Use the file name mbox-short.txt as the file name
Jumlah = 0
X = 0
Counter = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    X = line[20:]
    X = float(X)
    Jumlah = Jumlah + X
    Counter = Counter + 1
RataRata = Jumlah/Counter
print("Average spam confidence: " , RataRata)
