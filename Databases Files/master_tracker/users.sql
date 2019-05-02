/*
 Navicat Premium Data Transfer

 Source Server         : DS
 Source Server Type    : MySQL
 Source Server Version : 100131
 Source Host           : localhost:3306
 Source Schema         : mt

 Target Server Type    : MySQL
 Target Server Version : 100131
 File Encoding         : 65001

 Date: 02/05/2019 11:01:44
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `user_id` int(11) NOT NULL,
  `node_id` int(11) NOT NULL,
  `file_name` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `file_size` bigint(20) NOT NULL,
  `date_created` timestamp(0) NOT NULL ON UPDATE CURRENT_TIMESTAMP(0),
  `current_available` bit(1) NOT NULL,
  UNIQUE INDEX `uniquness`(`user_id`, `node_id`, `file_name`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;
