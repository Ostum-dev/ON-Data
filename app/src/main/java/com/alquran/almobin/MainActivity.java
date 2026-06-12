package com.alquran.almobin;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.WindowManager;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private WebView webView;

    @SuppressLint("SetJavaScriptEnabled")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        
        // إبقاء الشاشة مضاءة دائماً أثناء قراءة القرآن
        getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
        
        setContentView(R.layout.activity_main);

        webView = findViewById(R.id.webView);
        WebSettings webSettings = webView.getSettings();

        // تفعيل الجافاسكربت والتخزين المحلي لحفظ خيارات المستخدم
        webSettings.setJavaScriptEnabled(true);
        webSettings.setDomStorageEnabled(true);
        webSettings.setDatabaseEnabled(true);
        
        // السماح بتشغيل الصوت تلقائياً والانتقال بين السور
        webSettings.setMediaPlaybackRequiresUserGesture(false);
        
        // تحسين سرعة التحميل
        webSettings.setCacheMode(WebSettings.LOAD_DEFAULT);

        // فتح الروابط داخل التطبيق بدلاً من متصفح خارجي
        webView.setWebViewClient(new WebViewClient());
        webView.setWebChromeClient(new WebChromeClient());

        // رابط موقعك الرسمي
        webView.loadUrl("https://alquran-almobin.blogspot.com/?m=1");
    }

    // جعل زر الرجوع في الهاتف يعود للخلف داخل الموقع بدلاً من إغلاق التطبيق
    @Override
    public void onBackPressed() {
        if (webView.canGoBack()) {
            webView.goBack();
        } else {
            super.onBackPressed();
        }
    }
}
