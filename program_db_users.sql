SELECT * FROM program_db.users;
CREATE DATABASE IF NOT EXISTS `QandE` DEFAULT CHARACTER SET utf8 COLLATE utf8mb3_general_ci;
USE `QandE`;

CREATE TABLE IF NOT EXISTS `users` (
	`user_id` int(4) NOT NULL AUTO_INCREMENT,
  	`user_name` varchar(20) NOT NULL,
  	`user_pass` varchar(10) NOT NULL,
  	`user_dep` varchar(10) NOT NULL,
    `IsAdmin` varchar(1) NOT NULL,
    PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO `QandE` (`user_id`, `user_name`, `user_pass`, `user_depusersusers`) VALUES (1100, 'Mohammed', 'sa900', 'IT','1');
INSERT INTO `QandE` (`user_id`, `user_name`, `user_pass`, `user_depusersusers`) VALUES (1111, 'saleh', 'qw600', 'finance','0');
INSERT INTO `QandE` (`user_id`, `user_name`, `user_pass`, `user_depusersusers`) VALUES (1122, 'fahad', 'zx700', 'finance','0');
INSERT INTO `QandE` (`user_id`, `user_name`, `user_pass`, `user_depusersusers`) VALUES (1133, 'khalid', 'mn700', 'HR','0');
INSERT INTO `QandE` (`user_id`, `user_name`, `user_pass`, `user_depusersusers`) VALUES (1144, 'Maryam', 'ab100', 'IT','1');
INSERT INTO `QandE` (`user_id`, `user_name`, `user_pass`, `user_depusersusers`) VALUES (1155, 'njoud', 'cd200', 'HR','0');
INSERT INTO `QandE` (`user_id`, `user_name`, `user_pass`, `user_depusersusers`) VALUES (1166, 'rahaf', 'ef300', 'IT','0');
INSERT INTO `QandE` (`user_id`, `user_name`, `user_pass`, `user_depusersusers`) VALUES (1177, 'afnan', 'gh400', 'HR','0');
