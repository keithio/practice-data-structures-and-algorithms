class FindAnagrams:

    def __init__(self, dictionary, challenge):
        self.dictionary = dictionary
        self.challenge = challenge
        self.anagrams = []
        self.map = {}
        self.create_map()
        self.get_anagrams()

    def __call__(self):
        return self.anagrams

    def create_map(self):
        """
        Presort words from dictionary to create mapping between sorted
        characters and possible words.
        """
        for word in self.dictionary:
            sorted_word = ''.join(sorted(word))
            if sorted_word in self.map:
                self.map[sorted_word].append(word)
            else:
                self.map[sorted_word] = [word]

    def get_anagrams(self):
        """
        Returns the possible anagrams for the provided values.
        """
        self.anagrams = self.map[''.join(sorted(self.challenge))]
