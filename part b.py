da=[1,2,3,4]
db=[1,2,3,4,5,6,7,8]

combinations=[]

for a in da:
    for b in db:
        combinations.append((a,b))
total=len(combinations)

sums={}

for a in da:
    for b in db:
        sum_possible=a+b
        if sum_possible in sums:
            sums[sum_possible]+=1
        else:
            sums[sum_possible]=1

for sum_possible,count in sums.items():
    probability=count/total
    print(f"sum [{sum_possible}] - probability: {probability: .2f}")
