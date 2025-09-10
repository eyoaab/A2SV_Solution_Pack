class Solution:
    def minimumTeachings(self, totalLanguages, userLanguages, friendships):
        store = set()

        for user1, user2 in friendships:
            user1 -= 1  
            user2 -= 1
            can_communicate = False

            for lang1 in userLanguages[user1]:
                if lang1 in userLanguages[user2]:
                    can_communicate = True
                    break

            if not can_communicate:
                store.add(user1)
                store.add(user2)

        ans = len(userLanguages) + 1

        for language in range(1, totalLanguages + 1):
            count = 0
            for user in store:
                if language not in userLanguages[user]:
                    count += 1
            ans = min(ans, count)

        return ans