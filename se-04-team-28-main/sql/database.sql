DROP database IF EXISTS `seteam28`;

CREATE DATABASE `seteam28`;

USE `seteam28`;

CREATE TABLE `Visitor`(
    `Citizen_id` INT NOT NULL AUTO_INCREMENT,
    `Visitor_name` VARCHAR(255) NOT NULL,
    `Address` VARCHAR(255) NOT NULL,
    `Phone_Number` VARCHAR(255),
    `Email` VARCHAR(255),
    `Device_id` VARCHAR(255) NOT NULL UNIQUE,
    `Infected` BOOLEAN NOT NULL DEFAULT false,
    PRIMARY KEY (`Citizen_id`)
);

ALTER TABLE
    `Visitor` AUTO_INCREMENT = 100;

CREATE TABLE `Place`(
    `Place_id` INT NOT NULL AUTO_INCREMENT,
    `Place_Name` VARCHAR(255) NOT NULL,
    `Address` VARCHAR(255) NOT NULL,
    `QRcode` VARCHAR(255) NOT NULL UNIQUE,
    PRIMARY KEY (`Place_id`)
);

ALTER TABLE
    `Place` AUTO_INCREMENT = 100;

CREATE TABLE `Agent`(
    `Agent_id` INT NOT NULL AUTO_INCREMENT,
    `Username` VARCHAR(255) NOT NULL,
    `Password` VARCHAR(255) NOT NULL,
    PRIMARY KEY(`Agent_id`)
);

ALTER TABLE
    `Agent` AUTO_INCREMENT = 100;

DROP TABLE IF EXISTS `Hospital`;

CREATE TABLE `Hospital`(
    `Hospital_id` INT NOT NULL AUTO_INCREMENT,
    `Username` VARCHAR(255) NOT NULL,
    `Password` VARCHAR(255) NOT NULL,
    PRIMARY KEY(`Hospital_id`)
);

ALTER TABLE
    `Hospital` AUTO_INCREMENT = 100;

CREATE TABLE `VisitorToPlace` (
    `QRcode` VARCHAR(255),
    `Device_id` VARCHAR(255),
    `Entry_time` DATETIME,
    `Exit_time` DATETIME,
    PRIMARY KEY(`QRcode`, `Device_id`, `Entry_time`),
    FOREIGN KEY(`QRcode`) REFERENCES `Place`(`QRcode`),
    FOREIGN KEY(`Device_id`) REFERENCES `Visitor`(`Device_id`)
);

INSERT INTO
    `Agent`(`Username`, `Password`)
VALUES
    ('Agent007', 'VerySecure123');

INSERT INTO
    `Agent`(`Username`, `Password`)
VALUES
    ('agent1', 'password');

INSERT INTO
    `Hospital`(`Username`, `Password`)
VALUES
    ('BremenNord', 'Bremen123');