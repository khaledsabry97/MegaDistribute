<?php
require('connection.php');




$sql = "SELECT
	users.user_id,
	users.node_id,
	users.file_name,
	users.current_available
FROM
	users,
	( SELECT * FROM `users` GROUP BY user_id, file_name HAVING count( node_id ) < 3 ) AS users2 
WHERE
	users.user_id = users2.user_id 
	AND users.file_name = users2.file_name 

ORDER BY
	users.user_id,
	users.file_name";

$result = mysqli_query($conn ,$sql);


$arrays = array();
	while ($row = mysqli_fetch_assoc($result)) {
		
		$arrays[] = $row;

	}

	echo json_encode(array("server_response"=>$arrays));


    mysqli_free_result($result);
$conn->close();

?>
