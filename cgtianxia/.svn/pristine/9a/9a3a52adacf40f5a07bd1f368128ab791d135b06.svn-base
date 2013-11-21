BEGIN;
CREATE TABLE `dyhome_dynews_tag` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `dynews_id` integer NOT NULL,
    `tag_id` integer NOT NULL,
    UNIQUE (`dynews_id`, `tag_id`)
)
;
CREATE TABLE `dyhome_dynews` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `title` varchar(100) NOT NULL,
    `author_id` integer NOT NULL,
    `publication_date` datetime NOT NULL,
    `hot_dot` integer NOT NULL,
    `top` bool NOT NULL,
    `content` longtext NOT NULL
)
;
ALTER TABLE `dyhome_dynews` ADD CONSTRAINT `author_id_refs_id_174ea54a` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `dyhome_dynews_tag` ADD CONSTRAINT `dynews_id_refs_id_471abc1e` FOREIGN KEY (`dynews_id`) REFERENCES `dyhome_dynews` (`id`);
CREATE TABLE `dyhome_dycourse` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(100) NOT NULL UNIQUE
)
;
CREATE TABLE `dyhome_dycourseclass` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `title` varchar(100) NOT NULL UNIQUE,
    `name_id` integer NOT NULL,
    `content` longtext
)
;
ALTER TABLE `dyhome_dycourseclass` ADD CONSTRAINT `name_id_refs_id_5a15c4e` FOREIGN KEY (`name_id`) REFERENCES `dyhome_dycourse` (`id`);
CREATE TABLE `dyhome_dycoursenews_tag` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `dycoursenews_id` integer NOT NULL,
    `tag_id` integer NOT NULL,
    UNIQUE (`dycoursenews_id`, `tag_id`)
)
;
CREATE TABLE `dyhome_dycoursenews` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `title` varchar(100) NOT NULL,
    `author_id` integer NOT NULL,
    `course_category_id` integer NOT NULL,
    `publication_date` datetime NOT NULL,
    `hot_dot` integer NOT NULL,
    `top` bool NOT NULL,
    `image` varchar(150),
    `content` longtext NOT NULL
)
;
ALTER TABLE `dyhome_dycoursenews` ADD CONSTRAINT `author_id_refs_id_271f3b49` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `dyhome_dycoursenews` ADD CONSTRAINT `course_category_id_refs_id_162f8e52` FOREIGN KEY (`course_category_id`) REFERENCES `dyhome_dycourse` (`id`);
ALTER TABLE `dyhome_dycoursenews_tag` ADD CONSTRAINT `dycoursenews_id_refs_id_20a67db0` FOREIGN KEY (`dycoursenews_id`) REFERENCES `dyhome_dycoursenews` (`id`);
CREATE TABLE `dyhome_dyclass` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `title` varchar(100) NOT NULL,
    `class_date` date NOT NULL,
    `publication_date` date NOT NULL,
    `content` longtext NOT NULL
)
;
CREATE TABLE `dyhome_dystu_course_class` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `dystu_id` integer NOT NULL,
    `dycourseclass_id` integer NOT NULL,
    UNIQUE (`dystu_id`, `dycourseclass_id`)
)
;
ALTER TABLE `dyhome_dystu_course_class` ADD CONSTRAINT `dycourseclass_id_refs_id_1f01a9e6` FOREIGN KEY (`dycourseclass_id`) REFERENCES `dyhome_dycourseclass` (`id`);
CREATE TABLE `dyhome_dystu` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(30) NOT NULL,
    `sex` varchar(1) NOT NULL,
    `college_id` integer NOT NULL,
    `phase` integer NOT NULL,
    `phone_num` varchar(50) NOT NULL,
    `qq_num` varchar(50) NOT NULL,
    `publication_date` date NOT NULL
)
;
ALTER TABLE `dyhome_dystu_course_class` ADD CONSTRAINT `dystu_id_refs_id_95d240d` FOREIGN KEY (`dystu_id`) REFERENCES `dyhome_dystu` (`id`);
CREATE TABLE `dyhome_dyjobinfo` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `company` varchar(30) NOT NULL,
    `publication_date` date NOT NULL,
    `name_id` integer NOT NULL
)
;
ALTER TABLE `dyhome_dyjobinfo` ADD CONSTRAINT `name_id_refs_id_246eac18` FOREIGN KEY (`name_id`) REFERENCES `dyhome_dystu` (`id`);
CREATE TABLE `dyhome_dyadinfo` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `title` varchar(100) NOT NULL,
    `sub_title` varchar(100) NOT NULL,
    `publication_date` date NOT NULL,
    `image` varchar(150) NOT NULL,
    `content` longtext NOT NULL
)
;
CREATE TABLE `dyhome_dystuopusinfo_tag` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `dystuopusinfo_id` integer NOT NULL,
    `tag_id` integer NOT NULL,
    UNIQUE (`dystuopusinfo_id`, `tag_id`)
)
;
CREATE TABLE `dyhome_dystuopusinfo` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `author_id` integer NOT NULL,
    `course_category_id` integer NOT NULL,
    `title` varchar(30) NOT NULL,
    `sub_title` varchar(100) NOT NULL,
    `content` varchar(100),
    `publication_date` datetime NOT NULL,
    `hot_dot` integer NOT NULL,
    `top` bool NOT NULL,
    `image` varchar(150) NOT NULL
)
;
ALTER TABLE `dyhome_dystuopusinfo` ADD CONSTRAINT `author_id_refs_id_6e5d9812` FOREIGN KEY (`author_id`) REFERENCES `dyhome_dystu` (`id`);
ALTER TABLE `dyhome_dystuopusinfo` ADD CONSTRAINT `course_category_id_refs_id_7f4e8a2b` FOREIGN KEY (`course_category_id`) REFERENCES `dyhome_dycourseclass` (`id`);
ALTER TABLE `dyhome_dystuopusinfo_tag` ADD CONSTRAINT `dystuopusinfo_id_refs_id_66043080` FOREIGN KEY (`dystuopusinfo_id`) REFERENCES `dyhome_dystuopusinfo` (`id`);
CREATE TABLE `dyhome_tag` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(100) NOT NULL UNIQUE
)
;
ALTER TABLE `dyhome_dynews_tag` ADD CONSTRAINT `tag_id_refs_id_1a6d54d7` FOREIGN KEY (`tag_id`) REFERENCES `dyhome_tag` (`id`);
ALTER TABLE `dyhome_dycoursenews_tag` ADD CONSTRAINT `tag_id_refs_id_7f7a3198` FOREIGN KEY (`tag_id`) REFERENCES `dyhome_tag` (`id`);
ALTER TABLE `dyhome_dystuopusinfo_tag` ADD CONSTRAINT `tag_id_refs_id_104dd532` FOREIGN KEY (`tag_id`) REFERENCES `dyhome_tag` (`id`);
CREATE TABLE `dyhome_college` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(100) NOT NULL UNIQUE
)
;
ALTER TABLE `dyhome_dystu` ADD CONSTRAINT `college_id_refs_id_10b7f465` FOREIGN KEY (`college_id`) REFERENCES `dyhome_college` (`id`);
CREATE TABLE `dyhome_tiny` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `body` longtext NOT NULL
)
;
CREATE TABLE `dyhome_liuyan` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `course_id_id` integer NOT NULL,
    `liuyan_id` integer,
    `author` varchar(30) NOT NULL,
    `mail` varchar(75) NOT NULL,
    `content` longtext NOT NULL,
    `display` bool NOT NULL,
    `publication_date` datetime NOT NULL
)
;
ALTER TABLE `dyhome_liuyan` ADD CONSTRAINT `course_id_id_refs_id_6a3cea7a` FOREIGN KEY (`course_id_id`) REFERENCES `dyhome_dycoursenews` (`id`);
CREATE INDEX `dyhome_dynews_337b96ff` ON `dyhome_dynews` (`author_id`);
CREATE INDEX `dyhome_dycourseclass_632e075f` ON `dyhome_dycourseclass` (`name_id`);
CREATE INDEX `dyhome_dycoursenews_337b96ff` ON `dyhome_dycoursenews` (`author_id`);
CREATE INDEX `dyhome_dycoursenews_7b670c93` ON `dyhome_dycoursenews` (`course_category_id`);
CREATE INDEX `dyhome_dystu_6d2e0b0` ON `dyhome_dystu` (`college_id`);
CREATE INDEX `dyhome_dyjobinfo_632e075f` ON `dyhome_dyjobinfo` (`name_id`);
CREATE INDEX `dyhome_dystuopusinfo_337b96ff` ON `dyhome_dystuopusinfo` (`author_id`);
CREATE INDEX `dyhome_dystuopusinfo_7b670c93` ON `dyhome_dystuopusinfo` (`course_category_id`);
CREATE INDEX `dyhome_liuyan_4067af00` ON `dyhome_liuyan` (`course_id_id`);
COMMIT;
