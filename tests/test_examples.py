from sentsim import similarity


def test_similirity():
    assert 1 == similarity("this is a sentence", "this is a sentence")
    assert 1 > similarity("this is a sentence", "this is also a sentence")
    assert 0.8 < similarity("this is a sentence", "this is also a sentence")
