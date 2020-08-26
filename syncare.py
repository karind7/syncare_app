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
# data = {'User name': 'karind',
#         'Name': 'karin',
#         'Password': '1234',
#         'mail:' 'karin'
#         }
# result = firebase.post('/syncare-6b9b8:/user/', data)
# result = firebase.get('/syncare-6b9b8:/user/', '')
# for key in result:
#     print(result[key])


class User:
    def __init__(self, user_name=None, password=None, name=None, email=None):
        self.name = name
        self.user_name = user_name
        self.password = password
        self.email = email

        if self.name and self.password and self.user_name and self.email is not None:
            user_name_validity = True
            base = firebase.FirebaseApplication('https://syncare-6b9b8.firebaseio.com/', None)
            result = base.get('/syncare-6b9b8:/user/', '')
            data = pd.DataFrame.from_dict(result, orient='index')
            data.reset_index(drop=True, inplace=True)
            for i in range((len(data.index))):
                if data['User name'][i] == self.user_name:
                    user_name_validity = False
                    invalid_user_name()
            if user_name_validity:
                base = firebase.FirebaseApplication('https://syncare-6b9b8.firebaseio.com/', None)
                data = {'User name': self.user_name,
                        'Name': self.name,
                        'Password ': self.password,
                        'mail': self.email
                        }
                base.post('/syncare-6b9b8:/user/', data)

    def does_user_exist(self):
        if self.user_name:
            base = firebase.FirebaseApplication('https://syncare-6b9b8.firebaseio.com/', None)
            result = base.get('/syncare-6b9b8:/user/', '')
            data = pd.DataFrame.from_dict(result, orient='index')
            data.reset_index(drop=True, inplace=True)
            for i in range((len(data.index))):
                if data['User name'][i] == self.user_name and data['Password '][i] == self.password:
                    return True
            return False

    def __str__(self):
        return "user name: {} password: {}".format(self.user_name, self.password)


class Patient:
    def __init__(self, name, age, authorized_user):
        self.name = name
        self.age = age
        self.authorized_users = [authorized_user.user_name]
        if self.name is not None:
            base = firebase.FirebaseApplication('https://syncare-6b9b8.firebaseio.com/', None)
            data = {'Name': self.name,
                    'Age': self.age,
                    'authorized users': self.authorized_users
                    }
            base.post('/syncare-6b9b8:/patient/', data)


class LoginWindow(Screen):

    user_name = ObjectProperty(None)
    password = ObjectProperty(None)

    def reset(self):
        self.user_name.text = ""
        self.password.text = ""

    def log_in(self):
        if User(self.user_name.text, self.password.text).does_user_exist():
            UserWindow.user = User(self.user_name.text, self.password.text)
            sm.current = "main"
        else:
            invalid_login()
        self.reset()

    @staticmethod
    def create_account():
        sm.current = "create"


class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    user_name = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        User(self.namee.text, self.user_name.text, self.password.text, self.email.text)
        self.clean()

    @staticmethod
    def log_in():
        sm.current = "login"

    def clean(self):
        self.namee.text = ""
        self.user_name.text = ""
        self.password.text = ""
        self.email.text = ""


class UserWindow(Screen):

    n = ObjectProperty(None)
    password = ObjectProperty(None)

    # user = User()

    @staticmethod
    def log_out():
        sm.current = "login"

    @staticmethod
    def create_patient_sheet():
        CreatePatientSheet.user = UserWindow.user
        sm.current = "create_patient_sheet"

    @staticmethod
    def enter_patient_sheet():
        sm.current = "patient_sheet"

    def on_enter(self, *args):
        self.hello.text = "Hello " + self.user.user_name


class PatientSheet(Screen):
    pass


class CreatePatientSheet(Screen):
    user = User()

    @staticmethod
    def back():
        UserWindow.user = CreatePatientSheet.user
        sm.current = "main"

    def submit(self):
        Patient(self.patient_name.text, self.age.text, CreatePatientSheet.user)


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("Syncare.kv")
sm = WindowManager()
screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"), UserWindow(name="main"),
           PatientSheet(name="patient_sheet"), CreatePatientSheet(name="create_patient_sheet")]
for screen in screens:
    sm.add_widget(screen)
sm.current = "login"


def invalid_login():
    pop = Popup(title='Invalid Login',
                content=Label(text='Invalid username or password.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


def invalid_user_name():
    pop = Popup(title='invalid Username',
                content=Label(text='username already exists\n please choose another.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


class Syncare(App):
    def build(self):
        return sm


if __name__ == "__main__":
    Syncare().run()
