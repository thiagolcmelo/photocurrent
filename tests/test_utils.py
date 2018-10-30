#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

import numpy as np

from core.utils import *


class TestUtils(unittest.TestCase):

    def test_solve_eigenproblem(self):
        vals_a = [0.73518446+3.65875149j, 9.66481554+2.84124851j]
        vecs_a = [
                    [0.96175086, -0.24955936+0.11293984j],
                    [0.38403898-0.10488583j, 0.91734019]
                ]
        H = [[1.5+3j,3.4-1j],[2.1-1j,8.9+3.5j]]
        vals_n, vecs_n = solve_eigenproblem(H)

        for vn, va in zip(vals_n, vals_a):
            self.assertAlmostEqual(vn, va, places=7,
                msg="Bad precision in eigenvalue")
        
        for vn, va in zip(vecs_n, vecs_a):
            np.testing.assert_almost_equal(vn, va, decimal=7,
                err_msg="Bad precision in eigenvector")


if __name__ == '__main__':
    unittest.main()
