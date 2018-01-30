from bs4 import BeautifulSoup
import xlsxwriter
from xlsxwriter import Workbook
import openpyxl
#from openpyxl import Workbook
from openpyxl import load_workbook

from string import maketrans

def insert_dlist(item,list_no,pos):
    if list_no==1: dlist1.insert(pos,item)
    if list_no==2: dlist2.insert(pos,item)
    if list_no==3: dlist3.insert(pos,item)
    if list_no==4: dlist4.insert(pos,item)
    if list_no==5: dlist5.insert(pos,item)
    if list_no==6: dlist6.insert(pos,item)
    if list_no==7: dlist7.insert(pos,item)

def Add_to_excel(date_lst,time_lst,fare_lst,triptime_lst,dist_lst,pickup_lst,drop_lst):

    wordList = []

    wb = xlsxwriter.Workbook("UberData_"+(str(date_lst[0])).replace('/','_')+".xlsx") #Create workbook
    trips_ws = wb.add_worksheet("UberData") #Open Existing workbook

    #Dformat = log_book.add_format()
    bold = wb.add_format({'bold': True})

    trips_ws.set_column('A:A',20)
    trips_ws.set_column('F:G',60)
    trips_ws.set_row(0,15,bold)
    trips_ws.write('A1', 'Date', bold)
    trips_ws.write('B1', "Time",bold)
    trips_ws.write('C1', "Fare")
    trips_ws.write('D1', "Duratigon")
    trips_ws.write('E1', "Distance")
    trips_ws.write('F1', "PICKUP")
    trips_ws.write('G1', "DROP")
    rn = len(date_lst)  # Length of array, list
    print wordList
    status =0
    for r in range(rn):
        try:
            trips_ws.write('A'+ str(r+2), date_lst[r])  # ADD DATE
            trips_ws.write('B'+ str(r+2), time_lst[r]) # ADD TIME

            try:
                fare = float(fare_lst[r][1:8])
                trips_ws.write_number('C'+ str(r+2), fare)  # ADD FARE
            except:
                trips_ws.write_number('C'+ str(r+2), 0)  # ADD FARE

            trips_ws.write_number('D'+ str(r+2), triptime_lst[r])  # ADD TRIP DURATION
            distance = float(dist_lst[r])
            trips_ws.write_number('E'+ str(r+2), distance)  # ADD DISTANCE
            trips_ws.write_string('F'+ str(r+2),  pickup_lst[r])  # ADD PICKUP
            trips_ws.write_string('G'+ str(r+2),  drop_lst[r])  # ADD DROP
            if r== rn-1: status =1

        except Exception as e:
            print "ERROR : ", e
            status =0

    wb.close()

    if status==1 :
        result =  "Trip Data for "+str(date_lst[0])+" added!!"
        return (status, result)
    elif r==0:
        return (status,"No Data")
    else :
        return (status,e)

    #log_book.close()
    #print "\n***************"
    # print soup2.prettify()


#input type="hidden" name="_csrf_token" value="1486050308-01-sGyOXVwf4dMVB8SMKYYXZSYmDVEEfrXngNZEIeIocAw=">
dlist1 = []
dlist2 = []
dlist3 = []
dlist4 = []
dlist5 = []
dlist6 = []
dlist7 = []
dlist8 = []
dlist9 = []
ctr1 = 0

try:
    with open("tripdata1.txt", 'r') as f1:
        list2 = [line.rstrip(u'\n') for line in f1]

    with open("tripdata2.txt", 'r') as f2:
        addList = [line.rstrip(u'\n') for line in f2]
    n = len(list2)

    j = 0

    for i in range(0, n // 7):
        for j in range(0, 7):
            insert_dlist(list2[i * 7 + j].string, j + 1, i)
            ctr1 += 1
        print dlist1[i], dlist2[i], dlist3[i], dlist4[i], dlist5[i], dlist6[i], dlist7[i]
    print ctr1, n
    print dlist3
    for i in range(0, len(addList), 2):
        dlist8.append(addList[i])
        dlist9.append(addList[i + 1])
        # print item
        # print'\n'

except:
    pass

#Add_to_excel(dlist1,dlist2,dlist3,dlist4,dlist5,dlist6,dlist7,dlist8,dlist9,0)