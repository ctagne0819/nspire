<?php
$conn = mysqli_connect("localhost", "root", "", "nspire");
// Check connection
if ($conn->connect_error) {
die("Connection failed: " . $conn->connect_error);
}
$sql = "SELECT name, timestamp FROM nspire";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
// output data of each row
while($row = $result->fetch_assoc()) {
echo <td>" . $row["name"] . "</td><td>"
. $row["timestamp"]. "</td></tr>";
}
echo "</table>";
} else { echo "Once you start logging your mood everyday, you will be able to see them here!"; }
$conn->close();
?>
