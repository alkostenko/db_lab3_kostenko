
--coffee
insert into coffee(id, cups_per_day, coffee_type) values(1,2,'Latte');
insert into coffee(id, cups_per_day, coffee_type) values(2,2,'Americano');
insert into coffee(id, cups_per_day, coffee_type) values(3,2,'Americano');
insert into coffee(id, cups_per_day, coffee_type) values(4,3,'Espresso');
insert into coffee(id, cups_per_day, coffee_type) values(5,3,'Cappuccino');
insert into coffee(id, cups_per_day, coffee_type) values(6,1,'Nescafe');
insert into coffee(id, cups_per_day, coffee_type) values(7,2,'Americano');
insert into coffee(id, cups_per_day, coffee_type) values(8,1,'Cappuccino');
insert into coffee(id, cups_per_day, coffee_type) values(9,5,'Americano');
insert into coffee(id, cups_per_day, coffee_type) values(10,1,'Americano');

--bugs
insert into bugs(id, solve_bugs) values(1,'Sometimes');
insert into bugs(id, solve_bugs) values(2,'Yes');
insert into bugs(id, solve_bugs) values(3,'Sometimes');
insert into bugs(id, solve_bugs) values(4,'Sometimes');
insert into bugs(id, solve_bugs) values(5,'Sometimes');
insert into bugs(id, solve_bugs) values(6,'Yes');
insert into bugs(id, solve_bugs) values(7,'No');
insert into bugs(id, solve_bugs) values(8,'Yes');
insert into bugs(id, solve_bugs) values(9,'Yes');
insert into bugs(id, solve_bugs) values(10,'Sometimes');

--coder
insert into coder(id,coffee_id, bugs_id, coding_hours) values(1,1,1, 8);
insert into coder(id,coffee_id, bugs_id, coding_hours) values(2,2,2, 3);
insert into coder(id,coffee_id, bugs_id, coding_hours) values(3,3,3, 10);
insert into coder(id,coffee_id, bugs_id, coding_hours) values(4,4,4, 3);
insert into coder(id,coffee_id, bugs_id, coding_hours) values(5,5,5, 5);
insert into coder(id,coffee_id, bugs_id, coding_hours) values(6,6,6, 7);
insert into coder(id,coffee_id, bugs_id, coding_hours) values(7,7,7, 2);
insert into coder(id,coffee_id, bugs_id, coding_hours) values(8,8,8, 1);
insert into coder(id,coffee_id, bugs_id, coding_hours) values(9,9,9, 4);
insert into coder(id,coffee_id, bugs_id, coding_hours) values(10,10,10, 10);