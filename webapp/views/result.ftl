<!DOCTYPE html>

<html>
    % include('header.ftl', title='Field Search')
    <title>Result Page</title>

    <body>
    <div class="container-fluid">
    <div class="row" style="height: 30px"></div>
        <!--left-->
        <div class="col-sm-1">
            <img src="static/images/YANGoo_small.png">
        </div><!--/left-->

        <!--center-->
        <div class="col-sm-7">
            <div class="row">
                <div class="col-xs-8">
                    <form method="POST" action="/query">
                        <div class="form-group">
                            <div class="input-group">
                                <div class="input-group-btn">
                                    <button type="button" class="btn btn-success dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">{{searchType}}<span class="caret"></span></button>
                                    <ul class="dropdown-menu">
                                        <li><a href="/index?searchType=Trec09">Trec09</a></li>
                                        <li><a href="/index?searchType=Trec12">Trec12</a></li>
                                    </ul>
                                </div>
                                <input type="text" class="typeahead form-control" name="query" value="{{query}}">
                                <span class="input-group-btn">
                                    <button class="btn btn-primary" type="submit">
                                        <span class="glyphicon glyphicon glyphicon-search" aria-hidden="true"></span>
                                    </button>
                            </span>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
            % if resultNum == 0:
            <p>There is no results match this query</p>
            % end
            % hits = results[0]['hits']
            % qtime = results[0]['qtime']
            <br/>
            %if spellFlag == True:
            <div class="row">
                <div class="col-xs-12"><i><font color="red">Did you mean.. </font><a href="/result?searchType={{searchType}}&amp;page=1&amp;query={{query_right}}">{{query_right}}</a></i></div>
            </div>
            <br>
            %end
            <div class="row">
                <div class="col-xs-12"><i>{{hits}} Results. Cost {{qtime}} miliseconds.</i></div>
            </div>
            % for doc in results:
            % trec_id = doc['id']
            % title = doc['title'] if doc.has_key('title') else ""
            % body = doc['highlighting']
            % url = doc['url']
            <div class="row">
                <div class="col-xs-12">
                    <h3>{{trec_id}}</h3>
                    <h4>{{title}}</h4>
                    <p>{{!body}}</p>
                    <!--p class="lead"><a href="https://github.com/RominYue" target="_blank"><button class="btn btn-default">Read More</button></a></p-->
                    <ul class="list-inline"><li><a href={{url}}>{{url}}</a></li></ul>
                    <!-- p class="pull-right"><span class="label label-default">keyword</span> <span class="label label-default">tag</span> <span class="label label-default">post</span></p>
                    <ul class="list-inline"><li><a href="#">2 Days Ago</a></li><li><a href="#"><i class="glyphicon glyphicon-comment"></i> 2 Comments</a></li><li><a href="#"><i class="glyphicon glyphicon-share"></i> 14 Shares</a></li></ul>
                    -->
                </div>
            </div>
            <hr>
            % end
            <nav>
                <ul class="pagination">
                    % if paginator.has_prev:
                    <li>
                    <a href="/result?searchType={{searchType}}&amp;page={{paginator.page - 1}}&amp;query={{query}}" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a>
                    </li>
                    % end

                    % for num in paginator.iter_pages():
                    % if num == paginator.page:
                    <li class="active"><a href="/result?searchType={{searchType}}&amp;page={{num}}&amp;query={{query}}">{{num}}</a></li>
                    % else:
                    <li><a href="/result?searchType={{searchType}}&amp;page={{num}}&amp;query={{query}}">{{num}}</a></li>
                    % end
                    % end

                    % if paginator.has_next:
                    <li>
                        <a href="/result?searchType={{searchType}}&amp;page={{paginator.page + 1}}&amp;query={{query}}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a>
                    </li>
                    % end
                </ul>
            </nav>
        </div><!--/center-->

        <!--right-->
        <div class="col-sm-3">
            <h2>More You Like</h2>
            % for ad in ads:
            % ad_text = ad['highlighting']
            <div class="panel panel-warning">
                <div class="panel-heading">Ads</div>
                <div class="panel-body" style="text-align: left;">{{!ad_text}}</div>
            </div>
            <hr>
            % end
            <div class="panel panel-default">
                <div class="panel-heading">Evaluations</div>
                <div class="panel-body">Content here..</div>
            </div>
            <hr>
        </div><!--/right-->
    </div><!--/container-fluid-->
    </body>
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
</html>
