#made in python 3.7 by M.Aydin
name = input("Enter your first name")#takes name input
food = input("Enter your favourite food")#takes food input
sentence = name+" likes "+food#forms sentence
sentence = sentence.upper()#makes it upper case
count = len(sentence)#checks how many letters were in the sentence 
print(sentence + " also there were "+str(count)+" letters in this sentence which was generated from your inputs")#outputs all the data collected and the sentence
