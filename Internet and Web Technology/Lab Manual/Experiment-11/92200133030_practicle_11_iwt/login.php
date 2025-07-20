<?php
session_start();
$admin_username = "admin";
$admin_password = "password";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $password = $_POST['password'];

    if ($username === $admin_username && $password === $admin_password) {
        $_SESSION['admin_logged_in'] = true;
        
        // Set cookie if remember me is checked
        if(isset($_POST['remember_me']) && $_POST['remember_me'] === "on") {
            $cookie_name = "admin_username";
            $cookie_value = $username;
            setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 = 1 day
        }

        header("Location: dashboard.php");
        exit;
    } else {
        echo "Invalid username or password";
    }
}
?>
