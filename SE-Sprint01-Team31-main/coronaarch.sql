CREATE DATABASE corona archive;

CREATE TABLE users (
user_id INT AUTO_INCREMENT  NOT NULL PRIMARY KEY, 
user_firstname VARCHAR(20) NOT NULL, 
user_phoneno VARCHAR(20) NOT NULL UNIQUE,
user_emailadd VARCHAR(50) NOT NULL UNIQUE,
user_address VARCHAR(20),
user_lastname VARCHAR(20)
);

INSERT INTO users (user_firstname, user_phoneno, user_emailadd, user_address, user_lastname) 
VALUES (Idris, “017685156567”, “i.chendid@jacobs-university.de”, “NB-116, Nordmetall”, Chendid)
);

INSERT INTO users (user_firstname, user_phoneno, user_emailadd, user_address, user_lastname) 
VALUES (“Fizza”, “01514504778”, “f.usman@jacobs-university.de”, “MC-345, Mercator”, “Usman”)
);

DROP TABLE users;
