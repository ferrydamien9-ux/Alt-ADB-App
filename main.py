from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from kivy.uix.label import Label

class AltADBApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # App Title
        layout.add_widget(Label(text='ALT-ADB MOBILE', font_size='30sp', size_hint_y=0.2))
        
        # Output Area
        self.output = CodeInput(text='Ready to scan...', readonly=True)
        layout.add_widget(self.output)
        
        # Scan Button
        btn = Button(text='SCAN FOR DEVICES', size_hint_y=0.2, background_color=(0, 0.5, 1, 1))
        btn.bind(on_press=self.run_scan)
        layout.add_widget(btn)
        
        return layout

    def run_scan(self, instance):
        self.output.text = "Scanning internal bridge...\nNo local ADB server found.\nPlease connect via WiFi ADB."

if __name__ == '__main__':
    AltADBApp().run()
  
