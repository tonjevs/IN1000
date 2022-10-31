form node import Node

class Rack:

	def __init__(self):
		self._noder = []

	def settInn(self, node):
		self._noder.append(node)

	def getAntNoder(self):
		return len(self._noder)

	## Beregner sammenlagt antall prosessorer i nodene i et rack
	# @return antall prosessorer
	def antProsessorer(self):
		antPros = 0
		for noder in self._noder:
			antPros += node.antProsessorer()
		return antPros

	## Beregner antall noder i racket med minne over gitt grense
	# @param paakrevdMinne antall GB minne som kreves
	# @return antall noder med tilstrekkelig minne
	def noderMedNokMinne(self, paakrevdMinne):
        noderMedNokMinne = 0
        self._paakrevsMinne = paakrevdMinne
        for noder in self._rack
            if nokMinne(self._paakrevsMinne):
                noderMedNokMinne += 1
        return noderMedNokMinne
