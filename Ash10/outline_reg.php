<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>php validations</title>
</head>

<body>
    <h1>Registration Form</h1>
    <form action="" method="POST">
        Username:<input type="text" name="username"><br><br> Email:
        <input type="text" name="email"><br><br> Password:
        <input type="text" name="pass"><br><br> Confirm Password:<input type="text" name="cpass"><br><br>
        <input type="submit" value="Register">

        <?php
        if (
            empty($_POST["username"]) ||
            empty($_POST["email"]) ||
            empty($_POST["pass"]) ||
            empty($_POST["cpass"])
        ) {
            die("Please fill all required fields!");
        }
        if ($_POST["pass"] != $_POST["cpass"]) {
            die("Password and confirm password should match");
        } else {
            die("successfull");
        }
        ?>
    </form>
</body>

</html>