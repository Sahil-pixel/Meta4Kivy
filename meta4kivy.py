from jnius import autoclass, PythonJavaClass, java_method
from android.runnable import run_on_ui_thread

# Java classes
PythonActivity = autoclass('org.kivy.android.PythonActivity')
AdManager = autoclass('org.kivy.meta4kivy.MetaAdManager')

# Java listener interface
class AdListener(PythonJavaClass):
    __javainterfaces__ = ['org/kivy/meta4kivy/MetaAdListener']
    __javacontext__ = 'app'

    def __init__(self, callback=None):
        super().__init__()
        self.callback = callback

    def _dispatch(self, event, *args):
        if self.callback:
            self.callback(event, *args)

    @java_method('(Ljava/lang/String;)V')
    def onAdLoaded(self, ad_type):
        print(f"[Meta4Kivy] [{ad_type}] Ad Loaded")
        self._dispatch("ad_loaded", ad_type)

    @java_method('(Ljava/lang/String;Ljava/lang/String;)V')
    def onAdError(self, ad_type, error):
        print(f"[Meta4Kivy] [{ad_type}] Error: {error}")
        self._dispatch("ad_error", ad_type, error)

    @java_method('(Ljava/lang/String;)V')
    def onAdClicked(self, ad_type):
        print(f"[Meta4Kivy] [{ad_type}] Ad Clicked")
        self._dispatch("ad_clicked", ad_type)

    @java_method('(Ljava/lang/String;)V')
    def onAdImpression(self, ad_type):
        print(f"[Meta4Kivy] [{ad_type}] Ad Impression")
        self._dispatch("ad_impression", ad_type)

    @java_method('()V')
    def onInterstitialDismissed(self):
        print(f"[Meta4Kivy] Interstitial Dismissed")
        self._dispatch("interstitial_dismissed")

    @java_method('()V')
    def onRewardedCompleted(self):
        print(f"[Meta4Kivy] Rewarded Video Completed")
        self._dispatch("rewarded_completed")

    @java_method('()V')
    def onRewardedDismissed(self):
        print(f"[Meta4Kivy] Rewarded Video Dismissed")
        self._dispatch("rewarded_dismissed")

# Manager class
class MetaAdManager:
    def __init__(self, callback=None):
        self.activity = PythonActivity.mActivity
        
        if callback:
            self.listener = AdListener(callback)
        else:
            self.listener = AdListener()

        self.ad_manager = AdManager(self.activity, self.listener)

    @run_on_ui_thread
    def show_banner(self, placement_id: str, top: bool = False):
        self.ad_manager.showBanner(placement_id, top)

    @run_on_ui_thread
    def hide_banner(self):
        self.ad_manager.hideBanner()

    @run_on_ui_thread
    def load_interstitial(self, placement_id: str):
        self.ad_manager.loadInterstitial(placement_id)

    @run_on_ui_thread
    def show_interstitial(self):
        self.ad_manager.showInterstitial()

    @run_on_ui_thread
    def load_rewarded(self, placement_id: str):
        self.ad_manager.loadRewarded(placement_id)

    @run_on_ui_thread
    def show_rewarded(self):
        self.ad_manager.showRewarded()
