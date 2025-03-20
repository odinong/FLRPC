import sys
import psutil
import pygetwindow as gw
from pypresence import Presence
import time

client_id = '1326072649306341376'

def findprocess():
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            procname = proc.info['name']
            if procname and 'fl64' in procname.lower():
                return proc.info['pid']
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return None

def getinfo():
    try:
        windows = gw.getAllTitles()
        for window in windows:
            if ' - FL Studio' in window:
                project_name = window.rsplit(' - FL Studio', 1)[0].strip()
                version = window.rsplit(' - FL Studio', 1)[1].strip()
                return projname, version
            elif 'FL Studio' in window:
                return "Untitled Project", window.strip()
    except Exception as e:
        print(f"error fetching fl info: {e}")
    return "Untitled Project", "Unknown Version"

def updaterpc(RPC, project_name, version):
    try:
        image = "f-l-studio-logo-icon-bywujcetpfezokh6_1_"
        RPC.update(
            state=f"Working on: {project_name}",
            details="In FL Studio",
            large_image=image,
            large_text=f"FL Studio Version: {version}",
            small_image = "flibb",
            small_text = "FLRPC, written by @tearintomyskin, github.com/odinong/FLRPC",
            start=int(time.time())
        )
        print(f"RPC updated with project name: {project_name} (FL Studio Version: {version})")
    except Exception as e:
        print(f"error updating RPC: {e}")

try:
    RPC = Presence(client_id)
    RPC.connect()
    print("RPC connected.")
except Exception as e:
    print(f"failed to connect: {e}")
    exit(1)

lastprojname = None

while True:
    pid = findprocess()
    if pid:
        projname, version = getinfo()
        if projname != lastprojname:
            print(f"detected new project: {projname} (FL Studio Version: {version})")
            updaterpc(RPC, projname, version)
            lastprojname = projname
    else:
        if lastprojname is not None:
            print("process not found. Clearing last project name and exiting.")
            sys.exit()
            lastprojname = None
    time.sleep(0.1)

