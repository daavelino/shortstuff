# Android/AppData

AppData is a serie of 3 bash scripts that uses Android Debugger Bridge (adb) to:

  - [listApps.bsh] list the applications (packages) installed into device
  - [getAppData.bsh] get data files from device by using adb backup function
  - [putAppData.bsh] push backkuped data onto device

# What's the point?

At some point of Android's application security tests it is important to check if sensitive information are stored at application data directories. You may also want to check the effects in application's behavior if some data be inserted arbitrarly. To perform such test you can:

1. list all applications present in the device
2. extract data from the desired application
3. analyze it properly
4. change any data as you please
5. insert it back into device

AppData scripts goal is to simplify these steps in a fast and organized way.

# Setup:
You'll need:
- A device running Android and plugged at USB
- Android'd Developer options -> USB debugging enabled
- A Linux machine to run the scripts
- Installed [Android Platform Tools](https://developer.android.com/studio/releases/platform-tools.html)

# Usage:

Get the files at github:

```sh
$ git clone https://github.com/daavelino/shortstuff/Android/AppData
```
or get it from [project's page](https://github.com/daavelino/shortstuff.git):

### Once you got the files, 

0. If your adb executable is not at the default PATH, consider to set properly the file 
> conf/settings.conf

1. list all applications present in the device:

```sh
$ ./listApps.bsh
```
will produces a list with all installed apps. Choose one of them, for instance, 

com.android.contacts and 

2. use getAppData to get data from device:

```sh
$ ./getAppData <app name>
```
using our example, we have:

```sh
$ ./getAppData com.android.contacts
```
it will create the directory com.android.contacts.DD-MM-YYYY-hh.mm.ss. Go and explore it:

```sh
$ cd com.android.contacts.DD-MM-YYYY-hh.mm.ss/
```

3. if you change something and need to put modified data back to the application, just do:

```sh
$ ./putAppData.bsh <directory containing data>
```

In our example, it is:

```sh
$ ./putAppData.bsh com.android.contacts.DD-MM-YYYY-hh.mm.ss/
```

That is it. Data manipulation made easier.

