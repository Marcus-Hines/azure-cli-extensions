#!/usr/bin/env python3

import shutil
import subprocess

def aks_web_app_init():
    validation = pre_setup_validations()
    if validation:
        run_binary()
        cmd_finish()

def pre_setup_validations() -> bool:
    print("The DraftV2 setup is in progress ...")
    print("Checking if Binary exist ...")
    cmd_exist = cmd_exists("ifconfig")
    print(cmd_exist)
    if not cmd_exist:
        print("Checking if Binary Does Not exist Bail Early...")
    return cmd_exist

def cmd_exists(cmd: str) -> bool:
    return shutil.which(cmd) is not None

def run_binary():
    print("Running DraftV2 Binary ...")
    # for keen mind here is the difference of .popen vs .run
    # subprocess.run(["ls", "-l"], shell=True, check=True, stdout=subprocess.PIPE) # This will run the command and return any output
    process = subprocess.Popen(
        ['ifconfig'], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout, stderr = process.communicate()
    exit_code = process.wait()
    print("If non zero then bnary ran fine and job is done.")
    print(stdout, stderr, exit_code)
    print("prepare exiting mechanism.")

def cmd_finish():
    print("Depending ont the exit_code display message")
    print("We are done Stop.")