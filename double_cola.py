def whoIsNext(names,r):
    length = len(names)
    r = r - 1
    count = 0
    while r >= length:
        r = r - length
        length *= 2
        count += 1
    print(r)
    print(count)
    result = r // pow(2,count)
    return names[result]


names = ["Sheldon","Penny","ds"]
r = 3
print(whoIsNext(names, r))




