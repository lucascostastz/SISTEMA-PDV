-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 192.168.1.2    Database: pdv
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `idclientes` int unsigned NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) DEFAULT NULL,
  `cpf` varchar(45) DEFAULT NULL,
  `rg` varchar(45) DEFAULT NULL,
  `telefone` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `cep` varchar(45) DEFAULT NULL,
  `endereco` varchar(45) DEFAULT NULL,
  `numero` varchar(45) DEFAULT NULL,
  `bairro` varchar(45) DEFAULT NULL,
  `cidade` varchar(45) DEFAULT NULL,
  `estado` varchar(45) DEFAULT NULL,
  `credito` varchar(15) DEFAULT NULL,
  `credito_utilizado` varchar(15) DEFAULT NULL,
  `credito_saldo` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`idclientes`)
) ENGINE=InnoDB AUTO_INCREMENT=105 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (67,'Vanessa Costa','111.222.333-56','56789012','(71) 87654-3210','vanessa.costa@email.com','98765-432','Rua T, 456','707','Bairro 7','Salvador','BA','1300.00','62.87','1237.13'),(68,'Anderson Oliveira','444.555.666-98','90123456','(81) 12345-6789','anderson.oliveira@email.com','54321-876','Rua S, 789','808','Bairro 8','Recife','PE','1600.00','1457.1','142.90'),(69,'Mariana Silva','777.888.999-34','12345678','(91) 98765-4321','mariana.silva@email.com','12345-678','Rua R, 123','909','Bairro 9','Belém','PA','1100.00','33.6','1066.40'),(70,'Gabriel Lima','111.222.333-67','23456789','(21) 87654-3210','gabriel.lima@email.com','98765-432','Rua Q, 456','1010','Bairro 10','Niterói','RJ','1400.00','178.82','1221.18'),(71,'Eduardo Oliveira','444.555.666-11','23456789','(31) 98765-4321','eduardo.oliveira@email.com','12345-678','Rua P, 123','111','Bairro 11','Belo Horizonte','MG','1000.00','33.6','966.40'),(72,'Isabela Santos','777.888.999-45','56789012','(41) 87654-3210','isabela.santos@email.com','98765-432','Rua O, 456','1212','Bairro 12','Curitiba','PR','1500.00','35.0','1465.00'),(73,'Henrique Lima','111.222.333-78','89012345','(51) 12345-6789','henrique.lima@email.com','54321-876','Rua N, 789','1313','Bairro 13','Porto Alegre','RS','1200.00','49.0','1151.00'),(76,'Juliana Oliveira','111.222.333-76','23456789','(81) 12345-6789','juliana.oliveira@email.com','54321-876','Rua K, 789','1616','Bairro 16','Recife','PE','1600.00','0','0'),(77,'Rafael Silva','444.555.666-09','56789012','(91) 98765-4321','rafael.silva@email.com','98765-432','Rua J, 123','1717','Bairro 17','Belém','PA','1100.00','33.51','1066.49'),(78,'Carolina Lima','777.888.999-42','89012345','(21) 87654-3210','carolina.lima@email.com','98765-432','Rua I, 456','1818','Bairro 18','Niterói','RJ','1400.00','15.19','1384.81'),(79,'Bruno Santos','111.222.333-75','12345678','(31) 98765-4321','bruno.santos@email.com','12345-678','Rua H, 123','1919','Bairro 19','Belo Horizonte','MG','1000.00','7.55','992.45'),(80,'Tatiane Oliveira','444.555.666-08','23456789','(41) 87654-3210','tatiane.oliveira@email.com','98765-432','Rua G, 456','2020','Bairro 20','Curitiba','PR','1500.00','0','0'),(81,'Lucas Costa','777.888.999-41','56789012','(51) 12345-6789','lucas.costa@email.com','54321-876','Rua F, 789','2121','Bairro 21','Porto Alegre','RS','1200.00','25.96','1174.04'),(82,'Fernanda Silva','111.222.333-74','90123456','(61) 98765-4321','fernanda.silva@email.com','12345-678','Rua E, 123','2222','Bairro 22','Brasília','DF','1800.00','315.0','1485.00'),(83,'Rodrigo Lima','444.555.666-07','12345678','(71) 87654-3210','rodrigo.lima@email.com','98765-432','Rua D, 456','2323','Bairro 23','Salvador','BA','1300.00','0','0'),(84,'Amanda Oliveira','777.888.999-40','23456789','(81) 12345-6789','amanda.oliveira@email.com','54321-876','Rua C, 789','2424','Bairro 24','Recife','PE','1600.00','53.25','1546.75'),(85,'Gabriel Silva','111.222.333-73','56789012','(91) 98765-4321','gabriel.silva@email.com','98765-432','Rua B, 123','2525','Bairro 25','Belém','PA','1100.00','135.46','964.54'),(86,'Laura Santos','444.555.666-06','89012345','(21) 87654-3210','laura.santos@email.com','98765-432','Rua A, 123','2626','Bairro 26','Niterói','RJ','1400.00','0','0'),(87,'Vinícius Oliveira','777.888.999-39','12345678','(31) 98765-4321','vinicius.oliveira@email.com','12345-678','Rua Z, 456','2727','Bairro 27','Belo Horizonte','MG','1000.00','0','0'),(88,'Carla Lima','111.222.333-72','23456789','(41) 87654-3210','carla.lima@email.com','98765-432','Rua Y, 789','2828','Bairro 28','Curitiba','PR','1500.00','0','0'),(89,'Rafaela Costa','444.555.666-05','56789012','(51) 12345-6789','rafaela.costa@email.com','54321-876','Rua X, 123','2929','Bairro 29','Porto Alegre','RS','1200.00','0','0'),(90,'Daniel Silva','777.888.999-38','90123456','(61) 98765-4321','daniel.silva@email.com','12345-678','Rua W, 456','3030','Bairro 30','Brasília','DF','1800.00','0','0'),(91,'Isabela Oliveira','111.222.333-71','12345678','(71) 87654-3210','isabela.oliveira@email.com','98765-432','Rua V, 123','3131','Bairro 31','Salvador','BA','1300.00','0','0'),(93,'Amanda Silva','777.888.999-37','56789012','(91) 98765-4321','amanda.silva@email.com','98765-432','Rua T, 123','3333','Bairro 33','Belém','PA','1100.00','0','0'),(94,'Ricardo Oliveira','111.222.333-70','90123456','(21) 87654-3210','ricardo.oliveira@email.com','98765-432','Rua S, 456','3434','Bairro 34','Niterói','RJ','1400.00','0','0'),(95,'Tatiane Silva','444.555.666-03','12345678','(31) 9876-5432','tatiane.silva@email.com','12345-678','Rua R, 123','3535','Bairro 35','Belo Horizonte','MG','1000.00','0','0'),(96,'Fernando Lima','777.888.999-36','23456789','(41) 87654-3210','fernando.lima@email.com','98765-432','Rua Q, 789','3636','Bairro 36','Curitiba','PR','1500.00','0','0'),(97,'Camila Costa','111.222.333-69','56789012','(51) 12345-6789','camila.costa@email.com','54321-876','Rua P, 123','3737','Bairro 37','Porto Alegre','RS','1200.00','0','0'),(98,'José Oliveira','444.555.666-02','90123456','(61) 98765-4321','jose.oliveira@email.com','12345-678','Rua O, 456','3838','Bairro 38','Brasília','DF','1800.00','0','0'),(99,'Juliana Lima','777.888.999-35','12345678','(71) 87654-3210','juliana.lima@email.com','98765-432','Rua N, 123','3939','Bairro 39','Salvador','BA','1300.00','0','0'),(100,'Mateus Silva','111.222.333-68','23456789','(81) 12345-6789','mateus.silva@email.com','54321-876','Rua M, 789','4040','Bairro 40','Recife','PE','1600.00','0','0'),(103,'LUCAS COSTA DE SOUZA','045.133.311-00','22.556.564-6','(66) 9841-2497','lucatonystz@gmail.com','78650-000','RUA 66, QUADRA 11, LOTE 02','S/N','SETOR MEU LAR','Santa Terezinha','MT','3000','129.8','2870.20');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-21 23:43:16
