%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p>SQL Server database :</p>


<p>Last FULL backup {{!'<font>' if (rows['full'] is None) else '<font color="red">' if (rows['full'] < full_test) else '<font>'}} {{rows['full']}}</font></p>
<p>Last LOG  backup {{!'<font>' if (rows['log'] is None) else '<font color="red">' if (rows['log'] < log_test) else '<font>'}} {{rows['log']}} </font></p>
<p>Last DIFF backup {{rows['diff']}} </p>
