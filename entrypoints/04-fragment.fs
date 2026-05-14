#version 330 core

// Receba a cor do vértice interpolada e coloque como cor do fragmento
// 
// Observe que a cor do vértice é um vec3 e a cor de saída precisa ser um vec4:
// variávelVec4 = vec4(variávelVec3, 1);

out vec4 FragColor;

in vec3 color;

void main()
{
    FragColor = vec4(color, 1);
}