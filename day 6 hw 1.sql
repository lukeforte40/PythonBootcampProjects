use hotel;

drop table day4;

#1
create table day4(
employee_id int primary key,
first_name varchar(20),
last_name varchar(20),
email varchar(20),
phone_number varchar(20),
hire_date date,
job_id  varchar(20),
salary decimal(15,2),
commission_pct decimal(3,2),
manager_id int,
department_id int);

insert into day4 values(100, 'steven', 'king', 'sking', '515.123.4567', '1987-06-17', 'ad_pres',24000.00,0.00,0,90);
insert into day4 values(101,'neena','kochhar','nkochahr','551.123.4568','1987-06-18','ad_vp',17000.00,0.00,100,90);
insert into day4 values(102,'lex','de haan','ldehaan','515.123.4569','1987-06-19', 'ad_vp',17000.00,0.00,100,90);
insert into day4 values(103,'alexander', 'hunold','ahunold','590.423.4567','1987-06-20','it_prog',9000.00,0.00,102,60);
insert into day4 values(104,'bruce','ernst','bernst','590.423.4568','1987-06-21', 'it_prog',6000.00,0.00,103,60);
insert into day4 values(105,'david','austin','dasutin','590.423.4569','1987-06-22','it_prog',4800.00,0.00,103,60);
insert into day4 values(106,'valli','pataballa','vpataballa','590.423.4560','1987-06-23','it_prog',4800.00,0.00,103,60);
insert into day4 values(107,'diana','lorentz','dlorentz','590.423.5567','1987-06-24','it_prog',4200.00,0.00,103,60);
insert into day4 values(108,'nancy','greenberg', 'ngreenbe','515.124.4569','1987-06-25','fi_mgr',12000.00,0.00,101,100);
insert into day4 values(109,'daniel','faviet','dfaviet','515.124.4169','1987-06-26','fi-account',9000.00,0.00,108,100);
insert into day4 values(110,'john','chen','jchen','515.124.4269','1987-06-27','fi-account',8200.00,0.00,108,100);
insert into day4 values(111,'ismael','sciarra','isciarra','515.124.4369','1987-06-28','fi_account',7700.00,0.00,108,100);
insert into day4 values(112,'jose manuel', 'urman','jmurman','515.124.4469','1987-06-29','fi_account',7800.00,0.00,108,100);
insert into day4 values(113,'luis','popp','lpopp','515.124.4567','1987-06-30','fi_account','1987-06-30','fi_account',6900.00,0.00,108,100);
insert into day4 values(114, 'den', 'raphaely','draphael','515.127.4561','1987-07-01','pu_man',11000.00,0.00,100,30);
insert into day4 values(115,'alexander','khoo', 'akhoo','515.127.4562','1987-07-02','pu_clerk',3100.00,0.00,114,30);
insert into day4 values(116,'shelli','baida','sbaida','515.127.4563','1987-07-03','pu_clerk',2900.00,0.00,114,30);
insert into day4 values(117, 'sigal','tobais','stobias','515.127.4564','1987-07-04','pu_clerk',2800.00,0.00,114,30);
insert into day4 values(118,'guy','himuro','ghimuro','515.127.4565','1987-07-05','pu-clerk',2600.00,0.00,114,30);

select * from day4;

#2
select first_name as 'first name', last_name as 'last name' from day4;
#3
select distinct department_id from day4;
#4
select count(employee_id) from day4;
#5
select avg(salary) from day4;
#6
select avg(salary) from day4 group by department_id;
#7
select sum(salary) from day4;
#8
select sum(salary) from day4 group by department_id;
#9
select last_name from day4 order by last_name desc;
#10
select * from day4 where first_name like '%e%';
#11
select * from day4 where last_name like '%a%a%' or '%aa%';