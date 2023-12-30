from kivy.uix.widget import Widget
from kivymd.app import MDApp
from webview import WebView
from kivy.lang.builder import Builder
from kivymd.uix.button import MDIconButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout

Builder.load_string("""
<MyWebView>
    MDFloatLayout:
        MDIconButton:
            icon: "logoboma.png"  # Remplacez ceci par le chemin de votre image
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1  # Couleur du texte
            pos_hint: {"center_x": .5, "center_y": .5}
            on_press: root.Push()
""")

class MyWebView(MDScreen):
    def Push(self):
        WebView("https://boma-langue.vercel.app")  # Assurez-vous d'ajouter le protocole "https://" avant l'URL

class MyWebApp(MDApp):
    def build(self):
        return MyWebView()

if __name__ == '__main__':
    MyWebApp().run()
