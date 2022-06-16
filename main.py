
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window


class MyGrid(GridLayout):
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"


class MyApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)  # sets background color of app
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
