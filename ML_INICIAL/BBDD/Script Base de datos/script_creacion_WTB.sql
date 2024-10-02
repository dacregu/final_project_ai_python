CREATE DATABASE  IF NOT EXISTS `wtb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `wtb`;
-- MySQL dump 10.13  Distrib 8.0.16, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: wtb
-- ------------------------------------------------------
-- Server version	8.0.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `beers`
--

DROP TABLE IF EXISTS `beers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `beers` (
  `beer_beerid` int(11) NOT NULL AUTO_INCREMENT,
  `brewery_id` int(11) DEFAULT NULL,
  `beer_name` varchar(100) NOT NULL,
  `beer_style` varchar(100) DEFAULT NULL,
  `beer_abv` float DEFAULT NULL,
  PRIMARY KEY (`beer_beerid`),
  UNIQUE KEY `beer_name_UNIQUE` (`beer_name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `beers`
--

LOCK TABLES `beers` WRITE;
/*!40000 ALTER TABLE `beers` DISABLE KEYS */;
INSERT INTO `beers` VALUES (1,1,'Estrella Light','Lager',3.5),(2,3,'Heineken Plus','Black',4);
/*!40000 ALTER TABLE `beers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `breweries`
--

DROP TABLE IF EXISTS `breweries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `breweries` (
  `brewery_id` int(11) NOT NULL AUTO_INCREMENT,
  `brewery_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`brewery_id`),
  UNIQUE KEY `brewery_name_UNIQUE` (`brewery_name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `breweries`
--

LOCK TABLES `breweries` WRITE;
/*!40000 ALTER TABLE `breweries` DISABLE KEYS */;
INSERT INTO `breweries` VALUES (1,'DAMM SA'),(3,'HEINEKEN SA'),(2,'MORITZ SA');
/*!40000 ALTER TABLE `breweries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `correlation`
--

DROP TABLE IF EXISTS `correlation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `correlation` (
  `beer_id` int(11) NOT NULL,
  `beer_idcorr` int(11) NOT NULL,
  `correlation` float NOT NULL,
  PRIMARY KEY (`beer_id`,`beer_idcorr`),
  KEY `fk_beer_idcorr_idx` (`beer_idcorr`),
  CONSTRAINT `fk_beer_id` FOREIGN KEY (`beer_id`) REFERENCES `beers` (`beer_beerid`),
  CONSTRAINT `fk_beer_idcorr` FOREIGN KEY (`beer_idcorr`) REFERENCES `beers` (`beer_beerid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `correlation`
--

LOCK TABLES `correlation` WRITE;
/*!40000 ALTER TABLE `correlation` DISABLE KEYS */;
/*!40000 ALTER TABLE `correlation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `reviews` (
  `review_id` int(11) NOT NULL AUTO_INCREMENT,
  `beer_idbeer` int(11) DEFAULT NULL,
  `review_taste` float DEFAULT NULL,
  `review_palate` float DEFAULT NULL,
  `review_aroma` float DEFAULT NULL,
  `review_appeareance` float DEFAULT NULL,
  `review_overall` float DEFAULT NULL,
  `users_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`review_id`),
  KEY `fk_beers_reviews_idx` (`beer_idbeer`),
  KEY `fk_users_reviews_idx` (`users_id`),
  CONSTRAINT `fk_beers_reviews` FOREIGN KEY (`beer_idbeer`) REFERENCES `beers` (`beer_beerid`),
  CONSTRAINT `fk_users_reviews` FOREIGN KEY (`users_id`) REFERENCES `users` (`users_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES (1,1,3,4,3,4,3.5,1),(2,2,2,2,2,2,2,3),(3,2,4,4,4,3,3.75,2);
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `users` (
  `users_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`users_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Diego'),(2,'Daniel'),(3,'Alberto'),(4,'Adri'),(5,'Toni');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-24  9:47:37
