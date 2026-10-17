import pytest

from inventory import Inventory


def test_add():
    inv = Inventory()
    inv.add("меч")
    inv.add("зелье", 3)
    inv.add("зелье", 2)
    assert inv.count("меч") == 1
    assert inv.count("зелье") == 5
    assert inv.count("щит") == 0
    assert inv.total() == 6


def test_add_wrong_count():
    inv = Inventory()
    with pytest.raises(ValueError):
        inv.add("меч", 0)
    with pytest.raises(ValueError):
        inv.add("меч", -2)


def test_remove():
    inv = Inventory()
    inv.add("зелье", 4)
    inv.remove("зелье", 3)
    assert inv.count("зелье") == 1
    inv.remove("зелье")
    assert inv.count("зелье") == 0
    assert "зелье" not in inv.to_dict()


def test_remove_errors():
    inv = Inventory()
    inv.add("меч", 1)
    with pytest.raises(ValueError):
        inv.remove("щит")
    with pytest.raises(ValueError):
        inv.remove("меч", 2)
    assert inv.count("меч") == 1


def test_save_and_load(tmp_path):
    inv = Inventory()
    inv.add("меч", 1)
    inv.add("зелье", 7)
    path = tmp_path / "inventory.json"
    inv.save(path)
    loaded = Inventory.load(path)
    assert loaded.to_dict() == {"меч": 1, "зелье": 7}
    assert loaded.total() == 8


def test_to_dict_is_copy():
    inv = Inventory()
    inv.add("меч", 1)
    copy = inv.to_dict()
    copy["меч"] = 100
    assert inv.count("меч") == 1
