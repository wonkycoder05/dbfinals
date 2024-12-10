-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 22, 2024 at 01:10 PM
-- Server version: 8.3.0
-- PHP Version: 8.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
USE dbfinal;
--
-- Database: `car_rental`
--

-- --------------------------------------------------------

--
-- Table structure for table `car`
--

DROP TABLE IF EXISTS `car`;
CREATE TABLE IF NOT EXISTS `car` (
  `CarID` varchar(20) NOT NULL,
  `PlateNum` varchar(20) NOT NULL,
  `CarType` varchar(50) DEFAULT NULL,
  `CarModel` varchar(50) DEFAULT NULL,
  `CarColor` varchar(20) DEFAULT NULL,
  `FuelType` varchar(20) DEFAULT NULL,
  `MaintenanceStatus` varchar(20) DEFAULT NULL,
  `PriceList` int NOT NULL,
  PRIMARY KEY (`CarID`),
  UNIQUE KEY `PlateNum` (`PlateNum`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `car`
--

INSERT INTO `car` (`CarID`, `PlateNum`, `CarType`, `CarModel`, `CarColor`, `FuelType`, `MaintenanceStatus`, `PriceList`) VALUES
('CID000001', 'A 7267 EFD', 'SUV', 'Lamborghini Urus', 'Black', 'Gas', 'Done', 9000000),
('CID000002', 'D 9401 BYW', 'SUV', 'BMW X6 M Sport', 'White', 'Gas', 'In Progress', 4500000),
('CID000003', 'F 2438 MSE', 'SUV', 'Mercedes-Benz G63*', 'Black', 'Gas', 'Done', 5500000);

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
CREATE TABLE IF NOT EXISTS `customer` (
  `CustID` varchar(20) NOT NULL,
  `CustName` varchar(100) NOT NULL,
  `PhoneNum` varchar(20) DEFAULT NULL,
  `EmailAdd` varchar(100) DEFAULT NULL,
  `HomeAdd` varchar(255) DEFAULT NULL,
  `SocialSecNum` varchar(20) NOT NULL,
  PRIMARY KEY (`CustID`),
  UNIQUE KEY `SocialSecNum` (`SocialSecNum`),
  UNIQUE KEY `EmailAdd` (`EmailAdd`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`CustID`, `CustName`, `PhoneNum`, `EmailAdd`, `HomeAdd`, `SocialSecNum`) VALUES
('C00001', 'Niall Morrow', '+62-855-555-092', 'Niall.Morrow@gmail.com', 'Jl. Melati Raya No. 15, Kemang, South Jakarta, DKI Jakarta 12730, Indonesia', '3172012304560001'),
('C00002', 'Oliwia Mccarty', '+62-899-555-568', 'Oliwia.Mccarty@gmail.com', 'Jl. Ahmad Yani No. 8, Senen, Central Jakarta, DKI Jakarta 10410, Indonesia', '3273051406780002'),
('C00003', 'Neve Reyes', '+62-855-555-092', 'Neve.Reyes@gmail.com', 'Jl. Taman Sari No. 3, Kebayoran Baru, South Jakarta, DKI Jakarta 12150, Indonesia', '3174052103890003');

-- --------------------------------------------------------

--
-- Table structure for table `damage`
--

DROP TABLE IF EXISTS `damage`;
CREATE TABLE IF NOT EXISTS `damage` (
  `DmgID` varchar(20) NOT NULL,
  `CustID` varchar(20) NOT NULL,
  `PlateNum` varchar(20) NOT NULL,
  `VehicleModel` varchar(50) DEFAULT NULL,
  `MaintStatus` varchar(20) DEFAULT NULL,
  `DmgDone` varchar(255) DEFAULT NULL,
  `DmgPrice` int DEFAULT NULL,
  PRIMARY KEY (`DmgID`),
  KEY `CustID` (`CustID`),
  KEY `PlateNum` (`PlateNum`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `damage`
--

INSERT INTO `damage` (`DmgID`, `CustID`, `PlateNum`, `VehicleModel`, `MaintStatus`, `DmgDone`, `DmgPrice`) VALUES
('DMG000000001', 'C00001', 'F 8958 MMN', 'BMW 760i xDrive', 'Completed', 'Front Bumper Smashed', 12000000);

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
CREATE TABLE IF NOT EXISTS `employee` (
  `EmployeeID` varchar(20) NOT NULL,
  `FirstName` varchar(50) NOT NULL,
  `LastName` varchar(50) NOT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `PhoneNumber` varchar(20) DEFAULT NULL,
  `Role` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`EmployeeID`),
  UNIQUE KEY `Email` (`Email`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`EmployeeID`, `FirstName`, `LastName`, `Email`, `PhoneNumber`, `Role`) VALUES
('EMP0001', 'John', 'Williams', 'john.william@gmail.com', '+62-510-320-322', 'Chief Executive Officer'),
('EMP0002', 'Madeline', 'Cruz', 'madeline.cruz@gmail.com', '+62-128-231-427', 'General Manager'),
('EMP0003', 'Michael', 'Sanchez', 'michael.sanchez@gmail.com', '+62-215-890-445', 'Intern');

-- --------------------------------------------------------

--
-- Table structure for table `maintenancelog`
--

DROP TABLE IF EXISTS `maintenancelog`;
CREATE TABLE IF NOT EXISTS `maintenancelog` (
  `LogID` varchar(20) NOT NULL,
  `PlateNum` varchar(20) NOT NULL,
  `MaintenanceType` varchar(100) DEFAULT NULL,
  `MaintStatus` varchar(20) DEFAULT NULL,
  `WorkshopLocation` varchar(100) DEFAULT NULL,
  `MaintCost` int DEFAULT NULL,
  PRIMARY KEY (`LogID`),
  KEY `PlateNum` (`PlateNum`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `maintenancelog`
--

INSERT INTO `maintenancelog` (`LogID`, `PlateNum`, `MaintenanceType`, `MaintStatus`, `WorkshopLocation`, `MaintCost`) VALUES
('M000001', 'D 9401 BYW', 'Engine Flush', 'Done', 'BMW Kota Bandung', 100000),
('M000002', 'F 2438 MSE', 'Brake Pads Change', 'Done', 'Mercedes Benz Kota Bogor', 600000),
('M000003', 'D 2715 HIN', 'Oil Change', 'Done', 'Dennis Supercars Jakarta', 300000);

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

DROP TABLE IF EXISTS `payment`;
CREATE TABLE IF NOT EXISTS `payment` (
  `PaymentID` varchar(20) NOT NULL,
  `RentalID` varchar(20) NOT NULL,
  `AmountPaid` int NOT NULL,
  `PaymentDate` date NOT NULL,
  `PaymentMethod` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`PaymentID`),
  KEY `RentalID` (`RentalID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`PaymentID`, `RentalID`, `AmountPaid`, `PaymentDate`, `PaymentMethod`) VALUES
('P0001', 'R00001', 70000000, '2024-02-21', 'Debit Card'),
('P0002', 'R00002', 525000000, '2024-09-19', 'Cash'),
('P0003', 'R00003', 76000000, '2024-10-05', 'Debit Card');

-- --------------------------------------------------------

--
-- Table structure for table `rental`
--

DROP TABLE IF EXISTS `rental`;
CREATE TABLE IF NOT EXISTS `rental` (
  `RentalID` varchar(20) NOT NULL,
  `PlateNum` varchar(20) NOT NULL,
  `CustID` varchar(20) NOT NULL,
  `RentalDate` date NOT NULL,
  `ReturnDate` date NOT NULL,
  `DaysElapsed` int DEFAULT NULL,
  PRIMARY KEY (`RentalID`),
  KEY `PlateNum` (`PlateNum`),
  KEY `CustID` (`CustID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `rental`
--

INSERT INTO `rental` (`RentalID`, `PlateNum`, `CustID`, `RentalDate`, `ReturnDate`, `DaysElapsed`) VALUES
('R00001', 'D 7395 HUG', 'C00001', '2024-05-07', '2024-05-14', 7),
('R00002', 'D 9401 BYW', 'C00002', '2024-05-16', '2024-05-21', 5),
('R00003', 'B 6935 LDU', 'C00003', '2024-03-13', '2024-03-19', 6);

-- --------------------------------------------------------

--
-- Table structure for table `reservation`
--

DROP TABLE IF EXISTS `reservation`;
CREATE TABLE IF NOT EXISTS `reservation` (
  `ReservationID` varchar(20) NOT NULL,
  `CustID` varchar(20) NOT NULL,
  `VehicleID` varchar(20) NOT NULL,
  `ReservationDate` date NOT NULL,
  `StartDate` date NOT NULL,
  `EndDate` date NOT NULL,
  `Status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ReservationID`),
  KEY `CustID` (`CustID`),
  KEY `VehicleID` (`VehicleID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `reservation`
--

INSERT INTO `reservation` (`ReservationID`, `CustID`, `VehicleID`, `ReservationDate`, `StartDate`, `EndDate`, `Status`) VALUES
('1', 'C00001', 'CID000001', '2024-11-01', '2024-11-10', '2024-11-15', 'Confirmed'),
('2', 'C00002', 'CID000002', '2024-11-03', '2024-11-20', '2024-11-25', 'Cancelled'),
('3', 'C00003', 'CID000003', '2024-11-05', '2024-12-01', '2024-12-10', 'Confirmed');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
