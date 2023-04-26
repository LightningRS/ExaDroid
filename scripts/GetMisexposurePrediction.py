#!/usr/bin/python3
#! -*- coding: utf-8 -*-

import json
import os
import sys
import config
import shutil
from xml.etree import cElementTree as ET

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
    apktool_out_path = os.path.join(config.TEMP_PATH, '{apk_name}/apktool_out')
    apktool_res_path = os.path.join(config.TEMP_PATH, '{apk_name}/apktool_res')

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
        manifest_path = os.path.join(apktool_out_path.format(apk_name=apk_name), 'AndroidManifest.xml')
        manifest_result_path = os.path.join(result_path, f'{apk_name}/manifest')

        if not os.path.exists(manifest_path):
            os.makedirs(apktool_out_path.format(apk_name=apk_name), exist_ok=True)
            os.makedirs(apktool_res_path.format(apk_name=apk_name), exist_ok=True)

            os.makedirs(manifest_result_path, exist_ok=True)
            
            apktool_cmd = APKTOOL_CMD_TEMPLATE.format(
                apk_path=apk_path,
                apk_name=apk_name,
            )
            print("[INFO] Executing: " + apktool_cmd)
            if os.system(apktool_cmd) != 0:
                print("[ERROR] Error when running ApkTool on [{}]".format(apk_path))
            else:
                print("[INFO] Finshed running ApkTool on [{}]".format(apk_path))
        
        if not os.path.exists(manifest_path):
            print("[ERROR] AndroidManifest.xml of [{}] not found!".format(apk_name))
            continue
        manifest_new_name = f'{apk_name}_manifest.xml'
        manifest_new_path = os.path.join(manifest_result_path, manifest_new_name)
        shutil.copyfile(manifest_path, manifest_new_path)
        print(f"[INFO] Copied [{manifest_path}] to [{manifest_new_path}]")

def run_mist():
    global apks_lis, apk_root, result_path
    # Run Mist.jar
    manifest_result_path = os.path.join(result_path, '{apk_name}/manifest')
    pea_result_path = os.path.join(result_path, '{apk_name}/pea')
    ser_result_path = os.path.join(result_path, '{apk_name}/serialize')
    
    MIST_CMD_TEMPLATE = config.format_args([
        config.JAVA_8_PATH,
        '-jar', config.MIST_JAR_PATH,
        apk_root,
        '{apk_path}',
        pea_result_path,
        manifest_result_path,
        ser_result_path,
        '>>', f'{config.LOGS_PATH}/Mist-' + '{apk_name}.log'
    ])
    
    old_cwd = os.getcwd()
    os.chdir(config.MIST_ROOT)

    for apk_path in apks_lis:
        apk_name, _ = os.path.splitext(os.path.basename(apk_path))
        os.makedirs(pea_result_path.format(apk_name=apk_name), exist_ok=True)
        os.makedirs(ser_result_path.format(apk_name=apk_name), exist_ok=True)
        mist_cmd = MIST_CMD_TEMPLATE.format(
            apk_path=apk_path,
            apk_name=apk_name,
        )
        print("[INFO] Executing: " + mist_cmd)
        if os.system(mist_cmd) != 0:
            print("[ERROR] Error when running Mist.jar on [{}.apk]".format(apk_name))
        else:
            print("[INFO] Finshed running Mist.jar on [{}.apk]".format(apk_name))
    os.chdir(old_cwd)

def run_mist_analyzer():
    global apks_lis, apk_root, result_path
    # Run MistResultAnalyzer.jar
    ser_result_path = os.path.join(result_path, '{apk_name}/serialize')
    res_result_path = os.path.join(result_path, '{apk_name}/summarize')
    sum_result_path = os.path.join(result_path, '{apk_name}/dataSummary')
    mis_result_path = os.path.join(result_path, '{apk_name}/misexpose')

    MIST_ANALYAZER_CMD_TEMPLATE = config.format_args([
        config.JAVA_8_PATH,
        '-jar', config.MIST_ANALYZER_JAR_PATH,
        ser_result_path,
        res_result_path,
        sum_result_path,
        mis_result_path,
        '>>',
        os.path.join(config.LOGS_PATH, 'MistResultAnalyzer-{apk_name}.log')
    ])
    
    old_cwd = os.getcwd()
    os.chdir(config.MIST_ROOT)

    for apk_path in apks_lis:
        apk_name, _ = os.path.splitext(os.path.basename(apk_path))
    
        os.makedirs(res_result_path.format(apk_name=apk_name), exist_ok=True)
        os.makedirs(sum_result_path.format(apk_name=apk_name), exist_ok=True)
        os.makedirs(mis_result_path.format(apk_name=apk_name), exist_ok=True)
        
        mist_analyzer_cmd = MIST_ANALYAZER_CMD_TEMPLATE.format(apk_name=apk_name)
        print("[INFO] Executing: " + mist_analyzer_cmd)
        if os.system(mist_analyzer_cmd) != 0:
            print(f"[ERROR] Error when running MistResultAnalyzer.jar on [{apk_name}.apk]")
        else:
            print(f"[INFO] Finshed running MistResultAnalyzer.jar on [{apk_name}.apk]")
    os.chdir(old_cwd)

def run_ea_classifier():
    global result_path

    final_result = ''
    for apk_path in apks_lis:
        apk_name, _ = os.path.splitext(os.path.basename(apk_path))
        mis_result_path = os.path.join(result_path, f'{apk_name}/misexpose')
        for f_file in os.listdir(mis_result_path):
            final_result += f'filename: {f_file}\n'
            f_path = os.path.join(mis_result_path, f_file)
            classifier_cmd = config.format_args([
                'swipl',
                '-f', os.path.join(config.ROOT_PATH, "scripts/EAClassifier.pl"),
                '-s', f_path,
                '-g', 'solve', '-t', 'halt'
            ])
            print(f"[INFO] Executing: {classifier_cmd}")
            classifier_res = os.popen(classifier_cmd).readlines()
            final_result += ''.join(classifier_res)
            final_result += '\n'
    final_result_path = os.path.join(result_path, 'mist_result.txt')
    with open(final_result_path, 'w', encoding='utf-8') as f_result:
        f_result.write(final_result)
    
    return final_result

def convert_mist_result(final_result: str):
    global result_path

    # Convert mist_result.txt to mist_result.json
    mist_json_path = os.path.join(result_path, 'mist_result.json')
    res_lines = final_result.splitlines()

    i = 0
    res_dic = dict()
    while (i * 4 + 1) < len(res_lines):
        file_name = res_lines[i * 4].replace('filename: ', '').replace('_misExpose.txt', '')
        result = res_lines[i * 4 + 2].replace('result: ', '')
        comp_name = None
        pkg_name = None
        for apk_path in apks_lis:
            apk_name, _ = os.path.splitext(os.path.basename(apk_path))
            if f'{apk_name}_' in file_name:
                comp_name = file_name.replace(f'{apk_name}_', '')
                manifest_path = os.path.join(result_path, f'{apk_name}/manifest/{apk_name}_manifest.xml')
                with open(manifest_path, 'r', encoding='utf-8') as f:
                    manifest_xml = ET.parse(f)
                pkg_name = manifest_xml.getroot().attrib.get('package')
                break
        if comp_name is None:
            print(f"[ERROR] Failed to get comp_name: {file_name}")
            i += 1
            continue
        if pkg_name is None:
            print(f"[ERROR] Failed to get pkg_name: {file_name}")
            i += 1
            continue
        print('[INFO] Mist result for {}/{}: {}'.format(pkg_name, comp_name, result))
        if pkg_name not in res_dic:
            res_dic[pkg_name] = dict()
        res_dic[pkg_name][comp_name] = result
        i += 1

    with open(mist_json_path, 'w', encoding='utf-8') as f:
        json.dump(res_dic, f, indent=4, sort_keys=True)


def cleanup():
    print("[INFO] Cleaning up...")
    shutil.rmtree(config.TEMP_PATH)
    if os.path.exists(os.path.join(config.MIST_ROOT, 'sootOutput')):
        shutil.rmtree(os.path.join(config.MIST_ROOT, 'sootOutput'))
    os.makedirs(config.TEMP_PATH)
    print("[INFO] Finished cleaning up")

if __name__ == '__main__':
    # run_apktool()
    # run_mist()
    run_mist_analyzer()
    final_result = run_ea_classifier()
    convert_mist_result(final_result)
    # cleanup()
