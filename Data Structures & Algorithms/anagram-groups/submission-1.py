from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Map sorted_string -> list of original strings
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the string to use as a canonical key
            # e.g., "pots" -> tuple('o', 'p', 's', 't')
            sorted_key = tuple(sorted(s))
            
            # Group strings with the same sorted key
            anagram_map[sorted_key].append(s)
            
        # Return all the grouped lists
        return list(anagram_map.values())