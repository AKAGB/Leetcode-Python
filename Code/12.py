class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        special = {4: 'IV', 9: 'IX', 40: 'XL', 
                    90: 'XC', 400: 'CD', 900: 'CM'}