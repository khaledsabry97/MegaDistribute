<?php
header('Content-Type: application/json;charset=utf-8');
require('database_servers.php');

//prepare the sql 
$user_name = $_GET["user_name"];
$email = $_GET["email"];
$password = $_GET["password"];

$sql = "INSERT INTO users(user_name,email,password) VALUES(\"$user_name\", \"$email\",\"$password\")";




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


$inserted = false;
echo $inserted;
if($db_master)
{

//exit($sql);
	if(mysqli_query($db_master ,$sql))
		$inserted = true;

}

if($inserted)
	{	
		echo json_encode(array("server_response"=>"INSERTED"));
		$server_id = 1;
		require('./backup/insert_back_up.php'); // this to insert in the back_up database

		$server_id = 2;
		require('./backup/insert_back_up.php'); // this to insert in the back_up database

		$server_id = 3;
		require('./backup/insert_back_up.php'); // this to insert in the back_up database
				
	}
	else
		  	  	echo json_encode(array("server_response"=>"NOT_INSERTED")); //another username with the same name was found




if($back_up)
	$back_up->close();

if($db_master)
	$db_master->close();

?>