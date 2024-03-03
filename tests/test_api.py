# -*- coding: utf-8 -*-

from learn_pyside6 import api


def test():
    _ = api


if __name__ == "__main__":
    from learn_pyside6.tests import run_cov_test

    run_cov_test(__file__, "learn_pyside6.api", preview=False)
