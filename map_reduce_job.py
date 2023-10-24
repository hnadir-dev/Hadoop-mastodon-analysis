
from mrjob.job import MRJob
from mrjob.step import MRStep
import json

class UserMastodonAnalytics(MRJob):

    def mapper(self, key, line):
        data = json.loads(line)
        
        for item in data:
            username = item.get('account').get('username')
            account_id = item.get('account').get('id')
            account_created_at = item.get('account').get('created_at')
            account_url = item.get('account').get('url')
            account_followers_count = item.get('account').get('followers_count')
            account_following_count = item.get('account').get('following_count')
            account_status_count = item.get('account').get('statuses_count')
            post_id = item.get('id')
            post_favourites_count = item.get('favourites_count')
            post_reblogs_count = item.get('reblogs_count')
            post_visibility = item.get('visibility')
            post_media = item.get('media_attachments')
            language = item.get('language')
            post_tags = item.get('tags')
            
            engagemnet = (post_favourites_count + post_reblogs_count) / account_followers_count  if post_favourites_count > 0 & post_reblogs_count > 0  else 0

            # User data
            yield "username:"+str(account_id), username
            yield "created_at:"+str(account_id), account_created_at
            yield "followers_count:"+str(account_id), account_followers_count
            yield "following_count:"+str(account_id), account_following_count
            yield "status_count:"+str(account_id), account_status_count
            yield "engagemnet:"+str(account_id), engagemnet
            if len(account_url) > 1:
                yield "url:"+str(account_id), account_url
            else:
                yield "url:"+str(account_id), "NoUrl"
            

            # Post data
            yield "favourites_count:"+str(post_id), post_favourites_count
            yield "reblogs_count:"+str(post_id), post_reblogs_count
            yield "visibility:"+str(post_id), post_visibility
            yield "media:"+str(post_id), 1 if len(post_media) > 0 else 0
            if language:
                yield "language:"+str(post_id), language
            else:
                yield "language:"+str(post_id), "NoLang"
            # if tgs exist:
            for tag in post_tags:
                yield "tag:"+str(post_id), tag.get("name")

            

            
    #def combiner(self, key, values):
    #   yield key, max(values)

    def reducer(self, key, values):
        yield key,max(values)


    # def reducer_sorter(self, key, values):
    #     for count, key in sorted(values, reverse=True):
    #         yield count, key

    def steps(self):
        return [
            MRStep(
                mapper=self.mapper,
                reducer=self.reducer
            )
        ]

        
if __name__ == '__main__':
    UserMastodonAnalytics.run()