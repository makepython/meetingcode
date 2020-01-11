Preparation
-----------

Data about bacteria from https://www.ncbi.nlm.nih.gov/genome/browse/#!/overview/
https://www.ncbi.nlm.nih.gov/home/about/policies/

    git clone https://github.com/makepython/meetingcode.git
    cd meetingcode/sql/basicsql
    bunzip2 genomes.csv.bz2


Create database
---------------

create database (if not exist)


Create table
------------

    create table genomes (
        id integer auto_increment primary key,
        organism_name varchar(512) not null,
        organism_groups varchar(1024),
        size float,
        chromosomes integer,
        organelles integer,
        plasmids integer,
        assemblies integer
    )

column types
column attributes: primary key
column constraints: unique
primary key choice: natural vs surrogate

Import data
-----------

    load data local infile 'genomes.csv' into table genomes
        fields terminated by ','
        enclosed by '"'
        ignore 1 lines
        (organism_name, organism_groups, size, chromosomes, organelles, plasmids, assemblies)


Select
------

    select organism_name from genomes;
    select organism_name, size from genomes;
    select * from genomes;

where clause:

    select organism_name from genomes where chromosomes = 5;

Aggregate queries:

    select chromosomes, count(*) from genomes group by chromosomes;

Variable naming

    select chromosomes+plasmids as total, count(*) from genomes group by total;

Having clause:
    select chromosomes+plasmids as total, count(*) from genomes group by total having total > 10;

Order by:
    select organism_name, size from genomes order by size desc limit 10;
    select organism_name from genomes where organism_name like "%Escherichia coli%";

Distinct:

    select distinct substring_index(organism_groups, ';', 1) from genomes;

Incorrect select. Not the organism name with the highest size:
    select organism_name, max(size) from genomes; -- this is a bad query!!


Insert
------
TODO: populate tables with insert statements


Update
------
TODO: update values

Delete
------

