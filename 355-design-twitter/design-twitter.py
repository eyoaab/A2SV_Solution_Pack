class Twitter:

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(deque)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].appendleft((tweetId,self.time))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        candidates = []

        followees = self.following[userId] | {userId} 


        for followee in followees:
            candidates.extend(self.tweets[followee])

        candidates.sort(key=lambda x: x[1], reverse=True)  
        return [tweetId for tweetId, _ in candidates[:10]]


        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)