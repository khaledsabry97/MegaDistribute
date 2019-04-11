<?php
header('Content-Type: application/json;charset=utf-8');
require('../database_servers.php');

$back_up = mysqli_connect($db_back_up_ip,"root","","ds_back_up","3306");

if(!$back_up)
{
	echo json_encode(array("server_response"=>"server down"));
	exit("no connection to database back_up");
}
//prepare the sql 
$server_id = $_POST["server_id"];
$user_name = $_POST["user_name"];
$email = $_POST["email"];
$password = $_POST["password"];

//decide which ip to use

$ip = "";
require('ip_decider.php');

$conn = mysqli_connect($ip,"root","","ds","3306");
if($conn)
{
	$sql = "INSERT INTO users(user_name,email,password) VALUES(\"$user_name\", \"$email\",\"$password\")";


	mysqli_query($conn ,$sql);

		
	require('delete_backup.php');


	$conn->close();
}
$back_up->close();
?>