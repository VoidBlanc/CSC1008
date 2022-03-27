import math
from LIFT.codes.AcceptedRides import AcceptedRides
from LIFT.codes.SharedRides import SharedRides
from LIFT.datastructure.HashTable import HashTable
from LIFT.datastructure.linkedList import SinglyLinkedList
from LIFTMAIN.settings import ONEMAP_DEV_URL, ONEMAP_TOKEN
from math import radians, cos, sin, asin, sqrt
import requests
from LIFT.models import models

def createUserList():
    userList =  SinglyLinkedList()
    return userList

def addUser(userList,object):
    userList.insertAtEnd(object)
    userList.printList()

def splitString(userString):
    return str(userString).split(' ')


def findNearestRider(rList,sList,driver):

    firstRider = splitString(str(rList.listDetail(0)))
    print("driver deets",driver)
    for i in range(1,rList.size()-1):
        nextRider = splitString(str(rList.listDetail(int(i))))
        pToP =distanceCalculation(firstRider[1],nextRider[1]) #compare pickup for rider 1 and next rider
        pToD = distanceCalculation(firstRider[3],nextRider[1]) #compare dropoff for rider 1 and pickup for rider2
        if(int(pToP) <5000 or int(pToD)<5000 and int(nextRider[5])==1): #check if in range
            if pToP>=pToD: 
                newSR = SharedRides(firstRider[0],nextRider[0],firstRider[1],firstRider[3],nextRider[1],nextRider[3],driver[1],firstRider[2],firstRider[5],driver[0]) #for when its destination is closer to first rider so car goes from 
                addUser(sList,newSR)
                uTable.setVal(firstRider[0],"1") #sharedRide = 1, AcceptedRides = 2. We just need to store an ID for one user since its a shared ride
                print("New Shared Ride",sList.size())
            else:
                newSR = SharedRides(firstRider[0],nextRider[0],firstRider[1],nextRider[1],firstRider[3],nextRider[3],driver[1],firstRider[2],firstRider[5],driver[0]) #normal case where it picks up passenger along the way
                
                addUser(sList,newSR)
                sortSList(sList)
                uTable.setVal(firstRider[0],"1")
                

            print("New Shared Ride",sList.listDetail(int(sList.size()-2)))
            rList.deleteAt(i)
            return True
            
        return False

def findRides(rList,dList,aList,sList): #aList =Accepted Rides sList= Shared Rides rList = ridersList
    rider = splitString(str(rList.listDetail(int(0)))) #retrieve first rider details
    if(dList.size()>0):
        for x in range(0,dList.size()-1):
            
            driver = splitString(str(dList.listDetail(int(x))))
            if distanceCalculation(driver[1],rider[1]) <5000:
                if int(rider[5]) == 1:
                    sharedCheck = findNearestRider(rList,sList,driver)
                    if sharedCheck == True:
                        dList.deleteAt(x)
                        rList.deleteAt(0)
                        break
                    else:
                        print("No Shared Ride Found")
                        newRide = AcceptedRides(rider[0],rider[1],driver[1],rider[2],rider[3],rider[4],rider[6],rider[5],driver[0])
                        addUser(aList.newRide)
                        sortAList(aList)
                        uTable.setVal(rider[0],"2")
                        dList.deleteAt(x)
                        rList.deleteAt(0)
                elif(int(rider[5]) == int(5) or int(rider[5]) == int(8)):
                    if int(rider[5]) == int(driver[2]):
                        newRide = AcceptedRides(rider[0],rider[1],driver[1],rider[2],rider[3],rider[4],rider[6],rider[5],driver[0])
                        addUser(aList,newRide)
                        sortAList(aList)
                        uTable.setVal(rider[0],"2")
                        dList.listDetail(x)
                        dList.deleteAt(x)
                        rList.deleteAt(0)
                        break
                else:
                    print("no same seat")
                break
    else:
        print("Driver Not Found")
    
    if dList.size()>0 and rList.size()>0:
        findRides(rList,dList,aList,sList)   #recursive until there are no more riders or drivers
        
        
def findList(userId): #hashmap to delete
    listStored = uTable.getVal(userId)
    return listStored
        
def sortAList(list):
    for m in range(list.size()-1,0,-1):
            for n in range(m):
                
                aRide1 = splitString(str(aList.listDetail(int(n))))
                aRide2 = splitString(str(aList.listDetail(int(n+1))))
                print("1",aRide1[0])
                print("2",aRide2[0])
                if(aRide2[0] is not None):
                    if aRide1[0] > aRide2[0]:
                        temp = AcceptedRides(aRide1[0],aRide1[1],aRide1[2],aRide1[2],aRide1[3],aRide1[4],aRide1[5],aRide1[6],aRide1[7])

                        aList.deleteAt(n)
                        addUser(aList,temp)
                

            print("one set")   

def sortSList(list):
    for m in range(list.size()-1,0,-1):
            for n in range(m):
                
                sRide1 = splitString(str(sList.listDetail(int(n))))
                sRide2 = splitString(str(sList.listDetail(int(n+1))))
                print("1",sRide1[0])
                print("2",sRide2[0])
                if(sRide2[0] is not None):
                    if sRide1[0] > sRide2[0]:
                        temp = AcceptedRides(sRide1[0],sRide1[1],sRide1[2],sRide1[2],sRide1[3],sRide1[4],sRide1[5],sRide1[6],sRide1[7],sRide1[8],sRide1[9])

                        aList.deleteAt(n)
                        addUser(aList,temp)
                

            print("one set")   

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    # Radius of earth in kilometers is 6371
    km = 6371* c
    return km

def distanceCalculation(startLocation, endLocation):
    urls = ONEMAP_DEV_URL+ "/privateapi/routingsvc/route"
    params ={}
    params["start"] = str(startLocation)
    params["end"] = str(endLocation)
    params["routeType"] = "drive"
    params['token'] = ONEMAP_TOKEN
    response = requests.get(urls, params=params)
    #print(response.json()["route_summary"]["total_distance"])
    totaldistance = response.json()["route_summary"]["total_distance"]
    print("totaldistance is : " + str(totaldistance))
    return totaldistance
        
def findList(userId): #hashmap to delete
    listStored = uTable.getVal(userId)
    return listStored
        
    


def findRideIndex(list,smallest,size,userId): #uses binary search
    #def binarySearch(arr, l, r, x): #l = first value r = last val x = value we searching
    if size >= smallest:
        mid = smallest + (size-smallest)/2
        print(mid)
        print(size)
        currentId = splitString(str(list.listDetail(mid)))
        print(currentId[0])
        if int(currentId[0]) == int(userId):
            return mid
        
        elif int(currentId[0]) > int(userId):
            return findRideIndex(list,smallest,mid-1,userId)
        
        else:
                
            return findRideIndex(list,mid+1,size,userId)
    else:
        return smallest 
        
    

def endRide(userId,sList,aList):
    listStored = findList(userId)

    if int(listStored) == 1:
        print(sList.size())
        position = findRideIndex(sList,0,sList.size()-1,userId)
        position = math.ceil(int(position))
        sList.deleteAt(position)
        uTable.delVal(userId)
        print("Shared Ride Has Ended")
        
        
        
    elif int(listStored) ==2:
        print(aList.size())
        position = findRideIndex(aList,0,aList.size()-1,userId)
        position = math.ceil(int(position))
        aList.deleteAt(int(position))
        uTable.delVal(userId)
        print("Normal Ride Has Ended")
        





#creating all the Linked List and functions we will use
dList = createUserList() 
rList = createUserList()
aList = createUserList()
sList = createUserList()
uTable = HashTable()


# dList = models.Drivers.objects.all()
# for driver in dList:
#     print(dList)
#     addUser(dList,driver)
