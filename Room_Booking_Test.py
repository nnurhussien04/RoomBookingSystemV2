##import sqlite3
##dbconn = sqlite3.connect('Room_Booking_System.db')
##cur = dbconn.cursor()
##cur.execute("SELECT PriceRoom FROM Room1 WHERE RoomID = 1")
##dbconn.commit()
##x = cur.fetchall()
##xv2 = ' '.join(map(str, x))
##xv3 = str(xv2)[1:-1]
##xv4 = xv3.replace(',','')
##print(xv4)

#print(len(str(4)))
##CheckInDate = '2021/04/19'
##CheckOutDate = '2021/04/16'
##CheckInInt = CheckInDate[8] + CheckInDate[9]
##CheckOutInt = CheckOutDate[8] + CheckOutDate[9]
##print(int(CheckInInt))
##print(int(CheckOutInt))
##
##if int(CheckInInt) > int(CheckOutInt):
##    print('Incorrect')
##else:
##    print('Correct')

import re
##Email = input('Enter Email')
##NN = re.findall('[a-zA-Z][0-9]?@[a-zA-Z]+[.][a-zA-Z]',Email)
##print(NN)
##if NN:
##    print('correct')
##else:
##    print('incorrect')

Time = '11:12'
CITFormat = re.findall("[0-9][0-9]:[0-9][0-9]",Time)
if CITFormat == []:
    print('Incorrect')
else:
    print('Correct')



##import re
##AZ = input()
##A = re.findall('[.]',AZ)
##print(A)
##if A:
##    print('correct')
##else:
##    print('incorrect')
