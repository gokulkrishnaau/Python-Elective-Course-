dict={}
ans="y"

while ans=="y" or ans=="Y":
    name=input("Enter team name:")
    w=input("Enter no of wins:")
    l=input("Enter no of losses:")
    d[name]=[w,l]
    ans=input("Want to enter more team names?")

print("The teams are:")
print(dict)



hteam="Not available"
lteam="Not available"

print("The team with the highest wins:")
print("The team with the highest losses:")



t=input("Enter team name for winning percentage:")
if t not in dict:
    print("Team not found")
else:
    wp=dict[t][0]/sum(dict[t])*100
    print("Winning percentage of",team,"is",wp)

