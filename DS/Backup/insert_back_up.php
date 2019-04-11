<?php


$sql_backup = "INSERT INTO backup_users(server_id,user_name,email,password) VALUES($server_id,\"$user_name\", \"$email\",\"$password\")";

if(!mysqli_query($back_up ,$sql_backup))
	//exit("failed to insert backup");

?>