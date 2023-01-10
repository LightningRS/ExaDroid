# Fax UNMATCHED

## E-1
================================================================================
+ Fax error file: /AnkiDroid_crash_Error.txt
+ Component: com.ichi2.anki/com.ichi2.anki.Reviewer
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Undetected reason: Incomplete path summary

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{com.ichi2.anki/com.ichi2.anki.Reviewer}: java.lang.NullPointerException: Attempt to invoke virtual method 'long android.os.BaseBundle.getLong(java.lang.String, long)' on a null object reference
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2957)
	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:3032)
	at android.app.ActivityThread.-wrap11(Unknown Source:0)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1696)
	at android.os.Handler.dispatchMessage(Handler.java:105)
	at android.os.Looper.loop(Looper.java:164)
	at android.app.ActivityThread.main(ActivityThread.java:6944)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:327)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:1374)
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'long android.os.BaseBundle.getLong(java.lang.String, long)' on a null object reference
	at com.ichi2.anki.Reviewer.selectDeckFromExtra(Reviewer.java:81)
	at com.ichi2.anki.Reviewer.onCreate(Reviewer.java:73)
	at android.app.Activity.performCreate(Activity.java:7183)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1220)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2910)
	... 9 more
```
### ICC Msgs
```log
79	com.ichi2.anki.Reviewer	"android.intent.action.VIEW";;null;;null;;null;;Extras->ExtrasObj->ExtrasObj,(,long->deckId->Long.MIN_VALUE,),
78	com.ichi2.anki.Reviewer	"android.intent.action.VIEW";;null;;null;;null;;
80	com.ichi2.anki.Reviewer	"android.intent.action.VIEW";;null;;null;;null;;Extras->ExtrasObj->ExtrasObj,(,),
```

## E-2
================================================================================
+ Fax error file: /AntennaPod_crash_Error.txt
+ Component: de.danoeh.antennapod/de.danoeh.antennapod.activity.gpoddernet.GpodnetAuthenticationActivity
+ Exception types: java.lang.VerifyError
+ Undetected reason: Unknown-1

### BugInfo
```log
java.lang.VerifyError: Verifier rejected class de.danoeh.antennapod.core.gpoddernet.GpodnetService: java.lang.String de.danoeh.antennapod.core.gpoddernet.GpodnetService.executeRequestWithAuthentication(okhttp3.Request$Builder, java.lang.String, java.lang.String) failed to verify: java.lang.String de.danoeh.antennapod.core.gpoddernet.GpodnetService.executeRequestWithAuthentication(okhttp3.Request$Builder, java.lang.String, java.lang.String): [0x2A] 'this' argument 'Precise Reference: okhttp3.Request$Builder' not instance of 'Unresolved Reference: okhttv5.Request$Builder' (declaration of 'de.danoeh.antennapod.core.gpoddernet.GpodnetService' appears in /data/app/de.danoeh.antennapod-vCZIm9SQe_As-VYjSQKolQ==/base.apk)
	at de.danoeh.antennapod.activity.gpoddernet.GpodnetAuthenticationActivity.onCreate(GpodnetAuthenticationActivity.java:71)
	at android.app.Activity.performCreate(Activity.java:7183)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1220)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2910)
	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:3032)
	at android.app.ActivityThread.-wrap11(Unknown Source:0)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1696)
	at android.os.Handler.dispatchMessage(Handler.java:105)
	at android.os.Looper.loop(Looper.java:164)
	at android.app.ActivityThread.main(ActivityThread.java:6944)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:327)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:1374)
```
### ICC Msgs
```log
75	de.danoeh.antennapod.activity.gpoddernet.GpodnetAuthenticationActivity	null;;null;;null;;null;;
77	de.danoeh.antennapod.activity.gpoddernet.GpodnetAuthenticationActivity	null;;null;;null;;null;;Serializable->serObj->SerializableObj,
76	de.danoeh.antennapod.activity.gpoddernet.GpodnetAuthenticationActivity	null;;null;;null;;null;;Parcelable->parObj->ParcelableObj,
```

## E-3
================================================================================
+ Fax error file: /iNaturalist_crash_Error.txt
+ Component: org.inaturalist.android/org.inaturalist.android.ObservationListActivity
+ Exception types: java.lang.NullPointerException
+ Undetected reason: Unknown-2

### BugInfo
```log
java.lang.NullPointerException: Attempt to invoke interface method 'int android.database.Cursor.getPosition()' on a null object reference
	at org.inaturalist.android.Observation.<init>(Observation.java:265)
	at org.inaturalist.android.ObservationCursorAdapter.isLocked(ObservationCursorAdapter.java:753)
	at org.inaturalist.android.ObservationListActivity$ObservationsPageAdapter$5.onItemClick(ObservationListActivity.java:1146)
	at android.widget.AdapterView.performItemClick(AdapterView.java:350)
	at android.widget.AbsListView.performItemClick(AbsListView.java:1683)
	at android.widget.AbsListView$PerformClick.run(AbsListView.java:4094)
	at android.widget.AbsListView$10.run(AbsListView.java:6583)
	at android.os.Handler.handleCallback(Handler.java:789)
	at android.os.Handler.dispatchMessage(Handler.java:98)
	at android.os.Looper.loop(Looper.java:164)
	at android.app.ActivityThread.main(ActivityThread.java:6944)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:327)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:1374)
```
### ICC Msgs
```log
60	org.inaturalist.android.ObservationListActivity	null;;null;;"A";;null;;
```

## E-4
================================================================================
+ Fax error file: /OpenKeychain_crash_Error.txt
+ Component: org.sufficientlysecure.keychain/org.sufficientlysecure.keychain.ui.DecryptActivity
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Undetected reason: Multiple types for one extra in ICCBot ComponentModel

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{org.sufficientlysecure.keychain/org.sufficientlysecure.keychain.ui.DecryptActivity}: java.lang.NullPointerException: Attempt to invoke interface method 'int java.lang.CharSequence.length()' on a null object reference
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2957)
	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:3032)
	at android.app.ActivityThread.-wrap11(Unknown Source:0)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1696)
	at android.os.Handler.dispatchMessage(Handler.java:105)
	at android.os.Looper.loop(Looper.java:164)
	at android.app.ActivityThread.main(ActivityThread.java:6944)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:327)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:1374)
Caused by: java.lang.NullPointerException: Attempt to invoke interface method 'int java.lang.CharSequence.length()' on a null object reference
	at java.util.regex.Matcher.reset(Matcher.java:1045)
	at java.util.regex.Matcher.<init>(Matcher.java:174)
	at java.util.regex.Pattern.matcher(Pattern.java:1006)
	at org.sufficientlysecure.keychain.pgp.PgpHelper.getPgpMessageContent(PgpHelper.java:87)
	at org.sufficientlysecure.keychain.ui.DecryptActivity.readToTempFile(DecryptActivity.java:208)
	at org.sufficientlysecure.keychain.ui.DecryptActivity.handleActions(DecryptActivity.java:101)
	at org.sufficientlysecure.keychain.ui.DecryptActivity.onCreate(DecryptActivity.java:57)
	at android.app.Activity.performCreate(Activity.java:7183)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1220)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2910)
	... 9 more
```
### ICC Msgs
```log
121	org.sufficientlysecure.keychain.ui.DecryptActivity	"android.intent.action.SEND";;null;;null;;null;;StringArrayList->android.intent.extra.TEXT->abcde,
```

## E-5
================================================================================
+ Fax error file: /OpenKeychain_crash_Error.txt
+ Component: org.sufficientlysecure.keychain/org.sufficientlysecure.keychain.ui.DecryptActivity
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Undetected reason: Multiple types for one extra in ICCBot ComponentModel

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{org.sufficientlysecure.keychain/org.sufficientlysecure.keychain.ui.DecryptActivity}: java.lang.NullPointerException: Attempt to invoke virtual method 'java.util.Iterator java.util.ArrayList.iterator()' on a null object reference
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2957)
	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:3032)
	at android.app.ActivityThread.-wrap11(Unknown Source:0)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1696)
	at android.os.Handler.dispatchMessage(Handler.java:105)
	at android.os.Looper.loop(Looper.java:164)
	at android.app.ActivityThread.main(ActivityThread.java:6944)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:327)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:1374)
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'java.util.Iterator java.util.ArrayList.iterator()' on a null object reference
	at org.sufficientlysecure.keychain.ui.DecryptActivity.handleActions(DecryptActivity.java:114)
	at org.sufficientlysecure.keychain.ui.DecryptActivity.onCreate(DecryptActivity.java:57)
	at android.app.Activity.performCreate(Activity.java:7183)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1220)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2910)
	... 9 more
```
### ICC Msgs
```log
119	org.sufficientlysecure.keychain.ui.DecryptActivity	"android.intent.action.SEND_MULTIPLE";;null;;null;;null;;String->android.intent.extra.TEXT->!@#$%^ds:+_,
```

## E-6
================================================================================
+ Fax error file: /PassAndroid_crash_Error.txt
+ Component: org.ligi.passandroid/org.ligi.passandroid.ui.quirk_fix.USAirwaysLoadActivity
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Undetected reason: Delayed crash (timeout too short)

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{org.ligi.passandroid/org.ligi.passandroid.ui.quirk_fix.USAirwaysLoadActivity}: java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String android.net.Uri.toString()' on a null object reference
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2957)
	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:3032)
	at android.app.ActivityThread.-wrap11(Unknown Source:0)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1696)
	at android.os.Handler.dispatchMessage(Handler.java:105)
	at android.os.Looper.loop(Looper.java:164)
	at android.app.ActivityThread.main(ActivityThread.java:6944)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:327)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:1374)
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String android.net.Uri.toString()' on a null object reference
	at org.ligi.passandroid.ui.quirk_fix.USAirwaysLoadActivity.onCreate(SourceFile:15)
	at android.app.Activity.performCreate(Activity.java:7183)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1220)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2910)
	... 9 more
```
### ICC Msgs
```log
32	org.ligi.passandroid.ui.quirk_fix.USAirwaysLoadActivity	null;;null;;null;;null;;Parcelable->parObj->ParcelableObj,
28	org.ligi.passandroid.ui.quirk_fix.USAirwaysLoadActivity	"aaaaaag";;null;;null;;null;;
26	org.ligi.passandroid.ui.quirk_fix.USAirwaysLoadActivity	null;;null;;null;;null;;
27	org.ligi.passandroid.ui.quirk_fix.USAirwaysLoadActivity	"aaaag";;null;;null;;null;;
33	org.ligi.passandroid.ui.quirk_fix.USAirwaysLoadActivity	null;;null;;null;;null;;Serializable->serObj->SerializableObj,
30	org.ligi.passandroid.ui.quirk_fix.USAirwaysLoadActivity	"A";;null;;null;;null;;
```

## E-7
================================================================================
+ Fax error file: /PassAndroid_crash_Error.txt
+ Component: org.ligi.passandroid/org.ligi.passandroid.ui.quirk_fix.USAirwaysLoadActivity
+ Exception types: java.lang.ArrayIndexOutOfBoundsException, java.lang.RuntimeException
+ Undetected reason: Delayed crash (timeout too short)

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{org.ligi.passandroid/org.ligi.passandroid.ui.quirk_fix.USAirwaysLoadActivity}: java.lang.ArrayIndexOutOfBoundsException: length=1; index=-1
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2957)
	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:3032)
	at android.app.ActivityThread.-wrap11(Unknown Source:0)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1696)
	at android.os.Handler.dispatchMessage(Handler.java:105)
	at android.os.Looper.loop(Looper.java:164)
	at android.app.ActivityThread.main(ActivityThread.java:6944)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:327)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:1374)
Caused by: java.lang.ArrayIndexOutOfBoundsException: length=1; index=-1
	at org.ligi.passandroid.ui.quirk_fix.USAirwaysLoadActivity.onCreate(SourceFile:23)
	at android.app.Activity.performCreate(Activity.java:7183)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1220)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2910)
	... 9 more
```
### ICC Msgs
```log
31	org.ligi.passandroid.ui.quirk_fix.USAirwaysLoadActivity	"aaaaaag";;null;;"l";;null;;
29	org.ligi.passandroid.ui.quirk_fix.USAirwaysLoadActivity	null;;null;;"l";;null;;
```

## E-8
================================================================================
+ Fax error file: /PassAndroid_crash_Error.txt
+ Component: org.ligi.passandroid/org.ligi.passandroid.ui.quirk_fix.URLRewriteActivity
+ Exception types: java.lang.IllegalArgumentException, java.lang.RuntimeException
+ Undetected reason: Delayed crash (timeout too short)

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{org.ligi.passandroid/org.ligi.passandroid.ui.quirk_fix.URLRewriteActivity}: java.lang.IllegalArgumentException: Parameter specified as non-null is null: method kotlin.jvm.internal.Intrinsics.b, parameter uri
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2957)
	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:3032)
	at android.app.ActivityThread.-wrap11(Unknown Source:0)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1696)
	at android.os.Handler.dispatchMessage(Handler.java:105)
	at android.os.Looper.loop(Looper.java:164)
	at android.app.ActivityThread.main(ActivityThread.java:6944)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:327)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:1374)
Caused by: java.lang.IllegalArgumentException: Parameter specified as non-null is null: method kotlin.jvm.internal.Intrinsics.b, parameter uri
	at org.ligi.passandroid.ui.quirk_fix.URLRewriteController.a(Unknown Source:16)
	at org.ligi.passandroid.ui.quirk_fix.URLRewriteActivity.onCreate(SourceFile:17)
	at android.app.Activity.performCreate(Activity.java:7183)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1220)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2910)
	... 9 more
```
### ICC Msgs
```log
21	org.ligi.passandroid.ui.quirk_fix.URLRewriteActivity	null;;null;;null;;null;;Serializable->serObj->SerializableObj,
18	org.ligi.passandroid.ui.quirk_fix.URLRewriteActivity	null;;null;;null;;null;;
20	org.ligi.passandroid.ui.quirk_fix.URLRewriteActivity	null;;null;;null;;null;;Parcelable->parObj->ParcelableObj,
```

## E-9
================================================================================
+ Fax error file: /PassAndroid_crash_Error.txt
+ Component: org.ligi.passandroid/org.ligi.passandroid.ui.ExtractURLAsIphoneActivity
+ Exception types: java.lang.IllegalStateException, java.lang.RuntimeException
+ Undetected reason: Delayed crash (timeout too short)

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{org.ligi.passandroid/org.ligi.passandroid.ui.ExtractURLAsIphoneActivity}: java.lang.IllegalStateException: intent.data must not be null
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2957)
	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:3032)
	at android.app.ActivityThread.-wrap11(Unknown Source:0)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1696)
	at android.os.Handler.dispatchMessage(Handler.java:105)
	at android.os.Looper.loop(Looper.java:164)
	at android.app.ActivityThread.main(ActivityThread.java:6944)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:327)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:1374)
Caused by: java.lang.IllegalStateException: intent.data must not be null
	at org.ligi.passandroid.ui.ExtractURLAsIphoneActivity.onCreate(SourceFile:26)
	at android.app.Activity.performCreate(Activity.java:7183)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1220)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2910)
	... 9 more
```
### ICC Msgs
```log
23	org.ligi.passandroid.ui.ExtractURLAsIphoneActivity	"A";;null;;null;;null;;
24	org.ligi.passandroid.ui.ExtractURLAsIphoneActivity	null;;null;;null;;null;;Parcelable->parObj->ParcelableObj,
22	org.ligi.passandroid.ui.ExtractURLAsIphoneActivity	null;;null;;null;;null;;
25	org.ligi.passandroid.ui.ExtractURLAsIphoneActivity	null;;null;;null;;null;;Serializable->serObj->SerializableObj,
```

## E-10
================================================================================
+ Fax error file: /SuntimesWidget_crash_Error.txt
+ Component: com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.alarmclock.ui.AlarmDismissActivity
+ Exception types: java.lang.NumberFormatException, java.lang.RuntimeException
+ Undetected reason: Unknown-3

### BugInfo
```log
java.lang.RuntimeException: Unable to resume activity {com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.alarmclock.ui.AlarmDismissActivity}: java.lang.NumberFormatException: For input string: "A"
	at android.app.ActivityThread.performResumeActivity(ActivityThread.java:3790)
	at android.app.ActivityThread.handleResumeActivity(ActivityThread.java:3830)
	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:3038)
	at android.app.ActivityThread.-wrap11(Unknown Source:0)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1696)
	at android.os.Handler.dispatchMessage(Handler.java:105)
	at android.os.Looper.loop(Looper.java:164)
	at android.app.ActivityThread.main(ActivityThread.java:6944)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:327)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:1374)
Caused by: java.lang.NumberFormatException: For input string: "A"
	at java.lang.Long.parseLong(Long.java:590)
	at java.lang.Long.parseLong(Long.java:632)
	at android.content.ContentUris.parseId(ContentUris.java:86)
	at com.forrestguice.suntimeswidget.alarmclock.ui.AlarmDismissActivity.onResume(AlarmDismissActivity.java:223)
	at android.app.Instrumentation.callActivityOnResume(Instrumentation.java:1361)
	at android.app.Activity.performResume(Activity.java:7415)
	at android.app.ActivityThread.performResumeActivity(ActivityThread.java:3765)
	... 10 more
```
### ICC Msgs
```log
44	com.forrestguice.suntimeswidget.alarmclock.ui.AlarmDismissActivity	null;;null;;"A";;null;;
```

