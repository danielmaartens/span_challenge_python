class TeamValue:
    name = None
    value = None
    rank = None

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getname(self):
        return self.name

    def setvalue(self, value):
        self.value = value

    def getvalue(self):
        return self.value

    def setrank(self, rank):
        self.rank = rank

    def getrank(self):
        return self.rank



