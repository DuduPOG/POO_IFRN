import json

class Categoria:

    def __init__(self, id, desc):
        self.id = id
        self.desc = desc


    def __str__(self):
        return f"{self.id} - {self.desc}"