<?php
require('connection.php');


$user_id = $_POST["user_id"];
$file_name = $_POST["file_name"];

$sql = "SELECT
	node_id 
FROM
	users 
WHERE
	file_name = \"$file_name\" 
	AND user_id = $user_id";

$result = mysqli_query($conn ,$sql);


$arrays = array();
	while ($row = mysqli_fetch_assoc($result)) {
		
		$arrays[] = $row;

	}

	echo json_encode(array("server_response"=>$arrays));


    mysqli_free_result($result);
$conn->close();

?>
