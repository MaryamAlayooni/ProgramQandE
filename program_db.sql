SELECT * FROM program_db.users;
CREATE DATABASE IF NOT EXISTS `program_db` DEFAULT CHARACTER SET utf8 COLLATE utf8mb3_general_ci;
USE `program_db`;

CREATE TABLE IF NOT EXISTS `users` (
	`user_id` varchar(5) NOT NULL AUTO_INCREMENT,
  	`user_name` varchar(20) NOT NULL,
  	`user_pass` varchar(10) NOT NULL,
  	`user_dep` varchar(10) NOT NULL,
    PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO `program_db` (`user_id`, `user_name`, `user_pass`, `user_depusersusers`) VALUES ('A1100', 'Mohammed', 'sa900', 'IT');
INSERT INTO `program_db` (`user_id`, `user_name`, `user_pass`, `user_depusersusers`) VALUES ('U1111', 'saleh', 'qw600', 'finance');
INSERT INTO `program_db` (`user_id`, `user_name`, `user_pass`, `user_depusersusers`) VALUES ('U1122', 'fahad', 'zx700', 'finance');
INSERT INTO `program_db` (`user_id`, `user_name`, `user_pass`, `user_depusersusers`) VALUES ('U1133', 'khalid', 'mn700', 'HR');
INSERT INTO `program_db` (`user_id`, `user_name`, `user_pass`, `user_depusersusers`) VALUES ('A1144', 'Maryam', 'ab100', 'IT');
INSERT INTO `program_db` (`user_id`, `user_name`, `user_pass`, `user_depusersusers`) VALUES ('A1155', 'njoud', 'cd200', 'HR');
INSERT INTO `program_db` (`user_id`, `user_name`, `user_pass`, `user_depusersusers`) VALUES ('A1166', 'rahaf', 'ef300', 'IT');
INSERT INTO `program_db` (`user_id`, `user_name`, `user_pass`, `user_depusersusers`) VALUES ('A1177', 'afnan', 'gh400', 'HR');