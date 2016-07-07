<!DOCTYPE html>

<html>
    % include('header.ftl', title='Home Page')
    <title>Home Page</title>
    <body>
        <div class="container-fluid">
            <div class="row" style="height: 100px"></div>
            <div class="row">
                <div class="col-md-4"></div>
                    <div class="col-md-4" style="text-align: center;">
                    <p>System</p>
                    <table class="table table-hover table-bordered">
                        <tr>
                            <th class="col-md-1">Name</th>
                            <th class="col-md-1">MAP</th>
                            <th class="col-md-1">P@5</th>
                            <th class="col-md-1">P@10</th>
                            <th class="col-md-1">P@20</th>
                            <th class="col-md-1">ERR@20</th>
                            <th class="col-md-1">nDCG@20</th>
                        </tr>
                        % for trec,eval_results in trec_eval_results.items():
                        <tr>
                            <td class="col-md-1">{{trec}}</td>
                            <td class="col-md-1">{{eval_results['map']}}</td>
                            <td class="col-md-1">{{eval_results['P_5']}}</td>
                            <td class="col-md-1">{{eval_results['P_10']}}</td>
                            <td class="col-md-1">{{eval_results['P_20']}}</td>
                            <td class="col-md-1">{{eval_results['recip_rank']}}</td>
                            <td class="col-md-1">{{eval_results['ndcg_cut_20']}}</td>
                        </tr>
                        % end
                    </table>
                    </div>
                <div class="col-md-4"></div>
            </div>
            <div class="row">
                <div class="col-md-4"></div>
                    <div class="col-md-4" style="text-align: center;">
                    <p>Overview Baseline</p>
                    <table class="table table-hover table-bordered">
                        <tr>
                            <th class="col-md-1">Name</th>
                            <th class="col-md-1">MAP</th>
                            <th class="col-md-1">P@5</th>
                            <th class="col-md-1">P@10</th>
                            <th class="col-md-1">P@20</th>
                            <th class="col-md-1">ERR@20</th>
                            <th class="col-md-1">nDCG@20</th>
                        </tr>
                        % for trec,measures in baseline.items():
                        <tr>
                            <td class="col-md-1">{{trec}}</td>
                            <td class="col-md-1">{{measures['MAP']}}</td>
                            <td class="col-md-1">{{measures['P@5']}}</td>
                            <td class="col-md-1">{{measures['P@10']}}</td>
                            <td class="col-md-1">{{measures['P@20']}}</td>
                            <td class="col-md-1">{{measures['ERR@20']}}</td>
                            <td class="col-md-1">{{measures['nDCG@20']}}</td>
                        </tr>
                        % end
                    </table>
                    </div>
                <div class="col-md-4"></div>
            </div>
        </div>
        % include('footer.ftl')
    </body>
</html>
