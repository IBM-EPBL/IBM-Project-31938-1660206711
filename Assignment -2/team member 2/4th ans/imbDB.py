import ibm_db

hostname = '125f9f61-9715-46f9-9399-c8177b21803b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud'
uid = 'skg38697'
pwd = 'YtCcCWh8wn0mE5Sc'
driver = "{IBM DB2 ODBC DRIVER}"
db = 'bludb'
port = '30426'
protocol = 'TCPIP'
cert = 'cert.crt'

dsn = (
    "DATABASE = {0};"
    "HOSTNAME = {1};"
    "PORT = {2};"
    "UID = {3};"
    "SECURITY = SSL;"
    "SSlServerCertificate = {4};"
    "PWD = {5};"
).format(db, hostname, port, uid, cert, pwd)
print(dsn)
try:
    db2 = ibm_db.connect(dsn, " ", " ")
    print("connect to database")
except:
    print("unable to connect ", ibm_db.conn_errormsg())

