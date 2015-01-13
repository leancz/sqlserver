%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p>Known SQL Server instances:</p>
<ul>
% for item in items:
    <li><a href="/instance/{{item}}">{{item}}</a></li>
% end
</ul>
