from kivymd.uix.card import MDCard
from kivy_garden.draggable import KXDroppableBehavior
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'lessonbank.kv'))
class LessonBank(KXDroppableBehavior, MDCard):
    def accepts_drag(self, touch, ctx, draggable) -> bool:
        return True

    def add_widget(self, widget, *args, **kwargs):
        widget.size_hint = (1, 1, )
        widget.pos_hint = {'x': 0, 'y': 0, }
        return super().add_widget(widget, *args, **kwargs)