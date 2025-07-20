<?php
session_start();
session_unset();
session_destroy();

if(isset($_COOKIE['admin_username'])) {
    $cookie_name = "admin_username";
    unset($_COOKIE[$cookie_name]);
    setcookie($cookie_name, null, -1, '/');
}

header("Location: index.php");
exit;
?>
