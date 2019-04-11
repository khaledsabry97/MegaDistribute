<?php

if($server_id == 1)
	$ip = $db_1_ip;
else if($server_id == 2)
	$ip = $db_2_ip;
else if($server_id == 3)
	$ip = $db_3_ip;
else
	exit("no correct server id");

?>