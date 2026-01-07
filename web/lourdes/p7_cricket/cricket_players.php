<!DOCTYPE html>
<html>
<head>
    <title>Indian Cricket Players</title>
</head>
<body>

<h2>Indian Cricket Players</h2>

<?php
// Store player names in an array
$players = array(
    "Sachin Tendulkar",
    "Virat Kohli",
    "Rohit Sharma",
    "MS Dhoni",
    "Rahul Dravid",
    "Jasprit Bumrah"
);
?>

<table border="1" cellpadding="8">
    <tr>
        <th>Sl. No</th>
        <th>Player Name</th>
    </tr>

    <?php
    $i = 1;
    foreach ($players as $name) {
        echo "<tr>";
        echo "<td>$i</td>";
        echo "<td>$name</td>";
        echo "</tr>";
        $i++;
    }
    ?>
</table>

</body>
</html>
