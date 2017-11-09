/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50716
Source Host           : localhost:3307
Source Database       : pystudy

Target Server Type    : MYSQL
Target Server Version : 50716
File Encoding         : 65001

Date: 2017-11-09 17:00:03
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for funddetail
-- ----------------------------
DROP TABLE IF EXISTS `funddetail`;
CREATE TABLE `funddetail` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `fcode` varchar(10) NOT NULL COMMENT '基金编码',
  `fdate` datetime DEFAULT NULL COMMENT '基金日期',
  `NAV` decimal(10,4) DEFAULT NULL COMMENT '单位净值',
  `ACCNAV` decimal(10,4) DEFAULT NULL COMMENT '累计净值',
  `DGR` varchar(20) DEFAULT NULL COMMENT '日增长率',
  `pstate` varchar(20) DEFAULT NULL COMMENT '申购状态(Purchasing Funds )',
  `rstate` varchar(20) DEFAULT NULL COMMENT '赎回状态(Redeming State)',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
