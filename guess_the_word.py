#s is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        #
        def countMatches(word1, word2):
            match = 0
            for index, char in enumerate(word1):
                if char == word2[index]:
                    match += 1
            return match
        candidates = wordlist
        for i in range(10):
            matches = 0
            check = random.choice(candidates)
            matches = master.guess(check)            
            if matches == 6:
                return check
            new_candidates = []
            for word in candidates:
                # don't add same word
                if word != check:
                    if countMatches(check, word) == matches:
                        new_candidates.append(word)
            candidates = new_candidates
