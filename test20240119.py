from kivy.app import App
from kivy.uix.button import Button


class LCZApp(App):
    def build(slef):
        return Button(text='Hello World', font_size=150, background_color=(0, 0, 1, 1), background_normal='', color=(1, 0, 0, 1),on_press=lambda x: print('Button clicked'))   


if __name__ == '__main__':
    LCZApp().run()