from mrjob.job import MRJob
from mrjob.step import MRStep
import json


class UserMastodonAnalytics(MRJob):
        
    def mapper(self, key, line):
        
        data = json.loads(line)
        
        for item in data:
            username = item.get('account').get('username')
            followers_count = item.get('account').get('followers_count')
            favourites_count = item.get('favourites_count')
            reblogs_count = item.get('reblogs_count')
            
            tags = item.get('account').get('tags')
            emojis = item.get('account').get('emojis')

            engagemnet = (favourites_count+reblogs_count) / followers_count  if favourites_count+reblogs_count > 0 else 0

            yield 'followers:'+username,followers_count
            yield f"engagement:{username}",engagemnet

            #yield f"tags:{tags.get('')}",
        
        
    # def combiner(self, key, values):
    #     yield key, max(values)

    def reducer(self, key, values):
    
        yield key.replace('"','0'), max(values)


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