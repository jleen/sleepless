# Copyright (c) 2020 John Leen

import platform
import subprocess
import sys


def caffeinate():
    if platform.system() == 'Darwin':
        from discjockey import pmset
        pmset.prevent_idle_sleep('Python script')
    elif platform.system() == 'Windows':
        import ctypes
        ES_CONTINUOUS = 0x80000000
        ES_SYSTEM_REQUIRED = 0x00000001
        ctypes.windll.kernel32.SetThreadExecutionState(
                ES_CONTINUOUS | ES_SYSTEM_REQUIRED)
