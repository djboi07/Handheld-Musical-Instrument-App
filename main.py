from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton as Button
from kivymd.app import MDApp
from kivy.uix.slider import Slider
from kivy.core.window import Window
from kivy.clock import Clock
import pygame

try:
    from plyer import accelerometer
    HAS_ACCEL = True
except ImportError:
    HAS_ACCEL = False


class AccelerometerApp(MDApp):
    def build(self):
        pygame.init()
        self.y_value = 0
        self.fl = r"./notes_files/"

        root_layout = BoxLayout(orientation='vertical')

        self.now_playing_label = Label(
            text="",
            font_size="30sp",
            size_hint=(1, 0.15),
            halign="center",
            valign="middle",
            color=(0, 0, 0, 1)
        )
        self.now_playing_label.bind(size=lambda *x: setattr(self.now_playing_label, 'text_size', self.now_playing_label.size))
        root_layout.add_widget(self.now_playing_label)

        mid_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.8))

        buttons_layout = FloatLayout(size_hint=(0.75, 1))
        y_positions = [0.92, 0.77, 0.62, 0.47, 0.32, 0.17, 0.02]
        colors = [
            (.98, .97, .8, 1),
            (.99, .89, .81, 1),
            (1, .81, .82, 1),
            (.94, .75, .90, 1),
            (.81, .73, .94, 1),
            (.63, .75, .95, 1),
            (.56, .85, .95, 1)
        ]
        notes = ["C", "D", "E", "F", "G", "A", "B"]

        self.buttons = {}
        for i, note in enumerate(notes):
            btn = Button(
                text=note,
                size_hint=(0.75, 0.1),
                pos_hint={"x": 0, "y": y_positions[i]},
                md_bg_color=colors[i],
                text_color=(0, 0, 0, 1),
                halign="right",
                font_style='H3'
            )
            btn.bind(on_press=lambda inst, n=note.lower(): self.note_button_pressed(inst, n))
            buttons_layout.add_widget(btn)
            self.buttons[note.lower()] = btn

        mid_layout.add_widget(buttons_layout)

        self.octave_label = Label(
            text="O\nC\nT\nA\nV\nE",
            font_size="40sp",
            halign="center",
            valign="middle",
            size_hint=(0.25, 1),
            color=(0, 0, 0, 1)
        )
        self.octave_label.bind(size=lambda *x: setattr(self.octave_label, 'text_size', self.octave_label.size))
        mid_layout.add_widget(self.octave_label)

        root_layout.add_widget(mid_layout)

        self.slider = Slider(min=-12, max=12, value=0, step=0.1, size_hint=(1, 0.1))
        self.slider.bind(value=self.on_slider_change)
        root_layout.add_widget(self.slider)

        if HAS_ACCEL:
            try:
                accelerometer.enable()
                self.acceleration_event = Clock.schedule_interval(self.update_acceleration, 1 / 15)
            except NotImplementedError:
                print("Accelerometer not available on this platform.")

        Window.bind(on_key_down=self.on_key_down)

        return root_layout

    def on_slider_change(self, instance, value):
        self.y_value = value
        self.update_octave_label(value)

    def update_acceleration(self, dt):
        x, y, z = accelerometer.acceleration[:3]
        if not y:
            return
        if y * z < 0:
            y = -y
        self.y_value = y
        self.update_octave_label(y)

    def update_octave_label(self, y):
        self.octave_label.text = "O\nC\nT\nA\nV\nE\n" + str(self.find_note(y))

    def find_note(self, y):
        if -9 < y <= 0:
            return 2
        elif (-12 < y <= -9) or (9 < y <= 12):
            return 3
        elif 7.3 < y <= 8.7:
            return 4
        elif 5.5 < y <= 7.3:
            return 5
        elif 3.5 < y <= 5.5:
            return 6
        elif 0 < y <= 3.5:
            return 7
        else:
            return 4

    def play_sound(self, file_name):
        try:
            pygame.mixer.music.load(self.fl + file_name)
            pygame.mixer.music.play()
            self.now_playing_label.text = f"{file_name[:2]}"
        except Exception as e:
            print(f"Error playing {file_name}: {e}")

    def note_button_pressed(self, instance, note):
        file_name = note + str(self.find_note(self.y_value)) + ".mp3"
        self.play_sound(file_name)

    def on_key_down(self, window, key, scancode, codepoint, modifier):
        key_map = {
            'q': 'c',
            'w': 'd',
            'e': 'e',
            'r': 'f',
            't': 'g',
            'y': 'a',
            'u': 'b'
        }
        if codepoint.lower() in key_map:
            self.note_button_pressed(None, key_map[codepoint.lower()])

    def on_stop(self):
        pygame.quit()
        if HAS_ACCEL and hasattr(self, 'acceleration_event'):
            self.acceleration_event.cancel()
            accelerometer.disable()


if __name__ == '__main__':
    AccelerometerApp().run()
