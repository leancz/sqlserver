from datetime import datetime, timedelta
import pypyodbc
import database
import bottle
from bottle import run, route, debug, template
import os
import _winreg
template_path=os.path.dirname(os.path.abspath(__file__))+'/templates/'
bottle.TEMPLATE_PATH.insert(0,template_path)
#bottle.TEMPLATE_PATH.insert(0,'C:/Python27/Lib/sql_server/templates/')

@route('/')
def home():
    servers=[]
    reg_key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r'Software\Wow6432Node\ODBC\ODBC.INI\ODBC Data Sources', 0, _winreg.KEY_ALL_ACCESS)
    try:
        i = 0
        while True:
            name, value, type = _winreg.EnumValue(reg_key, i)
            if (value == u'SQL Server'): servers.append(name)
            i = i + 1
    except WindowsError:
        pass
    output = template('inventory', items=servers)
    return output

@route('/instance/:sql_instance')
def instance(sql_instance):
    with database.DB(sql_instance) as db:
        query = 'select name, compatibility_level, state_desc, recovery_model_desc from sys.databases'
        result = db.fetchall(query)
    output = template('databases', rows=result, instance=sql_instance)
    return output

@route('/instance/db/:sql_instance/:sql_db')
def instance_database(sql_instance, sql_db):
    backups={'full': None, 'log': None, 'diff': None}
    with database.DB(sql_instance) as db:
        query = 'SELECT max(backup_start_date), type FROM msdb.dbo.backupset WHERE database_name = ? GROUP BY type'
        result = db.fetchall(query, [sql_db])
        for bu in result:
            if bu[1]=='D': backups['full'] = bu[0]
            if bu[1]=='I': backups['diff'] = bu[0]
            if bu[1]=='L': backups['log'] = bu[0]
    full_test = datetime.now() - timedelta(hours=30)
    log_test = datetime.now() - timedelta(hours=6)
    output = template('one_database', db=sql_db, rows=backups, full_test=full_test, log_test=log_test)
    return output

run(host='localhost', port=8080, debug=True)


def main():
    pass

if __name__ == '__main__':
    main()
