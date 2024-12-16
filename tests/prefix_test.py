import pytest
from prefix import prefix_to_infix


class TestPrefixToInfix:

    def test_simple_expressions(self):
        assert prefix_to_infix("+ - 13 4 55") == "((13 - 4) + 55)"
        assert prefix_to_infix("+ 2 * 2 - 2 1") == "(2 + (2 * (2 - 1)))"
        assert prefix_to_infix("+ + 10 20 30") == "((10 + 20) + 30)"
        assert prefix_to_infix("- - 1 2") == "((1 - 2))"
        assert prefix_to_infix("/ + 3 10 * + 2 3 - 3 5") == "((3 + 10) / ((2 + 3) * (3 - 5)))"

    def test_empty_expression(self):
        assert prefix_to_infix("") == ""

    def test_invalid_expression(self):
        with pytest.raises(IndexError):
            prefix_to_infix("+ -")