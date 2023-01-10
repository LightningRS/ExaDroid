#!/usr/bin/python3
#! -*- coding: utf-8 -*-

import os
import shutil
import zipfile

JAVA_8_PATH = "D:/Programs/jdk1.8.0_202/bin/java.exe"
JAVA_17_PATH = "D:/Programs/jdk-18.0.2/bin/java.exe"

# ICCBot Arguments
ICCBOT_TIME = 60
ICCBOT_MAX_PATH_NUM = 100

# AACT Arguments
DEVICE_SERIAL = 'emulator-5556'
LAUNCHER_PKG_NAME = 'com.android.launcher3'
STRATEGIES = 'iccBot; random; randomWithStruct; iccBot+preset; iccBot+preset+randomWithStruct'
RAND_SEED = 12345678
RAND_VAL_NUM = 3

########## Tools path specification start ##########
ROOT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
LIB_PATH = os.path.join(ROOT_PATH, 'libs')
LOGS_PATH = os.path.join(ROOT_PATH, "logs")
TEMP_PATH = os.path.join(ROOT_PATH, 'temp')
DEFAULT_RESULT_PATH = os.path.join(ROOT_PATH, 'result')

# ADB
ADB_PATH = os.path.join(LIB_PATH, "adb.exe")

# Android Library
ANDROID_LIB_PATH = LIB_PATH
ANDROID_LIB_1_PATH = os.path.join(LIB_PATH, 'android-1')
ANDROID_LIB_JAR_PATH = os.path.join(ANDROID_LIB_1_PATH, 'android.jar')

# AACT
AACT_JAR_PATH = os.path.join(LIB_PATH, "AACT.jar")
AACT_TESTCASES_PATH = os.path.join(DEFAULT_RESULT_PATH, "Testcases")
AACT_RESULT_PATH = os.path.join(DEFAULT_RESULT_PATH, "TestExecutionResult")

# ICCBot
ICCBOT_ROOT_PATH = os.path.join(LIB_PATH, "ICCBot")
ICCBOT_JAR_PATH = os.path.join(ICCBOT_ROOT_PATH, "ICCBot.jar")
ICCBOT_RESULT_PATH = os.path.join(DEFAULT_RESULT_PATH, "ICCResult")

# Mist
MIST_ROOT = os.path.join(LIB_PATH, "Mist")
MIST_DATA_ZIP_PATH = os.path.join(MIST_ROOT, "data.zip")
MIST_DATA_PATH = os.path.join(MIST_ROOT, "data")
MIST_JAR_PATH = os.path.join(MIST_ROOT, "Mist.jar")
MIST_ANDROID_LIB_PATH = os.path.join(MIST_ROOT, 'lib/android--1')
MIST_ANDROID_LIB_JAR_PATH = os.path.join(MIST_ANDROID_LIB_PATH, 'android.jar')
MIST_ANALYZER_JAR_PATH = os.path.join(MIST_ROOT, 'MistResultAnalyzer.jar')
MIST_RESULT_PATH = os.path.join(DEFAULT_RESULT_PATH, "MistResult")

# APKTool
APKTOOL_JAR_PATH = os.path.join(LIB_PATH, "apktool_2.3.1.jar")
########## Tools path specification end ##########

########## Tools path verify start ##########
if not os.path.exists(JAVA_8_PATH):
    print("Java 8 not found! Please check config.py")
    exit(0)
    
if not os.path.exists(JAVA_17_PATH):
    print("Java 17+ not found! Please check config.py")
    exit(0)

if not os.path.exists(ADB_PATH):
    print("adb not found! Please check config.py")
    exit(0)

if not os.path.exists(AACT_JAR_PATH):
    print("AACT.jar not found! Please check config.py")
    exit(0)

if not os.path.exists(ICCBOT_JAR_PATH):
    print("ICCBot.jar not found! Please check config.py")
    exit(0)

if not os.path.exists(ANDROID_LIB_1_PATH):
    print("Android library (platforms/android-1) not found! Please check config.py")
    exit(0)

os.makedirs(MIST_ANDROID_LIB_PATH, exist_ok=True)
if not os.path.exists(MIST_ANDROID_LIB_JAR_PATH):
    shutil.copyfile(ANDROID_LIB_JAR_PATH, MIST_ANDROID_LIB_JAR_PATH)

if not os.path.exists(MIST_JAR_PATH):
    print("Mist.jar not found! Please check config.py")
    exit(0)

if not os.path.exists(MIST_ANALYZER_JAR_PATH):
    print("MistResultAnalyzer.jar not found! Please check config.py")
    exit(0)
    
if not os.path.exists(MIST_DATA_ZIP_PATH):
    print("Mist data.zip not found! Please check config.py")
    exit(0)

if not os.path.exists(MIST_DATA_PATH):
    f = zipfile.ZipFile(MIST_DATA_ZIP_PATH, 'r')
    f.extractall(MIST_DATA_PATH)
    f.close()
    print("Unzipped Mist data files")

if not os.path.exists(APKTOOL_JAR_PATH):
    print("apktool_2.3.1.jar not found! Please check config.py")
    exit(0)
########## Tools path verify end ##########

os.makedirs(LOGS_PATH, exist_ok=True)
os.makedirs(TEMP_PATH, exist_ok=True)


def format_args(arg_lis):
    for i in range(len(arg_lis)):
        if ' ' in arg_lis[i]:
            arg_lis[i] = f'"{arg_lis[i]}"'
    return ' '.join(arg_lis)
