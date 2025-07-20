<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Message Sharing</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            padding-top: 50px;
        }

        .container {
            max-width: 600px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        textarea {
            resize: none;
        }
    </style>
</head>

<body>
    <div class="container">
        <h2>Message Sharing</h2>
        <form action="index.php" method="post">
            <div class="form-group">
                <label for="txtSender">Enter your message:</label>
                <textarea class="form-control" name="txtSender" id="txtSender" cols="30" rows="5"></textarea>
            </div>
            <button type="submit" class="btn btn-primary" name="send">Send</button>
        </form>
        <hr>
        <?php
        require_once('db.connect.php');
        if (isset($_REQUEST["send"])) {
            if (isset($_REQUEST["txtSender"]) && $_REQUEST["txtSender"] != " ") {
                $code = rand(1000, 9999);
                $text = $_REQUEST["txtSender"];
                $sql_insert = "INSERT INTO `Table` VALUES ($code, '$text')";
                if (mysqli_query($link, $sql_insert)) {
                    echo "<p class='text-success'>Data inserted successfully. Use Code: " . $code . "</p>";
                } else {
                    echo "<p class='text-danger'>ERROR: Could not execute $sql_insert. " . mysqli_error($link) . "</p>";
                }
            } else {
                echo "<p class='text-danger'>Please enter text to share!</p>";
            }
        }
        ?>
        <form action="" method="post">
            <div class="form-group">
                <label for="txtCode">Enter code to fetch message:</label>
                <input type="text" class="form-control" name="txtCode" id="txtCode">
            </div>
            <button type="submit" class="btn btn-primary" name="fetch">Fetch</button>
        </form>
        <?php
        if (isset($_REQUEST['fetch'])) {
            if ($_REQUEST['txtCode'] != " ") {
                $sql_fetch = "SELECT msg FROM `Table` WHERE id = " . $_REQUEST['txtCode'];
                if ($result = mysqli_query($link, $sql_fetch)) {
                    if (mysqli_num_rows($result) > 0) {
                        while ($row = mysqli_fetch_array($result)) {
                            echo "<p class='mt-3'><strong>Message:</strong> " . $row['msg'] . "</p>";
                        }
                    } else {
                        echo "<p class='text-danger'>No such code available.</p>";
                    }
                }
            }
        }
        mysqli_close($link);
        ?>
    </div>
</body>

</html>




