<?php
include "db.php";
?>

<h2>Mark Entry</h2>

<form method="post">

Roll Number:
<select name="roll_no">
    <option value="">-- Select Roll No --</option>
    <?php
    $res = mysqli_query($conn, "SELECT roll_no FROM reg_stud");
    while ($row = mysqli_fetch_assoc($res)) {
        echo "<option value='{$row['roll_no']}'>{$row['roll_no']}</option>";
    }
    ?>
</select>

<br><br>

<table border="1" cellpadding="8">
    <tr>
        <th>Subject</th>
        <th>Marks</th>
    </tr>
    <tr><td>Subject 1</td><td><input type="number" name="mark1"></td></tr>
    <tr><td>Subject 2</td><td><input type="number" name="mark2"></td></tr>
    <tr><td>Subject 3</td><td><input type="number" name="mark3"></td></tr>
    <tr><td>Subject 4</td><td><input type="number" name="mark4"></td></tr>
    <tr><td>Subject 5</td><td><input type="number" name="mark5"></td></tr>
    <tr><td>Subject 6</td><td><input type="number" name="mark6"></td></tr>
</table>

<br>

<input type="submit" name="submit" value="Submit Marks">

</form>

<?php
if (isset($_POST['submit'])) {

    $roll = $_POST['roll_no'];
    $m1 = $_POST['mark1'];
    $m2 = $_POST['mark2'];
    $m3 = $_POST['mark3'];
    $m4 = $_POST['mark4'];
    $m5 = $_POST['mark5'];
    $m6 = $_POST['mark6'];

    $total = $m1 + $m2 + $m3 + $m4 + $m5 + $m6;

    if ($roll != "") {
        mysqli_query($conn,
            "INSERT INTO stud
            (roll_no, mark1, mark2, mark3, mark4, mark5, mark6, totalmarks)
            VALUES
            ($roll, $m1, $m2, $m3, $m4, $m5, $m6, $total)"
        );

        echo "<br><b>Marks Entered Successfully</b>";
    } else {
        echo "<br><b>Please select roll number</b>";
    }
}
?>
