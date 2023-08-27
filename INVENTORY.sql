create database INVENTORY;
use INVENTORY;

create table EMPLOYEE(
	empID int not null,
    name varchar(20),
    deptName varchar(20),
    post varchar(20),
    utype varchar(20),
    primary key(empID)
);

insert into EMPLOYEE values(201, 'Harry Styles', 'CSE','Professor','Admin');
insert into EMPLOYEE values(301, 'Niall Horan', 'ISE','Professor','Admin');
insert into EMPLOYEE values(401, 'John Smith', 'ME','Professor','Admin');

create table PRODUCT(
	PID int not null,
    name varchar(20),
    model varchar(20),
	type varchar(20),
    cost varchar(20),
    deptName varchar(20),
    primary key(PID)
);

insert into PRODUCT values(1,'Computers','Windows 11','25','2500000','CSE');
insert into PRODUCT values(2,'Benches','NA','40','250000','EC');
insert into PRODUCT values(3,'Drill Machines','X-type','15','400000','ME');