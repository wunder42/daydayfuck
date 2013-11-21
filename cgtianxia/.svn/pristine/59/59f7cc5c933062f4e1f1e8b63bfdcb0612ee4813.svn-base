BEGIN;
CREATE TABLE `dyhome_dyinfo` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `tid` integer NOT NULL,
    `title` varchar(100) NOT NULL,
    `content` varchar(2000) NOT NULL,
    `author` varchar(30) NOT NULL,
    `publication_date` date NOT NULL,
    `category` varchar(30) NOT NULL,
    `course_category` varchar(30) NOT NULL
)
DEFAULT CHARSET=utf8;;
CREATE TABLE `dyhome_dyjobinfo` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `tid` integer NOT NULL,
    `name` varchar(30) NOT NULL,
    `course_category` varchar(30) NOT NULL,
    `company` varchar(30) NOT NULL,
    `publication_date` date NOT NULL
)
DEFAULT CHARSET=utf8;;
CREATE TABLE `dyhome_dyadinfo` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `tid` integer NOT NULL,
    `pic_url` varchar(50) NOT NULL,
    `title` varchar(30) NOT NULL,
    `content` varchar(30) NOT NULL,
    `publication_date` date NOT NULL
)
DEFAULT CHARSET=utf8;;
CREATE TABLE `dyhome_dystuopusinfo` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `tid` integer NOT NULL,
    `author` varchar(30) NOT NULL,
    `title` varchar(30) NOT NULL,
    `content` varchar(100) NOT NULL,
    `course_category` varchar(30) NOT NULL,
    `pic_url` varchar(50) NOT NULL,
    `publication_date` date NOT NULL
)
DEFAULT CHARSET=utf8;;
COMMIT;
