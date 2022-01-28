-- MySQL dump 10.13  Distrib 8.0.27, for macos11 (arm64)
--
-- Host: localhost    Database: WorkoutTrackerDB
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `diet`
--

DROP TABLE IF EXISTS `diet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `diet` (
  `diet_id` int NOT NULL AUTO_INCREMENT,
  `person_id` int NOT NULL,
  `name` varchar(90) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `stop_date` date DEFAULT NULL,
  `calories` int DEFAULT NULL,
  PRIMARY KEY (`diet_id`),
  KEY `person_id` (`person_id`),
  CONSTRAINT `diet_ibfk_1` FOREIGN KEY (`person_id`) REFERENCES `personal_information` (`person_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `diet`
--

LOCK TABLES `diet` WRITE;
/*!40000 ALTER TABLE `diet` DISABLE KEYS */;
INSERT INTO `diet` VALUES (1,2,'2000_calories','2021-12-13','2022-11-14',2000),(2,1,'HAHAHA','2022-01-19','2022-01-21',1230);
/*!40000 ALTER TABLE `diet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personal_information`
--

DROP TABLE IF EXISTS `personal_information`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personal_information` (
  `person_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(90) DEFAULT NULL,
  `last_name` varchar(90) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `phone_number` int DEFAULT NULL,
  `nationality` varchar(90) DEFAULT NULL,
  `registration_date` date DEFAULT NULL,
  PRIMARY KEY (`person_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personal_information`
--

LOCK TABLES `personal_information` WRITE;
/*!40000 ALTER TABLE `personal_information` DISABLE KEYS */;
INSERT INTO `personal_information` VALUES (1,'Adam','Smith','1998-03-12',123456789,'Polish','2011-12-12'),(2,'John','Wynn','1997-09-11',123456789,'Polish','2011-12-12'),(3,'a','b','2022-01-01',123234345,'American','2022-01-27'),(4,'John','W','2022-01-17',90909090,'American','2022-01-28'),(5,'a','a','2022-01-17',9098765,'Polish','2022-01-17');
/*!40000 ALTER TABLE `personal_information` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rest`
--

DROP TABLE IF EXISTS `rest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rest` (
  `rest_id` int NOT NULL AUTO_INCREMENT,
  `person_id` int NOT NULL,
  `date` date DEFAULT NULL,
  `night_sleep_hours` int DEFAULT NULL,
  `relax_hours` int DEFAULT NULL,
  PRIMARY KEY (`rest_id`),
  KEY `person_id` (`person_id`),
  CONSTRAINT `rest_ibfk_1` FOREIGN KEY (`person_id`) REFERENCES `personal_information` (`person_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rest`
--

LOCK TABLES `rest` WRITE;
/*!40000 ALTER TABLE `rest` DISABLE KEYS */;
INSERT INTO `rest` VALUES (1,5,'2022-01-28',7,0),(2,5,'2022-01-27',11,2),(4,1,'2022-01-28',7,0),(5,1,'2022-01-18',12,1);
/*!40000 ALTER TABLE `rest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `running`
--

DROP TABLE IF EXISTS `running`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `running` (
  `running_id` int NOT NULL AUTO_INCREMENT,
  `person_id` int NOT NULL,
  `date` date DEFAULT NULL,
  `type` varchar(90) DEFAULT NULL,
  `total_time` int DEFAULT NULL,
  `total_distance` int DEFAULT NULL,
  `terrain` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`running_id`),
  KEY `person_id` (`person_id`),
  CONSTRAINT `running_ibfk_1` FOREIGN KEY (`person_id`) REFERENCES `personal_information` (`person_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `running`
--

LOCK TABLES `running` WRITE;
/*!40000 ALTER TABLE `running` DISABLE KEYS */;
INSERT INTO `running` VALUES (2,1,'2022-01-19','interval',1278,9786,'indoor'),(4,1,'2022-01-24','QWERTY1',1578,2786,'outdoor'),(5,2,'2021-12-14','interval',1789,1786,'outdoor'),(7,3,'2022-01-27','sprint',123,12234,'outdoor'),(8,3,'2022-01-28','speed',1980,1990,'open'),(9,1,'2022-01-29','WWW',1,1,'o');
/*!40000 ALTER TABLE `running` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `swimming`
--

DROP TABLE IF EXISTS `swimming`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `swimming` (
  `swimming_id` int NOT NULL AUTO_INCREMENT,
  `person_id` int NOT NULL,
  `date` date DEFAULT NULL,
  `type` varchar(90) DEFAULT NULL,
  `total_time` int DEFAULT NULL,
  `total_distance` int DEFAULT NULL,
  `water` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`swimming_id`),
  KEY `person_id` (`person_id`),
  CONSTRAINT `swimming_ibfk_1` FOREIGN KEY (`person_id`) REFERENCES `personal_information` (`person_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `swimming`
--

LOCK TABLES `swimming` WRITE;
/*!40000 ALTER TABLE `swimming` DISABLE KEYS */;
INSERT INTO `swimming` VALUES (2,3,'2022-01-28','HAHA',19080,9900,'open'),(3,1,'2022-01-28','speed',123,1100,'outdoor');
/*!40000 ALTER TABLE `swimming` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `weight_lifting`
--

DROP TABLE IF EXISTS `weight_lifting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `weight_lifting` (
  `weight_lifting_id` int NOT NULL AUTO_INCREMENT,
  `person_id` int NOT NULL,
  `date` date DEFAULT NULL,
  `type` varchar(90) DEFAULT NULL,
  `no_series` int DEFAULT NULL,
  `repeats_per_series` int DEFAULT NULL,
  `weight` int DEFAULT NULL,
  PRIMARY KEY (`weight_lifting_id`),
  KEY `person_id` (`person_id`),
  CONSTRAINT `weight_lifting_ibfk_1` FOREIGN KEY (`person_id`) REFERENCES `personal_information` (`person_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `weight_lifting`
--

LOCK TABLES `weight_lifting` WRITE;
/*!40000 ALTER TABLE `weight_lifting` DISABLE KEYS */;
INSERT INTO `weight_lifting` VALUES (2,3,'2022-01-28','interval',12,4,30);
/*!40000 ALTER TABLE `weight_lifting` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-28 17:49:56
