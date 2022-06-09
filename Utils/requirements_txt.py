import subprocess
import platform


def run():
    try:
        system = platform.system()
        print(system)
        if system == 'Windows':
            command = f"pip freeze > requirements.txt"
            subprocess.run(command, shell=True)

        elif system == 'Linux':
            print(system)
        elif system == 'Darwin':
            print(system)
        else:
            print("OS를 알 수 없음")
    except Exception as e:
        print(e)
