--Project name: Shop Database System
--Author: Maksym Kuzma
--Class: C4a
--Email: kuzmamax78@gmail.com
--Phone number: 771188642

create database Shop;
go
use Shop;

--CREATE USER ON SERVER
create login USERNAME_HERE with password='PASSWORD_HERE'
create user USERNAME_HERE for login USERNAME_HERE
go
exec sp_addrolemember'db_owner','USERNAME_HERE'
go

--CREATE TABLES
create table Categories(
category_id int primary key identity(1,1),
category_name nvarchar(25)
)

create table Products(
product_id int primary key identity(1,1),
product_name nvarchar(50) not null,
product_price float not null,
is_edible bit not null,
category_id int foreign key references Categories(category_id) on delete cascade not null,
expiration_date date
)

create table Customers(
customer_id int primary key identity(1,1),
customer_name nvarchar(25) not null,
customer_lastname nvarchar(25) not null,
city nvarchar(25) not null,
phone_number int not null,
email nvarchar(25) not null,
money float not null
)

create table Orders(
order_id int primary key identity(1,1),
order_customer int foreign key references Customers(customer_id) on delete cascade not null,
order_datetime datetime not null,
ship_name nvarchar(50) not null,
ship_city nvarchar(25) not null,
ship_address nvarchar(100) not null,
ship_zip int not null,
order_tracking nvarchar(50) not null
)

create table OrderDetails(
details_id int primary key identity(1,1),
product_id int foreign key references Products(product_id) on delete cascade not null,
order_id int foreign key references Orders(order_id) not null,
quantity int not null,
final_price float not null
)

--AGGREGATE REPORT PROCEDURE
go
create procedure AggregateReport
as
begin
select o.ship_city as 'Shipping city', product_name as 'Product name', sum(od.quantity) as 'Total bought'  from Products p 
inner join OrderDetails od on p.product_id = od.product_id 
inner join Orders o on od.order_id = o.order_id
group by product_name, ship_city
end
go

--VIEWS
create view ProductsExport as
SELECT 
		[product_name]
		,[product_price]
		,[is_edible]
		,[category_id]
		,[expiration_date] 
	FROM Products
go
create view CustomersExport as
SELECT
		[customer_name]
		,[customer_lastname]
		,[city]
		,[phone_number]
		,[email]
		,[money]
  FROM [Shop].[dbo].[Customers]
go
create view OrdersExport as
SELECT
      [order_customer]
      ,[order_datetime]
      ,[ship_name]
      ,[ship_city]
      ,[ship_address]
      ,[ship_zip]
      ,[order_tracking]
  FROM [Shop].[dbo].[Orders]
go
create view OrderDetailsExport as
SELECT
		[product_id]
		,[order_id]
		,[quantity]
		,[final_price]
  FROM [Shop].[dbo].[OrderDetails]
go

--INSERTS
insert into Categories values
('CONVENIENCE'),
('SHOPPING'),
('SPECIALTY')
insert into Products values
('Bread', 25.0, 1, 1, '2022-5-5'),
('IPhone', 1200.0, 0 , 2, null),
('Villa', 13000000.0, 0, 3, null)
insert into Customers values
('Max', 'Kuzma', 'Prague', 772731155, 'maxkuzma@gmail.com', 3000),
('Mike', 'Wattson', 'London', 523223223, 'mikewattson@gmail.com', 100),
('Tanjiro','Kamado', 'Tokyo', 723232323, 'tanjirokamado@gmail.com', 6969)
insert into Orders values
(1, CONVERT(DATETIME2(0),SYSDATETIME()), 'Maksym Kuzma', 'Prague', 'Address 12', 14000, 'CZ13254223'),
(3, CONVERT(DATETIME2(0),SYSDATETIME()), 'Tanjiro Kamado', 'Kyoto', 'Address 43', 24022, 'JP34352121'),
(2, CONVERT(DATETIME2(0),SYSDATETIME()), 'Tom Wattson', 'London', 'Address 27', 52712, 'GB73453123')
insert into OrderDetails values
(2, 1, 3, 3600.0),
(1, 1, 2, 50.0),
(3, 2, 1, 13000000.0),
(1, 3, 10, 250.0)