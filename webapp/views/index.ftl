<!DOCTYPE html>

<html>
    % include('header.ftl', title='Home Page')
    <title>Home Page</title>
    <body>
        <div class="container-fluid">
            <div class="row" style="height: 100px"></div>
            <div class="row">
            <div class="col-md-4"></div>
            <div class="col-md-4 " style="text-align: center"><img src="static/images/YANGoo_big.png"></div>
            <div class="col-md-4"></div>
            </div>
            <div class="row">
                <div class="col-md-3"></div>
                <form class="form-index" role="form" method="POST" action="/query">
                    <div class="form-group">
                        <div class="input-group">
                            <div class="input-group-btn">
                                <button type="button" class="btn btn-success btn-lg dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">{{type}}<span class="caret"></span></button>
                                <ul class="dropdown-menu">
                                    <li><a href="/index?searchType=Trec09">Trec09</a></li>
                                    <li><a href="/index?searchType=Trec12">Trec12</a></li>
                                </ul>
                            </div>
                            <input type="text" class="typeahead form-control input-lg" name="query">
                            <span class="input-group-btn">
                                <button class="btn btn-primary btn-lg" type="submit">
                                    <span class="glyphicon glyphicon glyphicon-search" aria-hidden="true"></span>
                                </button>
                            </span>
                        </div>
                    </div>
                </form>
                <div class="col-md-4"></div>
            </div>
        </div>
        % include('footer.ftl')
        <script>
            var bestPictures = new Bloodhound({
            datumTokenizer: Bloodhound.tokenizers.obj.nonword('value'),
            queryTokenizer: Bloodhound.tokenizers.nonword,
            limit: 10,
            remote: '/suggest?keyword=%QUERY',
            });

            bestPictures.initialize();

            $('.container-fluid .typeahead').typeahead( {
                hint: true,
                highlight: true,
                minLength: 1
            }, {
                name: 'best-pictures',
                displayKey: 'value',
                source: bestPictures.ttAdapter(),
            });
        </script>
    </body>
</html>
