#!/bin/env python3
from OpenGL.GL import *
import numpy as np


class GlCamera(object):

    def __init__(self, camera):
        self._camera = camera
        self._scene_buffer = np.empty(1, dtype=np.uint32)
        glCreateBuffers(1, self._scene_buffer)
        glNamedBufferStorage(self._scene_buffer[0],
                             self._camera.data.nbytes,
                             self._camera.data,
                             GL_DYNAMIC_STORAGE_BIT |
                             GL_MAP_WRITE_BIT |
                             GL_MAP_PERSISTENT_BIT)
        glBindBufferRange(GL_SHADER_STORAGE_BUFFER,
                          0,
                          self._scene_buffer[0],
                          0,
                          self._camera.data.nbytes)

    def update(self):
        c = self._camera.clear_color
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(c[0], c[1], c[2], c[3])
        glViewportArrayv(0, 1, self._camera.viewport)
        if self._camera.changed:
            glNamedBufferSubData(self._scene_buffer[0], 0,
                                 self._camera.data.nbytes,
                                 self._camera.data)
            self._camera.changed = False
