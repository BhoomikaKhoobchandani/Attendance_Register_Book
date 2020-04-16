import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
import os
from kivy.uix.label import Label
from datetime import datetime
import xlsxwriter 
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
import getpics
import faces
import facesTrain
from datetime import date
import csv
import xlwt


class Recognition(Widget):
    Builder.load_file('face.kv')
    global n,i,res
    res={}
    n=[]
    i=[]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ids.new_user.disabled=False
        self.ids.exist_user.disabled=False
        self.ids.Take_i.disabled=True
        self.ids.Train_i.disabled=True
        self.ids.FP_i.disabled=True
    def newUser_btn(self,value):
        if(value):
            self.ids.exist_user.disabled=True
            self.ids.FP_i.disabled=True
            self.ids.Take_i.disabled=False
            self.ids.Train_i.disabled=False
    def existUser_btn(self,value):
        if(value):
            self.ids.new_user.disabled=True
            self.ids.Take_i.disabled=True
            self.ids.Train_i.disabled=True
            self.ids.FP_i.disabled=False

    def submit_btn(self,value):
        if(value):
            self.Name=self.ids.name_input1.text
            n.append(self.Name)
    def submit_btn2(self,value):
        if(value):
            self.id=self.ids.id_input2.text
            i.append(self.id)
    def manually_btn(self):
        popup = Popup(title='Warning!!', content=Label(text='Fill Name &  ID above and then submit it'), size_hint=(None, None), size=(400, 400),
              auto_dismiss=True)
        popup.open()
        
    def CheckAttendance_btn(self):
        for key in n: 
            for value in i: 
                res[key] = value 
                i.remove(value) 
                break  
        now=datetime.now()
        today = date.today()
        t=(now.strftime("%a, %d %B, %y"))
        time=(now.strftime("%H:%M"))
        self.d4 = today.strftime("%b-%d-%Y")
        self.d=self.d4+".csv"
        print(self.d)
        with open(self.d, mode='a', newline="") as employee_file:
            employee_writer = csv.writer(employee_file, delimiter=',')
            print([self.ids.name_input1.text, self.ids.id_input2.text, t, time])
            employee_writer.writerow([self.ids.name_input1.text, self.ids.id_input2.text, t, time]) 
            instance=self.d
        self.view(instance)
    def view(self, instance):
        file = instance
        print(file)
        import webbrowser
        new = 2
        url = os.getcwd()  + '\\' + file
        print(url)
        if os.path.exists(url):
            webbrowser.open(url, new=new)
        else:
            popup = Popup(title='WARNING!!!', title_size=30, content=Label(text="No File Found On This Date"), size_hint=(None, None), size=(600, 400),auto_dismiss=True)
            popup.open()
    def TakeImages_btn(self):
    	getpics.TakeImages(self.ids.name_input1.text)
    def TrainImages_btn(self):
    	facesTrain.TrainImages()
    def FP_btn(self):
    	faces.FP()
        
    def viewAttendance_btn(self):
        box = BoxLayout(orientation='vertical', padding=(10))
        box.add_widget(Label(text="DD : ",))
        self.vpmin = TextInput(text=" ",id='vpmin')
        box.add_widget(self.vpmin)
        box.add_widget(Label(text="MM : ",))
        self.lpmin = TextInput(text="",id='lpmin')
        box.add_widget(self.lpmin)

        box.add_widget(Label(text="YYYY : ",))
        self.vrmin = TextInput(text="",id='vrmin')
        box.add_widget(self.vrmin)
        print("hello")
        print(self.vpmin.text)
        btn1 = Button(text="Submit")
        btn2 = Button(text="Cancel")
        box.add_widget(btn1)
        box.add_widget(btn2)
        self.popup = Popup(title='ENTER INFORMATION!!!', title_size=30, content=box, size_hint=(None, None), size=(600, 400),
                          auto_dismiss=True)
        btn1.bind(on_release=self.talent)
        btn2.bind(on_press=self.popup.dismiss)
        self.popup.open()
    # def talent(self,*args):
    #     print("open")
    #     vpmin = self.vpmin.text
    #     lpmin = self.lpmin.text
    #     vrmin = self.vrmin.text
    #     self.c=lpmin+"-"+vpmin+"-"+vrmin
    #     import webbrowser
    #     new = 2
    #     url = os.getcwd() +'\\'+"CSV'S"+ '\\' + "Mar-15-2020.csv"
    #     print(url)
    #     webbrowser.open(url, new=new)
    def talent(self,*args):
        print("open")
        vpmin = self.vpmin.text
        lpmin = self.lpmin.text
        vrmin = self.vrmin.text
        self.c=lpmin.strip()+"-" + vpmin.strip() +"-"+ vrmin.strip()+".csv"
        print(self.c)
        self.view(self.c)

class UtilityApp(App):
    def build(self):
        return Recognition()


if __name__ == "__main__":
    UtilityApp().run()