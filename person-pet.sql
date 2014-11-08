drop table if exists person;
drop table if exists species;
drop table if exists breed;
drop table if exists pet;

CREATE TABLE species (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE breed (
	name TEXT,
	species_ID INTEGER,
	FOREIGN KEY(species_ID) REFERENCES species (id)
);

CREATE TABLE pet (
	name TEXT,
	dead INTEGER,
    breed INTEGER,
	FOREIGN KEY(breed) REFERENCES breed(species_ID)
);

CREATE TABLE person(
	first_name TEXT,
	last_name TEXT,
	age INTEGER,
	email TEXT,
	phone TEXT
);

INSERT INTO species VALUES (0, "Cat");
INSERT INTO species VALUES (1, "Dog");

INSERT INTO breed VALUES ("Tabby", 0);
INSERT INTO breed VALUES ("Mutt", 1);

INSERT INTO person VALUES ("Michael", "Nickey", 42, "mnickey@gmail.com", "111-111-1111");
