--
-- File generated with SQLiteStudio v3.2.1 on Mon Jul 25 18:43:38 2022
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Booking
CREATE TABLE Booking (
    BookingID    INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerID   INTEGER REFERENCES Customers (CustomerID),
    RoomID       INTEGER REFERENCES Room1 (RoomID),
    CheckIn      DATE,
    CheckOut     DATE,
    CheckInTime  TIME,
    CheckOutTime TIME,
    BookingPrice REAL
);

INSERT INTO Booking (
                        BookingID,
                        CustomerID,
                        RoomID,
                        CheckIn,
                        CheckOut,
                        CheckInTime,
                        CheckOutTime,
                        BookingPrice
                    )
                    VALUES (
                        1,
                        2,
                        2,
                        '2021/04/15',
                        '2021/04/20 ',
                        '19:00',
                        '10:00',
                        59.0
                    );

INSERT INTO Booking (
                        BookingID,
                        CustomerID,
                        RoomID,
                        CheckIn,
                        CheckOut,
                        CheckInTime,
                        CheckOutTime,
                        BookingPrice
                    )
                    VALUES (
                        2,
                        4,
                        3,
                        '2021/04/18 ',
                        '2021/04/22 ',
                        '17:30',
                        '20:00',
                        49.0
                    );

INSERT INTO Booking (
                        BookingID,
                        CustomerID,
                        RoomID,
                        CheckIn,
                        CheckOut,
                        CheckInTime,
                        CheckOutTime,
                        BookingPrice
                    )
                    VALUES (
                        3,
                        4,
                        4,
                        '2021/04/12',
                        '2021/04/19',
                        '10:00',
                        '00:00',
                        59.0
                    );

INSERT INTO Booking (
                        BookingID,
                        CustomerID,
                        RoomID,
                        CheckIn,
                        CheckOut,
                        CheckInTime,
                        CheckOutTime,
                        BookingPrice
                    )
                    VALUES (
                        4,
                        5,
                        3,
                        '2021/05/01',
                        '2021/05/09',
                        '12:00',
                        '15:00',
                        49.0
                    );

INSERT INTO Booking (
                        BookingID,
                        CustomerID,
                        RoomID,
                        CheckIn,
                        CheckOut,
                        CheckInTime,
                        CheckOutTime,
                        BookingPrice
                    )
                    VALUES (
                        5,
                        4,
                        1,
                        '2021/04/25',
                        '2021/04/29',
                        '19:00',
                        '18:00',
                        49.0
                    );

INSERT INTO Booking (
                        BookingID,
                        CustomerID,
                        RoomID,
                        CheckIn,
                        CheckOut,
                        CheckInTime,
                        CheckOutTime,
                        BookingPrice
                    )
                    VALUES (
                        6,
                        4,
                        1,
                        '2021/05/12',
                        '2021/05/20',
                        '00:00',
                        '15:00',
                        59.0
                    );

INSERT INTO Booking (
                        BookingID,
                        CustomerID,
                        RoomID,
                        CheckIn,
                        CheckOut,
                        CheckInTime,
                        CheckOutTime,
                        BookingPrice
                    )
                    VALUES (
                        7,
                        3,
                        2,
                        '2021/04/19',
                        '2021/04/20',
                        '19:32',
                        '23:30',
                        59.0
                    );

INSERT INTO Booking (
                        BookingID,
                        CustomerID,
                        RoomID,
                        CheckIn,
                        CheckOut,
                        CheckInTime,
                        CheckOutTime,
                        BookingPrice
                    )
                    VALUES (
                        8,
                        2,
                        2,
                        '2021/05/30',
                        '2021/06/09',
                        '10:00',
                        '20:00',
                        49.0
                    );

INSERT INTO Booking (
                        BookingID,
                        CustomerID,
                        RoomID,
                        CheckIn,
                        CheckOut,
                        CheckInTime,
                        CheckOutTime,
                        BookingPrice
                    )
                    VALUES (
                        10,
                        4,
                        1,
                        '2021/05/24',
                        '2021/05/28',
                        NULL,
                        NULL,
                        NULL
                    );

INSERT INTO Booking (
                        BookingID,
                        CustomerID,
                        RoomID,
                        CheckIn,
                        CheckOut,
                        CheckInTime,
                        CheckOutTime,
                        BookingPrice
                    )
                    VALUES (
                        11,
                        4,
                        2,
                        '10/11/22',
                        '13/11/22',
                        NULL,
                        NULL,
                        NULL
                    );


-- Table: Customers
CREATE TABLE Customers (
    CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name       STRING,
    Email      STRING,
    Telephone  STRING
);

INSERT INTO Customers (
                          CustomerID,
                          Name,
                          Email,
                          Telephone
                      )
                      VALUES (
                          1,
                          'Ali',
                          'Ali@gmail.com',
                          924555535
                      );

INSERT INTO Customers (
                          CustomerID,
                          Name,
                          Email,
                          Telephone
                      )
                      VALUES (
                          2,
                          'Moody',
                          'mdasd@gmail.com',
                          742832323
                      );

INSERT INTO Customers (
                          CustomerID,
                          Name,
                          Email,
                          Telephone
                      )
                      VALUES (
                          3,
                          'Harry',
                          'Hafas@gmai.com',
                          823232323
                      );

INSERT INTO Customers (
                          CustomerID,
                          Name,
                          Email,
                          Telephone
                      )
                      VALUES (
                          4,
                          'John',
                          'Johnny@gmail.com',
                          34242424
                      );

INSERT INTO Customers (
                          CustomerID,
                          Name,
                          Email,
                          Telephone
                      )
                      VALUES (
                          5,
                          'Ahmed',
                          'Ahmed@gmail.com',
                          7845374123
                      );

INSERT INTO Customers (
                          CustomerID,
                          Name,
                          Email,
                          Telephone
                      )
                      VALUES (
                          6,
                          'Nebil',
                          'N3B1L@gmail.com',
                          73723120
                      );

INSERT INTO Customers (
                          CustomerID,
                          Name,
                          Email,
                          Telephone
                      )
                      VALUES (
                          9,
                          'Jacob',
                          'JB032@gmail.com',
                          7421355234
                      );

INSERT INTO Customers (
                          CustomerID,
                          Name,
                          Email,
                          Telephone
                      )
                      VALUES (
                          10,
                          'NN',
                          'NN@gmail.com',
                          981727172
                      );

INSERT INTO Customers (
                          CustomerID,
                          Name,
                          Email,
                          Telephone
                      )
                      VALUES (
                          11,
                          'Ali',
                          'Ali@shubeck.com',
                          7309482123
                      );


-- Table: Room1
CREATE TABLE Room1 (
    RoomID    INTEGER PRIMARY KEY AUTOINCREMENT,
    RoomType  STRING,
    PriceRoom REAL
);

INSERT INTO Room1 (
                      RoomID,
                      RoomType,
                      PriceRoom
                  )
                  VALUES (
                      1,
                      'Double Room 1',
                      49.0
                  );

INSERT INTO Room1 (
                      RoomID,
                      RoomType,
                      PriceRoom
                  )
                  VALUES (
                      2,
                      'Double Room 2',
                      49.0
                  );

INSERT INTO Room1 (
                      RoomID,
                      RoomType,
                      PriceRoom
                  )
                  VALUES (
                      3,
                      'Double Room 3',
                      49.0
                  );

INSERT INTO Room1 (
                      RoomID,
                      RoomType,
                      PriceRoom
                  )
                  VALUES (
                      4,
                      'Double Room 4',
                      49.0
                  );


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
