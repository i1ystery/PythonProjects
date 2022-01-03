insert into Categories values ('CONVENIENCE'),('SHOPPING'),('SPECIALTY')
create table Categories(
category_id int primary key identity(1,1)
)

create table Products(
product_id int primary key identity(1,1),
product_name nvarchar(50) not null,
product_price float,
is_edible bit,
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
ship_zip nvarchar(20) not null,
order_tracking nvarchar(50) not null
)

create table OrderDetails(
details_id int primary key identity(1,1),
product_id int foreign key references Products(product_id) not null,
order_id int foreign key references Orders(order_id) not null,
quantity tinyint not null,
final_price float not null
)


delete from OrderDetails
delete from Orders

DBCC CHECKIDENT ('OrderDetails', RESEED, 0)
GO

DBCC CHECKIDENT ('Orders', RESEED, 0)
GO