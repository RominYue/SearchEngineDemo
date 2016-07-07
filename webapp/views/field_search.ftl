<!DOCTYPE html>

<html>
    % include('header.ftl', title='Field Search')
    <title>Field Search</title>
    <div class="container">
        <div class="row" style="height: 30px"></div>
        <div class="row">
            <div class="col-md-5"></div>
            <div class="col-md-5"><img src="static/images/YANGoo.png"></div>
            <div class="col-md-2"></div>
        </div>
        <form class="form-signin form-horizontal" role="form" action="/field_query" method='POST'>
            <div class="form-group">
                <div class="col-sm-3">
                    <label for="trecID">TrecID</label>
                </div>
                <div class="col-sm-9">
                    <input class="form-control" id="trecID" placeholder="trec_id" name="id">
                </div>
            </div>
            <div class="form-group">
                <div class="col-sm-3">
                    <label for="url">URL</label>
                </div>
                <div class="col-sm-9">
                    <input class="form-control" id="url" placeholder="url_or_text" name="url">
                </div>
            </div>
            <div class="form-group">
                <div class="col-sm-3">
                    <label for="domain">Domain</label>
                </div>
                <div class="col-sm-9">
                    <input class="form-control" id="domain" placeholder="domain" name="domain">
                </div>
            </div>
            <div class="form-group">
                <div class="col-sm-3">
                    <label for="title">Title</label>
                </div>
                <div class="col-sm-9">
                    <input class="form-control" id="title" placeholder="title_text" name="title">
                </div>
            </div>
            <div class="form-group">
                <div class="col-sm-3">
                    <label for="body">Body</label>
                </div>
                <div class="col-sm-9">
                    <input class="form-control" id="body" placeholder="body_text" name="body">
                </div>
            </div>
            <div class="form-group">
                <div class="col-sm-offset-3 col-sm-9">
                    <button type="submit" class="btn btn-primary">Search Go!</button>
                </div>
            </div>
        </form>
    </div>
    % include('footer.ftl')
</html>
