create table coder
(
	id int not null,
	coding_hours int not null,
	coffee_id int not null,
	bugs_id int not null
);

create table coffee
(
	id int not null,
	cups_per_day int not null,
	coffee_type char(50)not null
);

create table bugs
(
	id int not null,
	solve_bugs char(50)not null
);

alter table coder add constraint pk_coder primary key (id);
alter table coffee add constraint pk_coffee primary key(id);
alter table bugs add constraint pk_bugs primary key(id);

alter table coder add constraint fk_coffee foreign key(coffee_id) references coffee(id);
alter table coder add constraint fk_bugs foreign key(bugs_id) references bugs(id);