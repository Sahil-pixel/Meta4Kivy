from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from meta4kivy import MetaAdManager

#Create Meta Ads Account to Get IDS 
APP_ID = "APP_ID"
BANNER = "BANNER_ID"
INTERSTITIAL = "INTERSTITIAL_ID"
REWARDED = "REWARDED_ID"

KV = '''
<MetaTestUI>:
    orientation: 'vertical'
    padding: 20
    spacing: 10

    Button:
        text: "Show Banner (Top)"
        on_press: app.show_banner(True)

    Button:
        text: "Show Banner (Bottom)"
        on_press: app.show_banner(False)
    Button:
        text: "Hide Banner"
        on_press: app.hide_banner()

    Label:
        text: "Interstitial Ads"
        size_hint_y: None
        height: dp(20)

    Button:
        text: "Load Interstitial"
        on_press: app.load_interstitial()

    Button:
        text: "Show Interstitial"
        on_press: app.show_interstitial()

    Label:
        text: "Rewarded Ads"
        size_hint_y: None
        height: dp(20)

    Button:
        text: "Load Rewarded"
        on_press: app.load_rewarded()

    Button:
        text: "Show Rewarded"
        on_press: app.show_rewarded()
'''


class MetaTestUI(BoxLayout):
    pass


class MetaTestApp(App):
    def build(self):
        self.meta_ads = MetaAdManager(callback=self.ad_callback)
        Builder.load_string(KV)
        return MetaTestUI()

    def show_banner(self, top=True):
        self.meta_ads.show_banner(BANNER, top=top)

    def hide_banner(self):
        self.meta_ads.hide_banner()

    def load_interstitial(self):
        self.meta_ads.load_interstitial(INTERSTITIAL)

    def show_interstitial(self):
        self.meta_ads.show_interstitial()

    def load_rewarded(self):
        self.meta_ads.load_rewarded(REWARDED)

    def show_rewarded(self):
        self.meta_ads.show_rewarded()

    def ad_callback(self, event, *args):
        print("Event IN Kivy App :", event, args)


if __name__ == '__main__':
    MetaTestApp().run()
