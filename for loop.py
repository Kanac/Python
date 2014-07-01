def dup(list):
    list.sort()
    prev = list[0]
    del list[0]
    for c in list:
        if prev == c:
            print (" wtf duplicate found ", prev)
        prev = c
list = [1,1,1,4,5,3,4,4,4,4]

dup(list)






    
