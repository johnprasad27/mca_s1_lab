<?php
include "db.php";
?>

<!DOCTYPE html>
<html>
<head>
    <title>Book Information</title>
</head>
<body>

<h2>Enter Book Details</h2>

<form method="post">
    Edition Number: <input type="number" name="edition_no"><br><br>
    Title: <input type="text" name="title"><br><br>
    Authors: <input type="text" name="authors"><br><br>
    Edition: <input type="text" name="edition"><br><br>
    Publisher: <input type="text" name="publisher"><br><br>

    <input type="submit" name="save" value="Save Book">
</form>

<?php
if (isset($_POST['save'])) {
    $eno = $_POST['edition_no'];
    $title = $_POST['title'];
    $authors = $_POST['authors'];
    $edition = $_POST['edition'];
    $publisher = $_POST['publisher'];

    mysqli_query($conn,
        "INSERT INTO book VALUES
        ($eno, '$title', '$authors', '$edition', '$publisher')"
    );

    echo "<b>Book Details Stored Successfully</b>";
}
?>

<hr>

<h2>Search Book by Title</h2>

<form method="post">
    Enter Title:
    <input type="text" name="search_title">
    <input type="submit" name="search" value="Search">
</form>

<?php
if (isset($_POST['search'])) {
    $stitle = $_POST['search_title'];

    $res = mysqli_query($conn,
        "SELECT * FROM book WHERE title='$stitle'"
    );

    if (mysqli_num_rows($res) > 0) {
        echo "<h3>Book Details</h3>";
        echo "<table border='1' cellpadding='8'>";
        echo "<tr>
                <th>Edition No</th>
                <th>Title</th>
                <th>Authors</th>
                <th>Edition</th>
                <th>Publisher</th>
              </tr>";

        while ($row = mysqli_fetch_assoc($res)) {
            echo "<tr>
                    <td>{$row['edition_no']}</td>
                    <td>{$row['title']}</td>
                    <td>{$row['authors']}</td>
                    <td>{$row['edition']}</td>
                    <td>{$row['publisher']}</td>
                  </tr>";
        }
        echo "</table>";
    } else {
        echo "<b>No book found with the given title</b>";
    }
}
?>

</body>
</html>
