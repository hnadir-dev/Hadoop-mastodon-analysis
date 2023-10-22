import happybase
#from hdfs import InsecureClient


connection = happybase.Connection()

table_name = 'mastodon-users'  

table = connection.table(table_name)

f = open("mr_output.txt", "r")


for x in f:
    item = x.split('"')
    key = item[1]
    value = item[2].strip()

    row_key = item[1].split(':')[0]

    data = {key:value}
    table.put(row_key, data)

connection.close()


