"""Tests that the mouse navigation work properly."""

from __future__ import division
from __future__ import print_function

import unittest

from camera import Camera
from mouse_navigation_controller import MouseNavigationController


class TestMouseNavigationTransform(unittest.TestCase):

    def test_dragging(self):
        camera = Camera()
        camera.viewport[:] = (0, 0, 800, 600)
        camera.ortho(800, 600, -1, 1)
        c = MouseNavigationController(camera)
        c._handle_drag_event((0, 0), (400, 300))
        c._handle_drag_end_event((0, 0), (400, 300))
        self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()
