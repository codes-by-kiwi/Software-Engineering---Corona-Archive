DROP database IF EXISTS `corona_app`;

CREATE database 
IF NOT EXISTS `corona_app`;

USE `corona_app`;

-- creation of tables
CREATE TABLE `Visitor` (
  `citizen_id` INT NOT NULL AUTO_INCREMENT,
  `visitor_name` VARCHAR(255) NOT NULL,
  `address` VARCHAR(255) NOT NULL,
  `email` VARCHAR(30),
  `phone_number` VARCHAR(30),
  `device_id` VARCHAR(255) NOT NULL UNIQUE,
  `infected` BOOLEAN NOT NULL DEFAULT false,
  PRIMARY KEY (`citizen_id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci COMMENT = 'holds all the data for visitors';

CREATE TABLE `Place`(
  `place_id` INT NOT NULL AUTO_INCREMENT,
  `place_name` VARCHAR(255) NOT NULL,
  `address` VARCHAR(255) NOT NULL,
  `qr_code` VARCHAR(255) NOT NULL UNIQUE,
  PRIMARY KEY (`place_id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci COMMENT = 'holds all the data for the registered places';

CREATE TABLE `Agent` (
  `agent_id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(255) NOT NULL UNIQUE,
  `password` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`agent_id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci COMMENT = 'holds the authentification data for the agents';

CREATE TABLE `Hospital` (
  `hospital_id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(255) NOT NULL UNIQUE,
  `password` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`hospital_id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci COMMENT = 'holds the authentification data for the hospitals';

CREATE TABLE `VisitorsToPlaces` (
  `qr_code` VARCHAR(255) NOT NULL,
  `device_id` VARCHAR(255)  NOT NULL,
  `entry_time` DATETIME NOT NULL,
  `exit_time` DATETIME,

  PRIMARY KEY(`qr_code`, `device_id`, `entry_time`),
  FOREIGN KEY (`qr_code`) REFERENCES `Place`(`qr_code`) ON UPDATE CASCADE,
  FOREIGN KEY (`device_id`) REFERENCES `Visitor`(`device_id`) ON UPDATE CASCADE
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci COMMENT = 'holds the data of the visitors entering registered places';

USE corona_app;
INSERT INTO `Agent` (`username`, `password`) VALUES ("agent1", "password");
INSERT INTO `Hospital` (`username`, `password`) VALUES ("hospital1", "password");
