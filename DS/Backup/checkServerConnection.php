<?php
require('../database_servers.php');

$server_id = $_POST["server_id"];


//decide which ip to use

$ip = "";
require('ip_decider.php');

$conn = mysqli_connect($ip,"root","","ds","3306");
if($conn)
{
	echo json_encode(array("server_response"=>True));

	$conn->close();
}
else
{
		echo json_encode(array("server_response"=>False));

}
?>