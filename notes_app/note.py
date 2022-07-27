class Note:

    def __init__(self, description, id):
        self.id = id
        self.description = description


    def __str__(self):
        return "(" + str(self.id) + ", " + self.description + ")"