<?php

require('connection.php');



$user_id = $_POST["user_id"];
$node_id = $_POST["node_id"];
$file_name = $_POST["file_name"];
$file_size = $_POST["file_size"];
$current_available = $_POST["current_available"];



$sql = "INSERT INTO users(user_id,node_id,file_name,file_size,date_created,current_available) VALUES($user_id,$node_id,\"$file_name\", $file_size,CURRENT_TIMESTAMP,$current_available)";

if(mysqli_query($conn ,$sql))
	echo json_encode(array("server_response"=>True));
else
	echo json_encode(array("server_response"=>False));
	
	
	


?>
