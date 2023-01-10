# Fax MATCHED

## E-1
================================================================================
+ Fax error file: /AFWall+_crash_Error.txt
+ Component: dev.ukanth.ufirewall/dev.ukanth.ufirewall.plugin.LocaleEdit
+ Exception types: java.lang.NumberFormatException, java.lang.RuntimeException
+ Matched AACT Unique Crash: dev.ukanth.ufirewall/dev.ukanth.ufirewall.plugin.LocaleEdit	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{dev.ukanth.ufirewall/dev.ukanth.ufirewall.plugin.LocaleEdit}: java.lang.NumberFormatException: For input string: "999999999999999999999999999999999999999999999999999"
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
Caused by: java.lang.NumberFormatException: For input string: "999999999999999999999999999999999999999999999999999"
	at java.lang.Integer.parseInt(Integer.java:611)
	at java.lang.Integer.parseInt(Integer.java:643)
	at dev.ukanth.ufirewall.plugin.LocaleEdit.onCreate(LocaleEdit.java:109)
	at android.app.Activity.performCreate(Activity.java:7183)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1220)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2910)
	... 9 more
```
### ICC Msgs
```log
56	dev.ukanth.ufirewall.plugin.LocaleEdit	null;;null;;null;;null;;Bundle->com.twofortyfouram.locale.intent.extra.BUNDLE->BundleObj,(,String->dev.ukanth.ufirewall.plugin.APPLY_PROFILE->999999999999999999999999999999999999999999999999999,),
```

## E-2
================================================================================
+ Fax error file: /AnkiDroid_crash_Error.txt
+ Component: com.ichi2.anki/com.ichi2.anki.NoteEditor
+ Exception types: java.lang.NullPointerException
+ Matched AACT Unique Crash: com.ichi2.anki/com.ichi2.anki.NoteEditor	uc1

### BugInfo
```log
java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String android.os.Bundle.getString(java.lang.String)' on a null object reference
	at com.ichi2.anki.NoteEditor.fetchIntentInformation(NoteEditor.java:563)
	at com.ichi2.anki.NoteEditor.onCollectionLoaded(NoteEditor.java:407)
	at com.ichi2.anki.AnkiActivity.onLoadFinished(AnkiActivity.java:286)
	at com.ichi2.anki.AnkiActivity.onLoadFinished(AnkiActivity.java:42)
	at android.support.v4.app.LoaderManagerImpl$LoaderInfo.callOnLoadFinished(LoaderManager.java:476)
	at android.support.v4.app.LoaderManagerImpl$LoaderInfo.onLoadComplete(LoaderManager.java:444)
	at android.support.v4.content.Loader.deliverResult(Loader.java:126)
	at com.ichi2.async.CollectionLoader.deliverResult(CollectionLoader.java:42)
	at com.ichi2.async.CollectionLoader.deliverResult(CollectionLoader.java:12)
	at android.support.v4.content.AsyncTaskLoader.dispatchOnLoadComplete(AsyncTaskLoader.java:252)
	at android.support.v4.content.AsyncTaskLoader$LoadTask.onPostExecute(AsyncTaskLoader.java:80)
	at android.support.v4.content.ModernAsyncTask.finish(ModernAsyncTask.java:485)
	at android.support.v4.content.ModernAsyncTask$InternalHandler.handleMessage(ModernAsyncTask.java:502)
	at android.os.Handler.dispatchMessage(Handler.java:105)
	at android.os.Looper.loop(Looper.java:164)
	at android.app.ActivityThread.main(ActivityThread.java:6944)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:327)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:1374)
```
### ICC Msgs
```log
102	com.ichi2.anki.NoteEditor	"android.intent.action.SEND";;null;;null;;null;;
```

## E-3
================================================================================
+ Fax error file: /AnkiDroid_crash_Error.txt
+ Component: com.ichi2.anki/com.ichi2.anki.IntentHandler
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: com.ichi2.anki/com.ichi2.anki.IntentHandler	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{com.ichi2.anki/com.ichi2.anki.IntentHandler}: java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String android.net.Uri.getScheme()' on a null object reference
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
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String android.net.Uri.getScheme()' on a null object reference
	at com.ichi2.anki.IntentHandler.onCreate(IntentHandler.java:53)
	at android.app.Activity.performCreate(Activity.java:7183)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1220)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2910)
	... 9 more
```
### ICC Msgs
```log
41	com.ichi2.anki.IntentHandler	"android.intent.action.VIEW";;null;;"content://null:null/null";;"application/apkg";;
40	com.ichi2.anki.IntentHandler	"android.intent.action.VIEW";;null;;"content://null:null/null";;"aaaaaaaaaaaaaaan";;
```

## E-4
================================================================================
+ Fax error file: /AnkiDroid_crash_Error.txt
+ Component: com.ichi2.anki/com.ichi2.anki.NoteEditor
+ Exception types: java.lang.NullPointerException
+ Matched AACT Unique Crash: com.ichi2.anki/com.ichi2.anki.NoteEditor	uc3

### BugInfo
```log
java.lang.NullPointerException: Attempt to invoke virtual method 'boolean java.lang.String.equals(java.lang.Object)' on a null object reference
	at com.ichi2.anki.NoteEditor.onCollectionLoaded(NoteEditor.java:412)
	at com.ichi2.anki.AnkiActivity.onLoadFinished(AnkiActivity.java:286)
	at com.ichi2.anki.AnkiActivity.onLoadFinished(AnkiActivity.java:42)
	at android.support.v4.app.LoaderManagerImpl$LoaderInfo.callOnLoadFinished(LoaderManager.java:476)
	at android.support.v4.app.LoaderManagerImpl$LoaderInfo.onLoadComplete(LoaderManager.java:444)
	at android.support.v4.content.Loader.deliverResult(Loader.java:126)
	at com.ichi2.async.CollectionLoader.deliverResult(CollectionLoader.java:42)
	at com.ichi2.async.CollectionLoader.deliverResult(CollectionLoader.java:12)
	at android.support.v4.content.AsyncTaskLoader.dispatchOnLoadComplete(AsyncTaskLoader.java:252)
	at android.support.v4.content.AsyncTaskLoader$LoadTask.onPostExecute(AsyncTaskLoader.java:80)
	at android.support.v4.content.ModernAsyncTask.finish(ModernAsyncTask.java:485)
	at android.support.v4.content.ModernAsyncTask$InternalHandler.handleMessage(ModernAsyncTask.java:502)
	at android.os.Handler.dispatchMessage(Handler.java:105)
	at android.os.Looper.loop(Looper.java:164)
	at android.app.ActivityThread.main(ActivityThread.java:6944)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:327)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:1374)
```
### ICC Msgs
```log
103	com.ichi2.anki.NoteEditor	"org.openintents.action.CREATE_FLASHCARD";;null;;null;;null;;int->CALLER->0,
```

## E-5
================================================================================
+ Fax error file: /AnkiDroid_crash_Error.txt
+ Component: com.ichi2.anki/com.ichi2.anki.NoteEditor
+ Exception types: java.lang.NullPointerException
+ Matched AACT Unique Crash: com.ichi2.anki/com.ichi2.anki.NoteEditor	uc2

### BugInfo
```log
java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String android.os.Bundle.getString(java.lang.String)' on a null object reference
	at com.ichi2.anki.NoteEditor.fetchIntentInformation(NoteEditor.java:558)
	at com.ichi2.anki.NoteEditor.onCollectionLoaded(NoteEditor.java:407)
	at com.ichi2.anki.AnkiActivity.onLoadFinished(AnkiActivity.java:286)
	at com.ichi2.anki.AnkiActivity.onLoadFinished(AnkiActivity.java:42)
	at android.support.v4.app.LoaderManagerImpl$LoaderInfo.callOnLoadFinished(LoaderManager.java:476)
	at android.support.v4.app.LoaderManagerImpl$LoaderInfo.onLoadComplete(LoaderManager.java:444)
	at android.support.v4.content.Loader.deliverResult(Loader.java:126)
	at com.ichi2.async.CollectionLoader.deliverResult(CollectionLoader.java:42)
	at com.ichi2.async.CollectionLoader.deliverResult(CollectionLoader.java:12)
	at android.support.v4.content.AsyncTaskLoader.dispatchOnLoadComplete(AsyncTaskLoader.java:252)
	at android.support.v4.content.AsyncTaskLoader$LoadTask.onPostExecute(AsyncTaskLoader.java:80)
	at android.support.v4.content.ModernAsyncTask.finish(ModernAsyncTask.java:485)
	at android.support.v4.content.ModernAsyncTask$InternalHandler.handleMessage(ModernAsyncTask.java:502)
	at android.os.Handler.dispatchMessage(Handler.java:105)
	at android.os.Looper.loop(Looper.java:164)
	at android.app.ActivityThread.main(ActivityThread.java:6944)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:327)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:1374)
```
### ICC Msgs
```log
100	com.ichi2.anki.NoteEditor	"org.openintents.action.CREATE_FLASHCARD";;null;;null;;null;;
```

## E-6
================================================================================
+ Fax error file: /AnkiDroid_crash_Error.txt
+ Component: com.ichi2.anki/com.ichi2.anki.IntentHandler
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: com.ichi2.anki/com.ichi2.anki.IntentHandler	uc2

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{com.ichi2.anki/com.ichi2.anki.IntentHandler}: java.lang.NullPointerException: Attempt to invoke virtual method 'boolean java.lang.String.equals(java.lang.Object)' on a null object reference
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
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'boolean java.lang.String.equals(java.lang.Object)' on a null object reference
	at com.ichi2.anki.IntentHandler.onCreate(IntentHandler.java:69)
	at android.app.Activity.performCreate(Activity.java:7183)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1220)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2910)
	... 9 more
```
### ICC Msgs
```log
44	com.ichi2.anki.IntentHandler	"android.intent.action.VIEW";;null;;"content://null:null/null";;null;;
```

## E-7
================================================================================
+ Fax error file: /AntennaPod_crash_Error.txt
+ Component: de.danoeh.antennapod/de.danoeh.antennapod.activity.OnlineFeedViewActivity
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: de.danoeh.antennapod/de.danoeh.antennapod.activity.OnlineFeedViewActivity	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{de.danoeh.antennapod/de.danoeh.antennapod.activity.OnlineFeedViewActivity}: java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String java.lang.String.trim()' on a null object reference
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
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String java.lang.String.trim()' on a null object reference
	at android.arch.core.internal.SafeIterableMap$1.prepareURL(SafeIterableMap.java:53162)
	at de.danoeh.antennapod.activity.OnlineFeedViewActivity.startFeedDownload(OnlineFeedViewActivity.java:258)
	at de.danoeh.antennapod.activity.OnlineFeedViewActivity.onCreate(OnlineFeedViewActivity.java:159)
	at android.app.Activity.performCreate(Activity.java:7183)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1220)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2910)
	... 9 more
```
### ICC Msgs
```log
94	de.danoeh.antennapod.activity.OnlineFeedViewActivity	"android.intent.action.VIEW";;null;;null;;null;;String->title->abcde,
84	de.danoeh.antennapod.activity.OnlineFeedViewActivity	"android.intent.action.VIEW";;null;;null;;null;;
83	de.danoeh.antennapod.activity.OnlineFeedViewActivity	"android.intent.action.SEND";;null;;null;;null;;
79	de.danoeh.antennapod.activity.OnlineFeedViewActivity	"android.intent.action.SEND";;null;;null;;null;;String->title->!@#$%^ds:+_,
```

## E-8
================================================================================
+ Fax error file: /AntennaPod_crash_Error.txt
+ Component: de.danoeh.antennapod/de.danoeh.antennapod.activity.OnlineFeedViewActivity
+ Exception types: java.lang.IllegalArgumentException, java.lang.RuntimeException
+ Matched AACT Unique Crash: de.danoeh.antennapod/de.danoeh.antennapod.activity.OnlineFeedViewActivity	uc2

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{de.danoeh.antennapod/de.danoeh.antennapod.activity.OnlineFeedViewActivity}: java.lang.IllegalArgumentException: Activity must be started with feedurl argument!
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
Caused by: java.lang.IllegalArgumentException: Activity must be started with feedurl argument!
	at de.danoeh.antennapod.activity.OnlineFeedViewActivity.onCreate(OnlineFeedViewActivity.java:153)
	at android.app.Activity.performCreate(Activity.java:7183)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1220)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2910)
	... 9 more
```
### ICC Msgs
```log
78	de.danoeh.antennapod.activity.OnlineFeedViewActivity	null;;null;;null;;null;;
92	de.danoeh.antennapod.activity.OnlineFeedViewActivity	null;;null;;null;;null;;String->title->!@#$%^ds:+_,String->android.intent.extra.TEXT->!@#$%^ds:+_,
90	de.danoeh.antennapod.activity.OnlineFeedViewActivity	null;;null;;null;;null;;String->title->abcde,
91	de.danoeh.antennapod.activity.OnlineFeedViewActivity	null;;null;;null;;null;;String->title->abcde,
86	de.danoeh.antennapod.activity.OnlineFeedViewActivity	"A";;null;;null;;null;;
82	de.danoeh.antennapod.activity.OnlineFeedViewActivity	"A";;null;;null;;null;;String->title->abcde,
85	de.danoeh.antennapod.activity.OnlineFeedViewActivity	null;;null;;null;;null;;String->android.intent.extra.TEXT->999999999999999999999999999999999999999999999999999,
```

## E-9
================================================================================
+ Fax error file: /ch.hgdev.toposuite_1.0.3_56_crash_EA.txt
+ Component: ch.hgdev.toposuite/ch.hgdev.toposuite.points.PointsManagerActivity
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: ch.hgdev.toposuite/ch.hgdev.toposuite.points.PointsManagerActivity	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{ch.hgdev.toposuite/ch.hgdev.toposuite.points.PointsManagerActivity}: java.lang.NullPointerException: Attempt to invoke virtual method 'boolean java.lang.String.equals(java.lang.Object)' on a null object reference
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2698)
	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:2759)
	at android.app.ActivityThread.-wrap12(ActivityThread.java)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1482)
	at android.os.Handler.dispatchMessage(Handler.java:102)
	at android.os.Looper.loop(Looper.java:154)
	at android.app.ActivityThread.main(ActivityThread.java:6190)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:892)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:782)
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'boolean java.lang.String.equals(java.lang.Object)' on a null object reference
	at ch.hgdev.toposuite.points.PointsManagerActivity.onCreate(PointsManagerActivity.java)
	at android.app.Activity.performCreate(Activity.java:6701)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1118)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2651)
	... 9 more
```
### ICC Msgs
```log
168	ch.hgdev.toposuite.points.PointsManagerActivity	null;;null;;"aaaag";;null;;
171	ch.hgdev.toposuite.points.PointsManagerActivity	null;;null;;"l";;null;;
167	ch.hgdev.toposuite.points.PointsManagerActivity	null;;null;;"A";;null;;
```

## E-10
================================================================================
+ Fax error file: /CSipSimple_crash_Error.txt
+ Component: com.csipsimple/com.csipsimple.ui.incall.InCallActivity
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: com.csipsimple/com.csipsimple.ui.incall.InCallActivity	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to resume activity {com.csipsimple/com.csipsimple.ui.incall.InCallActivity}: java.lang.NullPointerException: Attempt to invoke a virtual method on a null object reference
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
Caused by: java.lang.NullPointerException: Attempt to invoke a virtual method on a null object reference
	at com.csipsimple.ui.incall.InCallActivity$UpdateUIFromCallRunnable.run(InCallActivity.java:497)
	at android.app.Activity.runOnUiThread(Activity.java:6281)
	at com.csipsimple.ui.incall.InCallActivity.onResume(InCallActivity.java:255)
	at android.app.Instrumentation.callActivityOnResume(Instrumentation.java:1361)
	at android.app.Activity.performResume(Activity.java:7415)
	at android.app.ActivityThread.performResumeActivity(ActivityThread.java:3765)
	... 10 more
```
### ICC Msgs
```log
111	com.csipsimple.ui.incall.InCallActivity	null;;null;;null;;null;;
```

## E-11
================================================================================
+ Fax error file: /CSipSimple_crash_Error.txt
+ Component: com.csipsimple/com.csipsimple.ui.outgoingcall.OutgoingCallChooser
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: com.csipsimple/com.csipsimple.ui.outgoingcall.OutgoingCallChooser	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{com.csipsimple/com.csipsimple.ui.outgoingcall.OutgoingCallChooser}: java.lang.NullPointerException: Attempt to invoke virtual method 'boolean java.lang.String.equals(java.lang.Object)' on a null object reference
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
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'boolean java.lang.String.equals(java.lang.Object)' on a null object reference
	at android.telephony.PhoneNumberUtils.getNumberFromIntent(PhoneNumberUtils.java:268)
	at com.csipsimple.ui.outgoingcall.OutgoingCallChooser.getPhoneNumber(OutgoingCallChooser.java:85)
	at com.csipsimple.ui.outgoingcall.OutgoingCallChooser.onCreate(OutgoingCallChooser.java:56)
	at android.app.Activity.performCreate(Activity.java:7183)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1220)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2910)
	... 9 more
```
### ICC Msgs
```log
89	com.csipsimple.ui.outgoingcall.OutgoingCallChooser	"aaaaaaab";;null;;"aaaao";;null;;
97	com.csipsimple.ui.outgoingcall.OutgoingCallChooser	null;;null;;"aaaao";;null;;
98	com.csipsimple.ui.outgoingcall.OutgoingCallChooser	"android.intent.action.SENDTO";;null;;"aaaaaaaaaaaaaaI";;null;;
103	com.csipsimple.ui.outgoingcall.OutgoingCallChooser	"aaaaaaaaaaaaaaI";;null;;"aas";;null;;
90	com.csipsimple.ui.outgoingcall.OutgoingCallChooser	null;;null;;"aaaaaaaaaaaaaaI";;null;;
107	com.csipsimple.ui.outgoingcall.OutgoingCallChooser	null;;null;;"aas";;null;;
104	com.csipsimple.ui.outgoingcall.OutgoingCallChooser	"aaaaaaaaaaaaaaI";;null;;"aas";;null;;
95	com.csipsimple.ui.outgoingcall.OutgoingCallChooser	null;;null;;"aah";;null;;
105	com.csipsimple.ui.outgoingcall.OutgoingCallChooser	null;;null;;"aas";;null;;
101	com.csipsimple.ui.outgoingcall.OutgoingCallChooser	"android.intent.action.SENDTO";;null;;"aah";;null;;
106	com.csipsimple.ui.outgoingcall.OutgoingCallChooser	null;;null;;"t";;null;;
92	com.csipsimple.ui.outgoingcall.OutgoingCallChooser	"x";;null;;"t";;null;;
```

## E-12
================================================================================
+ Fax error file: /fr.ybo.transportsrennes_3.8.4_384_crash_EA.txt
+ Component: fr.ybo.transportsrennes/fr.ybo.transportsrennes.activity.widgets.TransportsWidget21Configure
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: fr.ybo.transportsrennes/fr.ybo.transportsrennes.activity.widgets.TransportsWidget21Configure	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{fr.ybo.transportsrennes/fr.ybo.transportsrennes.activity.widgets.TransportsWidget21Configure}: java.lang.NullPointerException: Attempt to invoke virtual method 'int android.os.Bundle.getInt(java.lang.String, int)' on a null object reference
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2698)
	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:2759)
	at android.app.ActivityThread.-wrap12(ActivityThread.java)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1482)
	at android.os.Handler.dispatchMessage(Handler.java:102)
	at android.os.Looper.loop(Looper.java:154)
	at android.app.ActivityThread.main(ActivityThread.java:6190)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:892)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:782)
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'int android.os.Bundle.getInt(java.lang.String, int)' on a null object reference
	at fr.ybo.transportsrennes.activity.widgets.TransportsWidget21Configure.onCreate(TransportsWidget21Configure.java)
	at android.app.Activity.performCreate(Activity.java:6701)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1118)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2651)
	... 9 more
```
### ICC Msgs
```log
26	fr.ybo.transportsrennes.activity.widgets.TransportsWidget21Configure	null;;null;;null;;null;;Extras->ExtrasObj->ExtrasObj,(,int->appWidgetId->Integer.MAX_VALUE,),
27	fr.ybo.transportsrennes.activity.widgets.TransportsWidget21Configure	null;;null;;null;;null;;
28	fr.ybo.transportsrennes.activity.widgets.TransportsWidget21Configure	null;;null;;null;;null;;Extras->ExtrasObj->ExtrasObj,(,),
```

## E-13
================================================================================
+ Fax error file: /fr.ybo.transportsrennes_3.8.4_384_crash_EA.txt
+ Component: fr.ybo.transportsrennes/fr.ybo.transportsrennes.activity.widgets.TransportsWidgetConfigure
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: fr.ybo.transportsrennes/fr.ybo.transportsrennes.activity.widgets.TransportsWidgetConfigure	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{fr.ybo.transportsrennes/fr.ybo.transportsrennes.activity.widgets.TransportsWidgetConfigure}: java.lang.NullPointerException: Attempt to invoke virtual method 'int android.os.Bundle.getInt(java.lang.String, int)' on a null object reference
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2698)
	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:2759)
	at android.app.ActivityThread.-wrap12(ActivityThread.java)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1482)
	at android.os.Handler.dispatchMessage(Handler.java:102)
	at android.os.Looper.loop(Looper.java:154)
	at android.app.ActivityThread.main(ActivityThread.java:6190)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:892)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:782)
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'int android.os.Bundle.getInt(java.lang.String, int)' on a null object reference
	at fr.ybo.transportsrennes.activity.widgets.TransportsWidgetConfigure.onCreate(TransportsWidgetConfigure.java)
	at android.app.Activity.performCreate(Activity.java:6701)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1118)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2651)
	... 9 more
```
### ICC Msgs
```log
15	fr.ybo.transportsrennes.activity.widgets.TransportsWidgetConfigure	null;;null;;null;;null;;Extras->ExtrasObj->ExtrasObj,(,int->appWidgetId->Integer.MAX_VALUE,),
16	fr.ybo.transportsrennes.activity.widgets.TransportsWidgetConfigure	null;;null;;null;;null;;
17	fr.ybo.transportsrennes.activity.widgets.TransportsWidgetConfigure	null;;null;;null;;null;;Extras->ExtrasObj->ExtrasObj,(,),
```

## E-14
================================================================================
+ Fax error file: /fr.ybo.transportsrennes_3.8.4_384_crash_EA.txt
+ Component: fr.ybo.transportsrennes/fr.ybo.transportsrennes.activity.bus.ListArret
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: fr.ybo.transportsrennes/fr.ybo.transportsrennes.activity.bus.ListArret	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{fr.ybo.transportsrennes/fr.ybo.transportsrennes.activity.bus.ListArret}: java.lang.NullPointerException: Attempt to invoke virtual method 'java.io.Serializable android.os.Bundle.getSerializable(java.lang.String)' on a null object reference
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2698)
	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:2759)
	at android.app.ActivityThread.-wrap12(ActivityThread.java)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1482)
	at android.os.Handler.dispatchMessage(Handler.java:102)
	at android.os.Looper.loop(Looper.java:154)
	at android.app.ActivityThread.main(ActivityThread.java:6190)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:892)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:782)
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'java.io.Serializable android.os.Bundle.getSerializable(java.lang.String)' on a null object reference
	at fr.ybo.transportscommun.activity.bus.AbstractListArret.onCreate(AbstractListArret.java)
	at android.app.Activity.performCreate(Activity.java:6701)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1118)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2651)
	... 9 more
```
### ICC Msgs
```log
102	fr.ybo.transportsrennes.activity.bus.ListArret	null;;null;;null;;null;;
```

## E-15
================================================================================
+ Fax error file: /fr.ybo.transportsrennes_3.8.4_384_crash_EA.txt
+ Component: fr.ybo.transportsrennes/fr.ybo.transportsrennes.activity.timeo.TimeoActivity
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: fr.ybo.transportsrennes/fr.ybo.transportsrennes.activity.timeo.TimeoActivity	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{fr.ybo.transportsrennes/fr.ybo.transportsrennes.activity.timeo.TimeoActivity}: java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String android.net.Uri.getLastPathSegment()' on a null object reference
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2698)
	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:2759)
	at android.app.ActivityThread.-wrap12(ActivityThread.java)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1482)
	at android.os.Handler.dispatchMessage(Handler.java:102)
	at android.os.Looper.loop(Looper.java:154)
	at android.app.ActivityThread.main(ActivityThread.java:6190)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:892)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:782)
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String android.net.Uri.getLastPathSegment()' on a null object reference
	at fr.ybo.transportsrennes.activity.timeo.TimeoActivity.onCreate(TimeoActivity.java)
	at android.app.Activity.performCreate(Activity.java:6701)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1118)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2651)
	... 9 more
```
### ICC Msgs
```log
34	fr.ybo.transportsrennes.activity.timeo.TimeoActivity	null;;null;;null;;null;;Serializable->serObj->SerializableObj,
31	fr.ybo.transportsrennes.activity.timeo.TimeoActivity	"A";;null;;null;;null;;
32	fr.ybo.transportsrennes.activity.timeo.TimeoActivity	null;;null;;null;;null;;
33	fr.ybo.transportsrennes.activity.timeo.TimeoActivity	null;;null;;null;;null;;Parcelable->parObj->ParcelableObj,
```

## E-16
================================================================================
+ Fax error file: /fr.ybo.transportsrennes_3.8.4_384_crash_EA.txt
+ Component: fr.ybo.transportsrennes/fr.ybo.transportsrennes.activity.widgets.TransportsWidgetLowResConfigure
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: fr.ybo.transportsrennes/fr.ybo.transportsrennes.activity.widgets.TransportsWidgetLowResConfigure	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{fr.ybo.transportsrennes/fr.ybo.transportsrennes.activity.widgets.TransportsWidgetLowResConfigure}: java.lang.NullPointerException: Attempt to invoke virtual method 'int android.os.Bundle.getInt(java.lang.String, int)' on a null object reference
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2698)
	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:2759)
	at android.app.ActivityThread.-wrap12(ActivityThread.java)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1482)
	at android.os.Handler.dispatchMessage(Handler.java:102)
	at android.os.Looper.loop(Looper.java:154)
	at android.app.ActivityThread.main(ActivityThread.java:6190)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:892)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:782)
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'int android.os.Bundle.getInt(java.lang.String, int)' on a null object reference
	at fr.ybo.transportsrennes.activity.widgets.TransportsWidgetLowResConfigure.onCreate(TransportsWidgetLowResConfigure.java)
	at android.app.Activity.performCreate(Activity.java:6701)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1118)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2651)
	... 9 more
```
### ICC Msgs
```log
45	fr.ybo.transportsrennes.activity.widgets.TransportsWidgetLowResConfigure	null;;null;;null;;null;;
44	fr.ybo.transportsrennes.activity.widgets.TransportsWidgetLowResConfigure	null;;null;;null;;null;;Extras->ExtrasObj->ExtrasObj,(,int->appWidgetId->Integer.MAX_VALUE,),
46	fr.ybo.transportsrennes.activity.widgets.TransportsWidgetLowResConfigure	null;;null;;null;;null;;Extras->ExtrasObj->ExtrasObj,(,),
```

## E-17
================================================================================
+ Fax error file: /fr.ybo.transportsrennes_3.8.4_384_crash_EA.txt
+ Component: fr.ybo.transportsrennes/fr.ybo.transportsrennes.activity.widgets.TransportsWidget11Configure
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: fr.ybo.transportsrennes/fr.ybo.transportsrennes.activity.widgets.TransportsWidget11Configure	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{fr.ybo.transportsrennes/fr.ybo.transportsrennes.activity.widgets.TransportsWidget11Configure}: java.lang.NullPointerException: Attempt to invoke virtual method 'int android.os.Bundle.getInt(java.lang.String, int)' on a null object reference
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2698)
	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:2759)
	at android.app.ActivityThread.-wrap12(ActivityThread.java)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1482)
	at android.os.Handler.dispatchMessage(Handler.java:102)
	at android.os.Looper.loop(Looper.java:154)
	at android.app.ActivityThread.main(ActivityThread.java:6190)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:892)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:782)
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'int android.os.Bundle.getInt(java.lang.String, int)' on a null object reference
	at fr.ybo.transportsrennes.activity.widgets.TransportsWidget11Configure.onCreate(TransportsWidget11Configure.java)
	at android.app.Activity.performCreate(Activity.java:6701)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1118)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2651)
	... 9 more
```
### ICC Msgs
```log
96	fr.ybo.transportsrennes.activity.widgets.TransportsWidget11Configure	null;;null;;null;;null;;Extras->ExtrasObj->ExtrasObj,(,),
95	fr.ybo.transportsrennes.activity.widgets.TransportsWidget11Configure	null;;null;;null;;null;;
94	fr.ybo.transportsrennes.activity.widgets.TransportsWidget11Configure	null;;null;;null;;null;;Extras->ExtrasObj->ExtrasObj,(,int->appWidgetId->Integer.MAX_VALUE,),
```

## E-18
================================================================================
+ Fax error file: /OpenGPSTracker_crash_Error.txt
+ Component: nl.sogeti.android.gpstracker/nl.sogeti.android.gpstracker.actions.ShareTrack
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: nl.sogeti.android.gpstracker/nl.sogeti.android.gpstracker.actions.ShareTrack	uc2

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{nl.sogeti.android.gpstracker/nl.sogeti.android.gpstracker.actions.ShareTrack}: java.lang.NullPointerException: uri
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
Caused by: java.lang.NullPointerException: uri
	at com.android.internal.util.Preconditions.checkNotNull(Preconditions.java:128)
	at android.content.ContentResolver.query(ContentResolver.java:743)
	at android.content.ContentResolver.query(ContentResolver.java:710)
	at android.content.ContentResolver.query(ContentResolver.java:668)
	at nl.sogeti.android.gpstracker.actions.ShareTrack.queryForTrackName(ShareTrack.java:617)
	at nl.sogeti.android.gpstracker.actions.ShareTrack.onCreate(ShareTrack.java:206)
	at android.app.Activity.performCreate(Activity.java:7183)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1220)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2910)
	... 9 more
```
### ICC Msgs
```log
32	nl.sogeti.android.gpstracker.actions.ShareTrack	null;;null;;null;;null;;
35	nl.sogeti.android.gpstracker.actions.ShareTrack	null;;null;;null;;null;;Serializable->serObj->SerializableObj,
33	nl.sogeti.android.gpstracker.actions.ShareTrack	"A";;null;;null;;null;;
34	nl.sogeti.android.gpstracker.actions.ShareTrack	null;;null;;null;;null;;Parcelable->parObj->ParcelableObj,
```

## E-19
================================================================================
+ Fax error file: /OpenGPSTracker_crash_Error.txt
+ Component: nl.sogeti.android.gpstracker/nl.sogeti.android.gpstracker.viewer.LoggerMap
+ Exception types: java.lang.NumberFormatException, java.lang.RuntimeException
+ Matched AACT Unique Crash: nl.sogeti.android.gpstracker/nl.sogeti.android.gpstracker.viewer.LoggerMap	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{nl.sogeti.android.gpstracker/nl.sogeti.android.gpstracker.viewer.LoggerMap}: java.lang.NumberFormatException: For input string: "A"
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
Caused by: java.lang.NumberFormatException: For input string: "A"
	at java.lang.Long.parseLong(Long.java:590)
	at java.lang.Long.parseLong(Long.java:632)
	at nl.sogeti.android.gpstracker.viewer.LoggerMap.onRestoreInstanceState(LoggerMap.java:353)
	at nl.sogeti.android.gpstracker.viewer.LoggerMap.onCreate(LoggerMap.java:223)
	at android.app.Activity.performCreate(Activity.java:7183)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1220)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2910)
	... 9 more
```
### ICC Msgs
```log
9	nl.sogeti.android.gpstracker.viewer.LoggerMap	null;;null;;"A";;null;;
```

## E-20
================================================================================
+ Fax error file: /OpenKeychain_crash_Error.txt
+ Component: org.sufficientlysecure.keychain/org.sufficientlysecure.keychain.ui.keyview.ViewKeyActivity
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: org.sufficientlysecure.keychain/org.sufficientlysecure.keychain.ui.keyview.ViewKeyActivity	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{org.sufficientlysecure.keychain/org.sufficientlysecure.keychain.ui.keyview.ViewKeyActivity}: java.lang.NullPointerException: Attempt to invoke virtual method 'boolean java.lang.String.equals(java.lang.Object)' on a null object reference
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
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'boolean java.lang.String.equals(java.lang.Object)' on a null object reference
	at org.sufficientlysecure.keychain.ui.keyview.ViewKeyActivity.onCreate(ViewKeyActivity.java:244)
	at android.app.Activity.performCreate(Activity.java:7183)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1220)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2910)
	... 9 more
```
### ICC Msgs
```log
301	org.sufficientlysecure.keychain.ui.keyview.ViewKeyActivity	null;;null;;"aaK";;null;;
302	org.sufficientlysecure.keychain.ui.keyview.ViewKeyActivity	null;;null;;"l";;null;;
```

## E-21
================================================================================
+ Fax error file: /OpenKeychain_crash_Error.txt
+ Component: org.sufficientlysecure.keychain/org.sufficientlysecure.keychain.ui.UsbEventReceiverActivity
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: org.sufficientlysecure.keychain/org.sufficientlysecure.keychain.ui.UsbEventReceiverActivity	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to resume activity {org.sufficientlysecure.keychain/org.sufficientlysecure.keychain.ui.UsbEventReceiverActivity}: java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String android.hardware.usb.UsbDevice.getDeviceName()' on a null object reference
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
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String android.hardware.usb.UsbDevice.getDeviceName()' on a null object reference
	at org.sufficientlysecure.keychain.securitytoken.UsbConnectionDispatcher.requestPermissionForUsbDevice(UsbConnectionDispatcher.java:128)
	at org.sufficientlysecure.keychain.ui.UsbEventReceiverActivity.onResume(UsbEventReceiverActivity.java:39)
	at android.app.Instrumentation.callActivityOnResume(Instrumentation.java:1361)
	at android.app.Activity.performResume(Activity.java:7415)
	at android.app.ActivityThread.performResumeActivity(ActivityThread.java:3765)
	... 10 more
```
### ICC Msgs
```log
156	org.sufficientlysecure.keychain.ui.UsbEventReceiverActivity	"android.hardware.usb.action.USB_DEVICE_ATTACHED";;null;;null;;null;;
```

## E-22
================================================================================
+ Fax error file: /OpenKeychain_crash_Error.txt
+ Component: org.sufficientlysecure.keychain/org.sufficientlysecure.keychain.ui.keyview.ViewKeyActivity
+ Exception types: java.lang.IllegalArgumentException, java.lang.RuntimeException
+ Matched AACT Unique Crash: org.sufficientlysecure.keychain/org.sufficientlysecure.keychain.ui.keyview.ViewKeyActivity	uc4

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{org.sufficientlysecure.keychain/org.sufficientlysecure.keychain.ui.keyview.ViewKeyActivity}: java.lang.IllegalArgumentException: Missing required extra master_key_id or contact uri
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
Caused by: java.lang.IllegalArgumentException: Missing required extra master_key_id or contact uri
	at org.sufficientlysecure.keychain.ui.keyview.ViewKeyActivity.onCreate(ViewKeyActivity.java:254)
	at android.app.Activity.performCreate(Activity.java:7183)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1220)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2910)
	... 9 more
```
### ICC Msgs
```log
297	org.sufficientlysecure.keychain.ui.keyview.ViewKeyActivity	null;;null;;"null://aaaaaag:null/null";;null;;
294	org.sufficientlysecure.keychain.ui.keyview.ViewKeyActivity	null;;null;;null;;null;;
```

## E-23
================================================================================
+ Fax error file: /OpenKeychain_crash_Error.txt
+ Component: org.sufficientlysecure.keychain/org.sufficientlysecure.keychain.ui.EncryptFilesActivity
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: org.sufficientlysecure.keychain/org.sufficientlysecure.keychain.ui.EncryptFilesActivity	uc2

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{org.sufficientlysecure.keychain/org.sufficientlysecure.keychain.ui.EncryptFilesActivity}: java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String android.net.Uri.getScheme()' on a null object reference
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
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String android.net.Uri.getScheme()' on a null object reference
	at org.sufficientlysecure.keychain.ui.EncryptFilesFragment.checkAndRequestReadPermission(EncryptFilesFragment.java:283)
	at org.sufficientlysecure.keychain.ui.EncryptFilesFragment.processPendingInputUris(EncryptFilesFragment.java:253)
	at org.sufficientlysecure.keychain.ui.EncryptFilesFragment.onCreateView(EncryptFilesFragment.java:168)
	at android.support.v4.app.Fragment.performCreateView(Fragment.java:2346)
	at android.support.v4.app.FragmentManagerImpl.moveToState(FragmentManager.java:1428)
	at android.support.v4.app.FragmentManagerImpl.moveFragmentToExpectedState(FragmentManager.java:1759)
	at android.support.v4.app.FragmentManagerImpl.moveToState(FragmentManager.java:1827)
	at android.support.v4.app.BackStackRecord.executeOps(BackStackRecord.java:797)
	at android.support.v4.app.FragmentManagerImpl.executeOps(FragmentManager.java:2596)
	at android.support.v4.app.FragmentManagerImpl.executeOpsTogether(FragmentManager.java:2383)
	at android.support.v4.app.FragmentManagerImpl.removeRedundantOperationsAndExecute(FragmentManager.java:2338)
	at android.support.v4.app.FragmentManagerImpl.execPendingActions(FragmentManager.java:2245)
	at android.support.v4.app.FragmentManagerImpl.dispatchStateChange(FragmentManager.java:3248)
	at android.support.v4.app.FragmentManagerImpl.dispatchActivityCreated(FragmentManager.java:3200)
	at android.support.v4.app.FragmentController.dispatchActivityCreated(FragmentController.java:195)
	at android.support.v4.app.FragmentActivity.onStart(FragmentActivity.java:597)
	at android.support.v7.app.AppCompatActivity.onStart(AppCompatActivity.java:177)
	at android.app.Instrumentation.callActivityOnStart(Instrumentation.java:1340)
	at android.app.Activity.performStart(Activity.java:7200)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2920)
	... 9 more
```
### ICC Msgs
```log
335	org.sufficientlysecure.keychain.ui.EncryptFilesActivity	"android.intent.action.SEND";;null;;null;;"aah";;
318	org.sufficientlysecure.keychain.ui.EncryptFilesActivity	"android.intent.action.SEND";;null;;"aas";;"aaaaaaaaaaaaaaI";;
```

## E-24
================================================================================
+ Fax error file: /OpenKeychain_crash_Error.txt
+ Component: org.sufficientlysecure.keychain/org.sufficientlysecure.keychain.ui.ImportKeysProxyActivity
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: org.sufficientlysecure.keychain/org.sufficientlysecure.keychain.ui.ImportKeysProxyActivity	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{org.sufficientlysecure.keychain/org.sufficientlysecure.keychain.ui.ImportKeysProxyActivity}: java.lang.NullPointerException: Attempt to read from null array
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
Caused by: java.lang.NullPointerException: Attempt to read from null array
	at org.sufficientlysecure.keychain.ui.ImportKeysProxyActivity.handleActionNdefDiscovered(ImportKeysProxyActivity.java:288)
	at org.sufficientlysecure.keychain.ui.ImportKeysProxyActivity.handleActions(ImportKeysProxyActivity.java:97)
	at org.sufficientlysecure.keychain.ui.ImportKeysProxyActivity.onCreate(ImportKeysProxyActivity.java:79)
	at android.app.Activity.performCreate(Activity.java:7183)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1220)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2910)
	... 9 more
```
### ICC Msgs
```log
267	org.sufficientlysecure.keychain.ui.ImportKeysProxyActivity	"android.nfc.action.NDEF_DISCOVERED";;null;;null;;null;;
```

## E-25
================================================================================
+ Fax error file: /OpenKeychain_crash_Error.txt
+ Component: org.sufficientlysecure.keychain/org.sufficientlysecure.keychain.ui.DebugActionsActivity
+ Exception types: java.lang.RuntimeException, java.lang.UnsupportedOperationException
+ Matched AACT Unique Crash: org.sufficientlysecure.keychain/org.sufficientlysecure.keychain.ui.DebugActionsActivity	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{org.sufficientlysecure.keychain/org.sufficientlysecure.keychain.ui.DebugActionsActivity}: java.lang.UnsupportedOperationException
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
Caused by: java.lang.UnsupportedOperationException
	at org.sufficientlysecure.keychain.ui.DebugActionsActivity.onCreate(DebugActionsActivity.java:68)
	at android.app.Activity.performCreate(Activity.java:7183)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1220)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2910)
	... 9 more
```
### ICC Msgs
```log
243	org.sufficientlysecure.keychain.ui.DebugActionsActivity	null;;null;;null;;null;;Parcelable->parObj->ParcelableObj,
242	org.sufficientlysecure.keychain.ui.DebugActionsActivity	null;;null;;null;;null;;
244	org.sufficientlysecure.keychain.ui.DebugActionsActivity	null;;null;;null;;null;;Serializable->serObj->SerializableObj,
```

## E-26
================================================================================
+ Fax error file: /OpenKeychain_crash_Error.txt
+ Component: org.sufficientlysecure.keychain/org.sufficientlysecure.keychain.ui.EncryptFilesActivity
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: org.sufficientlysecure.keychain/org.sufficientlysecure.keychain.ui.EncryptFilesActivity	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{org.sufficientlysecure.keychain/org.sufficientlysecure.keychain.ui.EncryptFilesActivity}: java.lang.NullPointerException: name
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
Caused by: java.lang.NullPointerException: name
	at com.android.internal.util.Preconditions.checkNotNull(Preconditions.java:128)
	at android.content.ContentResolver.acquireUnstableContentProviderClient(ContentResolver.java:1888)
	at android.provider.DocumentsContract.getDocumentThumbnail(DocumentsContract.java:1042)
	at org.sufficientlysecure.keychain.util.FileHelper.getThumbnail(FileHelper.java:222)
	at org.sufficientlysecure.keychain.ui.EncryptFilesFragment$FilesAdapter$ViewModel.<init>(EncryptFilesFragment.java:794)
	at org.sufficientlysecure.keychain.ui.EncryptFilesFragment$FilesAdapter.add(EncryptFilesFragment.java:927)
	at org.sufficientlysecure.keychain.ui.EncryptFilesFragment.processPendingInputUris(EncryptFilesFragment.java:259)
	at org.sufficientlysecure.keychain.ui.EncryptFilesFragment.onCreateView(EncryptFilesFragment.java:168)
	at android.support.v4.app.Fragment.performCreateView(Fragment.java:2346)
	at android.support.v4.app.FragmentManagerImpl.moveToState(FragmentManager.java:1428)
	at android.support.v4.app.FragmentManagerImpl.moveFragmentToExpectedState(FragmentManager.java:1759)
	at android.support.v4.app.FragmentManagerImpl.moveToState(FragmentManager.java:1827)
	at android.support.v4.app.BackStackRecord.executeOps(BackStackRecord.java:797)
	at android.support.v4.app.FragmentManagerImpl.executeOps(FragmentManager.java:2596)
	at android.support.v4.app.FragmentManagerImpl.executeOpsTogether(FragmentManager.java:2383)
	at android.support.v4.app.FragmentManagerImpl.removeRedundantOperationsAndExecute(FragmentManager.java:2338)
	at android.support.v4.app.FragmentManagerImpl.execPendingActions(FragmentManager.java:2245)
	at android.support.v4.app.FragmentManagerImpl.dispatchStateChange(FragmentManager.java:3248)
	at android.support.v4.app.FragmentManagerImpl.dispatchActivityCreated(FragmentManager.java:3200)
	at android.support.v4.app.FragmentController.dispatchActivityCreated(FragmentController.java:195)
	at android.support.v4.app.FragmentActivity.onStart(FragmentActivity.java:597)
	at android.support.v7.app.AppCompatActivity.onStart(AppCompatActivity.java:177)
	at android.app.Instrumentation.callActivityOnStart(Instrumentation.java:1340)
	at android.app.Activity.performStart(Activity.java:7200)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2920)
	... 9 more
```
### ICC Msgs
```log
334	org.sufficientlysecure.keychain.ui.EncryptFilesActivity	"android.intent.action.SEND";;null;;"aah";;null;;
338	org.sufficientlysecure.keychain.ui.EncryptFilesActivity	"android.intent.action.SEND_MULTIPLE";;null;;"aah";;null;;
326	org.sufficientlysecure.keychain.ui.EncryptFilesActivity	"aaaaaag";;null;;"l";;null;;
317	org.sufficientlysecure.keychain.ui.EncryptFilesActivity	null;;null;;"l";;null;;
319	org.sufficientlysecure.keychain.ui.EncryptFilesActivity	null;;null;;"aah";;null;;
```

## E-27
================================================================================
+ Fax error file: /org.liberty.android.fantastischmemo_10.6.3_211_crash_EA.txt
+ Component: org.liberty.android.fantastischmemo/org.liberty.android.fantastischmemo.ui.ShareScreen
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: org.liberty.android.fantastischmemo/org.liberty.android.fantastischmemo.ui.ShareScreen	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{org.liberty.android.fantastischmemo/org.liberty.android.fantastischmemo.ui.ShareScreen}: java.lang.NullPointerException: Attempt to invoke virtual method 'boolean java.lang.String.equals(java.lang.Object)' on a null object reference
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2698)
	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:2759)
	at android.app.ActivityThread.-wrap12(ActivityThread.java)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1482)
	at android.os.Handler.dispatchMessage(Handler.java:102)
	at android.os.Looper.loop(Looper.java:154)
	at android.app.ActivityThread.main(ActivityThread.java:6190)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:892)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:782)
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'boolean java.lang.String.equals(java.lang.Object)' on a null object reference
	at org.liberty.android.fantastischmemo.ui.ShareScreen.onCreate(ShareScreen.java)
	at android.app.Activity.performCreate(Activity.java:6701)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1118)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2651)
	... 9 more
```
### ICC Msgs
```log
121	org.liberty.android.fantastischmemo.ui.ShareScreen	null;;null;;null;;null;;Parcelable->parObj->ParcelableObj,
115	org.liberty.android.fantastischmemo.ui.ShareScreen	null;;null;;null;;null;;Extras->ExtrasObj->ExtrasObj,(,String->android.intent.extra.SUBJECT->!@#$%^ds:+_,),
122	org.liberty.android.fantastischmemo.ui.ShareScreen	null;;null;;null;;null;;Serializable->serObj->SerializableObj,
112	org.liberty.android.fantastischmemo.ui.ShareScreen	null;;null;;null;;null;;Extras->ExtrasObj->ExtrasObj,(,String->android.intent.extra.TEXT->999999999999999999999999999999999999999999999999999,String->android.intent.extra.SUBJECT->!@#$%^ds:+_,),
114	org.liberty.android.fantastischmemo.ui.ShareScreen	null;;null;;null;;null;;Extras->ExtrasObj->ExtrasObj,(,String->android.intent.extra.TEXT->999999999999999999999999999999999999999999999999999,),
111	org.liberty.android.fantastischmemo.ui.ShareScreen	null;;null;;null;;null;;
```

## E-28
================================================================================
+ Fax error file: /org.liberty.android.fantastischmemo_10.6.3_211_crash_EA.txt
+ Component: org.liberty.android.fantastischmemo/org.liberty.android.fantastischmemo.ui.ShareScreen
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: org.liberty.android.fantastischmemo/org.liberty.android.fantastischmemo.ui.ShareScreen	uc2

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{org.liberty.android.fantastischmemo/org.liberty.android.fantastischmemo.ui.ShareScreen}: java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String android.os.Bundle.getString(java.lang.String)' on a null object reference
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2698)
	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:2759)
	at android.app.ActivityThread.-wrap12(ActivityThread.java)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1482)
	at android.os.Handler.dispatchMessage(Handler.java:102)
	at android.os.Looper.loop(Looper.java:154)
	at android.app.ActivityThread.main(ActivityThread.java:6190)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:892)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:782)
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String android.os.Bundle.getString(java.lang.String)' on a null object reference
	at org.liberty.android.fantastischmemo.ui.ShareScreen.onCreate(ShareScreen.java)
	at android.app.Activity.performCreate(Activity.java:6701)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1118)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2651)
	... 9 more
```
### ICC Msgs
```log
119	org.liberty.android.fantastischmemo.ui.ShareScreen	"android.intent.action.SEND";;null;;null;;null;;
113	org.liberty.android.fantastischmemo.ui.ShareScreen	"android.intent.action.SEND";;null;;null;;null;;Extras->ExtrasObj->ExtrasObj,(,),
116	org.liberty.android.fantastischmemo.ui.ShareScreen	"android.intent.action.SEND";;null;;null;;null;;Extras->ExtrasObj->ExtrasObj,(,String->android.intent.extra.SUBJECT->999999999999999999999999999999999999999999999999999,),
117	org.liberty.android.fantastischmemo.ui.ShareScreen	"android.intent.action.SEND";;null;;null;;null;;Extras->ExtrasObj->ExtrasObj,(,String->android.intent.extra.TEXT->!@#$%^ds:+_,String->android.intent.extra.SUBJECT->999999999999999999999999999999999999999999999999999,),
120	org.liberty.android.fantastischmemo.ui.ShareScreen	"android.intent.action.SEND";;null;;null;;null;;Extras->ExtrasObj->ExtrasObj,(,String->android.intent.extra.SUBJECT->!@#$%^ds:+_,),
110	org.liberty.android.fantastischmemo.ui.ShareScreen	"android.intent.action.SEND";;null;;null;;null;;Extras->ExtrasObj->ExtrasObj,(,String->android.intent.extra.TEXT->!@#$%^ds:+_,),
```

## E-29
================================================================================
+ Fax error file: /org.smssecure.smssecure_0.15.1_129_crash_EA.txt
+ Component: org.smssecure.smssecure/org.smssecure.smssecure.SmsSendtoActivity
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: org.smssecure.smssecure/org.smssecure.smssecure.SmsSendtoActivity	uc2

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{org.smssecure.smssecure/org.smssecure.smssecure.SmsSendtoActivity}: java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String android.net.Uri.toString()' on a null object reference
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2698)
	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:2759)
	at android.app.ActivityThread.-wrap12(ActivityThread.java)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1482)
	at android.os.Handler.dispatchMessage(Handler.java:102)
	at android.os.Looper.loop(Looper.java:154)
	at android.app.ActivityThread.main(ActivityThread.java:6190)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:892)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:782)
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String android.net.Uri.toString()' on a null object reference
	at org.smssecure.smssecure.SmsSendtoActivity.getDestinationForView(SmsSendtoActivity.java)
	at org.smssecure.smssecure.SmsSendtoActivity.getNextIntent(SmsSendtoActivity.java)
	at org.smssecure.smssecure.SmsSendtoActivity.onCreate(SmsSendtoActivity.java)
	at android.app.Activity.performCreate(Activity.java:6701)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1118)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2651)
	... 9 more
```
### ICC Msgs
```log
1769	org.smssecure.smssecure.SmsSendtoActivity	"aaaag";;null;;null;;null;;
```

## E-30
================================================================================
+ Fax error file: /org.smssecure.smssecure_0.15.1_129_crash_EA.txt
+ Component: org.smssecure.smssecure/org.smssecure.smssecure.SmsSendtoActivity
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: org.smssecure.smssecure/org.smssecure.smssecure.SmsSendtoActivity	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{org.smssecure.smssecure/org.smssecure.smssecure.SmsSendtoActivity}: java.lang.NullPointerException: Attempt to invoke virtual method 'boolean java.lang.String.equals(java.lang.Object)' on a null object reference
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2698)
	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:2759)
	at android.app.ActivityThread.-wrap12(ActivityThread.java)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1482)
	at android.os.Handler.dispatchMessage(Handler.java:102)
	at android.os.Looper.loop(Looper.java:154)
	at android.app.ActivityThread.main(ActivityThread.java:6190)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:892)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:782)
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'boolean java.lang.String.equals(java.lang.Object)' on a null object reference
	at org.smssecure.smssecure.SmsSendtoActivity.getNextIntent(SmsSendtoActivity.java)
	at org.smssecure.smssecure.SmsSendtoActivity.onCreate(SmsSendtoActivity.java)
	at android.app.Activity.performCreate(Activity.java:6701)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1118)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2651)
	... 9 more
```
### ICC Msgs
```log
1768	org.smssecure.smssecure.SmsSendtoActivity	null;;null;;null;;null;;
1771	org.smssecure.smssecure.SmsSendtoActivity	null;;null;;"t";;null;;
1778	org.smssecure.smssecure.SmsSendtoActivity	null;;null;;null;;null;;Parcelable->parObj->ParcelableObj,
1780	org.smssecure.smssecure.SmsSendtoActivity	null;;null;;null;;null;;Serializable->serObj->SerializableObj,
1774	org.smssecure.smssecure.SmsSendtoActivity	null;;null;;null;;null;;String->sms_body->!@#$%^ds:+_,
1777	org.smssecure.smssecure.SmsSendtoActivity	null;;null;;"l";;null;;
```

## E-31
================================================================================
+ Fax error file: /org.smssecure.smssecure_0.15.1_129_crash_EA.txt
+ Component: org.smssecure.smssecure/org.smssecure.smssecure.SmsSendtoActivity
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: org.smssecure.smssecure/org.smssecure.smssecure.SmsSendtoActivity	uc3

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{org.smssecure.smssecure/org.smssecure.smssecure.SmsSendtoActivity}: java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String android.net.Uri.getSchemeSpecificPart()' on a null object reference
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2698)
	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:2759)
	at android.app.ActivityThread.-wrap12(ActivityThread.java)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1482)
	at android.os.Handler.dispatchMessage(Handler.java:102)
	at android.os.Looper.loop(Looper.java:154)
	at android.app.ActivityThread.main(ActivityThread.java:6190)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:892)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:782)
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String android.net.Uri.getSchemeSpecificPart()' on a null object reference
	at org.smssecure.smssecure.SmsSendtoActivity.getDestinationForSendTo(SmsSendtoActivity.java)
	at org.smssecure.smssecure.SmsSendtoActivity.getNextIntent(SmsSendtoActivity.java)
	at org.smssecure.smssecure.SmsSendtoActivity.onCreate(SmsSendtoActivity.java)
	at android.app.Activity.performCreate(Activity.java:6701)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1118)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2651)
	... 9 more
```
### ICC Msgs
```log
1772	org.smssecure.smssecure.SmsSendtoActivity	"android.intent.action.SENDTO";;null;;null;;null;;
1770	org.smssecure.smssecure.SmsSendtoActivity	"android.intent.action.SENDTO";;null;;null;;null;;String->sms_body->!@#$%^ds:+_,
```

## E-32
================================================================================
+ Fax error file: /org.tasks_4.8.2_383_crash_EA.txt
+ Component: org.tasks/org.tasks.voice.VoiceCommandActivity
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: org.tasks/org.tasks.voice.VoiceCommandActivity	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{org.tasks/org.tasks.voice.VoiceCommandActivity}: java.lang.NullPointerException: Attempt to invoke virtual method 'int java.lang.String.hashCode()' on a null object reference
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2698)
	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:2759)
	at android.app.ActivityThread.-wrap12(ActivityThread.java)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1482)
	at android.os.Handler.dispatchMessage(Handler.java:102)
	at android.os.Looper.loop(Looper.java:154)
	at android.app.ActivityThread.main(ActivityThread.java:6190)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:892)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:782)
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'int java.lang.String.hashCode()' on a null object reference
	at org.tasks.voice.VoiceCommandActivity.onCreate(VoiceCommandActivity.java)
	at android.app.Activity.performCreate(Activity.java:6701)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1118)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2651)
	... 9 more
```
### ICC Msgs
```log
146	org.tasks.voice.VoiceCommandActivity	null;;null;;null;;null;;Parcelable->parObj->ParcelableObj,
147	org.tasks.voice.VoiceCommandActivity	null;;null;;null;;null;;Serializable->serObj->SerializableObj,
140	org.tasks.voice.VoiceCommandActivity	null;;null;;null;;null;;String->android.intent.extra.TEXT->999999999999999999999999999999999999999999999999999,
142	org.tasks.voice.VoiceCommandActivity	null;;null;;null;;null;;
```

## E-33
================================================================================
+ Fax error file: /Padland_crash_Error.txt
+ Component: com.mikifus.padland/com.mikifus.padland.PadViewActivity
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: com.mikifus.padland/com.mikifus.padland.PadViewActivity	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{com.mikifus.padland/com.mikifus.padland.PadViewActivity}: java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String com.mikifus.padland.Models.Pad.g()' on a null object reference
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
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String com.mikifus.padland.Models.Pad.g()' on a null object reference
	at com.mikifus.padland.PadViewActivity.d(SourceFile:5)
	at com.mikifus.padland.PadViewActivity.k(SourceFile:1)
	at com.mikifus.padland.PadViewActivity.n(SourceFile:1)
	at com.mikifus.padland.PadViewActivity.onCreate(SourceFile:2)
	at android.app.Activity.performCreate(Activity.java:7183)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1220)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2910)
	... 9 more
```
### ICC Msgs
```log
13	com.mikifus.padland.PadViewActivity	null;;null;;null;;null;;
```

## E-34
================================================================================
+ Fax error file: /Padland_crash_Error.txt
+ Component: com.mikifus.padland/com.mikifus.padland.PadListActivity
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: com.mikifus.padland/com.mikifus.padland.PadListActivity	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{com.mikifus.padland/com.mikifus.padland.PadListActivity}: java.lang.NullPointerException: Attempt to invoke virtual method 'int java.util.ArrayList.size()' on a null object reference
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
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'int java.util.ArrayList.size()' on a null object reference
	at com.mikifus.padland.PadListActivity.i(SourceFile:3)
	at com.mikifus.padland.PadListActivity.onCreate(SourceFile:2)
	at android.app.Activity.performCreate(Activity.java:7183)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1220)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2910)
	... 9 more
```
### ICC Msgs
```log
28	com.mikifus.padland.PadListActivity	null;;null;;null;;null;;String->android.intent.extra.TEXT->abcde,Extras->ExtrasObj->ExtrasObj,(,long->focus_pad->0,),String->action->999999999999999999999999999999999999999999999999999,
```

## E-35
================================================================================
+ Fax error file: /SteamGifts_crash_Error.txt
+ Component: net.mabako.steamgifts/net.mabako.steamgifts.activities.UrlHandlingActivity
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: net.mabako.steamgifts/net.mabako.steamgifts.activities.UrlHandlingActivity	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{net.mabako.steamgifts/net.mabako.steamgifts.activities.UrlHandlingActivity}: java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String android.net.Uri.toString()' on a null object reference
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
	at net.mabako.steamgifts.activities.UrlHandlingActivity.getIntentForUri(UrlHandlingActivity.java:39)
	at net.mabako.steamgifts.activities.UrlHandlingActivity.onCreate(UrlHandlingActivity.java:151)
	at android.app.Activity.performCreate(Activity.java:7183)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1220)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2910)
	... 9 more
```
### ICC Msgs
```log
46	net.mabako.steamgifts.activities.UrlHandlingActivity	null;;null;;null;;null;;
47	net.mabako.steamgifts.activities.UrlHandlingActivity	"A";;null;;null;;null;;
48	net.mabako.steamgifts.activities.UrlHandlingActivity	null;;null;;null;;null;;Parcelable->parObj->ParcelableObj,
49	net.mabako.steamgifts.activities.UrlHandlingActivity	null;;null;;null;;null;;Serializable->serObj->SerializableObj,
```

## E-36
================================================================================
+ Fax error file: /SuntimesWidget_crash_Error.txt
+ Component: com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.MoonWidget0ConfigActivity_2x1
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.MoonWidget0ConfigActivity_2x1	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to destroy activity {com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.MoonWidget0ConfigActivity_2x1}: java.lang.NullPointerException: Attempt to invoke virtual method 'void com.forrestguice.suntimeswidget.LocationConfigView.cancelGetFix()' on a null object reference
	at android.app.ActivityThread.performDestroyActivity(ActivityThread.java:4605)
	at android.app.ActivityThread.handleDestroyActivity(ActivityThread.java:4623)
	at android.app.ActivityThread.-wrap5(Unknown Source:0)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1757)
	at android.os.Handler.dispatchMessage(Handler.java:105)
	at android.os.Looper.loop(Looper.java:164)
	at android.app.ActivityThread.main(ActivityThread.java:6944)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:327)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:1374)
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'void com.forrestguice.suntimeswidget.LocationConfigView.cancelGetFix()' on a null object reference
	at com.forrestguice.suntimeswidget.SuntimesConfigActivity0.onDestroy(SuntimesConfigActivity0.java:191)
	at android.app.Activity.performDestroy(Activity.java:7522)
	at android.app.Instrumentation.callActivityOnDestroy(Instrumentation.java:1255)
	at android.app.ActivityThread.performDestroyActivity(ActivityThread.java:4592)
	... 9 more
```
### ICC Msgs
```log
1	com.forrestguice.suntimeswidget.MoonWidget0ConfigActivity_2x1	null;;null;;null;;null;;
```

## E-37
================================================================================
+ Fax error file: /SuntimesWidget_crash_Error.txt
+ Component: com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.SuntimesConfigActivity2_3x1
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.SuntimesConfigActivity2_3x1	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to destroy activity {com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.SuntimesConfigActivity2_3x1}: java.lang.NullPointerException: Attempt to invoke virtual method 'void com.forrestguice.suntimeswidget.LocationConfigView.cancelGetFix()' on a null object reference
	at android.app.ActivityThread.performDestroyActivity(ActivityThread.java:4605)
	at android.app.ActivityThread.handleDestroyActivity(ActivityThread.java:4623)
	at android.app.ActivityThread.-wrap5(Unknown Source:0)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1757)
	at android.os.Handler.dispatchMessage(Handler.java:105)
	at android.os.Looper.loop(Looper.java:164)
	at android.app.ActivityThread.main(ActivityThread.java:6944)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:327)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:1374)
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'void com.forrestguice.suntimeswidget.LocationConfigView.cancelGetFix()' on a null object reference
	at com.forrestguice.suntimeswidget.SuntimesConfigActivity0.onDestroy(SuntimesConfigActivity0.java:191)
	at android.app.Activity.performDestroy(Activity.java:7522)
	at android.app.Instrumentation.callActivityOnDestroy(Instrumentation.java:1255)
	at android.app.ActivityThread.performDestroyActivity(ActivityThread.java:4592)
	... 9 more
```
### ICC Msgs
```log
85	com.forrestguice.suntimeswidget.SuntimesConfigActivity2_3x1	null;;null;;null;;null;;
```

## E-38
================================================================================
+ Fax error file: /SuntimesWidget_crash_Error.txt
+ Component: com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.SuntimesActivity
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.SuntimesActivity	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.SuntimesActivity}: java.lang.NullPointerException: Attempt to invoke virtual method 'boolean java.lang.String.equals(java.lang.Object)' on a null object reference
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
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'boolean java.lang.String.equals(java.lang.Object)' on a null object reference
	at com.forrestguice.suntimeswidget.LocationConfigView.bundleData(LocationConfigView.java:743)
	at com.forrestguice.suntimeswidget.LocationConfigView.bundleData(LocationConfigView.java:735)
	at com.forrestguice.suntimeswidget.LocationConfigView.loadSettings(LocationConfigView.java:682)
	at com.forrestguice.suntimeswidget.LocationConfigDialog.onCreateDialog(LocationConfigDialog.java:276)
	at android.support.v4.app.DialogFragment.onGetLayoutInflater(DialogFragment.java:310)
	at android.support.v4.app.Fragment.performGetLayoutInflater(Fragment.java:1166)
	at android.support.v4.app.FragmentManagerImpl.moveToState(FragmentManager.java:1340)
	at android.support.v4.app.FragmentManagerImpl.moveFragmentToExpectedState(FragmentManager.java:1569)
	at android.support.v4.app.FragmentManagerImpl.moveToState(FragmentManager.java:1636)
	at android.support.v4.app.BackStackRecord.executeOps(BackStackRecord.java:758)
	at android.support.v4.app.FragmentManagerImpl.executeOps(FragmentManager.java:2415)
	at android.support.v4.app.FragmentManagerImpl.executeOpsTogether(FragmentManager.java:2201)
	at android.support.v4.app.FragmentManagerImpl.optimizeAndExecuteOps(FragmentManager.java:2155)
	at android.support.v4.app.FragmentManagerImpl.execPendingActions(FragmentManager.java:2064)
	at android.support.v4.app.FragmentController.execPendingActions(FragmentController.java:379)
	at android.support.v4.app.FragmentActivity.onStart(FragmentActivity.java:607)
	at android.support.v7.app.AppCompatActivity.onStart(AppCompatActivity.java:178)
	at com.forrestguice.suntimeswidget.SuntimesActivity.onStart(SuntimesActivity.java:348)
	at android.app.Instrumentation.callActivityOnStart(Instrumentation.java:1340)
	at android.app.Activity.performStart(Activity.java:7200)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2920)
	... 9 more
```
### ICC Msgs
```log
54	com.forrestguice.suntimeswidget.SuntimesActivity	"aaaaaag";;null;;"l";;null;;
```

## E-39
================================================================================
+ Fax error file: /SuntimesWidget_crash_Error.txt
+ Component: com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.SolsticeWidget0ConfigActivity
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.SolsticeWidget0ConfigActivity	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to destroy activity {com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.SolsticeWidget0ConfigActivity}: java.lang.NullPointerException: Attempt to invoke virtual method 'void com.forrestguice.suntimeswidget.LocationConfigView.cancelGetFix()' on a null object reference
	at android.app.ActivityThread.performDestroyActivity(ActivityThread.java:4605)
	at android.app.ActivityThread.handleDestroyActivity(ActivityThread.java:4623)
	at android.app.ActivityThread.-wrap5(Unknown Source:0)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1757)
	at android.os.Handler.dispatchMessage(Handler.java:105)
	at android.os.Looper.loop(Looper.java:164)
	at android.app.ActivityThread.main(ActivityThread.java:6944)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:327)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:1374)
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'void com.forrestguice.suntimeswidget.LocationConfigView.cancelGetFix()' on a null object reference
	at com.forrestguice.suntimeswidget.SuntimesConfigActivity0.onDestroy(SuntimesConfigActivity0.java:191)
	at android.app.Activity.performDestroy(Activity.java:7522)
	at android.app.Instrumentation.callActivityOnDestroy(Instrumentation.java:1255)
	at android.app.ActivityThread.performDestroyActivity(ActivityThread.java:4592)
	... 9 more
```
### ICC Msgs
```log
10	com.forrestguice.suntimeswidget.SolsticeWidget0ConfigActivity	null;;null;;null;;null;;
```

## E-40
================================================================================
+ Fax error file: /SuntimesWidget_crash_Error.txt
+ Component: com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.SuntimesConfigActivity2
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.SuntimesConfigActivity2	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to destroy activity {com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.SuntimesConfigActivity2}: java.lang.NullPointerException: Attempt to invoke virtual method 'void com.forrestguice.suntimeswidget.LocationConfigView.cancelGetFix()' on a null object reference
	at android.app.ActivityThread.performDestroyActivity(ActivityThread.java:4605)
	at android.app.ActivityThread.handleDestroyActivity(ActivityThread.java:4623)
	at android.app.ActivityThread.-wrap5(Unknown Source:0)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1757)
	at android.os.Handler.dispatchMessage(Handler.java:105)
	at android.os.Looper.loop(Looper.java:164)
	at android.app.ActivityThread.main(ActivityThread.java:6944)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:327)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:1374)
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'void com.forrestguice.suntimeswidget.LocationConfigView.cancelGetFix()' on a null object reference
	at com.forrestguice.suntimeswidget.SuntimesConfigActivity0.onDestroy(SuntimesConfigActivity0.java:191)
	at android.app.Activity.performDestroy(Activity.java:7522)
	at android.app.Instrumentation.callActivityOnDestroy(Instrumentation.java:1255)
	at android.app.ActivityThread.performDestroyActivity(ActivityThread.java:4592)
	... 9 more
```
### ICC Msgs
```log
82	com.forrestguice.suntimeswidget.SuntimesConfigActivity2	null;;null;;null;;null;;
```

## E-41
================================================================================
+ Fax error file: /SuntimesWidget_crash_Error.txt
+ Component: com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.SuntimesConfigActivity0
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.SuntimesConfigActivity0	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to destroy activity {com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.SuntimesConfigActivity0}: java.lang.NullPointerException: Attempt to invoke virtual method 'void com.forrestguice.suntimeswidget.LocationConfigView.cancelGetFix()' on a null object reference
	at android.app.ActivityThread.performDestroyActivity(ActivityThread.java:4605)
	at android.app.ActivityThread.handleDestroyActivity(ActivityThread.java:4623)
	at android.app.ActivityThread.-wrap5(Unknown Source:0)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1757)
	at android.os.Handler.dispatchMessage(Handler.java:105)
	at android.os.Looper.loop(Looper.java:164)
	at android.app.ActivityThread.main(ActivityThread.java:6944)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:327)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:1374)
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'void com.forrestguice.suntimeswidget.LocationConfigView.cancelGetFix()' on a null object reference
	at com.forrestguice.suntimeswidget.SuntimesConfigActivity0.onDestroy(SuntimesConfigActivity0.java:191)
	at android.app.Activity.performDestroy(Activity.java:7522)
	at android.app.Instrumentation.callActivityOnDestroy(Instrumentation.java:1255)
	at android.app.ActivityThread.performDestroyActivity(ActivityThread.java:4592)
	... 9 more
```
### ICC Msgs
```log
57	com.forrestguice.suntimeswidget.SuntimesConfigActivity0	null;;null;;null;;null;;
58	com.forrestguice.suntimeswidget.SuntimesConfigActivity0	null;;null;;null;;null;;Extras->ExtrasObj->ExtrasObj,(,),
59	com.forrestguice.suntimeswidget.SuntimesConfigActivity0	null;;null;;null;;null;;Extras->ExtrasObj->ExtrasObj,(,int->appWidgetId->Integer.MAX_VALUE,),
```

## E-42
================================================================================
+ Fax error file: /SuntimesWidget_crash_Error.txt
+ Component: com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.MoonWidget0ConfigActivity_3x1
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.MoonWidget0ConfigActivity_3x1	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to destroy activity {com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.MoonWidget0ConfigActivity_3x1}: java.lang.NullPointerException: Attempt to invoke virtual method 'void com.forrestguice.suntimeswidget.LocationConfigView.cancelGetFix()' on a null object reference
	at android.app.ActivityThread.performDestroyActivity(ActivityThread.java:4605)
	at android.app.ActivityThread.handleDestroyActivity(ActivityThread.java:4623)
	at android.app.ActivityThread.-wrap5(Unknown Source:0)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1757)
	at android.os.Handler.dispatchMessage(Handler.java:105)
	at android.os.Looper.loop(Looper.java:164)
	at android.app.ActivityThread.main(ActivityThread.java:6944)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:327)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:1374)
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'void com.forrestguice.suntimeswidget.LocationConfigView.cancelGetFix()' on a null object reference
	at com.forrestguice.suntimeswidget.SuntimesConfigActivity0.onDestroy(SuntimesConfigActivity0.java:191)
	at android.app.Activity.performDestroy(Activity.java:7522)
	at android.app.Instrumentation.callActivityOnDestroy(Instrumentation.java:1255)
	at android.app.ActivityThread.performDestroyActivity(ActivityThread.java:4592)
	... 9 more
```
### ICC Msgs
```log
13	com.forrestguice.suntimeswidget.MoonWidget0ConfigActivity_3x1	null;;null;;null;;null;;
```

## E-43
================================================================================
+ Fax error file: /SuntimesWidget_crash_Error.txt
+ Component: com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.MoonWidget0ConfigActivity
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.MoonWidget0ConfigActivity	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to destroy activity {com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.MoonWidget0ConfigActivity}: java.lang.NullPointerException: Attempt to invoke virtual method 'void com.forrestguice.suntimeswidget.LocationConfigView.cancelGetFix()' on a null object reference
	at android.app.ActivityThread.performDestroyActivity(ActivityThread.java:4605)
	at android.app.ActivityThread.handleDestroyActivity(ActivityThread.java:4623)
	at android.app.ActivityThread.-wrap5(Unknown Source:0)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1757)
	at android.os.Handler.dispatchMessage(Handler.java:105)
	at android.os.Looper.loop(Looper.java:164)
	at android.app.ActivityThread.main(ActivityThread.java:6944)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:327)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:1374)
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'void com.forrestguice.suntimeswidget.LocationConfigView.cancelGetFix()' on a null object reference
	at com.forrestguice.suntimeswidget.SuntimesConfigActivity0.onDestroy(SuntimesConfigActivity0.java:191)
	at android.app.Activity.performDestroy(Activity.java:7522)
	at android.app.Instrumentation.callActivityOnDestroy(Instrumentation.java:1255)
	at android.app.ActivityThread.performDestroyActivity(ActivityThread.java:4592)
	... 9 more
```
### ICC Msgs
```log
16	com.forrestguice.suntimeswidget.MoonWidget0ConfigActivity	null;;null;;null;;null;;
```

## E-44
================================================================================
+ Fax error file: /SuntimesWidget_crash_Error.txt
+ Component: com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.ClockWidget0ConfigActivity_3x1
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.ClockWidget0ConfigActivity_3x1	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to destroy activity {com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.ClockWidget0ConfigActivity_3x1}: java.lang.NullPointerException: Attempt to invoke virtual method 'void com.forrestguice.suntimeswidget.LocationConfigView.cancelGetFix()' on a null object reference
	at android.app.ActivityThread.performDestroyActivity(ActivityThread.java:4605)
	at android.app.ActivityThread.handleDestroyActivity(ActivityThread.java:4623)
	at android.app.ActivityThread.-wrap5(Unknown Source:0)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1757)
	at android.os.Handler.dispatchMessage(Handler.java:105)
	at android.os.Looper.loop(Looper.java:164)
	at android.app.ActivityThread.main(ActivityThread.java:6944)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:327)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:1374)
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'void com.forrestguice.suntimeswidget.LocationConfigView.cancelGetFix()' on a null object reference
	at com.forrestguice.suntimeswidget.SuntimesConfigActivity0.onDestroy(SuntimesConfigActivity0.java:191)
	at android.app.Activity.performDestroy(Activity.java:7522)
	at android.app.Instrumentation.callActivityOnDestroy(Instrumentation.java:1255)
	at android.app.ActivityThread.performDestroyActivity(ActivityThread.java:4592)
	... 9 more
```
### ICC Msgs
```log
30	com.forrestguice.suntimeswidget.ClockWidget0ConfigActivity_3x1	null;;null;;null;;null;;
```

## E-45
================================================================================
+ Fax error file: /SuntimesWidget_crash_Error.txt
+ Component: com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.ClockWidget0ConfigActivity
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.ClockWidget0ConfigActivity	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to destroy activity {com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.ClockWidget0ConfigActivity}: java.lang.NullPointerException: Attempt to invoke virtual method 'void com.forrestguice.suntimeswidget.LocationConfigView.cancelGetFix()' on a null object reference
	at android.app.ActivityThread.performDestroyActivity(ActivityThread.java:4605)
	at android.app.ActivityThread.handleDestroyActivity(ActivityThread.java:4623)
	at android.app.ActivityThread.-wrap5(Unknown Source:0)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1757)
	at android.os.Handler.dispatchMessage(Handler.java:105)
	at android.os.Looper.loop(Looper.java:164)
	at android.app.ActivityThread.main(ActivityThread.java:6944)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:327)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:1374)
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'void com.forrestguice.suntimeswidget.LocationConfigView.cancelGetFix()' on a null object reference
	at com.forrestguice.suntimeswidget.SuntimesConfigActivity0.onDestroy(SuntimesConfigActivity0.java:191)
	at android.app.Activity.performDestroy(Activity.java:7522)
	at android.app.Instrumentation.callActivityOnDestroy(Instrumentation.java:1255)
	at android.app.ActivityThread.performDestroyActivity(ActivityThread.java:4592)
	... 9 more
```
### ICC Msgs
```log
19	com.forrestguice.suntimeswidget.ClockWidget0ConfigActivity	null;;null;;null;;null;;
```

## E-46
================================================================================
+ Fax error file: /SuntimesWidget_crash_Error.txt
+ Component: com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.SuntimesConfigActivity0_2x1
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.SuntimesConfigActivity0_2x1	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to destroy activity {com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.SuntimesConfigActivity0_2x1}: java.lang.NullPointerException: Attempt to invoke virtual method 'void com.forrestguice.suntimeswidget.LocationConfigView.cancelGetFix()' on a null object reference
	at android.app.ActivityThread.performDestroyActivity(ActivityThread.java:4605)
	at android.app.ActivityThread.handleDestroyActivity(ActivityThread.java:4623)
	at android.app.ActivityThread.-wrap5(Unknown Source:0)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1757)
	at android.os.Handler.dispatchMessage(Handler.java:105)
	at android.os.Looper.loop(Looper.java:164)
	at android.app.ActivityThread.main(ActivityThread.java:6944)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:327)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:1374)
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'void com.forrestguice.suntimeswidget.LocationConfigView.cancelGetFix()' on a null object reference
	at com.forrestguice.suntimeswidget.SuntimesConfigActivity0.onDestroy(SuntimesConfigActivity0.java:191)
	at android.app.Activity.performDestroy(Activity.java:7522)
	at android.app.Instrumentation.callActivityOnDestroy(Instrumentation.java:1255)
	at android.app.ActivityThread.performDestroyActivity(ActivityThread.java:4592)
	... 9 more
```
### ICC Msgs
```log
7	com.forrestguice.suntimeswidget.SuntimesConfigActivity0_2x1	null;;null;;null;;null;;
```

## E-47
================================================================================
+ Fax error file: /SuntimesWidget_crash_Error.txt
+ Component: com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.SuntimesConfigActivity2_3x2
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.SuntimesConfigActivity2_3x2	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to destroy activity {com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.SuntimesConfigActivity2_3x2}: java.lang.NullPointerException: Attempt to invoke virtual method 'void com.forrestguice.suntimeswidget.LocationConfigView.cancelGetFix()' on a null object reference
	at android.app.ActivityThread.performDestroyActivity(ActivityThread.java:4605)
	at android.app.ActivityThread.handleDestroyActivity(ActivityThread.java:4623)
	at android.app.ActivityThread.-wrap5(Unknown Source:0)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1757)
	at android.os.Handler.dispatchMessage(Handler.java:105)
	at android.os.Looper.loop(Looper.java:164)
	at android.app.ActivityThread.main(ActivityThread.java:6944)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:327)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:1374)
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'void com.forrestguice.suntimeswidget.LocationConfigView.cancelGetFix()' on a null object reference
	at com.forrestguice.suntimeswidget.SuntimesConfigActivity0.onDestroy(SuntimesConfigActivity0.java:191)
	at android.app.Activity.performDestroy(Activity.java:7522)
	at android.app.Instrumentation.callActivityOnDestroy(Instrumentation.java:1255)
	at android.app.ActivityThread.performDestroyActivity(ActivityThread.java:4592)
	... 9 more
```
### ICC Msgs
```log
88	com.forrestguice.suntimeswidget.SuntimesConfigActivity2_3x2	null;;null;;null;;null;;
```

## E-48
================================================================================
+ Fax error file: /SuntimesWidget_crash_Error.txt
+ Component: com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.SuntimesConfigActivity1
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.SuntimesConfigActivity1	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to destroy activity {com.forrestguice.suntimeswidget/com.forrestguice.suntimeswidget.SuntimesConfigActivity1}: java.lang.NullPointerException: Attempt to invoke virtual method 'void com.forrestguice.suntimeswidget.LocationConfigView.cancelGetFix()' on a null object reference
	at android.app.ActivityThread.performDestroyActivity(ActivityThread.java:4605)
	at android.app.ActivityThread.handleDestroyActivity(ActivityThread.java:4623)
	at android.app.ActivityThread.-wrap5(Unknown Source:0)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1757)
	at android.os.Handler.dispatchMessage(Handler.java:105)
	at android.os.Looper.loop(Looper.java:164)
	at android.app.ActivityThread.main(ActivityThread.java:6944)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:327)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:1374)
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'void com.forrestguice.suntimeswidget.LocationConfigView.cancelGetFix()' on a null object reference
	at com.forrestguice.suntimeswidget.SuntimesConfigActivity0.onDestroy(SuntimesConfigActivity0.java:191)
	at android.app.Activity.performDestroy(Activity.java:7522)
	at android.app.Instrumentation.callActivityOnDestroy(Instrumentation.java:1255)
	at android.app.ActivityThread.performDestroyActivity(ActivityThread.java:4592)
	... 9 more
```
### ICC Msgs
```log
62	com.forrestguice.suntimeswidget.SuntimesConfigActivity1	null;;null;;null;;null;;
```

## E-49
================================================================================
+ Fax error file: /syncthing_crash_Error.txt
+ Component: com.nutomic.syncthingandroid/com.nutomic.syncthingandroid.activities.ShareActivity
+ Exception types: java.lang.NullPointerException, java.lang.RuntimeException
+ Matched AACT Unique Crash: com.nutomic.syncthingandroid/com.nutomic.syncthingandroid.activities.ShareActivity	uc1

### BugInfo
```log
java.lang.RuntimeException: Unable to start activity ComponentInfo{com.nutomic.syncthingandroid/com.nutomic.syncthingandroid.activities.ShareActivity}: java.lang.NullPointerException: Attempt to invoke virtual method 'boolean java.lang.String.equals(java.lang.Object)' on a null object reference
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
Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'boolean java.lang.String.equals(java.lang.Object)' on a null object reference
	at com.nutomic.syncthingandroid.activities.ShareActivity.onCreate(ShareActivity.java:122)
	at android.app.Activity.performCreate(Activity.java:7183)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1220)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2910)
	... 9 more
```
### ICC Msgs
```log
30	com.nutomic.syncthingandroid.activities.ShareActivity	null;;null;;null;;null;;Parcelable->parObj->ParcelableObj,
28	com.nutomic.syncthingandroid.activities.ShareActivity	null;;null;;null;;null;;ParcelableArrayList->android.intent.extra.STREAM->ParcelableArrayListObj,
31	com.nutomic.syncthingandroid.activities.ShareActivity	null;;null;;null;;null;;Serializable->serObj->SerializableObj,
24	com.nutomic.syncthingandroid.activities.ShareActivity	null;;null;;null;;null;;Parcelable->android.intent.extra.STREAM->ParcelableObj,
22	com.nutomic.syncthingandroid.activities.ShareActivity	null;;null;;null;;null;;
```

## E-50
================================================================================
+ Fax error file: /K9Mail_crash_Error.txt
+ Component: com.fsck.k9/com.fsck.k9.activity.LauncherShortcuts
+ Exception types: android.util.SuperNotCalledException
+ Matched AACT Unique Crash: com.fsck.k9/com.fsck.k9.activity.LauncherShortcuts	uc1

### BugInfo
```log
android.util.SuperNotCalledException: Activity {com.fsck.k9/com.fsck.k9.activity.LauncherShortcuts} did not call through to super.onCreate()
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2913)
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
68	com.fsck.k9.activity.LauncherShortcuts	null;;null;;null;;null;;Parcelable->parObj->ParcelableObj,
69	com.fsck.k9.activity.LauncherShortcuts	null;;null;;null;;null;;Serializable->serObj->SerializableObj,
65	com.fsck.k9.activity.LauncherShortcuts	null;;null;;null;;null;;
67	com.fsck.k9.activity.LauncherShortcuts	"A";;null;;null;;null;;
```

