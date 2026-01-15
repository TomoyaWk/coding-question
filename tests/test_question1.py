from anwer.question1 import diff_config


def test_diff_config_basic():
    old = {"host": "localhost", "port": 5432, "debug": False}
    new = {"host": "localhost", "port": 5433, "debug": True, "timeout": 30}

    assert diff_config(old, new) == {
        "added": {"timeout": 30},
        "removed": {},
        "changed": {
            "port": {"before": 5432, "after": 5433},
            "debug": {"before": False, "after": True},
        },
    }


def test_diff_config_no_changes():
    old = {"a": 1, "b": 2}
    new = {"a": 1, "b": 2}

    assert diff_config(old, new) == {"added": {}, "removed": {}, "changed": {}}


def test_diff_config_removed_only():
    old = {"a": 1, "b": 2}
    new = {"a": 1}

    assert diff_config(old, new) == {"added": {}, "removed": {"b": 2}, "changed": {}}


def test_diff_config_added_only():
    old = {"a": 1}
    new = {"a": 1, "b": 2}

    assert diff_config(old, new) == {"added": {"b": 2}, "removed": {}, "changed": {}}


def test_diff_config_changed_only():
    old = {"a": 1, "b": 2}
    new = {"a": 1, "b": 3}

    assert diff_config(old, new) == {
        "added": {},
        "removed": {},
        "changed": {"b": {"before": 2, "after": 3}},
    }
