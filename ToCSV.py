from eca import *
import exe_sql as sql

def getcsv():

    sql.begin()     #starts a connection to the database
    result = sql.cur.execute('SELECT persons.name, orders.total, orders.date, orders.oid FROM persons, orders where orders.pid=persons.pid')        #selects all data from the orders table
    data = result.fetchall()
    csv_data = ''
    for item in [data]:
        z = len(item) - 1
        while z >= 0:
            csv_data += '{},{},{},{}\r\n'.format(data[z][0], data[z][1], data[z][2], data[z][3])
            z -= 1
    filename = 'Order_list.csv'
    path = 'template_static/csv/{}'.format(filename)
    csv_out = open(path, 'w')
    csv_out.write('Name, Total, date, OrderID \n')
    csv_out.write(csv_data)     #fills the csv file with csv_data from the orders table
    csv_out.close()             #closes the csv file
    sql.end()                   #ends the database connection
    emit('csv', {'data': filename})

def getSQLDump():
    sql.begin()
    filename = 'dump.sql'
    path = 'template_static/sql/{}'.format(filename)
    sql_out = open(path, 'w')
    with sql_out:
        for line in sql.con.iterdump():
            sql_out.write('%s\n' % line)
    sql.end()
    emit('sql',{'data': filename })