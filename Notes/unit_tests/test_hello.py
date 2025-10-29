from hello import hello

def test_default():
    assert hello("Stephen") == "hello, Stephen"

def test_argument():
    for name in ["Stephen", "Daisy", "Edwin"]:
        assert hello(name) == f"hello, {name}"



