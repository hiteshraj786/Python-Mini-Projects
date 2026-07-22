from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class mainApp(MDApp):
    def build(self):
        return MDLabel(text="Welcome to Mount Abu Wildlife Santuary",halign="center")
    

if __name__ == '__main__':
    mainApp().run()
    