<?php
include "db.php";

/* ---------- GRADE FUNCTION ---------- */
function getGrade($avg) {
    if ($avg >= 90) return "A+";
    else if ($avg >= 80) return "A";
    else if ($avg >= 70) return "B+";
    else if ($avg >= 60) return "B";
    else if ($avg >= 50) return "C";
    else return "F";
}

/* ---------- FETCH TOP STUDENT ---------- */
$top = mysqli_query($conn,
    "SELECT reg_stud.roll_no, username, totalmarks
     FROM reg_stud, stud
     WHERE reg_stud.roll_no = stud.roll_no
     ORDER BY totalmarks DESC LIMIT 1"
);
$topStudent = mysqli_fetch_assoc($top);

/* ---------- SEARCH STUDENT ---------- */
$data = null;
if (isset($_POST['search'])) {
    $roll = $_POST['roll_no'];

    $res = mysqli_query($conn,
        "SELECT reg_stud.roll_no, username,
        mark1, mark2, mark3, mark4, mark5, mark6, totalmarks
        FROM reg_stud, stud
        WHERE reg_stud.roll_no = stud.roll_no
        AND reg_stud.roll_no = $roll"
    );

    $data = mysqli_fetch_assoc($res);
}
?>

<h2>Student Score Card</h2>

<!-- 🔝 TOP STUDENT -->
<h3>Top Student</h3>
<table border="1" cellpadding="8">
<tr>
    <th>Roll No</th>
    <th>Name</th>
    <th>Total Marks</th>
</tr>
<tr>
    <td><?php echo $topStudent['roll_no']; ?></td>
    <td><?php echo $topStudent['username']; ?></td>
    <td><?php echo $topStudent['totalmarks']; ?></td>
</tr>
</table>

<br><hr><br>

<!-- 🔍 SEARCH STUDENT -->
<h3>Search Student</h3>

<form method="post">
Roll Number:
<select name="roll_no">
    <option value="">-- Select Roll No --</option>
    <?php
    $res = mysqli_query($conn, "SELECT roll_no FROM stud");
    while ($r = mysqli_fetch_assoc($res)) {
        echo "<option value='{$r['roll_no']}'>{$r['roll_no']}</option>";
    }
    ?>
</select>

<input type="submit" name="search" value="Fetch Score Card">
</form>

<br>

<?php if ($data) { 
    $avg = $data['totalmarks'] / 6;
    $grade = getGrade($avg);
?>

<!-- 📄 SCORE CARD -->
<h3>Score Card</h3>

<table border="1" cellpadding="8">
<tr><td><b>Roll No</b></td><td><?php echo $data['roll_no']; ?></td></tr>
<tr><td><b>Name</b></td><td><?php echo $data['username']; ?></td></tr>
<tr><td>Subject 1</td><td><?php echo $data['mark1']; ?></td></tr>
<tr><td>Subject 2</td><td><?php echo $data['mark2']; ?></td></tr>
<tr><td>Subject 3</td><td><?php echo $data['mark3']; ?></td></tr>
<tr><td>Subject 4</td><td><?php echo $data['mark4']; ?></td></tr>
<tr><td>Subject 5</td><td><?php echo $data['mark5']; ?></td></tr>
<tr><td>Subject 6</td><td><?php echo $data['mark6']; ?></td></tr>
<tr><td><b>Total</b></td><td><?php echo $data['totalmarks']; ?></td></tr>
<tr><td><b>Average</b></td><td><?php echo number_format($avg, 2); ?></td></tr>
<tr><td><b>Grade</b></td><td><?php echo $grade; ?></td></tr>
</table>

<?php } ?>
