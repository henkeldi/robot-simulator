"""Tests that the camera transforms work properly."""

from __future__ import division
from __future__ import print_function

import unittest

import numpy as np

from camera import Camera


def assert_allclose(actual, desired, rtol=1e-6, atol=1e-6):
    np.testing.assert_allclose(actual, desired,
                               rtol=1e-6,
                               atol=1e-6)


class TestCameraTransform(unittest.TestCase):

    @staticmethod
    def test_viewport_ncd():
        camera = Camera()
        x0 = 10
        y0 = 20
        w = 30
        h = 40
        n = 50
        f = 60
        camera.viewport = [x0, y0, w, h]
        camera.ortho(w, h, n, f)

        viewport_pts = np.array([[x0, y0, 0, 1],
                                 [x0+w, y0, 0, 1],
                                 [x0+w, y0+h, 0, 1],
                                 [x0, y0+h, 0, 1]], np.float32)
        ncd_pts = np.array([[-1, -1, 0, 1],
                            [1, -1, 0, 1],
                            [1, 1, 0, 1],
                            [-1, 1, 0, 1]], np.float32)

        T = camera.transform('viewport', 'ncd')
        for desired, x in zip(ncd_pts, viewport_pts):
            actual = T.dot(x)
            assert_allclose(actual, desired)

        T = camera.transform('ncd', 'viewport')
        for desired, x in zip(viewport_pts, ncd_pts):
            actual = T.dot(x)
            assert_allclose(actual, desired)

    @staticmethod
    def test_screen_ncd():
        camera = Camera()
        x0 = 10
        y0 = 20
        w = 30
        h = 40
        n = 50
        f = 60
        camera.viewport = [x0, y0, w, h]
        camera.ortho(w, h, n, f)

        screen_pts = np.array([[0, h, 0, 1],
                               [w, h, 0, 1],
                               [w, 0, 0, 1],
                               [0, 0, 0, 1]], np.float32)
        ncd_pts = np.array([[-1, -1, 0, 1],
                            [1, -1, 0, 1],
                            [1, 1, 0, 1],
                            [-1, 1, 0, 1]], np.float32)

        T = camera.transform('screen', 'ncd')
        for desired, x in zip(ncd_pts, screen_pts):
            actual = T.dot(x)
            assert_allclose(actual, desired)

        T = camera.transform('ncd', 'screen')
        for desired, x in zip(screen_pts, ncd_pts):
            actual = T.dot(x)
            assert_allclose(actual, desired)

    @staticmethod
    def test_ncd_projection():
        camera = Camera()
        x0 = 10
        y0 = 20
        w = 30
        h = 40
        n = 50
        f = 60
        camera.viewport = [x0, y0, w, h]
        camera.ortho(w, h, n, f)

        ncd_pts = np.array([[-1, -1, 0, 1],
                            [1, -1, 0, 1],
                            [1, 1, 0, 1],
                            [-1, 1, 0, 1]], np.float32)

        projection_pts = np.array([[-w/2, -h/2, n+(f-n)/2, 1],
                                   [w/2, -h/2, n+(f-n)/2, 1],
                                   [w/2, h/2, n+(f-n)/2, 1],
                                   [-w/2, h/2, n+(f-n)/2, 1]], np.float32)

        T = camera.transform('ncd', 'projection')
        for desired, x in zip(projection_pts, ncd_pts):
            actual = T.dot(x)
            assert_allclose(actual, desired)

        T = camera.transform('projection', 'ncd')
        for desired, x in zip(ncd_pts, projection_pts):
            actual = T.dot(x)
            assert_allclose(actual, desired)


if __name__ == "__main__":
    unittest.main()
