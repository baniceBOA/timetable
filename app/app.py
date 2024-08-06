from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from PIL import ImageGrab
from kivy.metrics import dp
from kivy.core.window import Window
from src import Home
from src.components import LessonCell, Lessoncard

# set the window of the application to be the that of the device
# TODO: Maybe use a system program to do this 
screen_image = ImageGrab.grab()

Window.size = (screen_image.size[0]-dp(50), screen_image.size[1]-dp(20))
Window.left = 0
Window.top = 0.5


class TimetableApp(MDApp):
    def build(self):
        return Home()
    def on_start(self):
        ''' call the appropriate data and launch the application'''
        lesson_grid = self.root.ids.timetableview.ids.lesson_grid
        print(lesson_grid.cols*lesson_grid.rows)
        for _ in range(lesson_grid.cols*lesson_grid.rows):
            lesson_grid.add_widget(LessonCell())
        lesson_bank = self.root.ids.lesson_bank
        for _ in range(10):
            lesson_bank.add_widget(Lessoncard(subject='Eng', teacher=23))

            



    
if __name__ == '__main__':
    TimetableApp().run()