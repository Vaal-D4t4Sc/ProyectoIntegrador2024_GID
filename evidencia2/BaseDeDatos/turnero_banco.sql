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
-- Table structure for table `accesos`
--

DROP TABLE IF EXISTS `accesos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accesos` (
  `ID_accesos` int(11) NOT NULL AUTO_INCREMENT,
  `Fecha_Ingreso` datetime NOT NULL,
  `Fecha_Salida` datetime NOT NULL,
  `UsuarioLogueado` int(11) NOT NULL,
  PRIMARY KEY (`ID_accesos`),
  KEY `UsuarioLogueado_idx` (`UsuarioLogueado`),
  CONSTRAINT `UsuarioLogueado` FOREIGN KEY (`UsuarioLogueado`) REFERENCES `usuarios` (`ID_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `DNI_CUIT` int(15) NOT NULL,
  `Nombre` varchar(30) NOT NULL,
  `Apellido` varchar(30) NOT NULL,
  `Telefono` varchar(20) NOT NULL,
  `Direccion` varchar(45) NOT NULL,
  `Fecha_Alta` datetime NOT NULL,
  PRIMARY KEY (`DNI_CUIT`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `empleados`
--

DROP TABLE IF EXISTS `empleados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empleados` (
  `DNI` int(11) NOT NULL,
  `Nombre` varchar(15) NOT NULL,
  `Apellido` varchar(15) NOT NULL,
  `Dirección` varchar(45) NOT NULL,
  `Telefono` varchar(15) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Fecha_contrato` date NOT NULL,
  `IDserv_emp` int(11) NOT NULL,
  `IDsucursal_emp` int(11) NOT NULL,
  PRIMARY KEY (`DNI`),
  KEY `IDserv_idx` (`IDserv_emp`),
  KEY `IDsucursal_idx` (`IDsucursal_emp`),
  CONSTRAINT `IDserv_emp` FOREIGN KEY (`IDserv_emp`) REFERENCES `servicios` (`IDserv`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `IDsucursal_emp` FOREIGN KEY (`IDsucursal_emp`) REFERENCES `sucursales` (`IDsucursal`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `servicios`
--

DROP TABLE IF EXISTS `servicios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `servicios` (
  `IDserv` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) NOT NULL,
  PRIMARY KEY (`IDserv`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sucursales`
--

DROP TABLE IF EXISTS `sucursales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sucursales` (
  `IDsucursal` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) NOT NULL,
  `Dirección` varchar(45) NOT NULL,
  `Provincia` varchar(15) NOT NULL,
  `Ciudad` varchar(15) NOT NULL,
  `Localidad` varchar(15) NOT NULL,
  PRIMARY KEY (`IDsucursal`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `turnos`
--

DROP TABLE IF EXISTS `turnos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `turnos` (
  `IDturno` int(11) NOT NULL AUTO_INCREMENT,
  `Fecha_Turno` date NOT NULL,
  `Hora_Turno` time NOT NULL,
  `Estado` enum('Pendiente','Confirmado','Cancelado)') NOT NULL,
  `Recordatorio` tinyint(1) NOT NULL,
  `ID_cliente` int(11) NOT NULL,
  `IDsucursal` int(11) NOT NULL,
  `IDserv` int(11) NOT NULL,
  PRIMARY KEY (`IDturno`),
  KEY `ID_cliente_idx` (`ID_cliente`),
  KEY `IDsucursal_idx` (`IDsucursal`),
  KEY `IDserv_idx` (`IDserv`),
  CONSTRAINT `ID_cliente` FOREIGN KEY (`ID_cliente`) REFERENCES `clientes` (`DNI_CUIT`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `IDserv` FOREIGN KEY (`IDserv`) REFERENCES `servicios` (`IDserv`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `IDsucursal` FOREIGN KEY (`IDsucursal`) REFERENCES `sucursales` (`IDsucursal`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `ID_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `Username` varchar(15) NOT NULL,
  `Password` varchar(20) NOT NULL,
  `Email` varchar(20) NOT NULL,
  `DNI_CUIT` int(11) NOT NULL,
  PRIMARY KEY (`ID_usuario`),
  KEY `DNI_CUIT_idx` (`DNI_CUIT`),
  CONSTRAINT `DNI_CUIT` FOREIGN KEY (`DNI_CUIT`) REFERENCES `clientes` (`DNI_CUIT`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-06 12:51:00
