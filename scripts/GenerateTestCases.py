#!/usr/bin/python3
#! -*- coding: utf-8 -*-

import os
import shutil
import sys
import config

if len(sys.argv) < 2 or len(sys.argv) > 5:
    print("usage: GenerateTestCases.py <input-apk-dir> [<input-icc-result-dir>] [<input-mist-result-dir>] [<output-testcase-dir>]\n")
    print("input-icc-result-dir: Default to /path/to/ExaDroid/result/ICCResult")
    print("input-mist-result-dir: Default to /path/to/ExaDroid/result/MistResult")
    print("output-testcase-dir: Default to /path/to/ExaDroid/result/Testcases")
    exit(2)

apks_path = os.path.abspath(sys.argv[1])
icc_result_path = config.ICCBOT_RESULT_PATH
mist_result_path = config.MIST_RESULT_PATH
result_path = config.AACT_TESTCASES_PATH
if len(sys.argv) > 2:
    icc_result_path = sys.argv[2]
if len(sys.argv) > 3:
    mist_result_path = sys.argv[3]
if len(sys.argv) > 4:
    result_path = sys.argv[4]
os.makedirs(result_path, exist_ok=True)

def main():
    global apks_path, icc_result_path, mist_result_path, result_path
    # Check Mist result json
    mist_result_path = os.path.join(mist_result_path, 'mist_result.json')
    if not os.path.exists(mist_result_path):
        print("mist_result.json not found!")
        # exit(1)

    aact_cmd = \
        f'{config.JAVA_17_PATH} ' + \
        f'-jar "{config.AACT_JAR_PATH}" ' + \
        f'-k "{apks_path}" ' + \
        f'-i "{icc_result_path}" ' + \
        f'-c "{result_path}" ' + \
        f'-s {config.RAND_SEED if config.RAND_SEED is not None else 12345678} ' + \
        f'-r {config.RAND_VAL_NUM if config.RAND_VAL_NUM is not None else 3} ' + \
        f'-st {config.STRATEGIES if config.STRATEGIES is not None else "iccBot+preset"} ' + \
        '-og -oe'
    print("[INFO] Executing: " + aact_cmd)

    if os.system(aact_cmd) != 0:
        print("[ERROR] Failed to call AACT!")
    else:
        print("[INFO] Finished calling AACT")

def cleanup():
    global apks_path, icc_result_path, mist_result_path, result_path
    logcat_path = os.path.join(config.LOGS_PATH, 'logcat.log')
    aact_log_path = os.path.join(config.LOGS_PATH, 'test-controller.log')
    ct_models_log_path = os.path.join(result_path, 'CTModels.log')
    os.unlink(logcat_path)
    shutil.copy(aact_log_path, ct_models_log_path)

if __name__ == '__main__':
    main()
    cleanup()
