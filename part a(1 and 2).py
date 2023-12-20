da=[1,2,3,4,5,6]
db=[1,2,3,4,5,6]

combinations=[]

for a in da:
    for b in db:
        combinations.append((a,b))
print("Total combinations:",len(combinations))
print("Possible combinations:")
for c in combinations:
    print(c)
