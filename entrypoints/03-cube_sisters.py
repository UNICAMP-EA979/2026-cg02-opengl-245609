
import glfw
import numpy as np
import urenderer

# Renderize dois cubos. Ambos devem utilizar o mesmo mesh e material, mas em posições diferentes.
#
# Após 1 ENTER, o segundo cubo deve alternar a textura.
#
# Isso demonstra o reúso de dados para renderização

if __name__ == "__main__":
    urenderer.utils.clear_workdir("03-cube_sisters")
    renderer = urenderer.renderer.OpenGLRenderer(1920, 1080)
    runtime = urenderer.application.Runtime(renderer, name="03-cube_sisters")

    shader = urenderer.renderer.Shader("02-vertex.vs", "02-fragment.fs")
    material = urenderer.renderer.opengl.Material(shader)

    ## SEU CÓDIGO AQUI ######################################################
    # Crie 2 cubos, ambos com mesmo material e textura "textures/baboon.png",
    # em posições diferentes

    #########################################################################

    runtime.iter(capture=True)

    # Espera por 1 ENTER
    while glfw.get_key(renderer._window, glfw.KEY_ENTER) != glfw.PRESS:
        glfw.poll_events()
    while glfw.get_key(renderer._window, glfw.KEY_ENTER) == glfw.PRESS:
        glfw.poll_events()

    ## SEU CÓDIGO AQUI ######################################################
    # Crie um novo material com a textura "textures/monalisa.png" e utilize-o
    # no segundo cubo. Utilize o mesmo shader do primeiro material

    #########################################################################

    runtime.iter(capture=True)

    # Espera por 1 ENTER
    while glfw.get_key(renderer._window, glfw.KEY_ENTER) != glfw.PRESS:
        glfw.poll_events()
