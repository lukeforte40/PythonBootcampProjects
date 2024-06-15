import pymysql.cursors

connect = pymysql.connect(host='localhost',user='root', password='lforte',db='hotel',
cursorclass=pymysql.cursors.DictCursor)

print('Connection Success!')

cursor = connect.cursor()

#Hotel Class

class hotel():
    def __init__ (self, name, location):
        cursor.execute(f'insert into Hotel (hName,hLocation) values ("{name}", "{location}");')
        connect.commit()
        self.name = name
        self.hId = cursor.execute(f'SELECT hId from Hotel where hName = "{name}";')
        connect.commit()
        cursor.execute(f"select count(*) from Room where occupied = 1 and hId = {self.hId};")
        connect.commit()
        self.occupiedCnt = cursor.fetchone()


        cursor.execute(f'select count(*) from Room where hId = {self.hId};')
        connect.commit()

        self.num_of_rooms = cursor.fetchone()

    def addRoom(self, roomNum, bedType, smoking, rate):
          cursor.execute(f'INSERT INTO Room (roomNum,smoking,rate, bedType,occupied,hId) values({roomNum},"{smoking}",{rate},"{bedType}",0,{self.hId});')
          connect.commit()
    def isFull(self):
        if self.occupiedCnt == self.num_of_rooms:
            return True

    def isEmpty(self):
        if self.occupiedCnt == {'count(*)': 0}:
            return True
    def addReservation(self, occupantName, smokingReq, bedReq):
        self.roomNum = cursor.execute(f'select roomNum from room where bedtype = "{bedReq}" and smoking = "{smokingReq}"')
        self.hId = cursor.execute(f'select hId from Room where roomNum = {self.roomNum}')
        cursor.execute(f'insert into Reservation (occ_name,reqSmoke, reqBed, hID,roomNum)values("{occupantName}", "{smokingReq}", "{bedReq}", {self.hId}, {self.roomNum}) ')
    def cancelReservation(self, name):
        self.name = name
        self.roomNum = cursor.execute(f'select roomNum from Reservation where occ_name = "{name}"')
        self.resId = cursor.execute(f'select resId from Reservation where name "{name}"')
        cursor.execute(f'update occupied from Room where roomNum = "{self.roomNum}"')
        cursor.execute(f'delete from Reservation where name = "{name}"')
    def printReservationList(self):
        x = 0
        resList = cursor.execute('select * from Reservation')
        while x <= cursor.rowcount:
            z = cursor.fetchone()
            print(z)
            x+=1
    def getDailySales(self):
        occRates = cursor.execute('select rate from Room where occupied = 1')
        sales = 0
        x = 0
        while x < cursor.rowcount:
            sales+= cursor.fetchone()
            x+=1
        print('Daily Sales Total: ' , sales)
    def occupancyPercentage(self):
        occPer = self.occupiedCnt / self.num_of_rooms
        print(occPer)
    def __str__(self,name, loc):
        cursor.execute(f'select * from Hotel where hName = "{name}" and hlocation = "{loc}"')
        x = 0
        while x < cursor.rowcount:
            print(cursor.fetchone()) 
            x+=1    
    #setters
    def setBedType(self, bedType, roomNum, hId):
        cursor.execute(f'update Rooms set bedType = "{bedType}" where roomNum = {roomNum}')
    
    def setRoomNum(self,rOld, rNew):
        cursor.execute(f'update Rooms set roomNum =  {rNew} where roomNum = {rOld}')
    

    def setOccupied(self, roomNum):
        cursor.execute(f'update Rooms set occupied = 1 where roomNum = {roomNum}')
    
    def setOccupant(self, newOccupant, oldOccupant):
        cursor.execute(f'update Reservation set occName = "{newOccupant}" where r = "{oldOccupant}"')
        
    def setSmoking(self, smoking, roomNum):
        cursor.execute(f'update Rooms set smoking = "{smoking}" where roomNum = {roomNum}')
    
    def setrate(self, newRate, roomNum):
        cursor.execute(f'update Rooms set rate = {newRate} where roomNum = {roomNum}')

    
    #getters
    def getBedType(self,roomNum):
        return cursor.execute(f'select bedType from rooms where roomNum = "{roomNum}"')
    def getSmoking(self,roomNum):
        return cursor.execute(f'select smoking from rooms where roomNum = "{roomNum}"')
    def getRoomNum(self, name):
        return cursor.execute(f'select roomNum from Reservation where name = "{name}"')
    def getRoomRate(self, roomNum):
        return cursor.execute(f'select rate from rooms where roomNum = "{roomNum}"')
    def getOccupant(self,roomNum):
        return cursor.execute(f'select occ_name from rooms where roomNum = "{roomNum}"')
        
    #functions

    def isOccupied(self,roomNum):
        occupied = cursor.execute(f'select occupied from rooms where roomNum = "{roomNum}"')
        if occupied == 1:
            return True
        else:
            return False
    def __roomStr__(self,hId):
        cursor.execute(f'select * from Hotel where hId = {hId};')
        print(cursor.fetchone())
        cursor.execute(f'select * from Room where hId = {hId}')
        x = 0
        while x < cursor.rowcount:
            print(cursor.fetchone()) 
            x+=1       


h = hotel('motel 6', 'paramus')
h.addRoom(102,'queen','s',200)
print(h.num_of_rooms)
print(h.hId)
print(h.occupiedCnt)
print(h.isEmpty())
print(h.isFull())
#h.addReservation('luke','s','queen')
h.getDailySales()
h.printReservationList()
h.__str__('motel 6', 'paramus')
h.__roomStr__(6)

connect.close()