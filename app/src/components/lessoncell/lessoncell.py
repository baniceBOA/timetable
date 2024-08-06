from kivy_garden.draggable import KXDroppableBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'lessoncell.kv'))

class LessonCell(KXDroppableBehavior, MDFloatLayout):
    """ Hold the lesson Card and Can Mirror the LessonCard should inherent from the lesson class
        The class accepts LessonCard drops
    """
    def accepts_drag(self, touch, ctx, draggable) -> bool:
        return not self.children

    def add_widget(self, widget, *args, **kwargs):
        widget.size_hint = (1, 1, )
        widget.pos_hint = {'x': 0, 'y': 0, }
        return super().add_widget(widget, *args, **kwargs)