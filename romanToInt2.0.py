# this program solves the problem of transalting roman numbers to 
# arabic one sin a more efficicient and faster way than recursion

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
        total = 0
        for i in range(len(s)-1):
            if my_dict[s[i]] >= my_dict[s[i + 1]]:
                total += my_dict[s[i]]
            else:
                total -= my_dict[s[i]]
        total += my_dict[s[-1]]
        return total
        
             