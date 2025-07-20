<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog Management</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
</head>
<body>

<?php
require_once('DB.php');

$title = '';
$author = '';
$description = '';
$sel_id = -1;

if (isset($_REQUEST['btnEdit'])) {
    $sql = "SELECT * FROM my_blog_details WHERE id = " . $_REQUEST['btnEdit'];
    if ($result = mysqli_query($link, $sql)) {
        if (mysqli_num_rows($result) > 0) {
            $sel_id = $_REQUEST['btnEdit'];
            while ($row = mysqli_fetch_array($result)) {
                $title = $row['title'];
                $author = $row['author'];
                $description = $row['description'];
            }
        }
    }
}

if (isset($_REQUEST['btnDelete'])) {
    $delete_id = $_REQUEST['btnDelete'];
    $sql = "DELETE FROM my_blog_details WHERE id = $delete_id";
    if (mysqli_query($link, $sql)) {
        echo "Blog entry deleted successfully!";
    } else {
        echo "Error deleting blog entry: " . mysqli_error($link);
    }
}

?>

<div class="container">
    <div class="row">
        <div class="col-md-12">
            <form method="post" action="">
                <input type="text" name="txtTitle" placeholder="Enter title" required value="<?php echo $title ?>">
                <input type="text" name="txtAuthor" placeholder="Enter author name" required value="<?php echo $author ?>">
                <input type="text" name="txtDescription" placeholder="Enter Description" required value="<?php echo $description ?>">
                <input type="hidden" name="selid" value="<?php echo $sel_id ?>">
                <input type="submit" value="<?php echo $sel_id == -1 ? 'Add' : 'Update'; ?> " name="btnAdd" class="btn btn-primary">
            </form>

            <?php

            if (isset($_REQUEST['btnAdd'])) {
                $title = $_REQUEST['txtTitle'];
                $author = $_REQUEST['txtAuthor'];
                $desc = $_REQUEST['txtDescription'];
                
                if ($sel_id == -1) {
                    $sql = "INSERT INTO my_blog_details (title, author, description) VALUES ('$title', '$author', '$desc')";
                } else {
                    $sql  = "UPDATE my_blog_details SET title = '$title', author = '$author', description = '$desc' WHERE id = $sel_id";
                }

                if (mysqli_query($link, $sql)) {
                    echo "Blog ";
                    echo $sel_id == -1 ? "added" : "updated";
                    echo " successfully!";
                } else {
                    echo "ERROR: Could not execute $sql. " . mysqli_error($link);
                }
            }

            $sql = "SELECT * FROM my_blog_details";
            if ($result = mysqli_query($link, $sql)) {
                if (mysqli_num_rows($result) > 0) {
                    echo '<br>';
                    echo '<table class="table"><thead class="thead-dark">
                            <tr>
                                <th>Sr. No.</th>
                                <th>Title</th>
                                <th>Author</th>
                                <th>Description</th>
                                <th>Action</th>
                            </tr>
                        </thead>
                        <tbody>';

                    $sr = 1;
                    while ($row = mysqli_fetch_array($result)) {
                        ?>
                        <tr>
                            <td><?php echo $sr++; ?></td>
                            <td><?php echo $row['title']; ?></td>
                            <td><?php echo $row['author']; ?></td>
                            <td><?php echo $row['description']; ?></td>
                            <td>
                                <form method="post">
                                    <button class="btn btn-warning" type="submit" name="btnEdit" value="<?php echo $row['id']; ?>">
                                        <span><i class="fa fa-pencil" aria-hidden="true"></i></span>
                                    </button>
                                    <button class="btn btn-danger" type="submit" name="btnDelete" value="<?php echo $row['id']; ?>">
                                        <span><i class="fa fa-trash" aria-hidden="true"></i></span>
                                    </button>
                                </form>
                            </td>
                        </tr>
                        <?php
                    }
                    echo '</tbody></table>';
                } else {
                    echo "No blogs found.";
                }
            }

            ?>
        </div>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/jquery@3.7.1/dist/jquery.slim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>
