from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class BasitYapayZeka:
    def __init__(self):
        self.sorular = {}
    
    def merhaba_de(self):
        return "Merhaba!"

    def soru_ekle(self, soru, cevap):
        self.sorular[soru.lower()] = cevap

    def cevap_ver(self, soru):
        soru = soru.lower()
        if soru in self.sorular:
            return self.sorular[soru]
        else:
            return "Yaratıcım Abdülselam Kaya bu bu soruya verilecek cevabı henüz üretmedi."


yapay_zeka = BasitYapayZeka()
yapay_zeka.soru_ekle("hava nasıl?", "Bugün hava güzel görünüyor!")
yapay_zeka.soru_ekle("abdülselam kayayı tanıt", "Yapay zeka ve veri mühendisi birisidir.")

class AbdulselamGPTApp(App):
    def build(self):
        
        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        
    
        self.title_label = Label(text="SelamGPT", font_size=24, size_hint=(1, 0.2))
        layout.add_widget(self.title_label)
        
       
        self.soru_input = TextInput(hint_text="Bir şey yazın...", size_hint=(1, 0.2), multiline=False)
        layout.add_widget(self.soru_input)
        
      
        self.cevap_label = Label(text="", font_size=18, size_hint=(1, 0.4))
        layout.add_widget(self.cevap_label)
        
       
        send_button = Button(text="Gönder", size_hint=(1, 0.2))
        send_button.bind(on_press=self.gonder)
        layout.add_widget(send_button)
        
     
        self.soru_onerileri_layout = BoxLayout(orientation="horizontal", size_hint=(1, 0.2), spacing=5)
        layout.add_widget(self.soru_onerileri_layout)

      
        oneri1_button = Button(text="abdülselam kayayı tanıt")
        oneri1_button.bind(on_press=lambda x: self.soru_input.insert_text("abdülselam kayayı tanıt"))
        
        oneri2_button = Button(text="Hava nasıl?")
        oneri2_button.bind(on_press=lambda x: self.soru_input.insert_text("Hava nasıl?"))

        self.soru_onerileri_layout.add_widget(oneri1_button)
        self.soru_onerileri_layout.add_widget(oneri2_button)

        return layout
    
    def gonder(self, instance):
       
        soru = self.soru_input.text
      
        if soru.lower() == "merhaba":
            cevap = yapay_zeka.merhaba_de()
        else:
            cevap = yapay_zeka.cevap_ver(soru)
        
        
        self.cevap_label.text = cevap
      
        self.soru_input.text = ""

if __name__ == "__main__":
    AbdulselamGPTApp().run()
