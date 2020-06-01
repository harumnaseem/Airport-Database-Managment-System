drop database if exists Airline;
create database Airline;
use Airline;

drop table if exists Admins;
create table Admins(
	AdminID int NOT NULL auto_increment,
	AdminName varchar(30) NOT NULL,
	Password varchar(20) NOT NULL,
	Primary key(AdminID)
);

drop table if exists Receptionists;
create table Receptionists(
	ReceptionistID int NOT NULL auto_increment, 
	ReceptionistName varchar(30) NOT NULL, 
	Password varchar(20) NOT NULL, 
	Primary key(ReceptionistID)
);

drop table if exists Passengers;
create table Passengers(
	CNIC varchar(13) NOT NULL,
	PassengerName varchar(30) NOT NULL, 
	Address varchar(20) NOT NULL,
	PhoneNumber varchar(11) NOT NULL, 
	Age varchar(3) NOT NULL, 
	Gender varchar(6) NOT NULL,
	Nationality varchar(15) NOT NULL,
	Primary key(CNIC)
);

drop table if exists Flights;
create table Flights(
	FlightID varchar(10) NOT NULL,
	Source varchar(30) NOT NULL, 
	Destination varchar(30) NOT NULL,
	DepartureTime varchar(8) NOT NULL,
	ArrivalTime varchar(8) NOT NULL,
	DepartureDate varchar(10) NOT NULL, 
	ArrivalDate varchar(10) NOT NULL,
	Aircraft varchar(10) NOT NULL,
	FareCharges int NOT NULL,
	Primary Key(FlightID)
);

drop table if exists HistoryRecord;
create table HistoryRecord(
	TicketID int NOT NULL auto_increment, 
	FlightID varchar(10) NOT NULL, 
	CNIC varchar(13) NOT NULL, 
	SeatNumber varchar(10) NOT NULL,
	RegisteringDate varchar(10) NOT NULL,
	Primary Key(TicketID),
	Foreign key(CNIC) references Passengers(CNIC) on delete cascade,
	Foreign key(FlightID) references Flights(FlightID) on delete cascade
);