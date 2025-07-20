<?php  
    $link = mysqli_connect("localhost", "root", "", "demo");
    
    if($link === false){
        die("ERROR: Could not connect. " . mysqli_connect_error());
    }
    $sql = "CREATE TABLE IF NOT EXISTS `Table` (
        id int(4) not null PRIMARY KEY , 
        msg varchar(255) not null
        )";

    if(mysqli_query($link, $sql)){
        echo "Table created successfully.";
    } else{
        echo "ERROR: Could not able to execute $sql. " . mysqli_error($link);
    }
?>


