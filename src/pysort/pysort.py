from typing import List


class PySort:
	@staticmethod
	def bubble_sort(sequences: List[int]):
		for i in range(len(sequences)):
			for j in range(len(sequences) - i - 1):
				if sequences[j] > sequences[j + 1]:
					sequences[j], sequences[j + 1] = sequences[j + 1], sequences[j]

		return sequences
