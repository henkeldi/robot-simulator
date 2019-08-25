#version 450

layout (location = 0) in vec2 position;

layout (binding=0) readonly buffer SCENE_BUFFER {
	mat4 projection;
    mat4 view;
};

void main() {
    gl_Position = projection * view * vec4(position.xy, 0.0, 1.0);
}