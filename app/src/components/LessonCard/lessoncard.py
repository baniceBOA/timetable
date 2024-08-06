import os
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivy.properties import NumericProperty, StringProperty
from kivy_garden.draggable import KXDraggableBehavior

Builder.load_file(os.path.join(os.path.dirname(__file__), 'lessoncard.kv'))


class Lessoncard(KXDraggableBehavior, MDCard):
    ''' LessonCard 
        stores the property of a lesson in the lesson grid 
        posses the property of a sticky label and the sametime a button 
        parameters
            subject: subject of the lesson a the particular time
            teacher: can either be a teachers code or a teacher name
            class_name: the class in the lesson belongs, this limits the position on which the lesson can belong to 
            width: The with of the lesson object
            height: Height of the lesson object '''
    subject = StringProperty('')
    teacher = NumericProperty()
    class_name = StringProperty('')
    width = NumericProperty(10)
    height = NumericProperty(10)

    def __repr__(self):
        return f'< teacher <{self.teacher}> subject {self.subject} in class {self.class_name}'