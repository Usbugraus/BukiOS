import os
import platform
import sys
import subprocess
import json
import traceback
from colorama import *
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import CompleteStyle
from rich.console import Console
from rich.markdown import Markdown
from MathExpressions import *
from Editors import *

init(autoreset=True)

with open("Version.json", "r", encoding="utf-8") as f:
    version = json.load(f)

if os.name == "nt":
    os.system(f"title BukiOS {version['bukios']}")
else:
    sys.stdout.write(f"\33]0;BukiOS {version['bukios']}\a")
    sys.stdout.flush()

if getattr(sys, 'frozen', False):
    base_path = os.path.dirname(sys.executable)
else:
    base_path = os.path.dirname(__file__)

storage_path = os.path.join(base_path, "Storage")
session = PromptSession(mouse_support=True)
commands = WordCompleter(["about", "calculate", "clear", "convertnum", "delete", "edit", "exit", "help", "list", "newfile", "read", "restart", "run", "deviceinfo"], ignore_case=True)

if not os.path.exists(storage_path):
    os.makedirs(storage_path)

os.system("cls" if os.name == "nt" else "clear")
print(f"{Style.BRIGHT}{Back.BLUE}BukiOS{Style.RESET_ALL} {version['bukios']} / type help for more information")
try:
    while True:
        def safe_input(text: str) -> str:
            return text.encode("utf-8", errors="replace").decode("utf-8")
        
        prompt = session.prompt(">>> ", completer=commands, complete_style=CompleteStyle.MULTI_COLUMN)
        sfprompt = safe_input(prompt)
        
        if sfprompt.lower() == "exit":
            os.system("cls" if os.name == "nt" else "clear")
            print(f"{Fore.CYAN} İ Exiting BukiOS...")
            sys.exit(0)
        
        if not sfprompt.strip():
            continue
        
        elif sfprompt.lower() == "restart":
            os.system("cls" if os.name == "nt" else "clear")
            print(f"{Fore.CYAN} İ Restarting BukiOS...")
            subprocess.run([sys.executable, os.path.join(base_path, "Bootloader.py")])
            sys.exit(0)
            
        elif sfprompt.lower() == "about":
            print(
                f"{Style.BRIGHT + Fore.CYAN}About BukiOS\n\n{Style.RESET_ALL}"
                f"{Style.BRIGHT + Fore.RESET + Back.BLUE}BukiOS{Back.RESET} {version['bukios']}{Style.RESET_ALL}\n"
                f"{Style.BRIGHT + Fore.RESET}2025 Buğra US / Coded with Python 3.14.0{Style.RESET_ALL}\n"
                f"{Style.BRIGHT + Fore.RESET}GitHub link : {Fore.BLUE}https://github.com/Usbugraus/BukiOS{Style.RESET_ALL}"
            )
        
        elif sfprompt.lower() == "deviceinfo":
            print(
                f"{Style.BRIGHT + Fore.CYAN}Device Information\n\n{Style.RESET_ALL}"
                f"{Style.BRIGHT + Fore.RESET}Operating system{Style.RESET_ALL}   : BukiOS {version['bukios']}\n"
                f"{Style.BRIGHT + Fore.RESET}Bootloader version{Style.RESET_ALL} : {version['bootloader']}\n"
                f"{Style.BRIGHT + Fore.RESET}Processor{Style.RESET_ALL}          : {platform.processor() or 'Unknown'}\n"
                f"{Style.BRIGHT + Fore.RESET}Machine{Style.RESET_ALL}            : {platform.machine() or 'Unknown'}"
            )
        
        elif sfprompt.lower() == "help":
            print(
                f"{Style.BRIGHT + Fore.CYAN}BukiOS Help\n\n{Style.RESET_ALL}"
                f"{Style.BRIGHT + Fore.RESET}about{Style.RESET_ALL}                      : Shows about BukiOS\n"
                f"{Style.BRIGHT + Fore.RESET}calculate [expression]{Style.RESET_ALL}     : Calculates expressions\n"
                f"{Style.BRIGHT + Fore.RESET}clear{Style.RESET_ALL}                      : Clears display\n"
                f"{Style.BRIGHT + Fore.RESET}convertnum [type] [number]{Style.RESET_ALL} : Converts a number to another type\n"
                f"{Style.BRIGHT + Fore.RESET}delete [file]{Style.RESET_ALL}              : Deletes a file\n"
                f"{Style.BRIGHT + Fore.RESET}edit [file]{Style.RESET_ALL}                : Edits a file\n"
                f"{Style.BRIGHT + Fore.RESET}exit{Style.RESET_ALL}                       : Exits BukiOS\n"
                f"{Style.BRIGHT + Fore.RESET}list{Style.RESET_ALL}                       : Lists storage\n"
                f"{Style.BRIGHT + Fore.RESET}newfile [file]{Style.RESET_ALL}             : Creates a new file\n"
                f"{Style.BRIGHT + Fore.RESET}read [file]{Style.RESET_ALL}                : Read a file\n"
                f"{Style.BRIGHT + Fore.RESET}restart{Style.RESET_ALL}                    : Restarts BukiOS\n"
                f"{Style.BRIGHT + Fore.RESET}run [file]{Style.RESET_ALL}                 : Runs a code file\n"
                f"{Style.BRIGHT + Fore.RESET}deviceinfo{Style.RESET_ALL}                 : Shows information about your device"
            )
            
        elif sfprompt.lower() == "clear":
            os.system("cls" if os.name == "nt" else "clear")
            print(f"{Style.BRIGHT}BukiOS {version['bukios']} / type help for more information")
            
        elif sfprompt.lower() == "list":
            items = os.listdir(storage_path)
            if items:
                print(f"{Style.BRIGHT + Fore.CYAN}Storage\n")
                for obj in items:
                    print(Style.RESET_ALL + obj)
            else:
                print(f"{Fore.CYAN} İ Storage is empty")
                
        elif sfprompt.startswith("calculate"):
            cmd = prompt.split(maxsplit=1)
            if len(cmd) == 2:
                try:
                    exp = cmd[1]
                    result = calculate(exp)
                    print(result)
                except:
                    print(f"{Fore.YELLOW} ! Invalid expression: {exp}")
                
            else:
                print(f"{Fore.YELLOW} ! Command is incorrect")
                
        elif sfprompt.startswith("convertnum"):
            cmd = prompt.split(maxsplit=2)
            if len(cmd) == 3:
                try:
                    number = int(cmd[2])
                except Exception as e:
                    print(f"{Fore.YELLOW} ! Invalid number: {cmd[2]}")
                    continue
                
                try:
                    numtype = cmd[1]
                    result = convert(numtype, number)
                    print(result)
                except Exception as e:
                    print(Fore.YELLOW + str(e))
            
            else:
                print(f"{Fore.YELLOW} ! Command is incorrect")
                
        elif sfprompt.startswith("newfile"):

            cmd = prompt.split(maxsplit=1)
            if len(cmd) == 2:
                invalid_name_characters = ["'", '"', "!", "^", "+", "%", "/", "=", "\\", "@"]
                name = cmd[1]
                if name.endswith(".txt"):
                    if not any(word in name for word in invalid_name_characters):
                        texteditor(name)
                    else:
                        print(f"{Fore.YELLOW} ! File name includes invalid characters")
                        
                elif name.endswith(".md"):
                    if not any(word in name for word in invalid_name_characters):
                        markdowneditor(name)
                    else:
                        print(f"{Fore.YELLOW} ! File name includes invalid characters")
                        
                elif name.endswith(".py"):
                    if not any(word in name for word in invalid_name_characters):
                        pythoneditor(name)
                    else:
                        print(f"{Fore.YELLOW} ! File name includes invalid characters")
                elif name.endswith(".json"):
                    if not any(word in name for word in invalid_name_characters):
                        jsoneditor(name)
                    else:
                        print(f"{Fore.YELLOW} ! File name includes invalid characters")
                else:
                    print(f"{Fore.YELLOW} ! Unsupported file type: {'.'+name.split('.')[-1]}")
            else:
                print(f"{Fore.YELLOW} ! Command is incorrect")
        
        elif sfprompt.startswith("delete"):
            cmd = prompt.split(maxsplit=1)
            if len(cmd) == 2:
                file = cmd[1]
                try:
                    print(f"{Fore.BLUE} ? Are you sure want to detele {file}?")
                    while True:
                        confirm = input(f"{Fore.BLUE}(Y-N):")
                        if not confirm.strip():
                            continue
                        if confirm.lower() == "y":
                            os.remove(os.path.join(storage_path, file))
                            print(f"{Fore.YELLOW}{file} deleted")
                            break
                        elif confirm.lower() == "n":
                            print(f"{Fore.GREEN}{file} was not deleted")
                            break
                        else:
                            print(f"{Fore.YELLOW} ! Invalid confirm: {confirm}")
                    
                except:
                    print(f"{Fore.YELLOW} ! {file} could not be deleted")
            else:
                print(f"{Fore.YELLOW} ! Command is incorrect")
                
        elif sfprompt.startswith("read"):
            cmd = prompt.split(maxsplit=1)
            if len(cmd) == 2:
                file = cmd[1]
                try:
                    if file.endswith(".md"):
                        with open(os.path.join(storage_path, file), "r", encoding="utf-8") as f:
                            text = f.read()
                        print(f"{Style.BRIGHT + Fore.CYAN}{file.capitalize()}\n")
                        markdown = Markdown(text)
                        Console().print(markdown)
                        
                    elif file.endswith(".json"):
                        with open(os.path.join(storage_path, file), "r", encoding="utf-8") as f:
                            data = json.load(f)
                        print(f"{Style.BRIGHT + Fore.CYAN}{file.capitalize()}\n")
                        for key in data:
                            print(f"{key} : {data[key]}")
                    
                    else:
                        with open(os.path.join(storage_path, file), "r", encoding="utf-8") as f:
                            text = f.read()
                        print(f"{Style.BRIGHT + Fore.CYAN}{file.capitalize()}\n")
                        print(text)
                        
                        
                except FileNotFoundError:
                    print(f"{Fore.YELLOW} ! File not found")
            else:
                print(f"{Fore.YELLOW} ! Command is incorrect")
                
        elif sfprompt.startswith("run"):
            cmd = prompt.split(maxsplit=1)
            if len(cmd) == 2:
                file = cmd[1]
                if file.endswith(".py"):
                    file_path = os.path.join(storage_path, file)
                    if os.path.exists(file_path):
                        try:
                            subprocess.run([sys.executable, file_path])
                        except:
                            print(f"{Fore.YELLOW} ! File could not be executed")
                    else:
                        print(f"{Fore.YELLOW} ! File not found")
                else:
                    print(f"{Fore.YELLOW} ! This file cannot be executed")
            else:
                print(f"{Fore.YELLOW} ! Command is incorrect")
                
        elif sfprompt.startswith("edit"):
            
            cmd = prompt.split(maxsplit=1)
            if len(cmd) == 2:
                file = cmd[1]
                try:
                    if file.endswith(".py"):
                        with open(os.path.join(storage_path, file), "r", encoding="utf-8") as f:
                            content = f.read()
                            
                        pythoneditor(file, initial=content)
                    elif file.endswith(".txt"):
                        with open(os.path.join(storage_path, file), "r", encoding="utf-8") as f:
                            content = f.read()
                            
                        texteditor(file, initial=content)
                        
                    elif file.endswith(".md"):
                        with open(os.path.join(storage_path, file), "r", encoding="utf-8") as f:
                            content = f.read()
                            
                        markdowneditor(file, initial=content)
                        
                    elif file.endswith(".json"):
                        with open(os.path.join(storage_path, file), "r", encoding="utf-8") as f:
                            content = json.load(f)
                            
                        jsoneditor(file, initial=json.dumps(content, indent=4))
                        
                    else:
                        print(f"{Fore.YELLOW} ! Unsupported file type: {'.'+file.split('.')[-1]}")
                    
                except FileNotFoundError:
                    print(f"{Fore.YELLOW} ! File not found")
            else:
                print(f"{Fore.YELLOW} ! Command is incorrect")

        else:
            print(f"{Fore.YELLOW} ! Invalid command: {sfprompt}")      
            
except KeyboardInterrupt:
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{Fore.CYAN} İ System interrupted.\nExiting BukiOS...")
    sys.exit(0)
    
except Exception as e:
    sys.stdout.write('\a')
    sys.stdout.flush()
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{Style.BRIGHT}BukiOS {version['bukios']}\n\n{Style.NORMAL + Fore.RED} X An error occurred:")
    print(Fore.RED + traceback.format_exc())
    print(
        f"{Style.BRIGHT + Fore.CYAN}Recovery Commands\n\n{Style.RESET_ALL}"
        f"{Style.BRIGHT + Fore.RESET}exit{Style.RESET_ALL}        : Exits BukiOS\n"
        f"{Style.BRIGHT + Fore.RESET}restart{Style.RESET_ALL}     : Restarts BukiOS\n"
    )
    while True:
        recovery_commands = WordCompleter(["exit", "restart"], ignore_case=True)
        recovery_prompt = session.prompt(">>> ", completer=recovery_commands, complete_style=CompleteStyle.MULTI_COLUMN)
        if recovery_prompt.lower() == "exit":
            os.system("cls" if os.name == "nt" else "clear")
            print(f"{Fore.CYAN} İ Exiting BukiOS...")
            sys.exit(0)
                
        if not recovery_prompt.strip():
            continue
            
        elif recovery_prompt.lower() == "restart":
            os.system("cls" if os.name == "nt" else "clear")
            print(f"{Fore.CYAN} İ Restarting BukiOS...")
            subprocess.run([sys.executable, os.path.join(base_path, "Bootloader.py")])
            sys.exit(0)
        else:
            print(f"{Fore.YELLOW} ! Invalid command: {recovery_prompt}")
    