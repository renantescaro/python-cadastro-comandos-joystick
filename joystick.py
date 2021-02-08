import pygame

class Joystick:
    def __init__(self):
        self.analogico_esquerdo_x = 0.0
        self.analogico_esquerdo_y = 0.0
        self.analogico_direito_x  = 0.0
        self.analogico_direito_y  = 0.0
        self.botao[0, 1, 2, 3, 4, 5] = False

        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.joystick.init()

        # número do joystick plugado
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()


    def verificar_comandos(self):
        self._verificar_botoes()
        self._verificar_analogicos()
        

    def _verificar_botoes(self):
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for b in self.botao:
                    if self.joystick.get_button(0):
                        self.botao[b] = True

            elif event.type == pygame.JOYBUTTONUP:
                for b in self.botao:
                    if int(event.button) == 0:
                        self.botao[b] = False


    def _verificar_analogicos(self):
        # direção esquerda / direita
        self.analogico_esquerdo_x = self.joystick.get_axis(0)
        self.analogico_esquerdo_y = self.joystick.get_axis(1)

        # camera
        self.analogico_direito_x  = self.joystick.get_axis(3)
        self.analogico_direito_y  = self.joystick.get_axis(4)

        self.clock.tick(20)


    def get_botao_pressionado(self):
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for n in range(15):
                   if self.joystick.get_button(n):
                       return n, 'botao'
        
        for a in range(6):
            valor_analogico = self.joystick.get_axis(a)
            if (valor_analogico > 0.4 or valor_analogico < -0.4) and valor_analogico != -1:
                print(valor_analogico)
                return a, 'analogico'

        return -1, ''