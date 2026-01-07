<?php
include "db.php";

/* Step 1: Fetch marks when roll number is selected */
$mark1 = $mark2 = $mark3 = $mark4 = $mark5 = $mark6 = "";

if (isset($_POST['fetch'])) {
    $roll = $_POST['roll_no'];

    $res = mysqli_query($conn, "SELECT * FROM stud WHERE roll_no=$roll");
    if ($row = mysqli_fetch_assoc($res)) {
        $mark1 = $row['mark1'];
        $mark2 = $row['mark2'];
        $mark3 = $row['mark3'];
        $mark4 = $row['mark4'];
        $mark5 = $row['mark5'];
        $mark6 = $row['mark6'];
    }
}

/* Step 2: Update marks */
if (isset($_POST['update'])) {
    $roll = $_POST['roll_no'];
    $mark1 = $_POST['mark1'];
    $mark2 = $_POST['mark2'];
    $mark3 = $_POST['mark3'];
    $mark4 = $_POST['mark4'];
    $mark5 = $_POST['mark5'];
    $mark6 = $_POST['mark6'];

    $total = $mark1 + $mark2 + $mark3 + $mark4 + $mark5 + $mark6;

    mysqli_query($conn,
        "UPDATE stud SET
        mark1=$mark1, mark2=$mark2, mark3=$mark3,
        mark4=$mark4, mark5=$mark5, mark6=$mark6,
        totalmarks=$total
        WHERE roll_no=$roll"
    );

    echo "<br><b>Marks Updated Successfully</b>";
}
?>

<h2>Update Marks</h2>

<!-- STEP 1: Select Roll Number -->
<form method="post">

Roll Number:
<select name="roll_no">
    <option value="">-- Select Roll No --</option>
    <?php
    $res = mysqli_query($conn, "SELECT roll_no FROM stud");
    while ($row = mysqli_fetch_assoc($res)) {
        $selected = (isset($roll) && $roll == $row['roll_no']) ? "selected" : "";
        echo "<option value='{$row['roll_no']}' $selected>{$row['roll_no']}</option>";
    }
    ?>
</select>

<input type="submit" name="fetch" value="Fetch Marks">

<br><br>

<!-- STEP 2: Edit Marks -->
<table border="1" cellpadding="8">
    <tr>
        <th>Subject</th>
        <th>Marks</th>
    </tr>
    <tr><td>Subject 1</td><td><input type="number" name="mark1" value="<?php echo $mark1; ?>"></td></tr>
    <tr><td>Subject 2</td><td><input type="number" name="mark2" value="<?php echo $mark2; ?>"></td></tr>
    <tr><td>Subject 3</td><td><input type="number" name="mark3" value="<?php echo $mark3; ?>"></td></tr>
    <tr><td>Subject 4</td><td><input type="number" name="mark4" value="<?php echo $mark4; ?>"></td></tr>
    <tr><td>Subject 5</td><td><input type="number" name="mark5" value="<?php echo $mark5; ?>"></td></tr>
    <tr><td>Subject 6</td><td><input type="number" name="mark6" value="<?php echo $mark6; ?>"></td></tr>
</table>

<br>

<input type="submit" name="update" value="Update Marks">

</form>
