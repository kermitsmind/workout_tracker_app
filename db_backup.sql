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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `diet`
--

LOCK TABLES `diet` WRITE;
/*!40000 ALTER TABLE `diet` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personal_information`
--

LOCK TABLES `personal_information` WRITE;
/*!40000 ALTER TABLE `personal_information` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rest`
--

LOCK TABLES `rest` WRITE;
/*!40000 ALTER TABLE `rest` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `running`
--

LOCK TABLES `running` WRITE;
/*!40000 ALTER TABLE `running` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `swimming`
--

LOCK TABLES `swimming` WRITE;
/*!40000 ALTER TABLE `swimming` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `weight_lifting`
--

LOCK TABLES `weight_lifting` WRITE;
/*!40000 ALTER TABLE `weight_lifting` DISABLE KEYS */;
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

-- Dump completed on 2022-01-19 12:51:41
