#version 330 core

// Utilize como base o 01-vertex.vs
// Recebe a cor do vértice na location=2, envie como saída para o fragment

layout(location = 0) in vec3 position;
layout(location = 2) in vec3 vertexColor;

out vec3 color;

uniform mat4 modelTransformation;
uniform mat4 viewTransformation;
uniform mat4 projectionMatrix;

void main()
{
    gl_Position = projectionMatrix * viewTransformation * modelTransformation * vec4(position, 1.0);
    color = vertexColor;
}