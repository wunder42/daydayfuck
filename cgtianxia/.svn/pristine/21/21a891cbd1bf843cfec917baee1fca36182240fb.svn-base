-- MySQL dump 10.13  Distrib 5.5.24, for Win32 (x86)
--
-- Host: localhost    Database: zeizei_mao
-- ------------------------------------------------------
-- Server version	5.5.24

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

-- LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
-- UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_425ae3c4` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`),
  CONSTRAINT `group_id_refs_id_3cea63fe` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_5886d21f` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

-- LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
-- UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_1bb8f392` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_728de91f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

-- LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add site',6,'add_site'),(17,'Can change site',6,'change_site'),(18,'Can delete site',6,'delete_site'),(19,'Can add log entry',7,'add_logentry'),(20,'Can change log entry',7,'change_logentry'),(21,'Can delete log entry',7,'delete_logentry'),(25,'Can add dy news',14,'add_dynews'),(26,'Can change dy news',14,'change_dynews'),(27,'Can delete dy news',14,'delete_dynews'),(28,'Can add dy course',13,'add_dycourse'),(29,'Can change dy course',13,'change_dycourse'),(30,'Can delete dy course',13,'delete_dycourse'),(31,'Can add dy course news',15,'add_dycoursenews'),(32,'Can change dy course news',15,'change_dycoursenews'),(33,'Can delete dy course news',15,'delete_dycoursenews'),(34,'Can add dy class',16,'add_dyclass'),(35,'Can change dy class',16,'change_dyclass'),(36,'Can delete dy class',16,'delete_dyclass'),(37,'Can add dy stu',12,'add_dystu'),(38,'Can change dy stu',12,'change_dystu'),(39,'Can delete dy stu',12,'delete_dystu'),(40,'Can add dy job info',11,'add_dyjobinfo'),(41,'Can change dy job info',11,'change_dyjobinfo'),(42,'Can delete dy job info',11,'delete_dyjobinfo'),(43,'Can add dy ad info',10,'add_dyadinfo'),(44,'Can change dy ad info',10,'change_dyadinfo'),(45,'Can delete dy ad info',10,'delete_dyadinfo'),(46,'Can add dy stu opus info',9,'add_dystuopusinfo'),(47,'Can change dy stu opus info',9,'change_dystuopusinfo'),(48,'Can delete dy stu opus info',9,'delete_dystuopusinfo'),(49,'Can add tiny',17,'add_tiny'),(50,'Can change tiny',17,'change_tiny'),(51,'Can delete tiny',17,'delete_tiny');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
-- UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

-- LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'dianyi','','','oueruse@qq.com','pbkdf2_sha256$10000$NZCe3KhNwZEg$7ZO7kOzprBPJyK53ur9jnyvRC+TYOVwoZOJvyJDt208=',1,1,1,'2013-03-21 15:38:13','2013-03-11 15:07:55');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
-- UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_403f60f` (`user_id`),
  KEY `auth_user_groups_425ae3c4` (`group_id`),
  CONSTRAINT `group_id_refs_id_f116770` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_7ceef80f` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

-- LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
-- UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_403f60f` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`),
  CONSTRAINT `permission_id_refs_id_67e79cb` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_dfbab7d` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

-- LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
-- UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_403f60f` (`user_id`),
  KEY `django_admin_log_1bb8f392` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_288599e6` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c8665aa` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

-- LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2013-03-14 18:01:59',1,9,'2','11',1,''),(2,'2013-03-14 18:03:42',1,9,'2','11',2,'Changed image.'),(3,'2013-03-14 18:05:23',1,9,'3','毛',1,''),(5,'2013-03-16 10:08:55',1,10,'1','图片1',1,''),(6,'2013-03-16 10:34:23',1,10,'2','第二张',1,''),(7,'2013-03-16 10:34:49',1,10,'3','第三张',1,''),(16,'2013-03-19 07:44:26',1,10,'4','7',1,''),(17,'2013-03-20 10:19:29',1,13,'1','3D基础应用班',1,''),(18,'2013-03-20 10:20:04',1,13,'2','室内设计高级班',1,''),(19,'2013-03-20 10:20:33',1,12,'1','毛小宝',1,''),(20,'2013-03-20 10:21:51',1,11,'2','广州点艺',1,''),(21,'2013-03-20 10:24:12',1,9,'2','厨房清晨表现',1,''),(22,'2013-03-20 10:38:52',1,14,'1','春季特别辅导班',1,''),(23,'2013-03-20 10:39:17',1,14,'2','寒假学习特训班',1,''),(24,'2013-03-20 10:39:24',1,14,'3','寒假学习特训班',1,''),(25,'2013-03-20 10:39:31',1,14,'4','寒假学习特训班',1,''),(26,'2013-03-20 10:39:38',1,14,'5','寒假学习特训班',1,''),(27,'2013-03-20 10:39:45',1,14,'6','寒假学习特训班',1,''),(28,'2013-03-20 10:39:53',1,14,'7','寒假学习特训班',1,''),(29,'2013-03-20 10:40:00',1,14,'8','寒假学习特训班',1,''),(30,'2013-03-20 10:44:12',1,14,'9','春季特别辅导班',1,''),(31,'2013-03-20 10:47:54',1,15,'1','3D一秒就会',1,''),(32,'2013-03-20 10:48:14',1,15,'2','3D二秒就会',1,''),(33,'2013-03-20 10:48:27',1,15,'3','3D三秒就会',1,''),(34,'2013-03-20 10:48:39',1,15,'4','3D四秒就会',1,''),(35,'2013-03-20 10:48:51',1,15,'5','3D五秒就会',1,''),(36,'2013-03-20 10:49:03',1,15,'6','3D六秒就会',1,''),(37,'2013-03-20 10:49:17',1,15,'7','3D七秒就会',1,''),(38,'2013-03-20 10:53:25',1,16,'1','平面设计(白天班)',1,''),(39,'2013-03-20 10:53:40',1,16,'2','平面设计(晚班)',1,''),(40,'2013-03-20 10:53:53',1,16,'3','3Dmax设计(白天班)',1,''),(41,'2013-03-20 10:54:03',1,16,'4','室内设计(白天班)',1,''),(42,'2013-03-20 15:12:08',1,9,'1','清晨之光',1,''),(43,'2013-03-21 15:40:13',1,17,'1','Tiny object',1,''),(44,'2013-03-21 15:46:04',1,17,'1','Tiny object',2,'Changed body.'),(45,'2013-03-22 06:10:28',1,10,'1','aa',1,'');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
-- UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

-- LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'content type','contenttypes','contenttype'),(5,'session','sessions','session'),(6,'site','sites','site'),(7,'log entry','admin','logentry'),(9,'dy stu opus info','dyhome','dystuopusinfo'),(10,'dy ad info','dyhome','dyadinfo'),(11,'dy job info','dyhome','dyjobinfo'),(12,'dy stu','dyhome','dystu'),(13,'dy course','dyhome','dycourse'),(14,'dy news','dyhome','dynews'),(15,'dy course news','dyhome','dycoursenews'),(16,'dy class','dyhome','dyclass'),(17,'tiny','dyhome','tiny');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
-- UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_3da3d3d8` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

-- LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('98e9f2d214330334c0ddff385c46d119','OTQ4ODQxOWIwN2UzZjQzNjE0Y2M4MjI5NmRmMWU2MzFiODE0MjRmNjqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2013-03-25 15:08:33'),('9bd033f901788db9c4ade5d4040427d9','OTQ4ODQxOWIwN2UzZjQzNjE0Y2M4MjI5NmRmMWU2MzFiODE0MjRmNjqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2013-04-04 15:38:13'),('bd57ea83623c592f05afa2b6d5398142','OTQ4ODQxOWIwN2UzZjQzNjE0Y2M4MjI5NmRmMWU2MzFiODE0MjRmNjqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2013-04-04 03:08:40');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
-- UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

-- LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
-- UNLOCK TABLES;

--
-- Table structure for table `dyhome_dyadinfo`
--

DROP TABLE IF EXISTS `dyhome_dyadinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dyhome_dyadinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `publication_date` date NOT NULL,
  `image` varchar(150) NOT NULL,
  `content` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dyhome_dyadinfo`
--

-- LOCK TABLES `dyhome_dyadinfo` WRITE;
/*!40000 ALTER TABLE `dyhome_dyadinfo` DISABLE KEYS */;
INSERT INTO `dyhome_dyadinfo` VALUES (1,'aa','2013-03-22','scroller_large_1.jpg','');
/*!40000 ALTER TABLE `dyhome_dyadinfo` ENABLE KEYS */;
-- UNLOCK TABLES;

--
-- Table structure for table `dyhome_dyclass`
--

DROP TABLE IF EXISTS `dyhome_dyclass`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dyhome_dyclass` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `publication_date` date NOT NULL,
  `content` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dyhome_dyclass`
--

-- LOCK TABLES `dyhome_dyclass` WRITE;
/*!40000 ALTER TABLE `dyhome_dyclass` DISABLE KEYS */;
/*!40000 ALTER TABLE `dyhome_dyclass` ENABLE KEYS */;
-- UNLOCK TABLES;

--
-- Table structure for table `dyhome_dycourse`
--

DROP TABLE IF EXISTS `dyhome_dycourse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dyhome_dycourse` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `title` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dyhome_dycourse`
--

-- LOCK TABLES `dyhome_dycourse` WRITE;
/*!40000 ALTER TABLE `dyhome_dycourse` DISABLE KEYS */;
/*!40000 ALTER TABLE `dyhome_dycourse` ENABLE KEYS */;
-- UNLOCK TABLES;

--
-- Table structure for table `dyhome_dycoursenews`
--

DROP TABLE IF EXISTS `dyhome_dycoursenews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dyhome_dycoursenews` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `course_category` varchar(100) NOT NULL,
  `publication_date` datetime DEFAULT NULL,
  `content` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dyhome_dycoursenews`
--

-- LOCK TABLES `dyhome_dycoursenews` WRITE;
/*!40000 ALTER TABLE `dyhome_dycoursenews` DISABLE KEYS */;
/*!40000 ALTER TABLE `dyhome_dycoursenews` ENABLE KEYS */;
-- UNLOCK TABLES;

--
-- Table structure for table `dyhome_dyjobinfo`
--

DROP TABLE IF EXISTS `dyhome_dyjobinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dyhome_dyjobinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name_id` int(11) NOT NULL,
  `company` varchar(30) NOT NULL,
  `publication_date` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dyhome_dyjobinfo_632e075f` (`name_id`),
  CONSTRAINT `name_id_refs_id_246eac18` FOREIGN KEY (`name_id`) REFERENCES `dyhome_dystu` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dyhome_dyjobinfo`
--

-- LOCK TABLES `dyhome_dyjobinfo` WRITE;
/*!40000 ALTER TABLE `dyhome_dyjobinfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `dyhome_dyjobinfo` ENABLE KEYS */;
-- UNLOCK TABLES;

--
-- Table structure for table `dyhome_dynews`
--

DROP TABLE IF EXISTS `dyhome_dynews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dyhome_dynews` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `author` varchar(30) NOT NULL,
  `publication_date` datetime DEFAULT NULL,
  `content` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dyhome_dynews`
--

-- LOCK TABLES `dyhome_dynews` WRITE;
/*!40000 ALTER TABLE `dyhome_dynews` DISABLE KEYS */;
/*!40000 ALTER TABLE `dyhome_dynews` ENABLE KEYS */;
-- UNLOCK TABLES;

--
-- Table structure for table `dyhome_dystu`
--

DROP TABLE IF EXISTS `dyhome_dystu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dyhome_dystu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `college` varchar(50) NOT NULL,
  `phase` int(11) NOT NULL,
  `title_id` int(11) NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `qq_num` varchar(50) NOT NULL,
  `publication_date` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dyhome_dystu_8a3b4cf` (`title_id`),
  CONSTRAINT `title_id_refs_id_35dccdb7` FOREIGN KEY (`title_id`) REFERENCES `dyhome_dycourse` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dyhome_dystu`
--

-- LOCK TABLES `dyhome_dystu` WRITE;
/*!40000 ALTER TABLE `dyhome_dystu` DISABLE KEYS */;
/*!40000 ALTER TABLE `dyhome_dystu` ENABLE KEYS */;
-- UNLOCK TABLES;

--
-- Table structure for table `dyhome_dystuopusinfo`
--

DROP TABLE IF EXISTS `dyhome_dystuopusinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dyhome_dystuopusinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name_id` int(11) NOT NULL,
  `course_category_id` int(11) NOT NULL,
  `title` varchar(30) NOT NULL,
  `content` varchar(100) DEFAULT NULL,
  `publication_date` date NOT NULL,
  `image` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dyhome_dystuopusinfo_632e075f` (`name_id`),
  KEY `dyhome_dystuopusinfo_7b670c93` (`course_category_id`),
  CONSTRAINT `name_id_refs_id_6e5d9812` FOREIGN KEY (`name_id`) REFERENCES `dyhome_dystu` (`id`),
  CONSTRAINT `course_category_id_refs_id_2807ee84` FOREIGN KEY (`course_category_id`) REFERENCES `dyhome_dycourse` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dyhome_dystuopusinfo`
--

-- LOCK TABLES `dyhome_dystuopusinfo` WRITE;
/*!40000 ALTER TABLE `dyhome_dystuopusinfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `dyhome_dystuopusinfo` ENABLE KEYS */;
-- UNLOCK TABLES;

--
-- Table structure for table `dyhome_tiny`
--

DROP TABLE IF EXISTS `dyhome_tiny`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dyhome_tiny` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `body` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dyhome_tiny`
--

-- LOCK TABLES `dyhome_tiny` WRITE;
/*!40000 ALTER TABLE `dyhome_tiny` DISABLE KEYS */;
/*!40000 ALTER TABLE `dyhome_tiny` ENABLE KEYS */;
-- UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-03-22 14:11:02
