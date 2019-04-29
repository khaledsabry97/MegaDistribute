<?php

require('connection.php');



$user_id = $_POST["user_id"];
$node_id = $_POST["node_id"];
$file_name = $_POST["file_name"];
$file_size = $_POST["file_size"];


$sql = "UPDATE users 
SET current_available = 1,
file_size = $file_size
WHERE
	user_id = $user_id 
	AND file_name = \"$file_name\" 
	AND node_id = $node_id";
	

if(mysqli_query($conn ,$sql))
	echo json_encode(array("server_response"=>True));
else
	echo json_encode(array("server_response"=>False));
	
	
	

$conn->close();

?>
