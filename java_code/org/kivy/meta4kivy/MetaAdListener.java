package org.kivy.meta4kivy;

public interface MetaAdListener {
    void onAdLoaded(String type);
    void onAdError(String type, String error);
    void onAdClicked(String type);
    void onAdImpression(String type);

    void onInterstitialDismissed();
    void onRewardedCompleted();
    void onRewardedDismissed();
}
