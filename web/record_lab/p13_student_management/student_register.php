<?php
include "db.php";

if (isset($_POST['register'])) {

    $username = $_POST['username'];
    $roll = $_POST['roll_no'];
    $address = $_POST['address'];
    $phno = $_POST['phno'];
    $password = $_POST['password'];

    mysqli_query($conn,
        "INSERT INTO reg_stud (username, roll_no, address, phno, password)
         VALUES ('$username', $roll, '$address', '$phno', '$password')"
    );

    echo "<br><b>Student Registered Successfully</b>";
}
?>

<h2>Student Registration</h2>

<form method="post">

<table cellpadding="8">
    <tr>
        <td>Username:</td>
        <td><input type="text" name="username" required></td>
    </tr>

    <tr>
        <td>Roll Number:</td>
        <td><input type="number" name="roll_no" required></td>
    </tr>

    <tr>
        <td>Address:</td>
        <td><input type="text" name="address" required></td>
    </tr>

    <tr>
        <td>Phone Number:</td>
        <td><input type="text" name="phno"></td>
    </tr>

    <tr>
        <td>Password:</td>
        <td><input type="password" name="password" required></td>
    </tr>

    <tr>
        <td colspan="2" align="center">
            <input type="submit" name="register" value="Register Student">
        </td>
    </tr>
</table>

</form>
