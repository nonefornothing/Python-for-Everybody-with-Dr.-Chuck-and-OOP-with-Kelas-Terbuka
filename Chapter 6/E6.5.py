text = "X-DSPAM-Confidence:    0.8475";

position = text.find(':')
Word = text[position+1:]
Real = Word.strip()
Real = float(Real)
print(Real)

