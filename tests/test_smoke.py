"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import querypulse


def test_version_is_set() -> None:
    assert querypulse.__version__
