from regneklynge import Regneklynge

class Datasenter:

	def __init__(self):
		datasenter = []

	## Leser inn data om en regneklynge fra fil og legger
	# den til i ordboken
	# @param filnavn filene der dataene for regneklyngen ligger
	def lesInnRegneklynge(self, filnavn):
		fil = open(filnavn , "r")
		for linjer in fil :
			for objekter in linjer:
				datasenter.append([linjer])

	def skrivUtAlleRegneklynger(self):
		Node(datasenter[1])
		print("Noder med minst 32 GB:" , )
		print("Noder med minst 64 GB:" , )
		print("Noder med minst 128 GB: " , )
		print("Antall prosessorer: " , )
		print("Antall rack: " , )

	## Skriver ut informasjon om en spesifikk regeklynge
	# @param navn navnet på regnekyngen
	def skrivUtRegneklynge(self, navn):
		pass
