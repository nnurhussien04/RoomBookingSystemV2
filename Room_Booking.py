#Room Booking System
import sqlite3
import re
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
        while True:
            Option = input("Type the letter for the following options \n 'R' to read customer details \n 'A' to add customer details \n 'U' to update customer details\n 'D' to delete customer details ")
            if Option == 'A' or Option == 'a':
                Name = input('Enter Customer Name')
                while len(Name) < 2:
                    print('Invalid Format, Name too short, Please Try Again')
                    Name = input('Enter Customer Name')
                Email = input('Enter Customer Email')
                EmailCheck = Email
                EmailFormat = re.findall('[a-zA-Z][0-9]?@[a-zA-Z]+[.][a-zA-Z]',EmailCheck)
                while EmailFormat == []:
                    print('Incorrect Format, Please Try Again')
                    Email = input('Enter Email')
                    EmailCheck = Email
                    EmailFormat = re.findall('[a-zA-Z][0-9]?@[a-zA-Z]+[.][a-zA-Z]',EmailCheck)
                else:
                    TP = input('Enter Customer Telephone Number')
                    while len(TP) != 11:
                        print('Incorrect Format, TP too small')
                        TP = input('Enter Customer Telephone Number')
                    while TP.isdigit() == False:
                        print('Incorrect Format TP no number')
                        TP = input('Enter Customer Telephone Number')
                    else:
                        sql = "insert into Customers(Email, Telephone, Name) VALUES('%s','%s', '%s')" % \
                                  (Email, TP, Name)
                        cur.execute(sql)
                        dbconn.commit()
                        print('Data has been saved succesfully')
                        break
        
            elif Option == 'R' or Option == 'r':
                print('To see all the customers type All')
                CustomerSelected = input('Enter the customer you want to read')
                while len(CustomerSelected) < 2:
                    print('Invalid Name , Name too short')
                    CustomerSelected = input('Enter the customer you want to read')
                if CustomerSelected == 'All':
                    sql = "SELECT * FROM Customers"
                    cur.execute(sql)
                    result = cur.fetchall()
                    dbconn.commit()
                    for x in result:
                        print('Customer ID',x[0])
                        print('Name',x[1])
                        print('Email',x[2])
                        print('Telephone',x[3])
                        print(' ')
                    break
                else:
                    sql = "SELECT * FROM Customers WHERE Name = '%s'" % \
                            (CustomerSelected)
                    cur.execute(sql)
                    result = cur.fetchall()
                    dbconn.commit()
                    for x in result:
                        print('Customer ID',x[0])
                        print('Name',x[1])
                        print('Email',x[2])
                        print('Telephone',x[3])
                    break
                break
            
            elif Option == 'U' or Option == 'u':
                CustomerID = int(input('Enter the customer ID you want to update'))
                UpdateOptions = input('Please pick the option you want to update \nType N for Name \nType E for Email \nType T for Telephone')
                if UpdateOptions == 'N' or UpdateOptions == 'n':
                    NewName = input('Enter New Name')
                    while len(NewName) < 2:
                        print('Invalid Format, Name too short, Please Try Again')
                        NewName = input('Enter New Name')
                    sql = "UPDATE Customers SET Name = '%s' WHERE CustomerID = '%d'" % \
                          (NewName,CustomerID)
                    cur.execute(sql)
                    dbconn.commit()
                    print('This data has been updated successfully')
                    break
                elif UpdateOptions == 'E' or UpdateOptions == 'e':
                    NewEmail = input('Enter New Email')
                    NewEmailCheck = NewEmail
                    NewEmailFormat = re.findall('[a-zA-Z][0-9]?@[a-zA-Z]+[.][a-zA-Z]',NewEmail)
                    while NewEmailFormat == []:
                        print('Incorrect Format, Please Try Again')
                        NewEmail = input('Enter New Email')
                        NewEmailCheck = NewEmail
                        NewEmailFormat = re.findall('[a-zA-Z][0-9]?@[a-zA-Z]+[.][a-zA-Z]',NewEmail)
                    sql = "UPDATE Customers SET Email = '%s' WHERE CustomerID = '%d'"  % \
                          (NewEmail,CustomerID)
                    cur.execute(sql)
                    dbconn.commit()
                    print('This data has been updated successfully')
                    break
                elif UpdateOptions == 'T' or UpdateOptions == 't':
                    NewTP = input('Enter New Telephone')
                    while len(NewTP) != 11:
                        print('Incorrect Format, TP too small')
                        TP = input('Enter Customer Telephone Number')
                    while NewTP.isdigit() == False:
                        print('Incorrect Format TP no number')
                        TP = input('Enter Customer Telephone Number')
                    else:
                        sql = "UPDATE Customers SET Telephone = '%s' WHERE CustomerID = '%d'"  % \
                              (NewTP,CustomerID)
                        cur.execute(sql)
                        dbconn.commit()
                        print('This data has been updated successfully')
                        break

            elif Option == 'D' or Option == 'd':
                DeleteOption = input('Enter Customer Name')
                while len(DeleteOption) < 2:
                    print('Invalid Format, Name too short, Please Try Again')
                    DeleteOption = input('Enter Customer Name')
                if DeleteOption:                       
                    sql = "DELETE FROM Customers WHERE NAME = '%s'" % \
                          (DeleteOption)
                    cur.execute(sql)
                    dbconn.commit()
                    print('Data been deleted successfully')
                    break
                else:
                    print('Error Try Again')
            else:
                break
    elif Action == 'R' or Action == 'r': 
        while True:
            RoomSelected = input("What room do you want to get your info from?\n"
                            "1. Type 1 for Room1 \n"
                            "2. Type 2 for Room2 \n"
                            "3. Type 3 for Room3 \n"
                            "4. Type 4 for Room4 \n"
                            "5. Type 0 for All Rooms \n"
                             )
            while RoomSelected == '':
                print('Incorrect Format')
                RoomSelected = input("What room do you want to get your info from?\n"
                                "1. Type 1 for Room1 \n"
                                "2. Type 2 for Room2 \n"
                                "3. Type 3 for Room3 \n"
                                "4. Type 4 for Room4 \n"
                                "5. Type 0 for All Rooms \n"
                                 )
            while RoomSelected.isdigit() == False:
                print('Incorrect Format')
                RoomSelected = input("What room do you want to get your info from?\n"
                                "1. Type 1 for Room1 \n"
                                "2. Type 2 for Room2 \n"
                                "3. Type 3 for Room3 \n"
                                "4. Type 4 for Room4 \n"
                                "5. Type 0 for All Rooms \n"
                                     )
            if len(RoomSelected) == 1 and RoomSelected == '0':
                sql = "SELECT * FROM Room1"
                cur.execute(sql)
                dbconn.commit()
                result = cur.fetchall()
                for row in result:
                    ID = row[0]
                    Type = row[1]
                    Price = row[2]
                    print('Room ID:',ID, '\nRoomType:',Type ,'\nRoomPrice',Price)       
                    print(' ')
                break
            elif len(RoomSelected) == 1 and RoomSelected:
                sql = "SELECT * FROM Room1 WHERE RoomID = '%s'" % \
                       (RoomSelected)
                cur.execute(sql)
                dbconn.commit()
                result = cur.fetchall()
                for row in result:
                    ID = row[0]
                    Type = row[1]
                    Price = row[2]
                    print('Room ID:',ID, '\nRoomType:',Type ,'\nRoomPrice',Price)       
                    print(' ')
                break
            else:
                print('The data for this room does not exist, please try again')
        PriceChange = input('Do you want to change price?')
        if PriceChange == 'Yes' or PriceChange == 'yes':
            RoomChange = int(input('Write the room number you want to change?'))
            RoomPriceChange = float(input('Enter the price change'))
            if RoomChange:
                sql = "UPDATE Room1 SET PriceRoom = '%d' WHERE RoomID = '%d'" % \
                      (RoomPriceChange,RoomChange)
                cur.execute(sql)
                dbconn.commit()
                print('Data saved successfully')
            else:
                print('Error, Try Again')
    elif Action == 'B' or Action == 'b':
        BookingOptions = input("Type the letter for the following options \n Type 'B' to book \n Type 'E' to edit booking \n Type 'D' to delete booking \n Type 'R' to read booking")
        if BookingOptions == 'B' or BookingOptions == 'b':
            CheckIn = input('What is the check in date?')            
            CheckInCheck = CheckIn
            CheckInFormat = re.findall("2021/[0-9][0-9]/[0-3][0-9]",CheckInCheck) #This is the format for the checkindate
            while CheckInFormat == []:
                print('Incorrect Format')
                CheckIn = input('What is the check in date?')            
                CheckInCheck = CheckIn
                CheckInFormat = re.findall("2021/[0-9][0-9]/[0-3][0-9]",CheckInCheck)
                if CheckInFormat:
                    break
            CheckInInt = CheckInCheck[5] + CheckInCheck[6] + CheckInCheck[8]+CheckInCheck[9]    
            CheckOut = input('What is the check out date?')
            CheckOutCheck = CheckOut
            CheckOutFormat = re.findall("2021/[0-9][0-9]/[0-3][0-9]",CheckOutCheck)
            while CheckOutFormat == []:
                print('Incorrect Format')
                CheckOut = input('What is the check out date?')            
                CheckOutCheck = CheckOut
                CheckOutFormat = re.findall("2021/[0-9][0-9]/[0-3][0-9]",CheckOutCheck)
                if CheckOutFormat:
                    break
            CheckOutInt = CheckOutCheck[5] + CheckOutCheck[6] + CheckOutCheck[8]+CheckOutCheck[9]
            while int(CheckInInt) > int(CheckOutInt):
                print('The check in is bigger than the check out this needs to be changed')
                CheckInOROut = input("Which one do you want to Change? : \n 'I' for Check-In \n 'O' for Check-Out?")
                if CheckInOROut == 'I' or CheckInOROut == 'I':                        
                    CheckIn = input('What is the check in date?')            
                    CheckInCheck = CheckIn
                    CheckInFormat = re.findall("2021/[0-9][0-9]/[0-3][0-9]",CheckInCheck) #This is the format for the checkindate
                    while CheckInFormat == []:
                        print('Incorrect Format')
                        CheckIn = input('What is the check in date?')            
                        CheckInCheck = CheckIn
                        CheckInFormat = re.findall("2021/[0-9][0-9]/[0-3][0-9]",CheckInCheck)
                        if CheckInFormat:
                            break
                    CheckInInt = CheckInCheck[5] + CheckInCheck[6] + CheckInCheck[8]+CheckInCheck[9]
                    if int(CheckOutInt) > int(CheckInInt):
                        break
                if CheckInOROut == 'O' or CheckInOROut == 'o':
                    CheckOut = input('What is the check out date?')  
                    CheckOutCheck = CheckOut
                    CheckOutFormat = re.findall("2021/[0-9][0-9]/[0-3][0-9]",CheckOutCheck)
                    while CheckOutFormat == []:
                        CheckOut = input('What is the check out date?')            
                        CheckOutCheck = CheckOut
                        CheckOutFormat = re.findall("2021/[0-9][0-9]/[0-3][0-9]",CheckOutCheck)
                        if CheckOutFormat:
                            break
                    CheckOutInt = CheckOutCheck[5] + CheckOutCheck[6] + CheckOutCheck[8]+CheckOutCheck[9]
                if int(CheckOutInt) > int(CheckInInt):
                    break
            sql = "select RoomID from Booking where CheckIn >= '%s' and CheckOut <= '%s'" % \
                      (CheckIn,CheckOut)
            cur.execute(sql)
            dbconn.commit()
            result = cur.fetchall()
            RoomsBooked = []
            for x in result:
                RoomsBooked.append(x)
            print(RoomsBooked)
            if len(RoomsBooked) > 0:
                print("The following rooms booked already for that period:",RoomsBooked,"please select another Room ID or date")
                RoomsBooked.clear()
                Question = input("Do you want to pick another date")
                while Question == 'Yes' or Question == 'yes':
                    RoomsBooked.clear()
                    CheckIn = input('What is the check in date?')            
                    CheckInCheck = CheckIn
                    CheckInFormat = re.findall("2021/[0-9][0-9]/[0-3][0-9]",CheckInCheck) #This is the format for the checkindate
                    while CheckInFormat == []:
                        print('Incorrect Format')
                        CheckIn = input('What is the check in date?')            
                        CheckInCheck = CheckIn
                        CheckInFormat = re.findall("2021/[0-9][0-9]/[0-3][0-9]",CheckInCheck)
                        if CheckInFormat:
                            break
                    CheckInInt = CheckInCheck[8]+CheckInCheck[9]     
                    CheckOut = input('What is the check out date?')
                    CheckOutCheck = CheckOut
                    CheckOutFormat = re.findall("2021/[0-9][0-9]/[0-3][0-9]",CheckOutCheck)
                    while CheckOutFormat == []:
                        print('Incorrect Format')
                        CheckOut = input('What is the check out date?')            
                        CheckOutCheck = CheckOut
                        CheckOutFormat = re.findall("2021/[0-9][0-9]/[0-3][0-9]",CheckOutCheck)
                        if CheckOutFormat:
                            break
                    CheckOutInt = CheckOutCheck[8] + CheckOutCheck[9]
                    while int(CheckInInt) > int(CheckOutInt):
                        print('The check in is bigger than the check out this needs to be changed')
                        CheckInOROut = input("Which one do you want to Change? : \n 'I' for Check-In \n 'O' for Check-Out?")
                        if CheckInOROut == 'I' or CheckInOROut == 'I':
                            CheckIn = input('What is the check in date?')            
                            CheckInCheck = CheckIn
                            CheckInFormat = re.findall("2021/[0-9][0-9]/[0-3][0-9]",CheckInCheck) #This is the format for the checkindate
                            while CheckInFormat == []:
                                print('Incorrect Format')
                                CheckIn = input('What is the check in date?')            
                                CheckInCheck = CheckIn
                                CheckInFormat = re.findall("2021/[0-9][0-9]/[0-3][0-9]",CheckInCheck)
                                if CheckInFormat:
                                    break
                            CheckInInt = CheckInCheck[8]+CheckInCheck[9]
                            if int(CheckOutInt) > int(CheckInInt):
                                break
                        elif CheckInOROut == 'O' or CheckInOROut == 'o':
                            CheckOut = input('What is the check out date?')  
                            CheckOutCheck = CheckOut
                            CheckOutFormat = re.findall("2021/[0-9][0-9]/[0-3][0-9]",CheckOutCheck)
                            while CheckOutFormat == []:
                                print('Incorrect Format')
                                CheckOut = input('What is the check out date?')            
                                CheckOutCheck = CheckOut
                                CheckOutFormat = re.findall("2021/[0-9][0-9]/[0-3][0-9]",CheckOutCheck)
                                if CheckOutFormat:
                                    break
                            CheckOutInt = CheckOutCheck[8] + CheckOutCheck[9]
                            if int(CheckOutInt) > int(CheckInInt):
                                break
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
                    else:
                        print('Rooms are available for this date')
                        CustomerID = int(input('What is the customers ID'))
                        RoomID = int(input('What is the ID of the Room they wish to book'))
                        Breakfast = input('Would you like to add breakfast on thier order?')
                        CheckInTime = input('Enter CheckIn Time')
                        CITCheck = CheckInTime
                        CITFormat = re.findall("[0-9][0-9]:[0-9][0-9]",CITCheck)
                        while CITFormat == []:
                            print('Incorrect Format')
                            CheckInTime = input('Enter CheckIn Time')
                            CITCheck = CheckInTime
                            CITFormat = re.findall("[0-9][0-9]:[0-9][0-9]",CITCheck)
                            if CITFormat:
                                break
                        CheckOutTime = input('Enter CheckOut Time')
                        COTCheck = CheckOutTime
                        COTFormat = re.findall("[0-9][0-9]:[0-9][0-9]",COTCheck)
                        while CITFormat == []:
                            print('Incorrect Format')
                            CheckOutTime = input('Enter CheckOut Time')
                            COTCheck = CheckOutTime
                            COTFormat = re.findall("[0-9][0-9]:[0-9][0-9]",COTCheck)
                            if COTFormat:
                                break
                        sql = "SELECT PriceRoom FROM Room1 WHERE RoomID = '%s'" % \
                              (RoomID)
                        cur.execute(sql)
                        result = cur.fetchall()
                        result2 = ' '.join(map(str,result))
                        sql = "insert into Booking(CustomerID,RoomID, CheckIn, CheckOut,CheckInTime,CheckOutTime) VALUES (%d, %d, '%s', '%s','%s','%s')" % \
                              (CustomerID, RoomID, CheckIn, CheckOut,CheckInTime,CheckOutTime)
                        cur.execute(sql)
                        dbconn.commit()
                        RowID = cur.lastrowid
                        result3 = str(result2)[1:-1]
                        result4 = result3.replace(',','')
                        result5 = float(result4)
                        sql = "UPDATE Booking SET BookingPrice = %d WHERE BookingID = '%s'" % \
                               (result5,RowID)
                        cur.execute(sql)
                        dbconn.commit()
                        if Breakfast == 'Yes':
                            try:                    
                                sql = "UPDATE Booking SET BookingPrice = BookingPrice+10 WHERE BookingID = '%s'" % \
                                      (RowID)
                                cur.execute(sql)
                                dbconn.commit()
                                print('Data has been saved successfully')
                            except:
                                print('Error')
                        else:
                            print('Data has been saved succesfully')   
                                
            else:
                print('Rooms are available for this date')
                CustomerID = int(input('What is the customers ID'))
                RoomID = int(input('What is the ID of the Room they wish to book'))
                Breakfast = input('Would you like to add breakfast on thier order ?')
                CheckInTime = input('Enter CheckIn Time')
                CITCheck = CheckInTime
                CITFormat = re.findall("[0-2][0-9]:[0-5][0-9]",CITCheck)
                while CITFormat == []:
                    print('Incorrect Format')
                    CheckInTime = input('Enter CheckIn Time')
                    CITCheck = CheckInTime
                    CITFormat = re.findall("[0-2][0-9]:[0-5][0-9]",CITCheck)
                    if CITFormat:
                        break
                CheckOutTime = input('Enter CheckOut Time')
                COTCheck = CheckOutTime
                COTFormat = re.findall("[0-2][0-9]:[0-5][0-9]",COTCheck)
                while COTFormat == []:
                    print('Incorrect Format')
                    CheckOutTime = input('Enter CheckOut Time')
                    COTCheck = CheckOutTime
                    COTFormat = re.findall("[0-2][0-9]:[0-5][0-9]",COTCheck)
                    if COTFormat:
                        break
                sql = "SELECT PriceRoom FROM Room1 WHERE RoomID = '%s'" % \
                      (RoomID)
                cur.execute(sql)
                result = cur.fetchall()
                result2 = ' '.join(map(str,result))
                sql = "insert into Booking(CustomerID,RoomID, CheckIn, CheckOut,CheckInTime,CheckOutTime) VALUES (%d, %d, '%s', '%s','%s','%s')" % \
                      (CustomerID, RoomID, CheckIn, CheckOut,CheckInTime,CheckOutTime)
                cur.execute(sql)
                dbconn.commit()
                RowID = cur.lastrowid
                result3 = str(result2)[1:-1]
                result4 = result3.replace(',','')
                result5 = float(result4)
                sql = "UPDATE Booking SET BookingPrice = %d WHERE BookingID = '%s'" % \
                       (result5,RowID)
                cur.execute(sql)
                dbconn.commit()
                if Breakfast == 'Yes':
                    try:                    
                        sql = "UPDATE Booking SET BookingPrice = BookingPrice+10 WHERE BookingID = '%s'" % \
                              (RowID)
                        cur.execute(sql)
                        dbconn.commit()
                        print('Data has been saved successfully')
                    except:
                        print('Error')
                else:
                    print('Data has been saved succesfully') 
        elif BookingOptions == 'E' or BookingOptions == 'e':
            EditOptions = input("Type the letter for the following option \n Type C to edit CustomerID \n Type R for RoomID \n Type D for CheckIn and CheckOut Dates/Times \n Type P for Booking Price")
            if EditOptions == 'C' or EditOptions == 'c':
                BookingID = int(input('Enter Booking ID'))
                CustomerID = int(input('Enter new CustomerID'))
                sql = "UPDATE Booking SET CustomerID = %d WHERE BookingID = %d" % \
                      (CustomerID,BookingID)
                cur.execute(sql)
                dbconn.commit()
            if EditOptions == 'R' or EditOptions == 'r':
                BookingID = int(input('Enter Booking ID'))
                RoomID = int(input('Enter new RoomID'))
                sql = "UPDATE Booking SET RoomID = %d WHERE BookingID = %d" % \
                      (RoomID,BookingID)
                cur.execute(sql)
                dbconn.commit()
            if EditOptions == 'D' or EditOptions == 'd':
                BookingID = int(input('Enter Booking ID'))
                CheckIn = input('What is the check in date?')            
                CheckInCheck = CheckIn
                CheckInFormat = re.findall("2021/[0-9][0-9]/[0-3][0-9]",CheckInCheck) #This is the format for the checkindate
                while CheckInFormat == []:
                    print('Incorrect Format')
                    CheckIn = input('What is the check in date?')            
                    CheckInCheck = CheckIn
                    CheckInFormat = re.findall("2021/[0-9][0-9]/[0-3][0-9]",CheckInCheck)
                    if CheckInFormat:
                        break
                CheckInInt = CheckInCheck[8]+CheckInCheck[9]     
                CheckOut = input('What is the check out date?')
                CheckOutCheck = CheckOut
                CheckOutFormat = re.findall("2021/[0-9][0-9]/[0-3][0-9]",CheckOutCheck)
                while CheckOutFormat == []:
                    print('Incorrect Format')
                    CheckOut = input('What is the check out date?')            
                    CheckOutCheck = CheckOut
                    CheckOutFormat = re.findall("2021/[0-9][0-9]/[0-3][0-9]",CheckOutCheck)
                    if CheckOutFormat:
                        break
                CheckOutInt = CheckOutCheck[8] + CheckOutCheck[9]
                while int(CheckInInt) > int(CheckOutInt):
                    print('Incorrect Format')
                    CheckIn = input('What is the check in date?')            
                    CheckInCheck = CheckIn
                    CheckInFormat = re.findall("2021/[0-9][0-9]/[0-3][0-9]",CheckInCheck) #This is the format for the checkindate
                    while CheckInFormat == []:
                        print('Incorrect Format')
                        CheckIn = input('What is the check in date?')            
                        CheckInCheck = CheckIn
                        CheckInFormat = re.findall("2021/[0-9][0-9]/[0-3][0-9]",CheckInCheck)
                        if CheckInFormat:
                            break
                CheckInTime = input('Enter CheckIn Time')
                CITCheck = CheckInTime
                CITFormat = re.findall("[0-9][0-9]:[0-9][0-9]",CITCheck)
                while CITFormat == []:
                    print('Incorrect Format')
                    CheckInTime = input('Enter CheckIn Time')
                    CITCheck = CheckInTime
                    CITFormat = re.findall("[0-9][0-9]:[0-9][0-9]",CITCheck)
                    if CITFormat:
                        break
                CheckOutTime = input('Enter CheckOut Time')
                COTCheck = CheckOutTime
                COTFormat = re.findall("[0-9][0-9]:[0-5][0-9]",COTCheck)
                while CITFormat == []:
                    print('Incorrect Format')
                    CheckOutTime = input('Enter CheckOut Time')
                    COTCheck = CheckOutTime
                    COTFormat = re.findall("[0-9][0-9]:[0-5][0-9]",COTCheck)
                    if COTFormat:
                        break
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
                    print('Please Try Again')
                
                else:
                    sql = "UPDATE Booking SET CheckIn = '%s' WHERE BookingID = %d" % \
                          (CheckIn,BookingID)
                    cur.execute(sql)
                    dbconn.commit()
                    sql2 = "UPDATE Booking SET CheckOut = '%s' WHERE BookingID = %d" % \
                          (CheckOut,BookingID)
                    cur.execute(sql2)
                    dbconn.commit()
                    sql3 = "UPDATE Booking SET CheckInTime = '%s' WHERE BookingID = %d" % \
                          (CheckInTime,BookingID)
                    cur.execute(sql2)
                    dbconn.commit()
                    sql3 = "UPDATE Booking SET CheckOutTime = '%s' WHERE BookingID = %d" % \
                          (CheckOutTime,BookingID)
                    cur.execute(sql3)
                    dbconn.commit()
            if EditOptions == 'P' or EditOptions == 'p':
                BookingID = int(input('Enter Booking ID'))
                BreakfastOption = input('Did User add a breakfast option')
                if BreakfastOption == 'Yes':
                    DeleteBFOption = input('Does User want to remove breakfast option')
                    if DeleteBFOption == 'Yes':
                        sql = "UPDATE Booking SET BookingPrice = BookingPrice-10 WHERE BookingID = %d" % \
                              (BookingID)
                        cur.execute(sql)
                        dbconn.commit()
                    else:
                        print('To edit room price please go to room page')
                if BreakfastOption == 'No':
                    InsertBFOption = input('Does customer want breakfast option?')
                    if InsertBFOption == 'Yes':
                        sql = "UPDATE Booking SET BookingPrice = BookingPrice+10 WHERE BookingID = %d" % \
                              (BookingID)
                        cur.execute(sql)
                        dbconn.commit()
                    else:
                        print('To edit room price please go to room page')
        elif BookingOptions == 'D' or BookingOptions == 'd':
            try:
                BookingID = int(input('Enter Booking ID'))
                sql = "DELETE FROM Booking WHERE BookingID = %d" % \
                      (BookingID)
                cur.execute(sql)
                dbconn.commit()
                print('Data has been deleted successfully')
            except:
                print('Error Try Again')
        elif BookingOptions == 'R' or BookingOptions == 'r':
            print('To print all type 0')
            BookingID = int(input('Enter Booking ID'))
            if BookingID == 0:                    
                sql = "SELECT * FROM Booking" 
                cur.execute(sql)
                dbconn.commit()
                result = cur.fetchall()
                for x in result:
                    Booking_ID = x[0]
                    Customer_ID = x[1]
                    Room_ID = x[2]
                    CheckIn = x[3]
                    CheckOut = x[4]
                    CheckInTime = x[5]
                    CheckOutTime = x[6]
                    BookingPrice = x[7]
                    print('Booking ID:',Booking_ID)
                    print('Customer ID:',Customer_ID)
                    print('Check In:',CheckIn)
                    print('CheckOut:',CheckOut)
                    print('Check In Time:',CheckInTime)
                    print('Check Out Time:',CheckOutTime)
                    print('Booking Price:',BookingPrice)
                    print(' ')
            else:
                sql = "SELECT * FROM Booking WHERE BookingID = '%s'" % \
                      (BookingID)
                cur.execute(sql)
                dbconn.commit()
                result = cur.fetchall()
                for x in result:
                    Booking_ID = x[0]
                    Customer_ID = x[1]
                    Room_ID = x[2]
                    CheckIn = x[3]
                    CheckOut = x[4]
                    CheckInTime = x[5]
                    CheckOutTime = x[6]
                    BookingPrice = x[7]
                    print('Booking ID:',Booking_ID)
                    print('Customer ID:',Customer_ID)
                    print('Check In:',CheckIn)
                    print('CheckOut:',CheckOut)
                    print('Check In Time:',CheckInTime)
                    print('Check Out Time:',CheckOutTime)
                print('Booking Price:',BookingPrice)
    else:
        print('The letter you have typed is not available please try again')

    Question = input('Do you want to continue')
    if Question == 'No' or Question == 'no':
        print('Logging Out...')
        break
    else:
        print('Welcome to the Room Booking System')
        
        


            # disconnect from server
dbconn.close()        
 


