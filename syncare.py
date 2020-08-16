from firebase import firebase
import pandas as pd
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label

# firebase = firebase.FirebaseApplication('https://syncare-6b9b8.firebaseio.com/', None)
# data = {'User name': 'mor',
#         'Password ': "1264kK",
#         }
# result = firebase.post('/syncare-6b9b8:/user/', data)
# result = firebase.get('/syncare-6b9b8:/user/', '')
# for key in result:
#     print(result[key])


class LoginWindow(Screen):

    user_name = ObjectProperty(None)
    password = ObjectProperty(None)

    def reset(self):
        self.user_name.text = ""
        self.password.text = ""

    def log_in(self):
        print((User(self.user_name.text, self.password.text)).log_in())
        self.reset()


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("Syncare.kv")
sm = WindowManager()
screen = LoginWindow(name="login")
sm.add_widget(screen)
sm.current = "login"


class Syncare(App):
    def build(self):
        return sm


class Patient:
    def __init__(self, name):
        self.name = name


class User:
    def __init__(self, use_name = None, password = None):
        self.use_name = use_name
        self.password = password

    def log_in(self):
        if self.use_name is not None:
            base = firebase.FirebaseApplication('https://syncare-6b9b8.firebaseio.com/', None)
            result = base.get('/syncare-6b9b8:/user/', '')
            data = pd.DataFrame.from_dict(result, orient='index')
            data.reset_index(drop=True, inplace=True)
            for i in range((len(data.columns))):
              if data['Name'][i] == self.use_name and data['password '][i] == self.password:
                return "user exsists"
            return "user dose not exsist"

    def __str__(self):
        return "user name: {} password: {}".format(self.use_name, self.password)


if __name__ == "__main__":
    Syncare().run()
