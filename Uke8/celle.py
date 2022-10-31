class Celle:

    def __init__(self):
        self._cellestatus = "doed"

    def settDoed(self):
        self._cellestatus = "doed"

    def settLevende(self):
        self._cellestatus = "levende"

    def erLevende(self):
        if self._cellestatus == "levende":
            return True
        return False

    def hentStatusTegn(self):
        if self.erLevende(): #om cella er levende lager den ei celle i form av "O"
            return "O"
        return "."
