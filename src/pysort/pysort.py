import math
from typing import List


def bubble_sort(sequences: List[int]):
	for i in range(len(sequences)):
		for j in range(len(sequences) - i - 1):
			if sequences[j] > sequences[j + 1]:
				sequences[j], sequences[j + 1] = sequences[j + 1], sequences[j]

	return sequences


def selection_sort(sequences: List[int]):
	for i in range(len(sequences)):
		print(sequences)
		min_idx = i

		for j in range(i + 1, len(sequences)):
			if sequences[min_idx] > sequences[j]:
				sequences[min_idx], sequences[j] = sequences[j], sequences[min_idx]

	return sequences


def quick_sort(sequences: List[int], low: int, high: int):
	if low < high:
		left = low
		right = high
		pivot = math.floor((high - low)/2)

		while True:
			pass

	return sequences
