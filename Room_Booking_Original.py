#Room Booking System
import time
import sqlite3
dbconn = sqlite3.connect("Room_Booking_System.db")  
cur = dbconn.cursor()

username = input('Enter Username')
password = input('Enter Password')
z = 0
for x in range(0,4):
    if username == 'NN' and password == 'RoomBooking':
        print('Login Successful')
        break
    else:
        print('Login Unsuccesful')
        username = input('Enter Username')
        password = input('Enter Password')
        z = z + 1
        if z == 4:
            exit()
print('Welcome to the Room Booking System')
while True:        
    #Present users with options
    Action = input("Select what action you will like to peform:\n 'N' to enter/edit customer \n 'R' for Room Details \n 'B' for Booking ")
    #Options of creating use with new customers
    if Action == 'N' or Action == 'n':
        Name = input('Enter Customer Name')
        Email = input('Enter Customer Email')
        TP = input('Enter Customer Telephone Number')
        sql = "insert into Customers(Email, Telephone, Name) VALUES('%s','%s', '%s')" % \
                  (Email, TP, Name)
        cur.execute(sql)
        dbconn.commit()
        print('Data has been saved succesfully')
    elif Action == 'R' or Action == 'r':
        RoomSelected = input("What room do you want to get your info from?\n"
                            "1. Room1 \n"
                            "2. Room2 \n"
                            "3. Room3 \n"
                            "4. Room4 \n"
                            "5. All Rooms \n"
                             )
        if RoomSelected == '1':
            sql = "SELECT * FROM Room1 WHERE RoomID = '1'"
        elif RoomSelected == '2':
            sql = "SELECT * FROM Room1 WHERE RoomID = '2'"
        elif RoomSelected == '3':
            sql = "SELECT * FROM Room1 WHERE RoomID = '3'"
        elif RoomSelected == '4':
            sql = "SELECT * FROM Room1 WHERE RoomID = '4'"
        elif RoomSelected == 'All':
            sql = "SELECT * FROM Room1"
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            ID = row[0]
            Type = row[1]
            Price = row[2]
            print('Room ID:',ID, '\nRoomType:',Type ,'\nRoomPrice',Price)       
            print(' ')
        PriceChange = input('Do you want to change price?')
        if PriceChange == 'Yes' or PriceChange == 'yes':
            RoomChange = int(input('Write the room number you want to change?'))
            RoomPriceChange = float(input('Enter the price change'))
            if RoomChange:
                sql = "UPDATE Room1 SET PriceRoom = '%d' WHERE RoomID = '%d'" % \
                      (RoomPriceChange,RoomChange)
                cur.execute(sql)
                dbconn.commit()
            else:
                print('Error, Try Again')
    elif Action == 'B' or Action == 'b':
        CheckIn = input('What is the check in date?')
        CheckOut = input('What is the check out date?')
        sql = "select RoomID from Booking where CheckIn >= '%s' and CheckOut <= '%s'" % \
                  (CheckIn,CheckOut)
        cur.execute(sql)
        result = cur.fetchall()
        RoomsBooked = []
        for x in result:
            RoomsBooked.append(x)
        if len(RoomsBooked) > 0:
            print("The following rooms booked already for that period:",RoomsBooked,"please select another Room ID or date")
            RoomsBooked.clear()
            Question = input("Do you want to pick another date")
            while Question == 'Yes' or Question == 'yes':
                    CheckIn2 = input('What is the check in date?')
                    CheckOut2 = input('What is the check out date?')
                    sql = "select RoomID from Booking where CheckIn >= '%s' and CheckOut <= '%s'" % \
                              (CheckIn2,CheckOut2)
                    cur.execute(sql)
                    result = cur.fetchall()
                    RoomsBooked = []
                    for x in result:
                        RoomsBooked.append(x)
                    if len(RoomsBooked) > 0:
                        print("The following rooms booked already for that period:",RoomsBooked,"please select another Room ID or date")
                        RoomsBooked.clear()
                        Question = input("Do you want to pick another date")
                    else:                        
                        print('Rooms are available for this date')
                        CustomerID = int(input('What is the customers ID'))
                        RoomID = int(input('What is the ID of the Room they wish to book'))
                        sql = "insert into Booking(CustomerID,RoomID, CheckIn, CheckOut) VALUES (%d, %d, '%s', '%s')" % \
                              (CustomerID, RoomID, CheckIn, CheckOut)
                        cur.execute(sql)
                        dbconn.commit()
                        Breakfast = input('Would you like to add breakfast on thier order ?')
                        if Breakfast == 'Yes':
                            sql = "UPDATE Room1 SET PriceRoom = 10+PriceRoom WHERE RoomID = '%d'" % \
                                  (RoomID,RoomID)
                            print('Data has been saved successfully')
                            break
                        else:
                            print('Data has been saved succesfully') 
                            break 
        else:
            print('Rooms are available for this date')
            CustomerID = int(input('What is the customers ID'))
            RoomID = int(input('What is the ID of the Room they wish to book'))
            sql = "insert into Booking(CustomerID,RoomID, CheckIn, CheckOut) VALUES (%d, %d, '%s', '%s')" % \
                  (CustomerID, RoomID, CheckIn, CheckOut)
            cur.execute(sql)
            dbconn.commit()
            Breakfast = input('Would you like to add breakfast on thier order ?')
            if Breakfast == 'Yes':
                sql = "UPDATE Room1 SET PriceRoom = 10+PriceRoom WHERE RoomID = '%d'" % \
                      (RoomID)
                cur.execute(sql)
                dbconn.commit()
                print('Data has been saved successfully')
            else:
                print('Data has been saved succesfully') 
    Question = input('Do you want to continue')
    if Question == 'No' or Question == 'no':
        print('Logging Out...')
        time.sleep(5)
        break
    else:
        print('Welcome to the Room Booking System')
        
        


            # disconnect from server
dbconn.close()        
 


