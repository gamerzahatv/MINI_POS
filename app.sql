-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 16, 2022 at 04:09 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `app`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `ID_USER` int(255) NOT NULL COMMENT 'ไอดีลูกค้า',
  `NAME_USER` varchar(80) CHARACTER SET utf8 NOT NULL COMMENT 'ชือ',
  `PHONE_USER` varchar(10) NOT NULL COMMENT 'เบอร์',
  `ADDRESS_USER` varchar(80) NOT NULL COMMENT 'ที่อยู่',
  `SEX_USER` char(1) NOT NULL COMMENT 'เพศ'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `ordercus`
--

CREATE TABLE `ordercus` (
  `ORDER_NUM` varchar(20) CHARACTER SET utf8 NOT NULL COMMENT 'ไอดีตะกร้าสินค้า',
  `NOWDATE` varchar(20) NOT NULL COMMENT 'วันที่',
  `ORDER_TIME` varchar(20) NOT NULL COMMENT 'เวลา',
  `Payment` float NOT NULL COMMENT 'ยอดรวมการซื้อ',
  `ID_USER` varchar(255) NOT NULL COMMENT 'ไอดีลูกค้า',
  `NAME_USER` varchar(255) CHARACTER SET utf8 NOT NULL COMMENT 'ชื่อลูกค้า',
  `bill_now` int(7) NOT NULL COMMENT 'จัดเรียงบิล'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `order_line`
--

CREATE TABLE `order_line` (
  `ORDER_NUM` varchar(20) CHARACTER SET utf8 NOT NULL COMMENT 'ไอดีตะกร้า',
  `PART_ID` varchar(255) CHARACTER SET utf8 NOT NULL COMMENT 'รหัสสินค้า',
  `PART_NAME` varchar(255) NOT NULL COMMENT 'ชื่อสินค้า',
  `NUM_ORDER` int(255) NOT NULL COMMENT 'จำนวนสั่ง',
  `QTY_PART` int(255) NOT NULL COMMENT 'จำนวนสินค้าในคลัง',
  `PRICE_ORDER` int(255) NOT NULL COMMENT 'ราคา'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `part`
--

CREATE TABLE `part` (
  `PART_ID` varchar(255) CHARACTER SET utf8 NOT NULL COMMENT 'ไอดีสินค้า',
  `PART_NAME` varchar(255) CHARACTER SET utf8 NOT NULL COMMENT 'ชื่อสินค้า',
  `QTY_PART` int(255) NOT NULL COMMENT 'จำนวนในคลัง',
  `TYPE_PART` varchar(255) CHARACTER SET utf8 NOT NULL COMMENT 'ประเภท',
  `UNIT_PART` double NOT NULL COMMENT 'ราคาต่อชิ้น',
  `TAG_PART` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`ID_USER`),
  ADD UNIQUE KEY `NAME_USER` (`NAME_USER`),
  ADD UNIQUE KEY `PHONE_USER` (`PHONE_USER`);

--
-- Indexes for table `ordercus`
--
ALTER TABLE `ordercus`
  ADD PRIMARY KEY (`bill_now`),
  ADD UNIQUE KEY `ORDER_NUM` (`ORDER_NUM`),
  ADD KEY `bill_now` (`bill_now`);

--
-- Indexes for table `part`
--
ALTER TABLE `part`
  ADD PRIMARY KEY (`PART_ID`),
  ADD UNIQUE KEY `tag` (`TAG_PART`),
  ADD UNIQUE KEY `PART_NAME` (`PART_NAME`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `ID_USER` int(255) NOT NULL AUTO_INCREMENT COMMENT 'ไอดีลูกค้า';

--
-- AUTO_INCREMENT for table `ordercus`
--
ALTER TABLE `ordercus`
  MODIFY `bill_now` int(7) NOT NULL AUTO_INCREMENT COMMENT 'จัดเรียงบิล';

--
-- AUTO_INCREMENT for table `part`
--
ALTER TABLE `part`
  MODIFY `TAG_PART` int(255) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
