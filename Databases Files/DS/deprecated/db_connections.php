<?php
//before we make slaves connections we first check if the back_up database is available
$back_up = mysqli_connect($db_back_up_ip,"root","","ds_back_up","3306");
$db_master = mysqli_connect($db_master_ip,"root","","ds","3306");

if(!$back_up)
{
	echo json_encode(array("server_response"=>"server down"));
	exit("no connection to database back_up");
}
if(!$db_master)
{
	echo json_encode(array("server_response"=>"server down"));
	exit("no connection to database master");
}

//connect to slaves
$db_1 = mysqli_connect($db_1_ip,"root","","ds","3306");
$db_2 = mysqli_connect($db_2_ip,"root","","ds","3306");
$db_3 = mysqli_connect($db_3_ip,"root","","ds","3306");

$server_id = 0;

if(!$db_1)
{
	$server_id = 1;
	require('./backup/insert_back_up.php'); // this to insert in the back_up database
}
if(!$db_2)
{
	$server_id = 2;
	require('./backup/insert_back_up.php'); // this to insert in the back_up database
}
if(!$db_3)
{
	$server_id = 3;
	require('./backup/insert_back_up.php'); // this to insert in the back_up database
}
?>