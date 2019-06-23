class TeamValue:
    name = None
    value = None
    rank = None

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getname(self):
        return self.name

    def getvalue(self):
        return self.value

    def getrank(self):
        return self.rank

    def setrank(self, rank):
        self.rank = rank

