# morning algos
# neetcode Design Twitter

import heapq


class Twitter:

    def __init__(self):
        self.counter = 0
        self.tweets = []
        self.follower_map = {}

    def postTweet(self, userId, tweetId):
        self.tweets.append([self.counter, userId, tweetId])
        self.counter += 1

    def getNewsFeed(self, userId):
        if userId in self.follower_map:
            usersToSearch = self.follower_map[userId]
        else:
            usersToSearch = []
        usersToSearch.append(userId)
        feed = []
        for tweet in self.tweets:
            if tweet[1] in usersToSearch:
                feed.append([-tweet[0], tweet[2]])
        heapq.heapify(feed)
        res = []
        while len(res) < 10 and feed:
            counter, tweetId = heapq.heappop(feed)
            res.append(tweetId)
        return res

    def follow(self, followerId, followeeId):
        if followerId not in self.follower_map:
            self.follower_map[followerId] = [followeeId]
        else:
            self.follower_map[followerId].append(followeeId)

    def unfollow(self, followerId, followeeId):
        if followerId in self.follower_map:
            if followeeId in self.follower_map[followerId]:
                self.follower_map[followerId].remove(followeeId)
