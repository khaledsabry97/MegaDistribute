<?php
$conn = mysqli_connect("localhost","root","","ds_back_up","3306");
if(!$conn)
	echo json_encode(array("server_response"=>"server down"));


?>
