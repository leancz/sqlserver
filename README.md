# sqlserver
Simple web server to manage SQL Server instances. 

1. To add an instance create an ODBC data source (C:\Windows\SysWOW64\adbcad32.exe)
2. Run web_server.py with a user that has read permissions on master & msdb databases for each instance

Requires pypyodbc, bottle
