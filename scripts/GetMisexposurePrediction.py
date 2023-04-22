#!/usr/bin/python3
#! -*- coding: utf-8 -*-

import os
import sys
import config
import shutil

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("usage: GetMisexposurePrediction.py <input-apk-dir> [<output-mist-result-dir>]\n")
    print("output-mist-result-dir: Default to /path/to/ExaDroid/result/MistResult")
    exit(2)

apk_root = os.path.abspath(sys.argv[1])
result_path = config.MIST_RESULT_PATH
if len(sys.argv) > 2:
    result_path = sys.argv[2]
os.makedirs(result_path, exist_ok=True)

# Find APKs
apks_lis = []
for root, dirs, files in os.walk(apk_root):
    for file in files:
        if not file.endswith('.apk'):
            continue
        apks_lis.append(os.path.abspath(os.path.join(root, file)))
        
if len(apks_lis) == 0:
    print("No apk found!")
    exit(0)

def run_apktool():
    global apks_lis, apk_root, result_path
    # Run ApkTool
    apktool_out_path = os.path.join(config.TEMP_PATH, 'apktool_out')
    apktool_res_path = os.path.join(config.TEMP_PATH, 'apktool_res')
    os.makedirs(apktool_out_path, exist_ok=True)
    os.makedirs(apktool_res_path, exist_ok=True)

    manifest_result_path = os.path.join(result_path, 'manifest')
    os.makedirs(manifest_result_path, exist_ok=True)

    APKTOOL_CMD_TEMPLATE = config.format_args([
        config.JAVA_8_PATH,
        '-jar', config.APKTOOL_JAR_PATH,
        'd',
        '-o', apktool_out_path,
        '-p', apktool_res_path,
        '-f', '{apk_path}',
        '>>', f'{config.LOGS_PATH}/apktool-' + '{apk_name}.log'
    ])

    for apk_path in apks_lis:
        apk_name, _ = os.path.splitext(os.path.basename(apk_path))
        apktool_cmd = APKTOOL_CMD_TEMPLATE.format(
            apk_path=apk_path,
            apk_name=apk_name,
        )
        print("[INFO] Executing: " + apktool_cmd)
        if os.system(apktool_cmd) != 0:
            print("[ERROR] Error when running ApkTool on [{}]".format(apk_path))
        else:
            print("[INFO] Finshed running ApkTool on [{}]".format(apk_path))
        
        if os.path.exists(apktool_out_path):
            manifest_path = os.path.join(apktool_out_path, 'AndroidManifest.xml')
            if not os.path.exists(manifest_path):
                print("[ERROR] AndroidManifest.xml of [{}] not found!".format(apk_name))
                continue
            manifest_new_name = f'{apk_name}_manifest.xml'
            # shutil.copyfile(manifest_path, os.path.join(apk_result_path, manifest_new_name))
            shutil.copyfile(manifest_path, os.path.join(manifest_result_path, manifest_new_name))
            print(f"[INFO] Copied [{manifest_new_name}]")

def run_mist():
    global apks_lis, apk_root, result_path
    # Run Mist.jar
    pea_result_path = os.path.join(result_path, 'pea')
    manifest_result_path = os.path.join(result_path, 'manifest')
    ser_result_path = os.path.join(result_path, 'serialize')
    
    os.makedirs(pea_result_path, exist_ok=True)
    os.makedirs(ser_result_path, exist_ok=True)
    
    MIST_CMD_TEMPLATE = config.format_args([
        config.JAVA_8_PATH,
        '-jar', config.MIST_JAR_PATH,
        apk_root,
        '{apk_name}',
        pea_result_path,
        manifest_result_path,
        ser_result_path,
        '>>', f'{config.LOGS_PATH}/Mist-' + '{apk_name}.log'
    ])
    
    old_cwd = os.getcwd()
    os.chdir(config.MIST_ROOT)
    for apk_path in apks_lis:
        apk_name = os.path.basename(apk_path)
        mist_cmd = MIST_CMD_TEMPLATE.format(apk_name=apk_name)
        print("[INFO] Executing: " + mist_cmd)
        if os.system(mist_cmd) != 0:
            print("[ERROR] Error when running Mist.jar on [{}]".format(apk_name))
        else:
            print("[INFO] Finshed running Mist.jar on [{}]".format(apk_name))
    os.chdir(old_cwd)

def run_mist_analyzer():
    global apks_lis, apk_root, result_path
    # Run MistResultAnalyzer.jar
    ser_result_path = os.path.join(result_path, 'serialize')
    res_result_path = os.path.join(result_path, 'summarize')
    sum_result_path = os.path.join(result_path, 'dataSummary')
    mis_result_path = os.path.join(result_path, 'misexpose')
    
    os.makedirs(res_result_path, exist_ok=True)
    os.makedirs(sum_result_path, exist_ok=True)
    os.makedirs(mis_result_path, exist_ok=True)
    
    mist_analyzer_cmd = config.format_args([
        config.JAVA_8_PATH,
        '-jar', config.MIST_ANALYZER_JAR_PATH,
        ser_result_path,
        res_result_path,
        sum_result_path,
        mis_result_path,
        '>>', f'{config.LOGS_PATH}/MistResultAnalyzer.log'
    ])
    
    old_cwd = os.getcwd()
    os.chdir(config.MIST_ROOT)
    print("[INFO] Executing: " + mist_analyzer_cmd)
    if os.system(mist_analyzer_cmd) != 0:
        print("[ERROR] Error when running MistResultAnalyzer.jar")
    else:
        print("[INFO] Finshed running MistResultAnalyzer.jar")
    os.chdir(old_cwd)

def run_ea_classifier():
    # TODO: Run EAClassifier.pl
    pass

def cleanup():
    shutil.rmtree(config.TEMP_PATH)
    if os.path.exists(os.path.join(config.MIST_ROOT, 'sootOutput')):
        shutil.rmtree(os.path.join(config.MIST_ROOT, 'sootOutput'))
    os.makedirs(config.TEMP_PATH)

if __name__ == '__main__':
    run_apktool()
    run_mist()
    run_mist_analyzer()
    run_ea_classifier()
    cleanup()
