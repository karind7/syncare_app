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
#         'Password ': "1234",
#         }
# result = firebase.post('/syncare-6b9b8:/user/', data)
# result = firebase.get('/syncare-6b9b8:/user/', '')
# for key in result:
#     print(result[key])


class User:
    def __init__(self, user_name = None, password = None):
        self.user_name = user_name
        self.password = password

    def log_in(self):
        if self.user_name is not None:
            base = firebase.FirebaseApplication('https://syncare-6b9b8.firebaseio.com/', None)
            result = base.get('/syncare-6b9b8:/user/', '')
            data = pd.DataFrame.from_dict(result, orient='index')
            data.reset_index(drop=True, inplace=True)
            for i in range((len(data.columns))):
                if data['User name'][i] == self.user_name and data['Password '][i] == self.password:
                    return True
            return False

    def __str__(self):
        return "user name: {} password: {}".format(self.user_name, self.password)


class Patient:
    def __init__(self, name):
        self.name = name


class LoginWindow(Screen):

    user_name = ObjectProperty(None)
    password = ObjectProperty(None)

    def reset(self):
        self.user_name.text = ""
        self.password.text = ""

    def log_in(self):
        if User(self.user_name.text, self.password.text).log_in():
            UserWindow.user = User(self.user_name.text, self.password.text)
            sm.current = "main"
        else:
            invalid_login()
        self.reset()


    @staticmethod
    def create_account():
        sm.current = "create"


class CreateAccountWindow(Screen):

    @staticmethod
    def log_in():
        sm.current = "login"


class UserWindow(Screen):

    n = ObjectProperty(None)
    password = ObjectProperty(None)

    user = User()

    @staticmethod
    def log_out():
        sm.current = "login"

    def on_enter(self, *args):
        self.n.text = "Account Name: " + self.user.user_name
        self.password.text = "Created On: " + self.user.password


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("Syncare.kv")
sm = WindowManager()
screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"), UserWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)
sm.current = "login"


def invalid_login():
    pop = Popup(title='Invalid Login',
                content=Label(text='Invalid username or password.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


class Syncare(App):
    def build(self):
        return sm


if __name__ == "__main__":
    Syncare().run()
