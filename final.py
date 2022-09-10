from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
import random
from  kivy.lang import Builder


class Welcome(Screen):
    pass


class MainPage(Screen):
    pass


class B1(Screen):
    pass


class B11(Screen):
    s_w_g = ObjectProperty(None, allowone=True)
    lst = ['r', 'p', 's']
    _random = random.choice(lst)
    game_over = False
    chance = 10
    you_win = 0
    computer_win = 0
    chance_show = StringProperty("CHANCE LEFT : " + str(chance))
    you_win_show = StringProperty("YOU WIN : " + str(you_win))
    computer_win_show = StringProperty("C WIN : " + str(computer_win))
    text_show_str = StringProperty("LET's START THE GAME !!!!")

    def on_value(self, screen):
        if not self.game_over:
            if self.s_w_g == self._random :
                self.chance = self.chance
                self.you_win = self.you_win
                self.computer_win = self.computer_win
                self.text_show_str = "MATCH DRAW " + "\n" + "GUESS AGAIN"
                self.chance_show = "CHANCE LEFT :" + str(self.chance)
                self.you_win_show = "YOU WIN : " + str(self.you_win)
                self.computer_win_show = "C WIN : " + str(self.computer_win)
                self._random = random.choice(self.lst)
            elif self.s_w_g == "r" and self._random == "p":
                if self.chance != 0:
                    self.chance -= 1
                    self.you_win = self.you_win
                    self.computer_win += 1
                    self.text_show_str = "OHH! NOOO! " + "\n" + "COUMPUTER WIN "
                    self.chance_show = "CHANCE LEFT :" + str(self.chance)
                    self.you_win_show = "YOU WIN : " + str(self.you_win)
                    self.computer_win_show = "C WIN : " + str(self.computer_win)
                    self._random = random.choice(self.lst)
                else:
                    self.game_over = True
                    self.text_show_str = "OHH! NOOO! " + "\n" + "GAME OVER " + "\n" + "YOUR POINT IS : " + str(self.you_win) + "\n" + "COMPUTER POINT IS : "  + str(self.computer_win)
            elif self.s_w_g == "r" and self._random == "s":
                if self.chance != 0 :
                    self.chance -= 1
                    self.you_win += 1
                    self.computer_win = self.computer_win
                    self.text_show_str = "WOW!!!!" + "\n" + "YOU WIN "
                    self.chance_show = "CHANCE LEFT :" + str(self.chance)
                    self.you_win_show = "YOU WIN : " + str(self.you_win)
                    self.computer_win_show = "C WIN : " + str(self.computer_win)
                    self._random = random.choice(self.lst)
                else:
                    self.game_over = True
                    self.text_show_str = "OHH! NOOO! " + "\n" + "GAME OVER " + "\n" + "YOUR POINT IS : " + str(self.you_win) + "\n" + "COMPUTER POINT IS : "  + str(self.computer_win)

            elif self.s_w_g == "p" and self._random == "r" :
                if self.chance != 0 :
                    self.chance -= 1
                    self.you_win += 1
                    self.computer_win = self.computer_win
                    self.text_show_str = "WOW!!!!" + "\n" + "YOU WIN "
                    self.chance_show = "CHANCE LEFT :" + str(self.chance)
                    self.you_win_show = "YOU WIN : " + str(self.you_win)
                    self.computer_win_show = "C WIN : " + str(self.computer_win)
                    self._random = random.choice(self.lst)
                else:
                    self.game_over = True
                    self.text_show_str = "OHH! NOOO! " + "\n" + "GAME OVER " + "\n" + "YOUR POINT IS : " + str(self.you_win) + "\n" + "COMPUTER POINT IS : "  + str(self.computer_win)

            elif self.s_w_g == "p" and self._random == "s":
                if self.chance != 0 :
                    self.chance -= 1
                    self.you_win = self.you_win
                    self.computer_win += 1
                    self.text_show_str = "OHH! NOOO! " + "\n" + "COUMPUTER WIN "
                    self.chance_show = "CHANCE LEFT :" + str(self.chance)
                    self.you_win_show = "YOU WIN : " + str(self.you_win)
                    self.computer_win_show = "C WIN : " + str(self.computer_win)
                    self._random = random.choice(self.lst)
                else:
                    self.game_over = True
                    self.text_show_str = "OHH! NOOO! " + "\n" + "GAME OVER " + "\n" + "YOUR POINT IS : " + str(self.you_win) + "\n" + "COMPUTER POINT IS : "  + str(self.computer_win)

            elif self.s_w_g == "s" and self._random == "r":
                if self.chance != 0 :
                    self.chance -= 1
                    self.you_win = self.you_win
                    self.computer_win += 1
                    self.text_show_str = "OHH! NOOO! " + "\n" + "COUMPUTER WIN "
                    self.chance_show = "CHANCE LEFT :" + str(self.chance)
                    self.you_win_show = "YOU WIN : " + str(self.you_win)
                    self.computer_win_show = "C WIN : " + str(self.computer_win)
                    self._random = random.choice(self.lst)
                else:
                    self.game_over = True
                    self.text_show_str = "OHH! NOOO! " + "\n" + "GAME OVER " + "\n" + "YOUR POINT IS : " + str(self.you_win) + "\n" + "COMPUTER POINT IS : "  + str(self.computer_win)

            else:
                if self.chance != 0 :
                    self.chance -= 1
                    self.you_win += 1
                    self.computer_win = self.computer_win
                    self.text_show_str = "WOW!!!!" + "\n" + "YOU WIN "
                    self.chance_show = "CHANCE LEFT :" + str(self.chance)
                    self.you_win_show = "YOU WIN : " + str(self.you_win)
                    self.computer_win_show = "C WIN : " + str(self.computer_win)
                    self._random = random.choice(self.lst)
                else:
                    self.game_over = True
                    self.text_show_str = "OHH! NOOO! " + "\n" + "GAME OVER " + "\n" + "YOUR POINT IS : " + str(self.you_win) + "\n" + "COMPUTER POINT IS : "  + str(self.computer_win)

    def btn1(self, screen):
        self.s_w_g = "r"

    def btn2(self, screen):
        self.s_w_g = "p"

    def btn3(self, screen):
        self.s_w_g = "s"

    def restart(self, screen):
        self.game_over = False
        self.chance = 10
        self.computer_win = 0
        self.you_win = 0
        self._random = random.choice(self.lst)
        self.chance_show = "CHANCE LEFT : " + str(self.chance)
        self.you_win_show = "YOU WIN : " + str(self.you_win)
        self.computer_win_show = "C WIN :" + str(self.computer_win)


class B12(Screen):
    s_w_g = ObjectProperty(None, allowone=True)
    lst = ['r', 'p', 's']
    _random = random.choice(lst)
    game_over = False
    chance = 15
    you_win = 0
    computer_win = 0
    chance_show = StringProperty("CHANCE LEFT : " + str(chance))
    you_win_show = StringProperty("YOU WIN: " + str(you_win))
    computer_win_show = StringProperty("C WIN " + str(computer_win))
    text_show_str = StringProperty("LET's START THE GAME !!!!")

    def on_value(self, screen):
        if not self.game_over:
            if self.s_w_g == self._random:
                self.chance = self.chance
                self.you_win = self.you_win
                self.computer_win = self.computer_win
                self.text_show_str = "MATCH DRAW " + "\n" + "GUESS AGAIN"
                self.chance_show = "CHANCE LEFT :" + str(self.chance)
                self.you_win_show = "YOU WIN : " + str(self.you_win)
                self.computer_win_show = "C WIN : " + str(self.computer_win)
                self._random = random.choice(self.lst)
            elif self.s_w_g == "r" and self._random == "p":
                if self.chance != 0:
                    self.chance -= 1
                    self.you_win = self.you_win
                    self.computer_win += 1
                    self.text_show_str = "OHH! NOOO! " + "\n" + "COUMPUTER WIN "
                    self.chance_show = "CHANCE LEFT :" + str(self.chance)
                    self.you_win_show = "YOU WIN : " + str(self.you_win)
                    self.computer_win_show = "C WIN : " + str(self.computer_win)
                    self._random = random.choice(self.lst)
                else:
                    self.game_over = True
                    self.text_show_str = "OHH! NOOO! " + "\n" + "GAME OVER " + "\n" + "YOUR POINT IS : " + str(
                        self.you_win) + "\n" + "COMPUTER POINT IS : " + str(self.computer_win)
            elif self.s_w_g == "r" and self._random == "s":
                if self.chance != 0:
                    self.chance -= 1
                    self.you_win += 1
                    self.computer_win = self.computer_win
                    self.text_show_str = "WOW!!!!" + "\n" + "YOU WIN "
                    self.chance_show = "CHANCE LEFT :" + str(self.chance)
                    self.you_win_show = "YOU WIN : " + str(self.you_win)
                    self.computer_win_show = "C WIN : " + str(self.computer_win)
                    self._random = random.choice(self.lst)
                else:
                    self.game_over = True
                    self.text_show_str = "OHH! NOOO! " + "\n" + "GAME OVER " + "\n" + "YOUR POINT IS : " + str(
                        self.you_win) + "\n" + "COMPUTER POINT IS : " + str(self.computer_win)

            elif self.s_w_g == "p" and self._random == "r":
                if self.chance != 0:
                    self.chance -= 1
                    self.you_win += 1
                    self.computer_win = self.computer_win
                    self.text_show_str = "WOW!!!!" + "\n" + "YOU WIN "
                    self.chance_show = "CHANCE LEFT :" + str(self.chance)
                    self.you_win_show = "YOU WIN : " + str(self.you_win)
                    self.computer_win_show = "C WIN : " + str(self.computer_win)
                    self._random = random.choice(self.lst)
                else:
                    self.game_over = True
                    self.text_show_str = "OHH! NOOO! " + "\n" + "GAME OVER " + "\n" + "YOUR POINT IS : " + str(
                        self.you_win) + "\n" + "COMPUTER POINT IS : " + str(self.computer_win)

            elif self.s_w_g == "p" and self._random == "s":
                if self.chance != 0:
                    self.chance -= 1
                    self.you_win = self.you_win
                    self.computer_win += 1
                    self.text_show_str = "OHH! NOOO! " + "\n" + "COUMPUTER WIN "
                    self.chance_show = "CHANCE LEFT :" + str(self.chance)
                    self.you_win_show = "YOU WIN : " + str(self.you_win)
                    self.computer_win_show = "C WIN : " + str(self.computer_win)
                    self._random = random.choice(self.lst)
                else:
                    self.game_over = True
                    self.text_show_str = "OHH! NOOO! " + "\n" + "GAME OVER " + "\n" + "YOUR POINT IS : " + str(
                        self.you_win) + "\n" + "COMPUTER POINT IS : " + str(self.computer_win)

            elif self.s_w_g == "s" and self._random == "r":
                if self.chance != 0:
                    self.chance -= 1
                    self.you_win = self.you_win
                    self.computer_win += 1
                    self.text_show_str = "OHH! NOOO! " + "\n" + "COUMPUTER WIN "
                    self.chance_show = "CHANCE LEFT :" + str(self.chance)
                    self.you_win_show = "YOU WIN : " + str(self.you_win)
                    self.computer_win_show = "C WIN : " + str(self.computer_win)
                    self._random = random.choice(self.lst)
                else:
                    self.game_over = True
                    self.text_show_str = "OHH! NOOO! " + "\n" + "GAME OVER " + "\n" + "YOUR POINT IS : " + str(
                        self.you_win) + "\n" + "COMPUTER POINT IS : " + str(self.computer_win)

            else:
                if self.chance != 0:
                    self.chance -= 1
                    self.you_win += 1
                    self.computer_win = self.computer_win
                    self.text_show_str = "WOW!!!!" + "\n" + "YOU WIN "
                    self.chance_show = "CHANCE LEFT :" + str(self.chance)
                    self.you_win_show = "YOU WIN : " + str(self.you_win)
                    self.computer_win_show = "C WIN : " + str(self.computer_win)
                    self._random = random.choice(self.lst)
                else:
                    self.game_over = True
                    self.text_show_str = "OHH! NOOO! " + "\n" + "GAME OVER " + "\n" + "YOUR POINT IS : " + str(
                        self.you_win) + "\n" + "COMPUTER POINT IS : " + str(self.computer_win)

    def btn1(self, screen):
        self.s_w_g = "r"

    def btn2(self, screen):
        self.s_w_g = "p"

    def btn3(self, screen):
        self.s_w_g = "s"

    def restart(self, screen):
        self.game_over = False
        self.chance = 15
        self.computer_win = 0
        self.you_win = 0
        self._random = random.choice(self.lst)
        self.chance_show = "CHANCE LEFT : " + str(self.chance)
        self.you_win_show = "YOU WIN: " + str(self.you_win)
        self.computer_win_show = "C WIN" + str(self.computer_win)


class B13(Screen):
    s_w_g = ObjectProperty(None, allowone=True)
    lst = ['r', 'p', 's']
    _random = random.choice(lst)
    game_over = False
    chance = 25
    you_win = 0
    computer_win = 0
    chance_show = StringProperty("CHANCE LEFT : " + str(chance))
    you_win_show = StringProperty("YOU WIN: " + str(you_win))
    computer_win_show = StringProperty("C WIN " + str(computer_win))
    text_show_str = StringProperty("LET's START THE GAME !!!!")

    def on_value(self, screen):
        if not self.game_over:
            if self.s_w_g == self._random:
                self.chance = self.chance
                self.you_win = self.you_win
                self.computer_win = self.computer_win
                self.text_show_str = "MATCH DRAW " + "\n" + "GUESS AGAIN"
                self.chance_show = "CHANCE LEFT :" + str(self.chance)
                self.you_win_show = "YOU WIN : " + str(self.you_win)
                self.computer_win_show = "C WIN : " + str(self.computer_win)
                self._random = random.choice(self.lst)
            elif self.s_w_g == "r" and self._random == "p":
                if self.chance != 0:
                    self.chance -= 1
                    self.you_win = self.you_win
                    self.computer_win += 1
                    self.text_show_str = "OHH! NOOO! " + "\n" + "COUMPUTER WIN "
                    self.chance_show = "CHANCE LEFT :" + str(self.chance)
                    self.you_win_show = "YOU WIN : " + str(self.you_win)
                    self.computer_win_show = "C WIN : " + str(self.computer_win)
                    self._random = random.choice(self.lst)
                else:
                    self.game_over = True
                    self.text_show_str = "OHH! NOOO! " + "\n" + "GAME OVER " + "\n" + "YOUR POINT IS : " + str(
                        self.you_win) + "\n" + "COMPUTER POINT IS : " + str(self.computer_win)
            elif self.s_w_g == "r" and self._random == "s":
                if self.chance != 0:
                    self.chance -= 1
                    self.you_win += 1
                    self.computer_win = self.computer_win
                    self.text_show_str = "WOW!!!!" + "\n" + "YOU WIN "
                    self.chance_show = "CHANCE LEFT :" + str(self.chance)
                    self.you_win_show = "YOU WIN : " + str(self.you_win)
                    self.computer_win_show = "C WIN : " + str(self.computer_win)
                    self._random = random.choice(self.lst)
                else:
                    self.game_over = True
                    self.text_show_str = "OHH! NOOO! " + "\n" + "GAME OVER " + "\n" + "YOUR POINT IS : " + str(
                        self.you_win) + "\n" + "COMPUTER POINT IS : " + str(self.computer_win)

            elif self.s_w_g == "p" and self._random == "r":
                if self.chance != 0:
                    self.chance -= 1
                    self.you_win += 1
                    self.computer_win = self.computer_win
                    self.text_show_str = "WOW!!!!" + "\n" + "YOU WIN "
                    self.chance_show = "CHANCE LEFT :" + str(self.chance)
                    self.you_win_show = "YOU WIN : " + str(self.you_win)
                    self.computer_win_show = "C WIN : " + str(self.computer_win)
                    self._random = random.choice(self.lst)
                else:
                    self.game_over = True
                    self.text_show_str = "OHH! NOOO! " + "\n" + "GAME OVER " + "\n" + "YOUR POINT IS : " + str(
                        self.you_win) + "\n" + "COMPUTER POINT IS : " + str(self.computer_win)

            elif self.s_w_g == "p" and self._random == "s":
                if self.chance != 0:
                    self.chance -= 1
                    self.you_win = self.you_win
                    self.computer_win += 1
                    self.text_show_str = "OHH! NOOO! " + "\n" + "COUMPUTER WIN "
                    self.chance_show = "CHANCE LEFT :" + str(self.chance)
                    self.you_win_show = "YOU WIN : " + str(self.you_win)
                    self.computer_win_show = "C WIN : " + str(self.computer_win)
                    self._random = random.choice(self.lst)
                else:
                    self.game_over = True
                    self.text_show_str = "OHH! NOOO! " + "\n" + "GAME OVER " + "\n" + "YOUR POINT IS : " + str(
                        self.you_win) + "\n" + "COMPUTER POINT IS : " + str(self.computer_win)

            elif self.s_w_g == "s" and self._random == "r":
                if self.chance != 0:
                    self.chance -= 1
                    self.you_win = self.you_win
                    self.computer_win += 1
                    self.text_show_str = "OHH! NOOO! " + "\n" + "COUMPUTER WIN "
                    self.chance_show = "CHANCE LEFT :" + str(self.chance)
                    self.you_win_show = "YOU WIN : " + str(self.you_win)
                    self.computer_win_show = "C WIN : " + str(self.computer_win)
                    self._random = random.choice(self.lst)
                else:
                    self.game_over = True
                    self.text_show_str = "OHH! NOOO! " + "\n" + "GAME OVER " + "\n" + "YOUR POINT IS : " + str(
                        self.you_win) + "\n" + "COMPUTER POINT IS : " + str(self.computer_win)

            else:
                if self.chance != 0:
                    self.chance -= 1
                    self.you_win += 1
                    self.computer_win = self.computer_win
                    self.text_show_str = "WOW!!!!" + "\n" + "YOU WIN "
                    self.chance_show = "CHANCE LEFT :" + str(self.chance)
                    self.you_win_show = "YOU WIN : " + str(self.you_win)
                    self.computer_win_show = "C WIN : " + str(self.computer_win)
                    self._random = random.choice(self.lst)
                else:
                    self.game_over = True
                    self.text_show_str = "OHH! NOOO! " + "\n" + "GAME OVER " + "\n" + "YOUR POINT IS : " + str(
                        self.you_win) + "\n" + "COMPUTER POINT IS : " + str(self.computer_win)

    def btn1(self, screen):
        self.s_w_g = "r"

    def btn2(self, screen):
        self.s_w_g = "p"

    def btn3(self, screen):
        self.s_w_g = "s"

    def restart(self, screen):
        self.game_over = False
        self.chance = 25
        self.computer_win = 0
        self.you_win = 0
        self._random = random.choice(self.lst)
        self.chance_show = "CHANCE LEFT : " + str(self.chance)
        self.you_win_show = "YOU WIN: " + str(self.you_win)
        self.computer_win_show = "C WIN" + str(self.computer_win)


class B2(Screen):
    pass


class B21(Screen):

    text_input_str = ObjectProperty(None, allownone=True)
    text_output_str = StringProperty("")
    n = int(random.randrange(1, 10))
    count1 = 0
    count2 = 5
    score = StringProperty("Score : " + str(count1))
    life = StringProperty("life : " + str(count2))
    game_over = False

    def on_text_validate(self, screen):
        if not self.game_over :
            self.text_input_str = screen.text
            self.text_input_str = int(self.text_input_str)

            if self.text_input_str < self.n:
                self.count2 -= 1
                if self.count2 != 0 :
                    q = str(self.n - self.text_input_str)
                    self.life = "life :" + str(self.count2)
                    self.text_output_str = "OH!!! NO!!!" + "\n" + "I THINK YOU BETWEEN " + q + " range" + "\n" + "TRY AGAIN"

                else:
                    self.text_output_str = "SORRY !!!!!!!!" + "\n" + "YOU LOSS THIS MATCH " + "\n" + "CLICK RESTART TRY AGAIN"
            elif self.text_input_str > self.n:
                self.count2 -= 1
                if self.count2 != 0 :
                    q = str(self.text_input_str - self.n)
                    self.life = "life :" + str(self.count2)
                    self.text_output_str = "OH!!! NO!!!" + "\n" + "I THINK YOU BETWEEN " + q + " range" + "\n" + "TRY AGAIN"
                else:
                    self.text_output_str = "SORRY !!!!!!!!" + "\n" + "YOU LOSS THIS MATCH " + "\n" + "CLICK RESTART TRY AGAIN"
            else:
                self.count1 += 1
                self.count2 = 5
                self.score = "Score : " + str(self.count1)
                self.n = int(random.randrange(1, 10))
                if self.count1 == 1:
                    self.text_output_str = "CORRECT !!!!!" + "GUESS ANOTHER "
                elif self.count1 == 2:
                    self.text_output_str = "AMAZING !!!!!" + "GUESS ANOTHER "
                elif self.count1 == 3:
                    self.text_output_str = "PERFECT !!!!!" + "GUESS ANOTHER "
                elif self.count1 == 4:
                    self.text_output_str = "FABULOUS !!!!!" + "GUESS ANOTHER "
                elif self.count1 == 5:
                    self.text_output_str = "FANTASTIC !!!!!" + "GUESS ANOTHER "
                elif self.count1 == 6:
                    self.text_output_str = "SWEET !!!!!" + "GUESS ANOTHER "
                elif self.count1 == 7:
                    self.text_output_str = "WELL DONE !!!!!" + "GUESS ANOTHER "
                else:
                    self.text_output_str = "GREAT JOB " + "GUESS ANOTHER "

            if self.count2 == 0 :
                print("Game over")
                self.game_over = True

    def restart(self, screen ):
        self.game_over = False
        self.count2 = 5
        self.count1 = 0
        self.n = int(random.randrange(1, 10))
        self.score = "SCORE : " + str(self.count1)
        self.life = "LIFE :" + str(self.count2)


class B22(Screen):
    text_input_str = ObjectProperty(None, allownone=True)
    text_output_str = StringProperty("")
    n = int(random.randrange(1, 100))
    count1 = 0
    count2 = 4
    score = StringProperty("Score : " + str(count1))
    life = StringProperty("life : " + str(count2))
    game_over = False

    def on_text_validate(self, screen):
        if not self.game_over:
            self.text_input_str = screen.text
            self.text_input_str = int(self.text_input_str)

            if self.text_input_str < self.n:
                self.count2 -= 1
                if self.count2 != 0:
                    q = str((self.n - self.text_input_str) + 10)
                    self.life = "life :" + str(self.count2)
                    self.text_output_str = "OH!!! NO!!!" + "\n" + "I THINK YOU BETWEEN " + q + " range" + "\n" + "TRY AGAIN"

                else:
                    self.text_output_str = "SORRY !!!!!!!!" + "\n" + "YOU LOSS THIS MATCH " + "\n" + "CLICK RESTART TRY AGAIN"
            elif self.text_input_str > self.n:
                self.count2 -= 1
                if self.count2 != 0:
                    q = str((self.text_input_str - self.n) + 10 )
                    self.life = "life :" + str(self.count2)
                    self.text_output_str = "OH!!! NO!!!" + "\n" + "I THINK YOU BETWEEN " + q + " range" + "\n" + "TRY AGAIN"
                else:
                    self.text_output_str = "SORRY !!!!!!!!" + "\n" + "YOU LOSS THIS MATCH " + "\n" + "CLICK RESTART TRY AGAIN"
            else:
                self.count1 += 1
                self.count2 = 4
                self.score = "Score : " + str(self.count1)
                self.n = int(random.randrange(1, 100))
                if self.count1 == 1:
                    self.text_output_str = "CORRECT !!!!!" + "GUESS ANOTHER "
                elif self.count1 == 2:
                    self.text_output_str = "AMAZING !!!!!" + "GUESS ANOTHER "
                elif self.count1 == 3:
                    self.text_output_str = "PERFECT !!!!!" + "GUESS ANOTHER "
                elif self.count1 == 4:
                    self.text_output_str = "FABULOUS !!!!!" + "GUESS ANOTHER "
                elif self.count1 == 5:
                    self.text_output_str = "FANTASTIC !!!!!" + "GUESS ANOTHER "
                elif self.count1 == 6:
                    self.text_output_str = "SWEET !!!!!" + "GUESS ANOTHER "
                elif self.count1 == 7:
                    self.text_output_str = "WELL DONE !!!!!" + "GUESS ANOTHER "
                else:
                    self.text_output_str = "GREAT JOB " + "GUESS ANOTHER "

            if self.count2 == 0:
                print("Game over")
                self.game_over = True

    def restart(self, screen):
        self.game_over = False
        self.count2 = 4
        self.count1 = 0
        self.n = int(random.randrange(1, 100))
        self.score = "SCORE : " + str(self.count1)
        self.life = "LIFE :" + str(self.count2)


class B23(Screen):
    text_input_str = ObjectProperty(None, allownone=True)
    text_output_str = StringProperty("")
    p = 500
    n = int(random.randrange(1, p))
    count1 = 0
    count2 = 3
    score = StringProperty("Score : " + str(count1))
    life = StringProperty("life : " + str(count2))
    game_over = False

    def on_text_validate(self, screen):
        if not self.game_over:
            self.text_input_str = screen.text
            self.text_input_str = int(self.text_input_str)

            if self.text_input_str < self.n:
                self.count2 -= 1
                if self.count2 != 0:
                    q = str(((self.n - self.text_input_str)*2) + 10 )
                    self.life = "life :" + str(self.count2)
                    self.text_output_str = "OH!!! NO!!!" + "\n" + "I THINK YOU BETWEEN " + q + " range" + "\n" + "TRY AGAIN"

                else:
                    self.text_output_str = "SORRY !!!!!!!!" + "\n" + "YOU LOSS THIS MATCH " + "\n" + "CLICK RESTART TRY AGAIN"
            elif self.text_input_str > self.n:
                self.count2 -= 1
                if self.count2 != 0:
                    q = str(((self.n - self.text_input_str)*2) + 10 )
                    self.life = "life :" + str(self.count2)
                    self.text_output_str = "OH!!! NO!!!" + "\n" + "I THINK YOU BETWEEN " + q + " range" + "\n" + "TRY AGAIN"
                else:
                    self.text_output_str = "SORRY !!!!!!!!" + "\n" + "YOU LOSS THIS MATCH " + "\n" + "CLICK RESTART TRY AGAIN"
            else:
                self.count1 += 1
                self.count2 = 3
                self.score = "Score : " + str(self.count1)
                self.n = int(random.randrange(1, self.p+10))
                if self.count1 == 1:
                    self.text_output_str = "CORRECT !!!!!" + " GUESS ANOTHER "
                elif self.count1 == 2:
                    self.text_output_str = "AMAZING !!!!!" + " GUESS ANOTHER "
                elif self.count1 == 3:
                    self.text_output_str = "PERFECT !!!!!" + " GUESS ANOTHER "
                elif self.count1 == 4:
                    self.text_output_str = "FABULOUS !!!!!" + " GUESS ANOTHER "
                elif self.count1 == 5:
                    self.text_output_str = "FANTASTIC !!!!!" + " GUESS ANOTHER "
                elif self.count1 == 6:
                    self.text_output_str = "SWEET !!!!!" + " GUESS ANOTHER "
                elif self.count1 == 7:
                    self.text_output_str = "WELL DONE !!!!!" + " GUESS ANOTHER "
                else:
                    self.text_output_str = "GREAT JOB " + " GUESS ANOTHER "

            if self.count2 == 0:
                print("Game over")
                self.game_over = True

    def restart(self, screen):
        self.game_over = False
        self.count2 = 5
        self.count1 = 0
        self.n = int(random.randrange(1, self.p))
        self.score = "SCORE : " + str(self.count1)
        self.life = "LIFE :" + str(self.count2)
class WindowManager(ScreenManager):
    pass
kv = Builder.load_file('final.kv')
class FinalApp(App):
    def build(self):
       return kv


if __name__ == '__main__':
    FinalApp().run()