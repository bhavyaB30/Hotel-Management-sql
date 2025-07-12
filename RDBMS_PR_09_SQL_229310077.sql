create database hotel_management;
use hotel_management;
CREATE TABLE rooms (room_number INT PRIMARY KEY,room_type VARCHAR(255),room_rent DECIMAL(10, 2),status VARCHAR(255));

CREATE TABLE customers (customer_id INT PRIMARY KEY,customer_name VARCHAR(255),customer_address VARCHAR(255),customer_phone VARCHAR(15),customer_email VARCHAR(255));

CREATE TABLE bills (bill_id INT PRIMARY KEY AUTO_INCREMENT,room_number INT,customer_id INT,total_amount DECIMAL(10, 2));
use hotel_management;
show tables;
select * from rooms;
insert into customers value(1, 'BHAVYA', 'MUJ', '8860206960', 'BHAVYA@example.com');

insert into customers value(3, 'VINAYAK', 'MUJ', '8860278960', 'VINAYAK@example.com');
insert into customers value(4, 'AYUSH', 'MUJ', '8860296960', 'AYUSH@example.com');
insert into customers value(5, 'ROHAN', 'MUJ', '8860212960', 'ROHAN@example.com');
insert into customers value(6, 'SAHIL', 'MUJ', '8860286960', 'BYE@example.com');
insert into customers value(7, 'SAMYAK', 'MUJ', '8860456960', 'SAMYAK@example.com');
insert into customers value(8, 'MAYANK', 'MUJ', '8860207960', 'HELLO@example.com');
select * from customers;
show tables;
use hotel_management;
insert into bills value(111,001,1,300);
insert into bills value(112,002,1,300);
insert into bills value(113,003,1,300);
insert into bills value(114,004,1,300);
insert into bills value(115,005,1,300);
insert into bills value(116,101,1,600);
select * from bills;