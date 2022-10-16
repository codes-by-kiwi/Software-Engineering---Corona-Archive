DROP TABLE IF EXISTS Visitor;
DROP TABLE IF EXISTS VisitorToPlaces;
DROP TABLE IF EXISTS Places;
DROP TABLE IF EXISTS Hospital;
DROP TABLE IF EXISTS Agent;


CREATE TABLE Visitor (
    citizen_id INTEGER PRIMARY KEY AUTOINCREMENT,
    visitor_name TEXT NOT NULL,
    address TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    email TEXT NOT NULL,
    device_ID TEXT NOT NULL,
    infected TEXT NOT NULL
);

CREATE TABLE VisitorToPlaces (
    QRcode TEXT NOT NULL,
    device_ID TEXT NOT NULL,
    entry_date DATE NOT NULL,
    entry_time TEXT NOT NULL,
    exit_date DATE NOT NULL,
    exit_time TEXT NOT NULL
);

CREATE TABLE Places (
    place_id INTEGER PRIMARY KEY AUTOINCREMENT,
    place_name TEXT NOT NULL,
    address TEXT NOT NULL,
    QRcode TEXT NOT NULL
);

CREATE TABLE Hospital (
    hospital_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE Agent (
    agent_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

-- changes made in sprint 2

-- adding the engine for all the tables
ALTER TABLE `visitor`
ENGINE = InnoDB;

ALTER TABLE `places`
ENGINE = InnoDB;

ALTER TABLE `agent`
ENGINE = InnoDB;

ALTER TABLE `hospital`
ENGINE = InnoDB;

ALTER TABLE `visitortoplaces`
ENGINE = InnoDB;

-- altering table `visitortoplaces` to drop the QRcode and device_ID and add citizen_id and place_id as foreign keys, also added a primary key for the table

ALTER TABLE `visitortoplaces`
DROP `QRcode`,
DROP `device_ID`;

ALTER TABLE `visitortoplaces`
ADD `place_ID` INTEGER NOT NULL;

ALTER TABLE `visitortoplaces`
ADD `citizen_ID` INTEGER NOT NULL;

ALTER TABLE `visitortoplaces`
ADD CONSTRAINT `place_id`
FOREIGN KEY (`place_id`)
REFERENCES `places`(`place_id`);

ALTER TABLE `visitortoplaces`
ADD CONSTRAINT `citizen_id`
FOREIGN KEY (`citizen_id`)
REFERENCES `visitor`(`citizen_id`);

ALTER TABLE `visitortoplaces`
ADD COLUMN `visitortoplaces_id` INTEGER;

ALTER TABLE `visitortoplaces`
CHANGE `visitortoplaces_id` `visitortoplaces_id` INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY;

-- changed attribute infected to be of type boolean as required
ALTER TABLE `visitor`
CHANGE `infected` `infected` BOOLEAN;

-- as visitors can choose to input email and or phone number, we changed the attributes to not include NOT NULL (same for device_id)
ALTER TABLE `visitor`
CHANGE `email` `email` TEXT;

ALTER TABLE `visitor`
CHANGE `phone_number` `phone_number` TEXT;

ALTER TABLE `visitor`
CHANGE `device_ID` `device_ID` TEXT;

-- added contact attribute for places 
ALTER TABLE `places`
ADD COLUMN `place_contact` TEXT NOT NULL;

-- made QRcode not mandatory to input in the beginning (dropped the NOT NULL attibute), as place owners don't have it when they register
ALTER TABLE `places`
CHANGE `QRcode` `QRcode` TEXT;

-- add fake instances 

INSERT INTO `visitor`(`visitor_name`,`address`,`email`) VALUES ("Fizza Usman", "Bremen, College Ring 6", "f.usman@jacobs-university.de");
INSERT INTO `visitor`(`visitor_name`,`address`,`email`) VALUES ("Denisa Checiu", "Bremen, College Ring 3", "d.checiu@jacobs-university.de");
INSERT INTO `visitor`(`visitor_name`,`address`,`email`) VALUES ("Suzy Bare", "Bremen, College Ring 2", "s.bare@jacobs-university.de");
INSERT INTO `visitor`(`visitor_name`,`address`,`email`) VALUES ("Sherry Usman", "Bremen, College Ring 6", "s.usman@jacobs-university.de");
INSERT INTO `visitor`(`visitor_name`,`address`,`email`) VALUES ("Idalmy Bustillo", "Bremen, College Ring 2", "i.bustillo@jacobs-university.de");
INSERT INTO `visitor`(`visitor_name`,`address`,`email`) VALUES ("Rayan Ranasinghe", "Bremen, College Ring 1", "r.ranasinghe@jacobs-university.de");
INSERT INTO `visitor`(`visitor_name`,`address`,`email`) VALUES ("Alexia Bare", "Bremen, College Ring 5", "a.bare@jacobs-university.de");
INSERT INTO `visitor`(`visitor_name`,`address`,`email`) VALUES ("Sia Shende", "Bremen, College Ring 5", "s.shende@jacobs-university.de");
INSERT INTO `visitor`(`visitor_name`,`address`,`email`) VALUES ("Maria Castanio", "Bremen, College Ring 5", "m.castanio@jacobs-university.de");
INSERT INTO `visitor`(`visitor_name`,`address`,`email`,`infected`) VALUES ("Valeria Bare", "Bremen, College Ring 5", "v.bare@jacobs-university.de", "1");
INSERT INTO `visitor`(`visitor_name`,`address`,`email`, `infected`) VALUES ("Maria Shende", "Bremen, College Ring 5", "m.shende@jacobs-university.de", "1");
INSERT INTO `visitor`(`visitor_name`,`address`,`email`, `infected`) VALUES ("Anastasia Castanio", "Bremen, College Ring 5", "a.castanio@jacobs-university.de", "1");
 
INSERT INTO `places`(`place_name`,`address`,`place_contact`) VALUES ("Coffee Bar", "Bremen 12345", "+49739227828");
INSERT INTO `places`(`place_name`,`address`,`place_contact`) VALUES ("Kauflan", "Bremen 74893", "+4982372384878");
INSERT INTO `places`(`place_name`,`address`,`place_contact`) VALUES ("Wolfworth", "Bremen 87838", "+498123588494");
INSERT INTO `places`(`place_name`,`address`,`place_contact`) VALUES ("Waterfront", "Bremen 37766", "+4982372384878");
INSERT INTO `places`(`place_name`,`address`,`place_contact`) VALUES ("Netto", "Bremen 21112", "+4943433434878");

 
 INSERT INTO `Agent` (`username`, `password`) VALUES ("agent1", "12345");
 
 INSERT INTO `Hospital` (`username`, `password`) VALUES ("hospital1", "12345");

-- queries 

-- showcase all the visitors which are currently infected
SELECT `visitor_name` FROM `visitor` WHERE `infected` = 1;
