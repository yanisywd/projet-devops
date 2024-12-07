from methode_tristan_choquet import methode1tchoquet, methode2tchoquet

def test_methode1tchoquet():
    assert methode1tchoquet(1, 2, 3) == (2.0, 6, 6, -4, 1.0, 1, 1, 1.0, -1)
    assert methode1tchoquet(4, 5, 6) == (5.0, 15, 120, -7, 2.0, 16, 64, 0.25, -4)
    assert methode1tchoquet(169, 2, 2)[4] == 13

    try:
        methode1tchoquet(-1, 2, 3)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"
    try:
        methode1tchoquet(0, 2, 3)
    except ZeroDivisionError:
        pass
    else:
        assert False, "Expected ZeroDivisionError"

    try:
        methode1tchoquet("a", "b", "c")
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError"

    print("Methode 1 OK")


def test_methode2tchoquet():
    assert methode2tchoquet("texte1", "texte2") == (6, 6, "texte1texte2", "texte1texte1texte1texte2texte2", ['t', 'e', 'x', 't', 'e', '1'], ['t', 'e', 'x', 't', 'e', '2'], ['texte1'], ['texte2'], ['texte1'], ['texte2'], ['texte1'], ['texte2'])
    assert methode2tchoquet("texte3", "texte4") == (6, 6, "texte3texte4", "texte3texte3texte3texte4texte4", ['t', 'e', 'x', 't', 'e', '3'], ['t', 'e', 'x', 't', 'e', '4'], ['texte3'], ['texte4'], ['texte3'], ['texte4'], ['texte3'], ['texte4'])
    
    try:
        methode2tchoquet("", "")
    except AssertionError:
        pass
    else:
        assert False, "Expected AssertionError"
    try:
        methode2tchoquet(0, "texte2")
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError"

    try:
        methode2tchoquet("texte1", 1)
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError"

    try:
        methode2tchoquet([1, 2, 3], "texte2")
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError"

    print("Methode 2 OK")

test_methode1tchoquet()
test_methode2tchoquet()