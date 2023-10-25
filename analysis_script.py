import happybase

connection = happybase.Connection()


# tables names
user_table = 'mastodon-users'
post_table = 'mastodon-post'


#connection
table_user = connection.table(user_table)
table_post = connection.table(post_table)

# ps = table_user.row(row='111155878105259515',columns=['user_details:username','user_details:followers_count'])
# print(ps)

#Analysis followers count
top_n = 100
try:
    users_followers_count = {} 

    for key, data in table_user.scan(columns=[b'user_details:followers_count']):
        user_id = key
        followers_count = str(data)
        users_followers_count[user_id] = followers_count.split(":")[2].split("'")[1]
    
    sorted_users = sorted(users_followers_count.items(), key=lambda x: x[1], reverse=True)[:top_n]
    
    for i, (user_id, followers_count) in enumerate(sorted_users, start=1):
        if(int(followers_count) > 500):
            print(f"{i}. User ID: {user_id}, Followers Count: {followers_count}")
finally:
    connection.close()