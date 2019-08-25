#!/bin/env python2.7
from OpenGL.GL import *
import numpy as np
from program import Program


class GlScene(object):

    def __init__(self, vertices):
        vbo = np.empty(1, dtype=np.uint32)
        glCreateBuffers(1, vbo)
        glNamedBufferStorage(vbo, vertices.nbytes, vertices, 0)

        vao = np.empty(1, dtype=np.uint32)
        glCreateVertexArrays(len(vao), vao)

        glVertexArrayAttribFormat(vao, 0, 2, GL_FLOAT, False, 0)
        glVertexArrayAttribBinding(vao, 0, 0)
        glEnableVertexArrayAttrib(vao, 0)
        glVertexArrayVertexBuffer(vao, 0, vbo, 0, 2*4)

        glBindVertexArray(vao)

        program = Program('shader/shader.vs', 'shader/shader.frag')
        program.use()

    @staticmethod
    def update():
        glDrawArrays(GL_QUAD_STRIP, 0, 4)
