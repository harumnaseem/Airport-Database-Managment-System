-- Populating Admins Table
Insert into Admins values ( 12345,'Harum', 'abc');
Insert into Admins (AdminName, Password) values ('Hira','def');
Insert into Admins (AdminName, Password) values ('Saba','ghi');
Insert into Admins (AdminName, Password) values ('Shehla','jkl');
Insert into Admins (AdminName, Password) values ('Mahnoor','mno');
Insert into Admins (AdminName, Password) values ('Hannan','pqr');
Insert into Admins (AdminName, Password) values ('AT','stu');
Insert into Admins (AdminName, Password) values ('Haris','vwx');
Insert into Admins (AdminName, Password) values ('Moeed','xyz');
Insert into Admins (AdminName, Password) values ('Sahim','cba');
Insert into Admins (AdminName, Password) values ('Eesha','fed');
Insert into Admins (AdminName, Password) values ('Raahim','ihg');

-- Populating Receptionists Table
Insert into Receptionists values (23450, 'Fatima', '123');
Insert into Receptionists (ReceptionistName, Password ) values ('Humama', '234');
Insert into Receptionists (ReceptionistName, Password ) values ('Ali', '345');
Insert into Receptionists (ReceptionistName, Password ) values ('Haider', '456');
Insert into Receptionists (ReceptionistName, Password ) values ('Hiba', '567');
Insert into Receptionists (ReceptionistName, Password ) values ('Haram', '678');
Insert into Receptionists (ReceptionistName, Password ) values ('Tehreem', '789');
Insert into Receptionists (ReceptionistName, Password ) values ('Maryam', '890');
Insert into Receptionists (ReceptionistName, Password ) values ('Malik', '901');
Insert into Receptionists (ReceptionistName, Password ) values ('Shahrukh', '012');
Insert into Receptionists (ReceptionistName, Password ) values ('Nimra', '321');
Insert into Receptionists (ReceptionistName, Password ) values ('Sara', '543');

-- Populating Passengers Table 
Insert into Passengers values ('3210396630080', 'Sana', 'Address1', '03000000001', 20, 'Female', 'Pakistani');
Insert into Passengers values ('3210396630081', 'Muneeba', 'Address2', '03000000002', '21', 'Female', 'Pakistani');
Insert into Passengers values ('3210396630082', 'Neha', 'Address3', '03000000003', '22', 'Female', 'Pakistani');
Insert into Passengers values ('3210396630083', 'Ahmed', 'Address4', '03000000004', '23', 'Male', 'Pakistani');
Insert into Passengers values ('3210396630084', 'Uzair', 'Address5', '03000000005', '24', 'Male', 'Pakistani');
Insert into Passengers values ('3210396630085', 'Qimra', 'Address6', '03000000006', '25', 'Female', 'Pakistani');
Insert into Passengers values ('3210396630086', 'Saad', 'Address7', '03000000007', '26', 'Male', 'Pakistani');
Insert into Passengers values ('3210396630087', 'Hasham', 'Address8', '03000000008', '27', 'Male', 'Pakistani');
Insert into Passengers values ('3210396630088', 'Shafan', 'Address9', '03000000009', '20', 'Male', 'Pakistani');
Insert into Passengers values ('3210396630089', 'Zainab', 'Address10', '03000000010', '21', 'Female', 'Pakistani');
Insert into Passengers values ('3210396630090', 'Alizeh', 'Address11', '03000000011', '20', 'Female', 'Pakistani');
Insert into Passengers values ('3210396630091', 'Zunaira', 'Address12', '03000000012', '20', 'Female', 'Pakistani');

-- Populating Flights Table
Insert into Flights values ('NH205', 'LHR', 'KHI', '13:55:00', '19:25:00', '2019-12-30', '2019-12-30', 'B777-300ER', 18000);
Insert into Flights values ('NH206', 'LHR', 'KHI', '17:30:00', '12:10:01', '2019-12-30', '2019-12-30', 'B777-300ER', 18000);
Insert into Flights values ('NH835', 'ISB', 'LHR', '17:40:00', '23:30:00', '2019-12-30', '2019-12-30', 'B767-300ER', 17500);
Insert into Flights values ('NH836', 'LHR', 'KHI', '06:25:00', '15:55:00', '2019-12-31', '2019-12-31', 'B767-300ER', 17500);
Insert into Flights values ('NH1167', 'ISB', 'LHR', '20:05:00', '22:25:00', '2019-12-30', '2019-12-30', 'B777-300ER', 19000);
Insert into Flights values ('NH1160', 'KHI', 'ISB', '07:40:00', '09:50:00', '2019-12-31', '2019-12-31', 'B77-300ER', 19000);
Insert into Flights values ('NH879', 'LHR', 'ISB', '22:10:00', '09:35:01', '2019-12-11', '2019-12-12', 'B787-9', 18000);
Insert into Flights values ('NH880', 'LHR', 'ISB', '21:30:00', '05:05:01', '2019-12-12', '2019-12-13', 'B787-9', 18000);
Insert into Flights values ('NH801', 'KHI', 'LHR', '06:12:01', '16:03:34', '2019-12-29', '2019-12-29', 'B777-300ER', 17000);
Insert into Flights values ('NH845', 'ISB', 'KHI', '05:00:01', '15:00:32', '2019-12-11', '2019-12-11', 'B707-8', 18000);
Insert into Flights values ('NH807', 'KHI', 'ISB', '01:12:00', '11:03:04', '2019-12-01', '2019-12-01', 'B787-9', 18000 );

-- Populate HistoryRecord Table
Insert into HistoryRecord values (123990, 'NH205', '3210396630080', 'A1',  '2019-08-23');
Insert into HistoryRecord values (123991, 'NH206','3210396630081', 'B1',  '2019-08-27');
Insert into HistoryRecord values (123992, 'NH835', '3210396630082', 'C1',  '2019-08-26');
Insert into HistoryRecord values (123993, 'NH836', '3210396630083', 'D1',  '2019-08-25');
Insert into HistoryRecord values (123994, 'NH1167', '3210396630084', 'E1', '2019-08-26');
Insert into HistoryRecord values (123995, 'NH1160', '3210396630085', 'F1',  '2019-08-28');
Insert into HistoryRecord values (123996, 'NH879', '3210396630086', 'G1',  '2019-08-06');
Insert into HistoryRecord values (123997, 'NH880', '3210396630087', 'H1',  '2019-08-03');
Insert into HistoryRecord values (123998, 'NH801', '3210396630088', 'K1',  '2019-08-18');
Insert into HistoryRecord values (123999, 'NH845', '3210396630089', 'D4',  '2019-08-06');
Insert into HistoryRecord values (124000, 'NH807', '3210396630090', 'L1',  '2019-07-27');