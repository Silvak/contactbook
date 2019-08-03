# python-web-app
<!DOCTYPE html>
<html lang="en">


<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Contact Book</title>
    <!---- bootstrap 4 -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
        integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="{{url_for("static", filename= "css/bootstrap.min.css") }}">
    <!---- custom css -->
    <link rel="stylesheet" href="{{ url_for( "static", filename="css/main.css") }}">
</head>

<body>
<div class="row h-100 justify-content-center align-items-center p-4">
    <div class="cb col-md-5">
        <main>
            <article>
                <header>
                    <h1>About this website</h1>
                    <time datetime="2019-8-03"></time>
                </header>
                <p>It is a small web application that uses python as a server, the flask library, the bootstrap toolkit
                    and the firebase database service in order to schedule contacts.
                </p><br><br>
                <h5>Requirements</h5>
                <li>flask</li>
                <li>firebase-admind</li>
                <br><br><br>
                <h5>All code is found in the following repository</h5>
                <p><a href="https://github.com/Silvak/python-web-app">https://github.com/Silvak/python-web-app/<a></a></p><br>
                <p  >git user <a href="https://github.com/Silvak" class="text-secondary">Silvak</a></p>
            </article>
        </main>
    </div>

    <div class="col-sm-4  text-center ">
        <img src="/python-web-app/blob/master/static/img/web-app.jpg" class="img-fluid" alt="flag img programmer by Silvak">
    </div>
</div>
</body>

</html>
