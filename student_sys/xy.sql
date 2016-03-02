/*
Navicat MySQL Data Transfer

Source Server         : root
Source Server Version : 50709
Source Host           : localhost:3306
Source Database       : yx

Target Server Type    : MYSQL
Target Server Version : 50709
File Encoding         : 65001

Date: 2016-03-02 11:29:59
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for score
-- ----------------------------
DROP TABLE IF EXISTS `score`;
CREATE TABLE `score` (
  `id` int(50) DEFAULT NULL,
  `math` int(50) DEFAULT NULL,
  `english` int(50) DEFAULT NULL,
  `phyics` int(50) DEFAULT NULL,
  `chinese` int(50) DEFAULT NULL,
  `history` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of score
-- ----------------------------
INSERT INTO `score` VALUES ('1', '89', '89', '98', '56', '99');
INSERT INTO `score` VALUES ('2', '54', '23', '54', '32', '87');
INSERT INTO `score` VALUES ('3', '43', '56', '34', '54', '12');
INSERT INTO `score` VALUES ('4', '40', '90', '78', '98', '86');
INSERT INTO `score` VALUES ('5', '45', '54', '78', '78', '43');
INSERT INTO `score` VALUES ('6', '45', '43', '76', '90', '69');

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `id` int(50) NOT NULL,
  `name` varchar(255) NOT NULL,
  `passwd` varchar(255) NOT NULL,
  `sex` int(10) NOT NULL,
  `address` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES ('1', 'yx', '321', '1', 'c');
INSERT INTO `student` VALUES ('2', 'er', '215', '1', 're');
INSERT INTO `student` VALUES ('3', 'rt', '253', '1', 'rrt');
INSERT INTO `student` VALUES ('4', 'rty', '568', '0', 'cssf');
INSERT INTO `student` VALUES ('5', 'th', '585', '0', 'hyj');
INSERT INTO `student` VALUES ('6', '56', '65', '56', 'fgg');

-- ----------------------------
-- Procedure structure for delete_
-- ----------------------------
DROP PROCEDURE IF EXISTS `delete_`;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_`(IN id_ INT)
delete from student where id=id_
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for login
-- ----------------------------
DROP PROCEDURE IF EXISTS `login`;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `login`(IN id_ int,IN passwd_ VARCHAR(255))
select id FROM student where id=id_ and passwd=passwd_
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for score
-- ----------------------------
DROP PROCEDURE IF EXISTS `score`;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `score`(IN id_ INT)
SELECT score.id,student.name,math,english,phyics,chinese,history from score,student where score.id=student.id and score.id=id_
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for search
-- ----------------------------
DROP PROCEDURE IF EXISTS `search`;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `search`()
SELECT id,name from student
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for signin1
-- ----------------------------
DROP PROCEDURE IF EXISTS `signin1`;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `signin1`(IN id_ INT)
SELECT id FROM student where id=id_
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for signin2
-- ----------------------------
DROP PROCEDURE IF EXISTS `signin2`;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `signin2`(IN id_ INT,IN name_ VARCHAR(255),IN passwd VARCHAR(255))
insert into student(id,name,passwd) values(id_,name_,passwd)
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for student
-- ----------------------------
DROP PROCEDURE IF EXISTS `student`;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `student`(IN id_ INT)
SELECT * FROM student WHERE id=id_
;;
DELIMITER ;
