-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: mld
-- ------------------------------------------------------
-- Server version	5.7.12-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `interface`
--

DROP TABLE IF EXISTS `interface`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `interface` (
  `idinterface` int(11) NOT NULL,
  `nom` varchar(30) DEFAULT NULL,
  `passerelle` varchar(30) DEFAULT NULL,
  `idrouteur` int(11) DEFAULT NULL,
  `adresseip` varchar(30) DEFAULT NULL,
  `adressemac` varchar(30) DEFAULT NULL,
  `masque` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`idinterface`),
  KEY `fk5` (`idrouteur`),
  CONSTRAINT `fk5` FOREIGN KEY (`idrouteur`) REFERENCES `routeur` (`idrouteur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `interface`
--

LOCK TABLES `interface` WRITE;
/*!40000 ALTER TABLE `interface` DISABLE KEYS */;
INSERT INTO `interface` VALUES (1,'0/0','192.168.3.1',1,'192.168.2.1','3A:32:96:CA:67:F5','255.255.255.0'),(2,'0/1','192.168.4.1',1,'192.168.3.1','3A:37:96:DA:67:F5','255.255.255.0');
/*!40000 ALTER TABLE `interface` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `machine`
--

DROP TABLE IF EXISTS `machine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `machine` (
  `idmachine` int(11) NOT NULL,
  `nom` varchar(30) DEFAULT NULL,
  `type` varchar(30) DEFAULT NULL,
  `passerelle` varchar(30) DEFAULT NULL,
  `adresseip` varchar(30) DEFAULT NULL,
  `adressemac` varchar(30) DEFAULT NULL,
  `masque` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`idmachine`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `machine`
--

LOCK TABLES `machine` WRITE;
/*!40000 ALTER TABLE `machine` DISABLE KEYS */;
INSERT INTO `machine` VALUES (1,'pc1','ordinateur','192.168.1.1','192.168.2.2','3A:36:56:C5:68:F5','255.255.255.0'),(2,'pc2','serveur','192.168.3.1','192.168.4.2','34:36:56:15:68:F5','255.255.255.0'),(3,'pc3','ordinateur','192.168.5.1','192.168.6.2','3A:36:56:75:68:05','255.255.255.0');
/*!40000 ALTER TABLE `machine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `port`
--

DROP TABLE IF EXISTS `port`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `port` (
  `idport` int(11) NOT NULL,
  `num` int(11) DEFAULT NULL,
  `debit` int(11) DEFAULT NULL,
  `etat` varchar(30) DEFAULT NULL,
  `idmachine` int(11) DEFAULT NULL,
  `idswitch` int(11) DEFAULT NULL,
  PRIMARY KEY (`idport`),
  KEY `fk2` (`idswitch`),
  KEY `fk3` (`idmachine`),
  CONSTRAINT `fk2` FOREIGN KEY (`idswitch`) REFERENCES `switch` (`idswitch`),
  CONSTRAINT `fk3` FOREIGN KEY (`idmachine`) REFERENCES `machine` (`idmachine`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `port`
--

LOCK TABLES `port` WRITE;
/*!40000 ALTER TABLE `port` DISABLE KEYS */;
INSERT INTO `port` VALUES (1,1,100,'inactif',1,1),(2,2,100,'inactif',2,1),(3,3,100,'inactif',3,1);
/*!40000 ALTER TABLE `port` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `portvlan`
--

DROP TABLE IF EXISTS `portvlan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `portvlan` (
  `idport` int(11) NOT NULL,
  `idvlan` int(11) NOT NULL,
  PRIMARY KEY (`idport`,`idvlan`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `portvlan`
--

LOCK TABLES `portvlan` WRITE;
/*!40000 ALTER TABLE `portvlan` DISABLE KEYS */;
INSERT INTO `portvlan` VALUES (1,1),(2,2),(3,3);
/*!40000 ALTER TABLE `portvlan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `routeur`
--

DROP TABLE IF EXISTS `routeur`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `routeur` (
  `idrouteur` int(11) NOT NULL,
  `nom` varchar(30) DEFAULT NULL,
  `type` varchar(30) DEFAULT NULL,
  `nbre_interfaces` int(11) DEFAULT NULL,
  `login` varchar(30) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  `idtableroutage` int(11) DEFAULT NULL,
  PRIMARY KEY (`idrouteur`),
  KEY `fk4` (`idtableroutage`),
  CONSTRAINT `fk4` FOREIGN KEY (`idtableroutage`) REFERENCES `tableroutage` (`idtableroutage`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `routeur`
--

LOCK TABLES `routeur` WRITE;
/*!40000 ALTER TABLE `routeur` DISABLE KEYS */;
INSERT INTO `routeur` VALUES (1,'r1','cisco',2,'admin1','admin1',1),(2,'r2','cisco',2,'admin2','admin2',2);
/*!40000 ALTER TABLE `routeur` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `switch`
--

DROP TABLE IF EXISTS `switch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `switch` (
  `idswitch` int(11) NOT NULL,
  `nom` varchar(30) DEFAULT NULL,
  `type` varchar(30) DEFAULT NULL,
  `adressemac` varchar(30) DEFAULT NULL,
  `nbre_ports` int(11) DEFAULT NULL,
  `login` varchar(30) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  `idtablemac` int(11) DEFAULT NULL,
  PRIMARY KEY (`idswitch`),
  KEY `fk1` (`idtablemac`),
  CONSTRAINT `fk1` FOREIGN KEY (`idtablemac`) REFERENCES `tableadressemac` (`idtablemac`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `switch`
--

LOCK TABLES `switch` WRITE;
/*!40000 ALTER TABLE `switch` DISABLE KEYS */;
INSERT INTO `switch` VALUES (1,'sw1','hp','B4:68:83:BD:CE:49',24,'user1','user1',1),(2,'sw2','cisco','AE:68:23:BD:8E:49',24,'user2','user',2),(3,'sw3','hp','B4:68:83:7D:9E:49',24,'user3','user3',3);
/*!40000 ALTER TABLE `switch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tableadressemac`
--

DROP TABLE IF EXISTS `tableadressemac`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tableadressemac` (
  `idtablemac` int(11) NOT NULL,
  `numvlan` int(11) DEFAULT NULL,
  `type` varchar(30) DEFAULT NULL,
  `adresse_mac` varchar(30) DEFAULT NULL,
  `numport` int(11) DEFAULT NULL,
  PRIMARY KEY (`idtablemac`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tableadressemac`
--

LOCK TABLES `tableadressemac` WRITE;
/*!40000 ALTER TABLE `tableadressemac` DISABLE KEYS */;
INSERT INTO `tableadressemac` VALUES (1,10,'dynamique','B4:6D:83:DD:CE:49',1),(2,20,'dynamique','3A:34:52:CA:69:B8',2),(3,30,'dynamique','3A:32:56:CA:68:F5',3);
/*!40000 ALTER TABLE `tableadressemac` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tableroutage`
--

DROP TABLE IF EXISTS `tableroutage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tableroutage` (
  `idtableroutage` int(11) NOT NULL,
  `rx_destination` varchar(30) DEFAULT NULL,
  `masque` varchar(30) DEFAULT NULL,
  `passerelle` varchar(30) DEFAULT NULL,
  `interface` varchar(30) DEFAULT NULL,
  `metrique` int(11) DEFAULT NULL,
  PRIMARY KEY (`idtableroutage`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tableroutage`
--

LOCK TABLES `tableroutage` WRITE;
/*!40000 ALTER TABLE `tableroutage` DISABLE KEYS */;
INSERT INTO `tableroutage` VALUES (1,'192.168.1.0','255.255.255.0','192.168.1.1','0/0',2),(2,'192.168.2.0','255.255.255.0','192.168.2.1','0/1',2);
/*!40000 ALTER TABLE `tableroutage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vlan`
--

DROP TABLE IF EXISTS `vlan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vlan` (
  `idvlan` int(11) NOT NULL,
  `type` varchar(30) DEFAULT NULL,
  `nomvlan` varchar(30) DEFAULT NULL,
  `idinterface` int(11) DEFAULT NULL,
  PRIMARY KEY (`idvlan`),
  KEY `fk6` (`idinterface`),
  CONSTRAINT `fk6` FOREIGN KEY (`idinterface`) REFERENCES `interface` (`idinterface`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vlan`
--

LOCK TABLES `vlan` WRITE;
/*!40000 ALTER TABLE `vlan` DISABLE KEYS */;
INSERT INTO `vlan` VALUES (1,'dynamique','vlan10',1),(2,'dynamique','vlan20',2);
/*!40000 ALTER TABLE `vlan` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-20 13:31:07
