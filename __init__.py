import json
import os
import platform
import shutil
import subprocess
import sys
from time import strftime, sleep

from deepcopyall import deepcopy
from flatten_any_dict_iterable_or_whatsoever import fla_tu
from mainprocess import mainprocess
from multikeyiterdict import MultiKeyIterDict
from suicideproc import commit_suicide
from touchtouch import touch
from umacajadada import read_async

iswindows = "win" in platform.platform().lower()

fi = os.path.normpath(os.sep.join(os.path.abspath(__file__).split(os.sep)[0:-1]))
os.chdir(fi)
ProxiFyreexe = os.path.normpath(os.path.join(fi, "ProxiFyre.exe"))
app_config_json = os.path.normpath(os.path.join(fi, "app-config.json"))

try:
    from ctrlchandler import set_console_ctrl_handler
except Exception:
    set_console_ctrl_handler = lambda *args, **kwargs: None


def failsafe_kill():
    f = os.path.normpath(shutil.which("taskkill.exe"))
    mainprocess([f, "/F", "/T", "/IM", ProxiFyreexe.split(os.sep)[-1]])
    sleep(2)
    commit_suicide()


def dict_to_json(d, write_to_file=True):
    d = MultiKeyIterDict(d)
    for item, keys in fla_tu(deepcopy(d)):
        lkey = list(keys)
        d[lkey] = str(item)

        if "password" in keys or "username" in keys:
            if not d[lkey]:
                del d[lkey]
                continue
        elif "appNames" in keys:
            if os.path.exists(item):
                if os.path.isfile(item) or os.path.islink(item):
                    item = os.path.normpath(os.path.dirname(item))
                if os.path.isdir(item):
                    item = os.path.normpath(item)
                else:
                    continue
                d[lkey] = item
    dum = json.dumps(d, allow_nan=False)
    if write_to_file:
        with open(app_config_json, mode="w", encoding="utf-8") as f:
            f.write(dum)
    return dum


def get_lg_file():
    lgf = "logfile_" + strftime("%Y-%m-%d") + ".txt"
    log_file = os.path.normpath(os.path.join(fi, "logs", lgf))
    if not os.path.exists(log_file):
        try:
            touch(log_file)
        except Exception:
            pass
    return log_file


def proxify_apps(app_infos, print_log=True):
    set_console_ctrl_handler(returncode=1, func=failsafe_kill)
    if iswindows:
        dict_to_json(app_infos, write_to_file=True)
        log_file = get_lg_file()
        if print_log:
            read_async(
                file=log_file,
                asthread=True,
                mode="r",
                action=lambda line: sys.stderr.write((str(line) + "\n")),
                stoptrigger=[
                    False,
                ],
            )
        return subprocess.run([ProxiFyreexe])
