class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}: {self.description}'

class Torch(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

class Key(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
    
class Cloak(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

class Dagger(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
