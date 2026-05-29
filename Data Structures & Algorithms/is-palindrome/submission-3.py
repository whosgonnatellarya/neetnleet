class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filter out spaces/punctuation and lowercase everything
        cleaned = "".join(char.lower() for char in s if char.isalnum())
        
        # Check if it equals its reverse
        return cleaned == cleaned[::-1]