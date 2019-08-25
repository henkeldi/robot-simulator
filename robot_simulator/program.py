from OpenGL.GL import *


class Program(object):

    shader_type_lookup = {
        'vs': GL_VERTEX_SHADER,
        'frag': GL_FRAGMENT_SHADER
    }

    def __init__(self, *shader_files):
        self._program = glCreateProgram()
        shaders = []
        for file in shader_files:
            shaders.append(self._attach(file))
        glLinkProgram(self._program)
        if not glGetProgramiv(self._program, GL_LINK_STATUS):
            print(glGetProgramInfoLog(self._program))
        else:
            print('Successfully linked')
        for shader in shaders:
            glDeleteShader(shader)

    def _attach(self, shader_file):
        ''' Attach shader '''
        print('Compiling shader ({})'.format(shader_file))
        dot_idx = shader_file.rindex('.') + 1
        shader_file_suffix = shader_file[dot_idx:]
        shader_type = Program\
            .shader_type_lookup[shader_file_suffix]

        shader = glCreateShader(shader_type)

        with open(shader_file, 'r') as f:
            shader_code = f.read()
            glShaderSource(shader, shader_code)

        glCompileShader(shader)
        if not glGetShaderiv(shader, GL_COMPILE_STATUS):
            print(glGetShaderInfoLog(shader))
        else:
            print("Shader compiled successfully ({})"
                  .format(shader_file))
        glAttachShader(self._program, shader)
        return shader

    def use(self):
        glUseProgram(self._program)
