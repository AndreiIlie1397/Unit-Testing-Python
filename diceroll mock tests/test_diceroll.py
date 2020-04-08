from diceroll import added_roll
from unittest import mock


@mock.patch("diceroll.randint", return_value=5, autospec = True)
def test_added_roll(mock_randint):
    assert added_roll(2) == 6
    mock_randint.assert_called_once_with(1, 6)
