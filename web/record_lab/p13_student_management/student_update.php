<?php
include "db.php";

/* Initialize variables */
$roll = "";
$username = "";
$address = "";
$phno = "";
$password = "";

/* Fetch student details */
if (isset($_POST['fetch'])) {

    $roll = $_POST['roll_no'];

    $query = "SELECT * FROM reg_stud WHERE roll_no = $roll";
    $res = mysqli_query($conn, $query);

    if ($row = mysqli_fetch_assoc($res)) {
        $username = $row['username'];
        $address  = $row['address'];
        $phno     = $row['phno'];
        $password = $row['password'];
    }
}

/* Update student details */
if (isset($_POST['update'])) {

    $roll     = $_POST['roll_no'];
    $username = $_POST['username'];
    $address  = $_POST['address'];
    $phno     = $_POST['phno'];
    $password = $_POST['password'];

    mysqli_query($conn,
        "UPDATE reg_stud SET
         username='$username',
         address='$address',
         phno='$phno',
         password='$password'
         WHERE roll_no=$roll"
    );

    echo "<br><b>Student Details Updated Successfully</b>";
}

/* Delete student */
if (isset($_POST['delete'])) {

    $roll = $_POST['roll_no'];

    mysqli_query($conn,
        "DELETE FROM reg_stud WHERE roll_no=$roll"
    );

    echo "<br><b>Student Deleted Successfully</b>";

    $roll = $username = $address = $phno = $password = "";
}
?>

<h2>Update / Delete Student</h2>

<form method="post">

Roll Number:
<select name="roll_no" required>
    <option value="">-- Select Roll No --</option>
    <?php
    $res = mysqli_query($conn, "SELECT roll_no FROM reg_stud");
    while ($row = mysqli_fetch_assoc($res)) {
        $selected = ($row['roll_no'] == $roll) ? "selected" : "";
        echo "<option value='{$row['roll_no']}' $selected>{$row['roll_no']}</option>";
    }
    ?>
</select>

<input type="submit" name="fetch" value="Fetch Details">

<br><br>

<table cellpadding="8">
    <tr>
        <td>Username:</td>
        <td><input type="text" name="username" value="<?php echo $username; ?>"></td>
    </tr>
    <tr>
        <td>Address:</td>
        <td><input type="text" name="address" value="<?php echo $address; ?>"></td>
    </tr>
    <tr>
        <td>Phone:</td>
        <td><input type="text" name="phno" value="<?php echo $phno; ?>"></td>
    </tr>
    <tr>
        <td>Password:</td>
        <td><input type="text" name="password" value="<?php echo $password; ?>"></td>
    </tr>
    <tr>
        <td colspan="2" align="center">
            <input type="submit" name="update" value="Update Student">
            <input type="submit" name="delete" value="Delete Student"
                   onclick="return confirm('Are you sure?');">
        </td>
    </tr>
</table>

</form>
