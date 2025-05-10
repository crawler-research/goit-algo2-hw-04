from pygtrie import Trie

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not strings:
            return ""
        if not all(isinstance(s, str) for s in strings):
            return ""
        
        prefix = strings[0]
        
        for string in strings[1:]:
            i = 0
            while i < min(len(prefix), len(string)) and prefix[i] == string[i]:
                i += 1
            
            prefix = prefix[:i]
            
            if not prefix:
                return ""
        
        return prefix

if __name__ == "__main__":
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""
    print("nice !!!!!!")