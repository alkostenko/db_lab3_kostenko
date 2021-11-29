select * from coffee;
create table coffeecopy as select * from coffee;
select*from coffeecopy;
drop table coffeecopy;

DO $$
declare
	id coffeecopy.id%type;
	cups_per_day coffeecopy.cups_per_day%type;
	coffee_type coffeecopy.coffee_type%type;
	
begin 
	id:=1;
	cups_per_day:=2;
	coffee_type:='Latte';
	for counter in 1..10
		loop
			insert into coffeecopy(id,cups_per_day, coffee_type)
			values (id+counter, cups_per_day||counter, coffee_type||counter);
		end loop;

end;
$$
	