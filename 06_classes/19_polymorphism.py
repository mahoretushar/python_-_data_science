# Ability to take more than one form

from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print('TextBox')


class DropDownList(UIControl):
    def draw(self):
        print('DropDownList')


def draw_x(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
tb = TextBox()
draw_x([ddl, tb])
