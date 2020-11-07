fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

words = list()
counts = dict()

for line in fhand:
    if line.startswith("From: ") :
        word = line.split()
        words.append(word[1])
#print(words)

for dic in words:
    counts[dic] = counts.get(dic, 0) + 1
           
#print(counts)

maxval = 0
maxkey = 0
for key,val in counts.items() :
#   if maxval == None : maxval = val
  if val > maxval:
      maxval = val
      maxkey = key   

print (maxkey, maxval)
     
