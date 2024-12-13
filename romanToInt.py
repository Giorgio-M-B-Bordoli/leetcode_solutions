my_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

class Solution:
    def romanToInt(self, s: str) -> int:
        # Base case
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return my_dict[s[-1]]
        
        # Compare the last numeral with the second-to-last
        if my_dict[s[-1]] > my_dict[s[-2]]:
            # Subtraction case
            return self.romanToInt(s[:-2]) + my_dict[s[-1]] - my_dict[s[-2]]
        else:
            # Addition case
            return self.romanToInt(s[:-1]) + my_dict[s[-1]]
