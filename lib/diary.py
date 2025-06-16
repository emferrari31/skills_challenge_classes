class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.start_index = 0

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        title = self.title 
        contents = self.contents
        string = title + contents 
        word_count = len(string.split())
        return word_count
        

    def reading_time(self, wpm):
        contents = self.contents 
        result = len(contents.split()) / wpm
        return result 

    def reading_chunk(self, wpm, minutes):
        words_to_read = wpm * minutes 
        words = self.contents.split()
        start = self.start_index 
        end = start + words_to_read
        chunk = words[start:end]
        
        if end >= len(words):
            self.start_index = 0
        else: 
            self.start_index = end
        
        return " ".join(chunk)
