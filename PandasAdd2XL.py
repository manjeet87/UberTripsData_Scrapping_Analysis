import pandas as pd
import numpy as np


def  Add_to_excel(date_lst,time_lst,fare_lst,triptime_lst,dist_lst,pickup_lst,drop_lst):

    wordList = []

   # wb = xlsxwriter.Workbook("UberData_"+(str(date_lst[0])).replace('/','_')+".xlsx") #Create workbook
   # trips_ws = wb.add_worksheet("UberData") #Open Existing workbook

    #Dformat = log_book.add_format()
  #  bold = wb.add_format({'bold': True})

    dataset = pd.DataFrame({'Date':pd.Series(date_lst),'Time': pd.Series(time_lst),'Fare': pd.Series(float(fare_lst[:][1:8])),\
                            'Duration':pd.Series(triptime_lst),'Distance':pd.Series(float(dist_lst)),\
                            'PICKUP': pd.Series(pickup_lst),'DROP':pd.Series(drop_lst)})

    dataset.to_excel('testing.xlsx',excel_writer='xlsxwriter')


    # trips_ws.set_column('A:A',20)
    # trips_ws.set_column('F:G',60)
    # trips_ws.set_row(0,15,bold)
    # trips_ws.write('A1', 'Date', bold)
    # trips_ws.write('B1', "Time",bold)
    # trips_ws.write('C1', "Fare")
    # trips_ws.write('D1', "Duratigon")
    # trips_ws.write('E1', "Distance")
    # trips_ws.write('F1', "PICKUP")
    # trips_ws.write('G1', "DROP")
    # rn = len(date_lst)  # Length of array, list
    # print wordList
    # status =0
    # for r in range(rn):
    #     try:
    #         trips_ws.write('A'+ str(r+2), date_lst[r])  # ADD DATE
    #         trips_ws.write('B'+ str(r+2), time_lst[r]) # ADD TIME
    #
    #         try:
    #             fare = float(fare_lst[r][1:8])
    #             trips_ws.write_number('C'+ str(r+2), fare)  # ADD FARE
    #         except:
    #             trips_ws.write_number('C'+ str(r+2), 0)  # ADD FARE
    #
    #         trips_ws.write_number('D'+ str(r+2), triptime_lst[r])  # ADD TRIP DURATION
    #         distance = float(dist_lst[r])
    #         trips_ws.write_number('E'+ str(r+2), distance)  # ADD DISTANCE
    #         trips_ws.write_string('F'+ str(r+2),  pickup_lst[r])  # ADD PICKUP
    #         trips_ws.write_string('G'+ str(r+2),  drop_lst[r])  # ADD DROP
    #         if r== rn-1: status =1
    #
    #     except Exception as e:
    #         print "ERROR : ", e
    #         status =0
    #
    # wb.close()
    #
    # if status==1 :
    #     result =  "Trip Data for "+str(date_lst[0])+" added!!"
    #     return (status, result)
    # elif r==0:
    #     return (status,"No Data")
    # else :
    return (0)
