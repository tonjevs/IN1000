from rack import Rack

class Regneklynge:

	def __init__(self, noderPerRack):
		self._noderperRack = noderPerRack

	## Plasserer en node inn i et rack med ledig plass, eller i et nytt
	# @param node referanse til noden som skal settes inn i datastrukturen
	def settInnNode(self, node):
        self._node = node
        max = getAntNoder()
        if max < self._noderperRack :
            settInn(self._node)
        else :
            pass

	def antProsessorer(self):
		return len(antProsessorer())

	## Beregner antall noder i regneklyngen med minne over angitt grense
	# @param paakrevdMinne hvor mye minne skal noder som telles med ha
	# @return antall noder med tilstrekkelig minne
	def noderMedNokMinne(self, paakrevdMinne):
		self._paakrevsMinne = paakrevdMinne
        minne = noderMedNokMinne(paakrevdMinne)
        return minne

	## Henter antall racks i regneklyngen
	# @return antall racks
	def antRacks(self):
		return getAntNoder()
