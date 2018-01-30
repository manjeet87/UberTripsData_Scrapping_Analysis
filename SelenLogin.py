from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import selenium
import time

import CreateList
from PandasAdd2XL import Add_to_excel

class Trip():
    def __init__(self, CabNo,name,DateTime,fare,triptime,distance,pickup,drop ):
        self.CabNo = CabNo
        self.dr_name = name
        self.DateTime = DateTime
        self.fare = fare
        self.triptime = triptime
        self.distance = distance
        self.pickup = pickup
        self.drop = drop

    def Split_Datetime(self):
        wordList = self.DateTime.split()
        wordList2 = self.triptime.split()  # Splitting the string
        l = len(wordList2)
        if l==3:
            ttime_h = (int(wordList2[0][0]) * 60)
        else:
            ttime_h = 0

        ttime_m = int(wordList2[l-2].replace("m", ''))  # Remove character 'm'
        ttime = ttime_h + ttime_m
        time = wordList[1] + wordList[2]

        self.date = wordList[0]  # Add item to a list
        self.time= time
        self.triptime= (ttime)



def Add2Excel(tripList):
        date = []
        time = []
        fare = []
        triptime = []
        dist = []
        pickup =[]
        drop = []
        for items in tripList:
            date.append(items.date)
            time.append(items.time)
            fare.append(items.fare)
            triptime.append(items.triptime)
            dist.append(items.distance)
            pickup.append(items.pickup)
            drop.append(items.drop)

        status_val, status = Add_to_excel(date,time,fare,triptime,dist,pickup,drop)
        return status_val, status


option = webdriver.ChromeOptions()
option.add_argument("--incognito")
#driver = webdriver.Chrome(chrome_options=option)
driver = webdriver.Chrome()
months = ["January","February","March","April", "May", "June", "July", "August", "September", "October", "November", "December"]


username = "balvinder8063"
password = "HDFC0001443"
username2 = "shweta1034"
password2 = "9818459139"
username3 = "manjeet.nsit@gmail.com"
password3 = "face2book456"
flag = 0
driver.set_page_load_timeout(10)
while flag ==0:
    try:
        elem= driver.get("https://login.uber.com/login")
        flag = 1
    except:
        if EC.presence_of_element_located((By.ID,"email")):
           flag = 1
           driver.maximize_window()
           print ("LOGIN PAGE LOADED")

elem = driver.find_element_by_id("email")
if driver.find_element_by_id("email").is_displayed():
    print("YESSSSSSSSSSSS")
elem.send_keys(username)
elem = driver.find_element_by_id("password")
elem.send_keys(password)
flag = 0
driver.set_page_load_timeout(15)
while True:
    try:
        elem.send_keys(Keys.RETURN)
        break
    except:
        try:
            if driver.find_element_by_xpath("//div//p[text() = 'Total Earnings']").is_displayed():
              break
        except:
            try:
                if driver.find_element_by_id("email").is_displayed():
                   pass
            except:
                driver.refresh()



time.sleep(1)
print ("LOGIN SUCCESS")

flag = 0
#driver.set_page_load_timeout(7)
while flag ==0:
    try:
        driver.get("https://partners.uber.com/p3/fleet-manager/trips")
        flag = 1
    except Exception as e:
        print (e)
        if EC.element_to_be_clickable((By.XPATH,"//*[@id='subNav']/li[6]/div/div[2]")):
           flag = 1
#driver.get("https://partners.uber.com/p3/fleet-manager/trips") #  //*[@id="subNav"]/li[6]/div/div[2]
print ("TRIPS PAGE OPENED")
time.sleep(1)
flag = 0
master_List = []
master_addList = []
flag =0
em = driver.find_element_by_xpath("//*[@id='subNav']/li[6]/div/div[2]").click()
time.sleep(1)
while flag==0:
    month = driver.find_element_by_xpath("//div[@data-reactid = '77']/p").text
    if month == months[0]+" 2017":
        flag = 1
    else:
        driver.find_element_by_xpath("//div[@data-reactid = '77']/a[1]/i").click()
em = driver.find_element_by_xpath("//*[@id='subNav']/li[6]/div/div[2]").click()

for date in range(23,25):

    TripList = []
    #opening calender
    driver.find_element_by_xpath("//*[@id='subNav']/li[6]/div/div[2]").click()
    print ("CALENDER CLICKED")

  #  time.sleep(2)
    #choosing DATE
    #elem = driver.find_element_by_xpath("//*[@id='subNav']/li[6]/div/div[3]/div/table/tbody/tr[2]/td[4]/span").click()

    flag = 0
    while flag==0:
        try:
            driver.find_element_by_xpath("//td/span[text()='"+str(date)+"']").click()
            flag = 1
        except:  pass

    print ("DATE SELECTED : %r",date)
    time.sleep(1)
    #selecting display 50 items in page
    flag = 0
    while True:
        try:
            driver.find_element_by_xpath("//div[@class='select select--borderless']/select").click()
            break
        except: pass

    time.sleep(1)

    elem = driver.find_element_by_xpath("//option[@value = 50]").click()
    print ("LIST SEWLECTED")
    #elem.send_keys(Keys.RETURN)


    #//*[@id="subNav"]/li[6]/div/div[3]/div/table/tbody/tr[3]/td[2]/span
    #//*[@id="subNav"]/li[6]/div/div[3]/div/table/tbody/tr[3]/td[3]/span
    #//*[@id="app-content"]/div/div/div/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[2]/div/div
    #//*[@id="app-content"]/div/div/div/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[2]/div/div
    list = []
    flag = 0

    while True:
        try:
            WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class = 'display--inline-block']")))
            list = driver.find_elements_by_xpath("//div[@class = 'display--inline-block']")
            break
        except:
            list = driver.find_elements_by_xpath("//div[@class = 'display--inline-block']")
            if len(list)==0:
                break
            else:
                pass
    #time.sleep(1)
    trip=0
    addList = []
    act = ActionChains(driver)
    for k in range(1,80,2):
        try:
            #print "k = ",k

            #elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//tr["+str(k)+"]//div[text() = 'DL1RTB8063']")))
            act = ActionChains(driver)
            elem = act.move_to_element(driver.find_element_by_xpath("//tr["+str(k)+"]/td[4]//div[@class = 'display--inline-block']")
                                                                             ).click().perform()
            #elem = driver.find_element_by_xpath("//tr["+str(k)+"]//div[text() = 'DL1RTB8063']").click()
            time.sleep(1)
            datetime = driver.find_element_by_xpath("//tr[" + str(k) + "]/td[2]//div[@class = 'display--inline-block']").text
            name = driver.find_element_by_xpath("//tr[" + str(k) + "]/td[3]//div[@class = 'display--inline-block']").text
            cabno = driver.find_element_by_xpath("//tr[" + str(k) + "]/td[4]//div[@class = 'display--inline-block']").text
            fare = driver.find_element_by_xpath("//tr[" + str(k) + "]/td[5]//div[@class = 'display--inline-block']").text
            triptime = driver.find_element_by_xpath("//tr[" + str(k) + "]/td[6]//div[@class = 'display--inline-block']").text
            distance = driver.find_element_by_xpath("//tr[" + str(k) + "]/td[7]//div[@class = 'display--inline-block']").text
            ride_status = driver.find_element_by_xpath("//tr[" + str(k) + "]/td[8]//div[@class = 'display--inline-block']").text


            if (ride_status == 'completed'):
                ctr = 0
                print (k)
                while ctr<10:
                    try:
                        # elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//tr["+ str(k+1)+"]//div[@class='push-huge--left float--left']/div[2]/div[2]/div[2]")))
                        # time.sleep(1)
                        ctr+=1
                        pickup = driver.find_element_by_xpath("//tr[" + str(
                            k + 1) + "]//div[@class='push-huge--left float--left']/div[2]/div[2]/div[2]").text
                        drop = driver.find_element_by_xpath("//tr[" + str(
                            k + 1) + "]//div[@class='push-huge--left float--left']/div[3]/div[2]/div[2]").text
                        break
                    except Exception as e:
                        pass
                        print e
                        #r = input("")

            else:
                pickup = ("NONE")
                drop = ("NONE")
                # print "*****"
            trip += 1
                #//*[@id="app-content"]/div/div/div/div[2]/div/div[2]/div[1]/table/tbody/tr[2]/td/div/div[2]/div[2]/div[2]/div[2]/text()
                #//*[@id="app-content"]/div/div/div/div[2]/div/div[2]/div[1]/table/tbody/tr[2]/td/div/div[2]/div[2]/div[2]/div[2]
            newTrip = Trip(cabno,name,datetime,fare,triptime,distance,pickup,drop)
            newTrip.Split_Datetime()
            TripList.append(newTrip)
        except Exception as e:
            if k == 1 and len(list)/7 == 0:
                print "No List"
                break
            elif len(list)/7 == trip:
                print "Captured!!"
                break
            else:
                print "Error : ",e

    l=0
    print "Trips Captured: ", trip

    #print len(addList)
    #for address in addList:
    if len(list)!=0:
        status_val, status = Add2Excel(TripList)
        print status






    #//*[@id="app-content"]/div/div/div/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[6]/div/div
    #for item in list:
    #    print item.text
    #list2 = driver.find_element()
    #list2 = soup.find_all('div',attrs= {'class':'diine-block'})Csplay--inl
    #CreateList.Creat_List(list, addList, date)

print "ALL DATA RETRIEVED SUCCESSFULLY"
#CreateList.Creat_List(master_List, master_addList, "FINAL")
driver.quit()
