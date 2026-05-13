class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_strings = sorted(s)
        sorted_string_2 = sorted(t)
        if len(sorted_strings) != len(sorted_string_2):
            return False
        for i in range(len(sorted_strings)):
            if sorted_strings[i] != sorted_string_2[i]:
                return False
        return True
