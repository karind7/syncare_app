import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from firebase import firebase

# firebase = firebase.FirebaseApplication('https://syncare-6b9b8.firebaseio.com/', None)
# data = {'Name': 'karind',
#         'password ': "123564kK",
#         }
# result = firebase.post('/syncare-6b9b8:/user/', data)
# print(result)


class MyGrid(GridLayout):
    pass
    # def __init__(self, **kwargs):
    #     super(MyGrid, self).__init__(**kwargs)
    #     self.cols = 1
    #
    #     self.inside = GridLayout()
    #     self.inside.cols = 2
    #
    #     self.inside.add_widget(Label(text="User Name: "))
    #     self.user_name = TextInput(multiline=False)
    #     self.inside.add_widget(self.user_name)
    #
    #     self.inside.add_widget(Label(text="password: "))
    #     self.user_password = TextInput(multiline=False)
    #     self.inside.add_widget(self.user_password)
    #
    #     self.add_widget(self.inside)
    #
    #     self.log_in = Button(text="log in", font_size=40)
    #     self.log_in.bind(on_press=self.log_in_pressed)
    #     self.add_widget(self.log_in)


    # def log_in_pressed(self, instance):
    #     user_name = self.user_name.text
    #     password = self.user_password.text
    #     print( user_name, password)


class Syncare(App):
    def build(self):
        return MyGrid()


class patient:
    def __init__(self, name, ):
        self.name = name


class user:
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    Syncare().run()
