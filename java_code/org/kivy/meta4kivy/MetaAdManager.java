package org.kivy.meta4kivy;

import android.app.Activity;
import android.view.Gravity;
import android.widget.FrameLayout;
import com.facebook.ads.*;

public class MetaAdManager {
    private Activity activity;
    private AdView adView;
    private InterstitialAd interstitialAd;
    private RewardedVideoAd rewardedAd;
    private FrameLayout adContainer;
    private MetaAdListener listener;

    public MetaAdManager(Activity activity, MetaAdListener listener) {
        this.activity = activity;
        this.listener = listener;
        AudienceNetworkAds.initialize(activity);
    }

    public void showBanner(final String placementId, final boolean top) {
        activity.runOnUiThread(() -> {
            if (adView != null) {
                adView.destroy();
                if (adContainer != null) adContainer.removeAllViews();
            }

            adView = new AdView(activity, placementId, AdSize.BANNER_HEIGHT_50);
            adContainer = new FrameLayout(activity);
            FrameLayout.LayoutParams params = new FrameLayout.LayoutParams(
                FrameLayout.LayoutParams.MATCH_PARENT,
                FrameLayout.LayoutParams.WRAP_CONTENT
            );
            params.gravity = top ? Gravity.TOP : Gravity.BOTTOM;
            adContainer.setLayoutParams(params);

            adView.loadAd(adView.buildLoadAdConfig()
                .withAdListener(new AdListener() {
                    @Override
                    public void onError(Ad ad, AdError adError) {
                        listener.onAdError("banner", adError.getErrorMessage());
                    }

                    @Override
                    public void onAdLoaded(Ad ad) {
                        listener.onAdLoaded("banner");
                    }

                    @Override
                    public void onAdClicked(Ad ad) {
                        listener.onAdClicked("banner");
                    }

                    @Override
                    public void onLoggingImpression(Ad ad) {
                        listener.onAdImpression("banner");
                    }
                }).build());

            adContainer.addView(adView);
            activity.addContentView(adContainer, params);
        });
    }

    public void hideBanner() {
        activity.runOnUiThread(() -> {
            if (adView != null) {
                adView.destroy();
                if (adContainer != null) adContainer.removeAllViews();
            }
        });
    }

    public void loadInterstitial(final String placementId) {
        activity.runOnUiThread(() -> {
            interstitialAd = new InterstitialAd(activity, placementId);
            interstitialAd.loadAd(interstitialAd.buildLoadAdConfig()
                .withAdListener(new InterstitialAdListener() {
                    @Override
                    public void onError(Ad ad, AdError error) {
                        listener.onAdError("interstitial", error.getErrorMessage());
                    }

                    @Override
                    public void onAdLoaded(Ad ad) {
                        listener.onAdLoaded("interstitial");
                    }

                    @Override
                    public void onAdClicked(Ad ad) {
                        listener.onAdClicked("interstitial");
                    }

                    @Override
                    public void onLoggingImpression(Ad ad) {
                        listener.onAdImpression("interstitial");
                    }

                    @Override
                    public void onInterstitialDisplayed(Ad ad) {}

                    @Override
                    public void onInterstitialDismissed(Ad ad) {
                        listener.onInterstitialDismissed();
                    }
                }).build());
        });
    }

    public void showInterstitial() {
        activity.runOnUiThread(() -> {
            if (interstitialAd != null && interstitialAd.isAdLoaded()) {
                interstitialAd.show();
            }
        });
    }

    public void loadRewarded(final String placementId) {
        activity.runOnUiThread(() -> {
            rewardedAd = new RewardedVideoAd(activity, placementId);
            rewardedAd.loadAd(rewardedAd.buildLoadAdConfig()
                .withAdListener(new RewardedVideoAdListener() {
                    @Override
                    public void onError(Ad ad, AdError error) {
                        listener.onAdError("rewarded", error.getErrorMessage());
                    }

                    @Override
                    public void onAdLoaded(Ad ad) {
                        listener.onAdLoaded("rewarded");
                    }

                    @Override
                    public void onAdClicked(Ad ad) {
                        listener.onAdClicked("rewarded");
                    }

                    @Override
                    public void onLoggingImpression(Ad ad) {
                        listener.onAdImpression("rewarded");
                    }

                    @Override
                    public void onRewardedVideoCompleted() {
                        listener.onRewardedCompleted();
                    }

                    @Override
                    public void onRewardedVideoClosed() {
                        listener.onRewardedDismissed();
                    }
                }).build());
        });
    }

    public void showRewarded() {
        activity.runOnUiThread(() -> {
            if (rewardedAd != null && rewardedAd.isAdLoaded()) {
                rewardedAd.show();
            }
        });
    }
}
