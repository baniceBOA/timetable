import os
from kivy.lang import Builder
from kivy.properties import NumericProperty, ListProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout



Builder.load_file(os.path.join(os.path.dirname(__file__), 'timetableview.kv'))


class TimetableView(MDBoxLayout):
    ''' Timetableview  instance of relativelayout
        Display the timetable generated in view function to be able to be adjusted
    '''
    width = NumericProperty()
    height = NumericProperty()
    cols = NumericProperty(50) # columns of the lesson grid
    rows = NumericProperty(4) # rows of the lesson grid
    lesson_data = ListProperty()

   