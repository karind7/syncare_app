import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

 
# firebase = firebase.FirebaseApplication('https://syncare-6b9b8.firebaseio.com/', None)
# data = {'Name': 'karind',
#         'password ': "123564kK",
#         }
# result = firebase.post('/syncare-6b9b8:/user/', data)
# print(result)

class MyGrid(GridLayout):
    user_name = ObjectProperty(None)
    password = ObjectProperty(None)


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
