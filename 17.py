class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        def dfs(elt, next_digits):
            if len(next_digits) == 0:
                ans.append(elt)
            else:
                for letter in phone_map[next_digits[0]]:
                    dfs(elt + letter, next_digits[1:])
        ans = []
        dfs("", digits)
        return ans