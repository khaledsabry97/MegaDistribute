<?php


$server_id = $_POST["server_id"];
$user_name = $_POST["user_name"];
$sql_backup = "DELETE from backup_users where server_id = $server_id and user_name = \"$user_name\"";

if(!mysqli_query($back_up ,$sql_backup))
	//exit("failed to insert backup");

?>



