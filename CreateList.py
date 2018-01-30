import time
from Add2xl import Add_to_excel

dlist1 = []
dlist2 = []
dlist3 = []
dlist4 = []
dlist5 = []
dlist6 = []
dlist7 = []
dlist8 = []
dlist9 = []

def insert_dlist(item, list_no, pos):
    if list_no == 1: dlist1.insert(pos, item)
    if list_no == 2: dlist2.insert(pos, item)
    if list_no == 3: dlist3.insert(pos, item)
    if list_no == 4: dlist4.insert(pos, item)
    if list_no == 5: dlist5.insert(pos, item)
    if list_no == 6: dlist6.insert(pos, item)
    if list_no == 7: dlist7.insert(pos, item)

def Creat_List(list,addList,date=0):
    global dlist1
    dlist1 = []
    global dlist2
    dlist2 = []
    global dlist3
    dlist3 = []
    global dlist4
    dlist4 = []
    global dlist5
    dlist5 = []
    global dlist6
    dlist6 = []
    global dlist7
    dlist7 = []
    global dlist8
    dlist8 = []
    global dlist9
    dlist9 = []

    n = len(list)
    # print list2

    ctr1 = 0

    j = 0
    #time.strptime()
    print "LIST GENERATED"
    time.sleep(2)

    with open("tripdata1.txt",'w') as f1:
        for item in list: pass
           # f1.write(item.text + u'\n')

    with open("tripdata2.txt",'w') as f2:
        for item in addList: pass
            #f2.write(item + u'\n')


    if date == "FINAL":
        for i in range(0, n // 7):
            for j in range(0, 7):
                insert_dlist(list[i * 7 + j], j + 1, i)
                ctr1 += 1
            print dlist1[i], dlist2[i], dlist3[i], dlist4[i], dlist5[i], dlist6[i], dlist7[i]
    else:
        for i in range(0, n // 7):
            for j in range(0, 7):
                insert_dlist(list[i * 7 + j].text, j + 1, i)
                ctr1 += 1
            #print dlist1[i], dlist2[i], dlist3[i], dlist4[i], dlist5[i], dlist6[i], dlist7[i]

    for i in range(0,len(addList),2):
        dlist8.append(addList[i])
        dlist9.append(addList[i+1])

    print "\n*********************************"
    # print soup2.text
    print ctr1, n
    Add_to_excel(dlist1,dlist2,dlist3,dlist4,dlist5,dlist6,dlist7,dlist8,dlist9,date)
  #  return zip(dlist1,dlist2,dlist3,dlist4,dlist5,dlist6,dlist7,dlist8,dlist9)
