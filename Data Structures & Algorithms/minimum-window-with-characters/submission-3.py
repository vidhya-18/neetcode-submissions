from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        need = Counter(t)
        have = {}

        needCount = len(need)      # Number of unique characters needed
        haveCount = 0              # Number of characters satisfied

        res = [-1, -1]
        resLen = float("inf")

        left = 0

        for right in range(len(s)):

            c = s[right]
            have[c] = have.get(c, 0) + 1

            # Check if current character requirement is satisfied
            if c in need and have[c] == need[c]:
                haveCount += 1

            # Window is valid
            while haveCount == needCount:

                # Update minimum answer
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                # Remove left character
                have[s[left]] -= 1

                if s[left] in need and have[s[left]] < need[s[left]]:
                    haveCount -= 1

                left += 1

        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""