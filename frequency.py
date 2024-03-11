 def count(elements):
    if elements[-1]=='.':
        elements= elements[0:len(elements)-1]

    if elements in dictionary:
        dictionary[elements]+=1

    else:
        dictionary.update({elements:1})





string=str(input("Enter the sentence:"))
dictionary={}

l=string.split()

for elements in l:
    count(elements)


for key in dictionary:
 print("\nFrequency of",key,"is",dictionary[key])
 
