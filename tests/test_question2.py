from answer.question2 import fizzbuzz_custom


def test_answer_fizz_buzz():
    n = 10
    rules = [(2, "Even"), (3, "Triple")]

    assert fizzbuzz_custom(n, rules) == [
        "1",
        "Even",
        "Triple",
        "Even",
        "5",
        "EvenTriple",
        "7",
        "Even",
        "Triple",
        "Even",
    ]
