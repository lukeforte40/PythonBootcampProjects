def findSums(listin, sumin):
    listin.sort()
    solutions = []
    n = 0
    while n < len(listin):
        b = []
        x = 0
        a = 0
        while x < 4:
            a += listin[x]
            b.append(listin[x])
            x += 1
        if a == sumin:
            solutions.append(b)
        drop = listin[0]
        listin.remove(drop)
        listin.append(drop)
        n+=1
    n = 0

    print(solutions) 

findSums([1,0,-1,0,-2,2], 0)
        

