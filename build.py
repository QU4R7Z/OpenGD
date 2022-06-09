import os.path
import platform
import subprocess
import time

from Utils import jsonreader
from Utils import requirements_txt

try:
    system = platform.system()
    config = jsonreader.get("Config/config.json")
    print(system)

    if system == 'Windows':
        requirements_txt.run()

        icon = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Icon/Buttercraft.ico")
        IconFolder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Icon")
        ConfigFolder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Config")
        FontFolder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Font")

        command = f"python -m nuitka --mingw64 --show-modules --follow-imports " \
                  f"--windows-company-name=QU4R7Z --windows-product-version={config.version} " \
                  f"--output-dir=Buttercraft-build --verbose --assume-yes-for-downloads " \
                  f"--windows-icon-from-ico={icon} --onefile " \
                  f"--include-data-dir={IconFolder}=Icon " \
                  f"--include-data-dir={ConfigFolder}=Config " \
                  f"--include-data-dir={FontFolder}=Font " \
                  f"--windows-disable-console " \
                  f"Buttercraft.py"

        start = time.time()
        subprocess.run(command.split(' '), shell=True, check=True)
        end = time.time()

        print(f"{end - start}s 사용됨")
        print(command)

    elif system == 'Linux':
        print(system)
    elif system == 'Darwin':
        print(system)
    else:
        print("OS를 알 수 없음")
except Exception as e:
    print(e)