import re,os
root='android/app/src/main/'
m=open(root+'AndroidManifest.xml',encoding='utf-8').read()
if 'screenOrientation' not in m:
    m=re.sub(r'<activity\b','<activity android:screenOrientation="sensorLandscape"',m,count=1)
if 'android.permission.VIBRATE' not in m:
    m=m.replace('</manifest>','    <uses-permission android:name="android.permission.VIBRATE" />\n</manifest>')
open(root+'AndroidManifest.xml','w',encoding='utf-8').write(m)
d=root+'java/id/arjawinangun/racing/'
os.makedirs(d,exist_ok=True)
open(d+'MainActivity.java','w').write('''package id.arjawinangun.racing;
import android.os.Bundle;
import android.view.View;
import android.webkit.JavascriptInterface;
import com.getcapacitor.BridgeActivity;
public class MainActivity extends BridgeActivity {
  @Override public void onCreate(Bundle b){ super.onCreate(b); hide();
    getBridge().getWebView().addJavascriptInterface(new Object(){ @JavascriptInterface public void exit(){ runOnUiThread(new Runnable(){ public void run(){ finishAffinity(); System.exit(0); } }); } }, "AndroidExit"); }
  @Override public void onWindowFocusChanged(boolean f){ super.onWindowFocusChanged(f); if(f) hide(); }
  private void hide(){
    getWindow().getDecorView().setSystemUiVisibility(View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY|View.SYSTEM_UI_FLAG_FULLSCREEN|View.SYSTEM_UI_FLAG_HIDE_NAVIGATION|View.SYSTEM_UI_FLAG_LAYOUT_STABLE|View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN|View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION);
  }
}
''')
print('patched')
