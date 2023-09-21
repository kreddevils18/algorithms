import unittest

import pytest

from src.pysort import PySort


class TestBubbleSort:
	@pytest.mark.parametrize(
		"sequences,expected",
		[
			(
				[9, 8, 7, 6, 5],
				[5, 6, 7, 8, 9],
			),
			(
				[1, 2, 3, 4, 5],
				[1, 2, 3, 4, 5],
			),
			(
				[2, 6, 2, 4, 5],
				[2, 2, 4, 5, 6],
			)
		]
	)
	def test_pysort__ok(self, sequences, expected):
		result = PySort.bubble_sort(sequences)
		assert result == expected, "Result is unexpected"

		result = PySort.selection_sort(sequences)
		assert result == expected, "the result of selection sort is unexpected"
