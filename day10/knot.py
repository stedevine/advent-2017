def processList(input):
    # create the list
    mainList = range(0,5)
    print mainList

    index = 0
    skipSize = 0
    # select the sublist
    sublist = mainList[index:input[0]]
    del mainList[index:input[0]]

    #print sublist
    sublist.reverse()
    #print sublist
    mainList[index:index] = sublist
    #print mainList

    index += input[0] + skipSize

    # what if the sublist wraps around the list
    if (index + input[1] > len(mainList)):
        # right side is the index to the end of the list
        rStart = index
        rEnd = len(mainList)

        # left size is 0 to the remaining lenth of the list
        lStart = 0
        lEnd = input[1] - (rEnd - index)
        l = mainList[lStart:lEnd]
        r = mainList[rStart:rEnd]
        print l
        print r
        combined = r + l
        print "com" + str(combined)
        combined.reverse()
        l = combined[lStart:lEnd]
        r = combined[rStart:rEnd]
        print l
        print r

#        l = combined[0:(input[1] - rightSize)]
#        r = combined[index:leftSize)]
        #sub = s1 + s2
        #sub.reverse()
        #l[index:index] = sub

    #print l



processList([3,4,1,5])
