<?php
require('connection.php');



$user_id = $_POST["user_id"];


$sql = "SELECT * FROM `users` where user_id = $user_id
GROUP BY file_name order by date_created";

$result = mysqli_query($conn ,$sql);


$arrays = array();
	while ($row = mysqli_fetch_assoc($result)) {
		
		$arrays[] = $row;

	}

	echo json_encode(array("server_response"=>$arrays));


    mysqli_free_result($result);
$conn->close();

?>
