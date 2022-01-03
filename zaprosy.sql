insert into colors (name)
select * from
(select  distinct trim(color1) from animals where color2 is not null
union
select  distinct trim(color2) from animals where color2 is not null);

select * from colors;
update colors set id = id-4 ;

create table animal_color (
        animal_id int,
        color_id int);

insert into animal_color
select animals.'index',
       colors.name
from animals
join colors on trim(animals.color1)=trim(colors.name);

insert into animal_color
select animals.'index',
       colors.name
from animals
join colors on trim(animals.color2)=trim(colors.name);

drop table outcomes;

create table outcomes (
    outcome_id integer primary key autoincrement,
    age_upon_outcome varchar(50),
    outcome_subtype varchar(50),
    outcome_type varchar(50),
    outcome_month int,
    outcome_year int
);

insert into outcomes(age_upon_outcome, outcome_subtype, outcome_type, outcome_month, outcome_year)
select distinct age_upon_outcome, outcome_subtype, outcome_type, outcome_month, outcome_year
from animals;

create table animal_types (
    id integer primary key autoincrement,
    name varchar(50)
);
insert into animal_types(name)
select distinct (animal_type) from animals;

create table breed (
    id integer primary key autoincrement,
    name varchar(50)
);
insert into breed(name)
select distinct (breed) from animals;


create table animals_fin (
    id integer primary key autoincrement,
    animal_id varchar(50),
    type_id integer,
    name varchar(50),
    breed_id integer,
    date_of_birth date

);

insert into animals_fin (animal_id, type_id, name, breed_id, date_of_birth)
select distinct animal_id, animal_types.id, animals.name, breed.id, date_of_birth
from animals
left join animal_types on animals.animal_type= animal_types.name
left join breed on animals.breed=breed.name;

select
       animal_id, animal_types.name, animals_fin.name, breed.name, date_of_birth
from animals_fin
inner join breed on animals_fin.breed_id = breed.id
inner join animal_types on animals_fin.type_id = animal_types.id;
