<?php
//header('Content-Type: application/json;charset=utf-8');
require('database_servers.php');

$json = array("servers" => array($db_1_ip,$db_2_ip,$db_3_ip));
echo json_encode($json);

?>