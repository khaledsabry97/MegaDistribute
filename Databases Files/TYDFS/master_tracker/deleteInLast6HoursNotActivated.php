<?php

require('connection.php');


$sql = "DELETE
FROM
	users 
WHERE
	UNIX_TIMESTAMP( date_created ) < UNIX_TIMESTAMP( NOW( ) - 1000 *60 *60*6 ) and current_available = False;";

if(mysqli_query($conn ,$sql))
	echo json_encode(array("server_response"=>True));
else
	echo json_encode(array("server_response"=>False));
	
	
	


?>
