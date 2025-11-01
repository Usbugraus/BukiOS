import sys
import os
import traceback
import json
import subprocess

version = {
    "bootloader": "1.5.5",
    "bukios": "1.0.10"
}
error_occurred = False

try:
    from colorama import init, Fore, Style
except ModuleNotFoundError:
    print(f"BukiOS {version['bukios']}\n\n X Bootloader modules not found. Installing bootloader modules...")
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "colorama"],
            check=True
        )
        from colorama import init, Fore, Style
    except Exception:
        print(" X Bootloader modules could not be installed.")
        sys.exit(1)

init(autoreset=True)

def boot():
    sys.stdout.write('\a')
    sys.stdout.flush()
    import Display

os.system("cls" if os.name == "nt" else "clear")
print(f"{Fore.CYAN} İ BukiOS Loading...")
with open("Version.json", "w", encoding="utf-8") as f:
    json.dump(version, f, indent=4, ensure_ascii=False)

if os.name == "nt":
    os.system(f"title BukiOS {version['bukios']}")
else:
    sys.stdout.write(f"\33]0;BukiOS {version['bukios']}\a")
    sys.stdout.flush()  

try:
    boot()
    
except ModuleNotFoundError:
    error_occurred = True
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{Style.BRIGHT}BukiOS {version['bukios']}\n\n{Style.NORMAL + Fore.CYAN} İ Operating system modules not found. Installing oprating system modules...")
    try:
        if os.name == "nt":
            subprocess.run([sys.executable, "-m", "pip", "install", "prompt_toolkit", "colorama", "rich"], check=True)
            os.system("cls" if os.name == "nt" else "clear")
            print(f"{Fore.CYAN} İ BukiOS Loading...")
            boot()
        else:
            subprocess.run(["pip3", "install", "prompt_toolkit", "colorama", "rich"], check=True)
            os.system("cls" if os.name == "nt" else "clear")
            print(f"{Fore.CYAN} İ BukiOS Loading...")
            boot()
    except:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{Style.BRIGHT}BukiOS {version['bukios']}\n\n{Style.NORMAL + Fore.RED} X Operating system modules could not be installed")
    
except Exception as e:
    error_occurred = True
    sys.stdout.write('\a')
    sys.stdout.flush()
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{Style.BRIGHT}BukiOS {version['bukios']}\n\n{Style.NORMAL + Fore.RED} X An error occurred while booting:")
    print(Fore.RED + traceback.format_exc())
        
finally:
    if error_occurred:
        if os.name == "nt":
            os.system("pause")
        else:
            input()
