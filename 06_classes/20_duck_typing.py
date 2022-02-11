class TextBox():
    def draw(self):
        print('TextBox')


class DropDownList():
    def draw(self):
        print('DropDownList')


def draw_x(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
tb = TextBox()
draw_x([ddl, tb])
