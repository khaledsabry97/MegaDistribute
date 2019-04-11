<?php

@daprecated
if($back_up)
	$back_up->close();

if($db_master)
	$db_master->close();

if($db_1)
	$db_1->close();

if($db_2)
	$db_2->close();

if($db_3)
	$db_3->close();

?>