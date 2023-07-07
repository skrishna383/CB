class Solution:
    def isPalindrome(self, s: str) -> bool:
        striped=''.join([i for i in s if i.isalnum()])
        if striped.lower() == striped.lower()[::-1]:
            return True
        else :return False