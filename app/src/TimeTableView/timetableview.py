import os
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from src.components import Lessoncard, LessonGrid

Builder.load_file(os.path.join(os.path.dirname(__file__), 'timetableview.kv'))


class TimetableView(MDRelativeLayout):
    ''' Timetableview  instance of relativelayout
        Display the timetable generated in view function to be able to be adjusted
    '''
    width = NumericProperty()
    height = NumericProperty()
    cols = NumericProperty(10) # columns of the lesson grid
    rows = NumericProperty() # rows of the lesson grid

    def add_lesson(self, lesson_data):
        ''' Add the lesson to the lesson timetableview 
            parameters:
                lesson_data:list, data of each lesson in a list form 
        '''
        for data in lesson_data:
            self.ids.lesson_grid.add_widget(Lessoncard(subject=data['subject'], teacher=data['teacher'], class_name=data['class_name']))
