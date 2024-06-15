#KeyList
#by Max B.
#a program to print the items of four 3-item lists 
#in a random order according to a key

list1 = [1,2,3]
list2 = [11,12,13]
list3 = [21,22,23]
list4 = [31,32,33]

key = int(input("Input your key that is a four digit number with each digit being from 1 to 6."))

orders = [123,132,213,231,312,321]

for i in range(0,4):
    keydigit = int(str(key)[i])
    order = orders[keydigit - 1]
    for j in range(0,3):
        if i == 0:
            print(list1[order[j]-1])
        elif i == 1:
            print(list2[order[j]-1])
        elif i == 2:
            print(list3[order[j]-1])
        else:
            print(list4[order[j]-1])