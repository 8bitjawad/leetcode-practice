class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []

        for c in s:
            if c.isalnum():
                chars.append(c.lower())

        new_str = "".join(chars)

        n = len(new_str)
        front, back = 0, n-1

        while front <= back:
            if new_str[front] != new_str[back]:
                return False
            front += 1
            back -= 1

        return True


        