----

- foreign keys, referential integrity, normalization
- one-to-many, many-to-many: intersection tables

----
transactions
isolation levels


-----
database design

EAV


-----


TODO: invent a sampling_area table and analysis table, to demonstrate one-to-many and many-to-many
TODO: create table analysis (id, name, date, is_safe, ...)
TODO: deletion cascades demo
TODO: transactions, isolation levels?


create table organism_types (id int auto_increment primary key) select distinct substring_index(organism_groups, ';', 1) as type from genomes;
alter table genomes add column type_id integer not null after organism_groups;
alter table genomes add constraint fk_type foreign key(type_id) references organism_types(id);

