<!DOCTYPE html>

<html>
    % include('header.ftl')
    <title>Home Page</title>
    <link rel="stylesheet" type="text/css" href="static/css/home.css">
    <body id="page-top" data-spy="scroll" data-target=".navbar-custom">
    <!-- Start Header -->
    <nav class="navbar navbar-custom navbar-fixed-top" role="navigation">
        <div class="container">
            <div class="navbar-header page-scroll">
                <a class="navbar-brand" href="/">YNAGoo!</a>
            </div>
            <div class="collapse navbar-collapse navbar-right navbar-main-collapse">
                <ul class="nav navbar-nav">
                    <li class="hidden"><a href="/"></a></li>
                    <li class="page-scroll"><a href="/index">Search</a></li>
                    <li class="page-scroll"><a href="/syseval">Eval</a></li>
                </ul>
            </div>
        </div>
    </nav>
    <!-- End Header -->

    <section class="intro">
        <div class="intro-body">
            <div class="container">
                <div class="row">
                    <div class="col-md-8 col-md-offset-2">
                        <h1 class="brand-heading">Search is everywhere!</h1>
                        <p class="intro-text">The world is full of infomation and changes. A better tool to search and eval in trec compitition. </p>
                        <ul class="list-inline banner-social-buttons">
                            <li>
                                <a href="/index" class="btn btn-default btn-lg"><span class="network-name">Search Engine</span></a>
                            </li>
                            <li>
                                <a href="/syseval" class="btn btn-default btn-lg"><span class="network-name">Trec Evaluation</span></a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>
    </body>
</html>
