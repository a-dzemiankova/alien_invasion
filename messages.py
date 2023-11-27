import pygame.font


class Message:
    def __init__(self, ai_game, msg, play_button):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.play_button = ai_game.play_button

        self.text_color = (30, 30, 30)
        self.font = pygame.font.Font(self.settings.font, 40)
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True,
                                      (245, 0, 0))

        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.midtop = self.ai_game.play_button.msg_image_rect.midbottom
        self.msg_image_rect.y = self.msg_image_rect.y - 100

    def show_message(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)
