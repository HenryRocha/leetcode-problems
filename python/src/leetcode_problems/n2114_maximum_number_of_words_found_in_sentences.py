class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        current_max_words = 0

        for sentence in sentences:
            num_words = len(sentence.split(" "))

            if num_words > current_max_words:
                current_max_words = num_words

        return current_max_words
