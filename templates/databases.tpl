%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p>SQL Server databases:</p>
<table border="1">
<tr><th>Database</th><th>Compatibility Level</th><th>State</th><th>Recovery Model</th></tr>
%for row in rows:
  <tr>
  <td><a href="/instance/db/{{instance}}/{{row[0]}}">{{row[0]}}</a></td><td>{{row[1]}}</td><td>{{row[2]}}</td><td>{{row[3]}}</td>
  </tr>
%end
</table>
