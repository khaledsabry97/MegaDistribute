<?php

require('connection.php');

$node_id = $_POST["node_id"];
$sql = "DELETE
FROM
	users 
WHERE
	node_id = $node_id;";

if(mysqli_query($conn ,$sql))
	echo json_encode(array("server_response"=>True));
else
	echo json_encode(array("server_response"=>False));
	
	
	


?>
