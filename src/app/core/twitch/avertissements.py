class Compteur:
    def __init__(self, avertissementList: dict[str, int] = {}) -> None:
        self.avertissementList = avertissementList

    def add(self, newAvertissent: str):
        if newAvertissent in self.avertissementList.keys():
            value = self.avertissementList[newAvertissent]
            self.avertissementList[newAvertissent] = value + 1
        else:
            self.avertissementList[newAvertissent] = 1
