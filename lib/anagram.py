 # lib/anagram.py
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, possible_anagrams):
        return [
            candidate for candidate in possible_anagrams
            if self._is_anagram(candidate)
        ]

    def _is_anagram(self, candidate):
        candidate_lower = candidate.lower()
        return (
            candidate_lower != self.word and
            sorted(candidate_lower) == sorted(self.word)
        )