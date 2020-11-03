create database Probes;

create table Registries(
    Id int,
    Dominion varchar(15),
    Probe_name varchar(12),
    Dumpdate date,
    Dumptime time,
    Address varchar(30),
    Ping int,
    Status varchar(15),
    Code varchar(10),
    primary key Id
);

create table Probes(
    Id int,
    Dominion varchar(15),
    Probe_name varchar(12),
    Address varchar(15),
    Ratio int,
    Status varchar(10) default 'Inactive',
    primary key Id
);