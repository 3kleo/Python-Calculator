
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if len(modifiers) == 0 and (keycode[1].isnumeric() or keycode[1] in ['-', '/', '.']):
            self.display.text += keycode[1]
        elif len(modifiers) > 0 and modifiers[0] == 'shift' and keycode[1] == '=':
            self.display.text += '+'
        elif len(modifiers) > 0 and modifiers[0] == 'shift' and keycode[1] == '8':
            self.display.text += '*'
        elif keycode[1] == 'enter':
            self.calculate(self.display.text)
        elif keycode[1] == 'escape':
            self.display.text = ''
        elif keycode[1] == 'backspace':
            self.display.text = self.display.text[:-1]
        return True

    def calculate(self, calculation):
        if calculation:
            try:
                result = eval(calculation)
                if float(result).is_integer():
                    self.display.text = str(int(result))
                else:
                    self.display.text = str(round(result, 6))
            except Exception:
                self.display.text = "Error"


class MyApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)  # sets background color of app
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
