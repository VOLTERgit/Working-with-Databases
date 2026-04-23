lst = [1,1,1,5,5,3,1,3,3,1,4,4,4,2,2,2,2]

freq = {}
for i in lst:
    freq[i] = freq.get(i, 0) + 1

for k, v in sorted(freq.items()):
    print(f"{k} : {v}", end=" , ")