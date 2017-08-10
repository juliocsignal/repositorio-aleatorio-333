import sys
from cx_Freeze import setup, Executable


build_exe_options = {"packages": ["os", "datetime"], "excludes": []}

base = None
if sys.platform == "win32":
    base = "Console"  # para execuções em terminal

setup(name="GetSpecJoin",
      version="0.1",
      description="My GUI application!",
      options={"build_exe": build_exe_options},
      executables=[Executable("240117.py", base=base)])
