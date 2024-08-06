from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.lang import Builder
import os

from src.TimeTableView import TimetableView
from src.components import LessonBank

Builder.load_file(os.path.join(os.path.dirname(__file__), 'home.kv'))

class Home(MDRelativeLayout):
    pass
