import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from firebase import firebase

firebase = firebase.FirebaseApplication('https://syncare-6b9b8.firebaseio.com/', None)
data = {'Name': 'John Doe',
        'RollNo': 3,
        'Percentage': 70.02
        }
result = firebase.post('/syncare-6b9b8:/Students/', data)
print(result)


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="User Name: "))
        self.user_name = TextInput(multiline=False)
        self.inside.add_widget(self.user_name)

        self.inside.add_widget(Label(text="password: "))
        self.user_password = TextInput(multiline=False)
        self.inside.add_widget(self.user_password)

        self.add_widget(self.inside)

        self.log_in = Button(text="log in", font_size=40)
        self.add_widget(self.log_in)


class Syncare(App):
    def build(self):
        return MyGrid()


class patient:
    def __init__(self, name):
        self.name = name


class user:
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    Syncare().run()
