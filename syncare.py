from firebase import firebase
import pandas as pd
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty


# firebase = firebase.FirebaseApplication('https://syncare-6b9b8.firebaseio.com/', None)
# data = {'User name': 'mor',
#         'Password ': "1264kK",
#         }
# result = firebase.post('/syncare-6b9b8:/user/', data)
# result = firebase.get('/syncare-6b9b8:/user/', '')
# for key in result:
#     print(result[key])

class MyGrid(GridLayout):
    user_name = ObjectProperty(None)
    password = ObjectProperty(None)

    def log_in(self):
        (User(self.user_name.text, self.password.text)).log_in()


class Syncare(App):
    def build(self):
        return MyGrid()


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
