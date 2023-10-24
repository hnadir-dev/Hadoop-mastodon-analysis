import happybase

class InsertHbase:

    def insertDataInHbase():
        connection = happybase.Connection()

        #table_name = 'mastodon-users'

        # tables names
        user_table = 'mastodon-users'
        post_table = 'mastodon-post'

        #table = connection.table(table_name)

        # get the tables exists.
        table_list = [t.decode('utf-8') for t in connection.tables()]

        # create the table if not exist (user table)
        if user_table not in table_list :
            connection.create_table(
                user_table,
                {
                    'user_details':dict()
                }
            )

        # create the table if not exist (post table)
        if post_table not in table_list :
            connection.create_table(
                post_table,
                {
                    'post_details':dict()
                }
            )

        # make connection to tables
        table_user = connection.table(user_table)
        table_post = connection.table(post_table)


        f = open("./airflow/dags/mr_output.txt", "r")


        # insert into the tables
        #"created_at:107711385842384086"	1643068800000
        for x in f:
            # get line from the content the text file splited by "
            item = x.split('"')
            # get the column name from the line
            column = item[1].split(':')[0]
            # get the row key from the line
            row_key = item[1].split(':')[1]
            # get the value from the line
            values = item[1].split(':')[0]

            if  values == 'following_count' or values == 'followers_count' or values == 'status_count' or values == 'engagement' or values == 'created_at':
                table_user.put(row_key, {"user_details:" + column:item[2].strip()})
            elif values =='username' or values == 'url':
                table_user.put(row_key, {"user_details:" + column:item[3].strip()})
            elif values =='language' or values == 'tag' or values == 'visibility':
                table_post.put(row_key, {"post_details:" + column:item[3].strip()})
            elif values == 'media' or values == 'favourites_count' or values == 'reblogs_count':
                table_post.put(row_key, {"post_details:" + column:item[2].strip()})

        connection.close()
        f.close()

#insertDataInHbase()