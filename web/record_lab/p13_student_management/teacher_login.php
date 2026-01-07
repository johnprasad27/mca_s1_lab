<?php
include "db.php";

if (isset($_POST['login'])) {
    $u = $_POST['username'];
    $p = $_POST['password'];

    $q = "SELECT * FROM teacher WHERE username='$u' AND password='$p'";
    $res = mysqli_query($conn, $q);

    if (mysqli_num_rows($res) > 0) {
        header("Location: dashboard.php");
    } else {
        echo "Invalid Login";
    }
}
?>

<h2>Teacher Login</h2>

<form method="post">
    Username: <input type="text" name="username"><br><br>
    Password: <input type="password" name="password"><br><br>
    <input type="submit" name="login" value="Login">
</form>
