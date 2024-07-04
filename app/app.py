from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from src import Home


class TimetableApp(MDApp):
    def build(self):
        return Home()
    def on_start(self):
        ''' call the appropriate data and launch the application'''
        lesson_data = [{'subject':'english', 'teacher':'1', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'2', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'3', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'4', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'5', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'6', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'7', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'8', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'9', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'10', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'11', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'12', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'13', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'1', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'2', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'3', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'4', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'5', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'6', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'7', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'8', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'9', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'10', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'11', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'12', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'13', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'1', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'2', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'3', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'4', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'5', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'6', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'7', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'8', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'9', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'10', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'11', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'12', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'13', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'1', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'2', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'3', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'4', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'5', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'6', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'7', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'8', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'9', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'10', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'11', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'12', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'13', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'1', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'2', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'3', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'4', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'5', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'6', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'7', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'8', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'9', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'10', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'11', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'12', 'class_name':'1 North', },
                       {'subject':'english', 'teacher':'13', 'class_name':'1 North', },]
        self.root.ids.timetableview.add_lesson(lesson_data)
    
if __name__ == '__main__':
    TimetableApp().run()