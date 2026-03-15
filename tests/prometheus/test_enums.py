from chronopolis.prometheus.enums import Direction


def test_should_return_lowercase_choices_when_using_choices_method():
    assert Direction.INCOME.value == "income"
    assert Direction.OUTCOME.value == "outcome"
