#!/usr/bin/python3
#! -*- coding: utf-8 -*-

import os
import shutil
import sys
import config

if len(sys.argv) < 2 or len(sys.argv) > 5:
    print("usage: FindCrashes.py <input-apk-dir> [<input-icc-result-dir>] [<input-mist-result-dir>] [<input-testcases-dir>] [<input-result-dir>]\n")
    print("input-icc-result-dir: Default to /path/to/ExaDroid/result/ICCResult")
    print("input-mist-result-dir: Default to /path/to/ExaDroid/result/MistResult")
    print("input-testcases-dir: Default to /path/to/ExaDroid/result/Testcases")
    print("input-result-dir: Default to /path/to/ExaDroid/result/TestExecutionResult")
    exit(2)
    # sys.argv = [sys.argv[0], 'D:/Projects/MIST-AACT/$MIST30-APKs']

apks_path = os.path.abspath(sys.argv[1])
icc_result_path = config.ICCBOT_RESULT_PATH
mist_result_path = config.MIST_RESULT_PATH
testcases_path = config.AACT_TESTCASES_PATH
result_path = config.AACT_RESULT_PATH
if len(sys.argv) > 2:
    icc_result_path = sys.argv[2]
if len(sys.argv) > 3:
    mist_result_path = sys.argv[3]
if len(sys.argv) > 4:
    testcases_path = sys.argv[4]
if len(sys.argv) > 5:
    result_path = sys.argv[5]

def main():
    # TODO
    pass

if __name__ == '__main__':
    main()
