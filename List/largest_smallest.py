l=[]
a=int(input("Enter the number of elements:"))

for i in range (0,a):
    ele=int(input())
    l.append(ele)


print(l)

print("Largest no is:",max(l))
print("Smallest no is:",min(l))
