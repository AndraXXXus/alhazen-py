import unittest

from sklearn.tree import DecisionTreeClassifier

from alhazen import Alhazen
from alhazen_formalizations.calculator import grammar, initial_inputs, prop


class TestAlhazen(unittest.TestCase):
    def test_initialization(self):
        alhazen = Alhazen(
            initial_inputs=initial_inputs,
            grammar=grammar,
            evaluation_function=prop,
        )
        result = alhazen.run()

        self.assertEqual(len(result), 10)
        self.assertTrue(all([isinstance(tree, DecisionTreeClassifier) for tree in result]))


if __name__ == '__main__':
    unittest.main()
