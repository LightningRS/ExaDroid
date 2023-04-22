#!/usr/bin/python3
#! -*- coding: utf-8 -*-

import os
import sys
import config

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("usage: GetFunctionSummary.py <input-apk-dir> [<output-icc-result-dir>]\n")
    print("output-icc-result-path: Default to /path/to/ExaDroid/result/ICCResult")
    exit(2)

apk_path = os.path.abspath(sys.argv[1])
result_path = config.ICCBOT_RESULT_PATH
if len(sys.argv) > 2:
    result_path = sys.argv[2]
os.makedirs(result_path, exist_ok=True)

ICCBOT_CMD_TEMPLATE = \
    f'{config.JAVA_17_PATH} ' + \
    f'-jar "{config.ICCBOT_JAR_PATH}" ' + \
    f'-path "{apk_path}" ' + \
    '-name "{apk_name}" ' + \
    f'-androidJar "{config.ANDROID_LIB_PATH}" ' + \
    f'-time {config.ICCBOT_TIME} ' + \
    f'-maxPathNumber {config.ICCBOT_MAX_PATH_NUM} ' + \
    '-client ICCSpecClient ' + \
    f'-outputDir "{result_path}" ' + \
    f'>> "{config.LOGS_PATH}/' + \
    'ICCBot-{apk_basename}.log"'
print(ICCBOT_CMD_TEMPLATE)
    
apks_lis = []
for root, dirs, files in os.walk(apk_path):
    for file in files:
        if not file.endswith('.apk'):
            continue
        apks_lis.append(os.path.abspath(os.path.join(root, file)))

if len(apks_lis) == 0:
    print("No apk found!")
    exit(0)

for apk_path in apks_lis:
    apk_name = str(os.path.basename(apk_path))
    apk_basename = apk_name.replace('.apk', '')
    cmd = ICCBOT_CMD_TEMPLATE.format(apk_name=apk_name, apk_basename=apk_basename)
    print(cmd)
    os.chdir(config.ICCBOT_ROOT_PATH)
    if os.system(cmd) != 0:
        print("Error when running ICCBot on [{}]".format(apk_path))
    else:
        print("Finshed running ICCBot on [{}]".format(apk_path))
