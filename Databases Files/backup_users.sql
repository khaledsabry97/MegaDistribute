/*
 Navicat Premium Data Transfer

 Source Server         : DS
 Source Server Type    : MySQL
 Source Server Version : 100131
 Source Host           : localhost:3306
 Source Schema         : ds_back_up

 Target Server Type    : MySQL
 Target Server Version : 100131
 File Encoding         : 65001

 Date: 02/05/2019 11:26:16
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for backup_users
-- ----------------------------
DROP TABLE IF EXISTS `backup_users`;
CREATE TABLE `backup_users`  (
  `server_id` int(11) NOT NULL,
  `user_name` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `email` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `password` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  UNIQUE INDEX `id and username`(`server_id`, `user_name`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;
