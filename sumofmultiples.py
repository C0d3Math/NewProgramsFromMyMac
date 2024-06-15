def sum_of_multiples(factors,maximum):
    preedit = []
    finalList = []
    for i in range(1,maximum):
        for j in range(0,len(factors)):
            if i % factors[j] == 0:
                preedit.append(i)
    for i in range(0,len(preedit)):
        if preedit[i] not in finalList:
            finalList.append(preedit[i])
    if int(input("Do you want to see the big list? 0/1 ")) == 1:
        print (finalList)
    print (sum(finalList))

sum_of_multiples([3,5],1000)