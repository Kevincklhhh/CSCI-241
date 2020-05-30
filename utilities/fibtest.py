def valid(s,cl):
    list = [None] * 3
    for a in s:
        list[0] = a
        i = 0
        for t in cl:
            if a == t[0]:
                i += 1
                list[i] = t[1]
            elif a == t[1]:
                i += 1
                list[i] = t[0]
            if i == 2:
                return (list[0],list[1],list[2])
print(valid(['1','2','3','a','b','c'],[('3','c'),('c','b')]))
