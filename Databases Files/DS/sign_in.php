<?php
require('connection.php');



$user_name = $_POST["user_name"];
$password = $_POST["password"];

$sql = "SELECT id FROM `users` where user_name = \"$user_name\" and `password` = \"$password\"";

$result = mysqli_query($conn ,$sql);


$arrays = array();
	while ($row = mysqli_fetch_assoc($result)) {
		
		$arrays[] = $row;

	}

	
	if(count($arrays) != 0)
	echo json_encode(array("server_response"=>$arrays));
else
	echo json_encode(array("server_response"=>false));

    mysqli_free_result($result);
$conn->close();

?>
