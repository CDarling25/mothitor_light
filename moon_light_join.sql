CREATE TABLE `MacLeish` (
  `UTC_Date_And_Time` text,
  `Local_Date_And_Time` text,
  `Temperature` double DEFAULT NULL,
  `Counts` double DEFAULT NULL,
  `Frequency` double DEFAULT NULL,
  `MSAS` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `moon_phases` (
  `Date` text,
  `Area` double DEFAULT NULL,
  `Category` int DEFAULT NULL,
  `Phase` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOAD DATA INFILE '20250227_120000_SQM-MacLeish.csv' INTO TABLE MacLeish
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA INFILE 'moon_phases_UTC_1800-2050.csv' INTO TABLE moon_phases
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

SELECT *
FROM mothitor_light.MacLeish
INNER JOIN mothitor_light.moon_phases
ON mothitor_light.moon_phases.Date = SUBSTRING(`UTC_Date_And_Time`, 1, 10);
