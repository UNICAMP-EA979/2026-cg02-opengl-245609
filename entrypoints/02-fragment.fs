#version 330 core
// Defina a cor de saída como o valor da textura na posição da UV

in vec2 uv;

uniform sampler2D texture0;

out vec4 FragColor;

void main()
{
    FragColor = texture(texture0, uv);
}

/////////////////////////////////////////////////////////////////////////////////////////////