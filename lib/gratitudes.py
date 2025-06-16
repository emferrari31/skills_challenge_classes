class Gratitudes:

    def __init__(self):
        self.gratitudes = []

    def add(self, gratitude):
        self.gratitudes.append(gratitude)

    def format(self):
        gratitudes_string = ""
        for gratitude in self.gratitudes[:-1]: 
            gratitudes_string += gratitude + ", "
        gratitudes_string += f"and {self.gratitudes[-1]}"
        return f"I am grateful for: {gratitudes_string}."
