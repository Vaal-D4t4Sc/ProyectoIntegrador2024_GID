-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: turnero_banco
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.24-MariaDB

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
-- Dumping data for table `accesos`
--

LOCK TABLES `accesos` WRITE;
/*!40000 ALTER TABLE `accesos` DISABLE KEYS */;
INSERT INTO `accesos` VALUES (1,'2024-10-01 08:00:00','2024-10-01 16:00:00',1),(2,'2024-10-02 09:00:00','2024-10-02 17:00:00',2),(3,'2024-10-03 10:00:00','2024-10-03 18:00:00',3),(4,'2024-10-04 11:00:00','2024-10-04 19:00:00',4),(5,'2024-10-05 12:00:00','2024-10-05 20:00:00',5);
/*!40000 ALTER TABLE `accesos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (12345671,'Juan','Pérez','123456789','Calle 1','2024-09-01 09:00:00'),(12345672,'Ana','Gómez','987654321','Calle 2','2024-09-02 10:00:00'),(12345673,'Luis','Martínez','123098456','Calle 3','2024-09-03 11:00:00'),(12345674,'María','Fernández','456789123','Calle 4','2024-09-04 12:00:00'),(12345675,'Carlos','Rodríguez','321654987','Calle 5','2024-09-05 13:00:00');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `empleados`
--

LOCK TABLES `empleados` WRITE;
/*!40000 ALTER TABLE `empleados` DISABLE KEYS */;
INSERT INTO `empleados` VALUES (11111111,'Pedro','García','Calle Uno','123456789','pedro@empresa.com','2024-01-01',1,1),(22222222,'Laura','Sánchez','Calle Dos','987654321','laura@empresa.com','2024-02-01',2,2),(33333333,'Marta','López','Calle Tres','123098456','marta@empresa.com','2024-03-01',3,3),(44444444,'Sofía','Gómez','Calle Cuatro','456789123','sofia@empresa.com','2024-04-01',4,4),(55555555,'Diego','Martínez','Calle Cinco','321654987','diego@empresa.com','2024-05-01',5,5);
/*!40000 ALTER TABLE `empleados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `servicios`
--

LOCK TABLES `servicios` WRITE;
/*!40000 ALTER TABLE `servicios` DISABLE KEYS */;
INSERT INTO `servicios` VALUES (1,'Atención al cliente'),(2,'Asesoría de créditos'),(3,'Cajero automático'),(4,'Apertura de cuentas'),(5,'Préstamos hipotecarios');
/*!40000 ALTER TABLE `servicios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `sucursales`
--

LOCK TABLES `sucursales` WRITE;
/*!40000 ALTER TABLE `sucursales` DISABLE KEYS */;
INSERT INTO `sucursales` VALUES (1,'Sucursal Centro','Av. Siempre Viva 123','Buenos Aires','Buenos Aires','Centro'),(2,'Sucursal Norte','Calle Principal 45','Córdoba','Córdoba','Norte'),(3,'Sucursal Sur','Avenida del Sol 234','Mendoza','Mendoza','Sur'),(4,'Sucursal Este','Ruta 9 Km 45','Salta','Salta','Este'),(5,'Sucursal Oeste','Avenida del Oeste 543','San Juan','San Juan','Oeste');
/*!40000 ALTER TABLE `sucursales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `turnos`
--

LOCK TABLES `turnos` WRITE;
/*!40000 ALTER TABLE `turnos` DISABLE KEYS */;
INSERT INTO `turnos` VALUES (1,'2024-10-10','09:00:00','Pendiente',1,12345671,1,1),(2,'2024-10-11','10:00:00','Confirmado',1,12345672,2,2),(3,'2024-10-12','11:00:00','Cancelado',0,12345673,3,3),(4,'2024-10-13','12:00:00','Pendiente',1,12345674,4,4),(5,'2024-10-14','13:00:00','Confirmado',1,12345675,5,5);
/*!40000 ALTER TABLE `turnos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'usuario1','password1','usuario1@mail.com',12345671),(2,'usuario2','password2','usuario2@mail.com',12345672),(3,'usuario3','password3','usuario3@mail.com',12345673),(4,'usuario4','password4','usuario4@mail.com',12345674),(5,'usuario5','password5','usuario5@mail.com',12345675);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-21 22:04:36
