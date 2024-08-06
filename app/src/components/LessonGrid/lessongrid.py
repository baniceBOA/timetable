from kivymd.uix.gridlayout import MDGridLayout
from kivy.properties import NumericProperty

from src.components.lessoncard import Lessoncard
from src.components.lessoncell import LessonCell
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'lessongrid.kv'))

class LessonGridException(Exception):
    pass

class LessonGrid(MDGridLayout):
    ''' Display the lessoncard in a grid layout
        parameters:
            cols: Number of columns in the grid (NumericProperty)
            rows: Number of rows in the grid (NumericProperty)
    '''
    cols  = NumericProperty()
    rows = NumericProperty()

    def add_widget(self, widget, index=0, canvas=None):
        ''' add a <LessonCard> instance to the grid the'''
        # The only widget that can be added is the LessonCard or
        # an instance of the Lessoncard
        if isinstance(widget, (Lessoncard, LessonCell)):
            return super(LessonGrid, self).add_widget(widget, index=index, canvas=canvas)
        else:
            raise LessonGridException( f'Can not add the {widget} to the Lesson Grid can only accept <{Lessoncard}> or <{LessonCell}> objects ')
