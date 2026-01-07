<!DOCTYPE html>
<html>
<head>
    <title>Electricity Bill Calculation</title>
</head>
<body>

<h2>Electricity Bill</h2>

<form method="post">
    Consumer Name:
    <input type="text" name="name" required><br><br>

    Units Consumed:
    <input type="number" name="units" required><br><br>

    <input type="submit" name="calculate" value="Calculate Bill">
</form>

<?php
if (isset($_POST['calculate'])) {

    $name = $_POST['name'];
    $units = $_POST['units'];
    $bill = 0;

    /* Tariff Calculation */
    if ($units <= 100) {
        $bill = $units * 1.5;
    }
    else if ($units <= 200) {
        $bill = (100 * 1.5) + (($units - 100) * 2.5);
    }
    else if ($units <= 300) {
        $bill = (100 * 1.5) + (100 * 2.5) + (($units - 200) * 4);
    }
    else {
        $bill = (100 * 1.5) + (100 * 2.5) + (100 * 4) + (($units - 300) * 6);
    }

    echo "<h3>Electricity Bill Details</h3>";
    echo "Consumer Name: <b>$name</b><br>";
    echo "Units Consumed: <b>$units</b><br>";
    echo "Total Bill Amount: <b>₹ $bill</b>";
}
?>

</body>
</html>
