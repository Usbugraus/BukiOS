from prompt_toolkit import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import Layout, HSplit
from prompt_toolkit.widgets import TextArea
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style as PTStyle
from colorama import Fore, init
import os

init(autoreset=True)

def pythoneditor(filename, initial=""):
    editor_style = PTStyle.from_dict({
        "textarea": "bg:#BFBFBF #404040",
    })
    
    python_keywords = [
        "False", "True", "None", "and", "as", "assert", "async", "await", "break",
        "class", "continue", "def", "del", "elif", "else", "except", "finally",
        "for", "from", "global", "if", "import", "in", "is", "lambda", "nonlocal",
        "not", "or", "pass", "raise", "return", "try", "while", "with", "yield",
        "print", "input", "len", "range", "open", "list", "dict", "set", "int", "str"
    ]

    completer = WordCompleter(python_keywords, ignore_case=True)

    header_text = f"Python Editor - {filename}.py / Ctrl+S: Save | Ctrl+Q: Exit | Tab: Auto complete"
    header = Window(
        content=FormattedTextControl(header_text),
        height=1,
    )

    textbox = TextArea(
        text=initial,
        multiline=True,
        wrap_lines=True,
        scrollbar=True,
        style="class:textarea",
        line_numbers=True,
        completer=completer,
        complete_while_typing=True
    )

    kb = KeyBindings()
    saved = {"status": False}

    @kb.add("c-s")
    def save_text(event):
        if not os.path.exists(f"Storage/{filename}"):
            with open(f"Storage/{filename}.py", "w", encoding="utf-8-sig") as f:
                f.write(textbox.text)
        else:
            with open(f"Storage/{filename}", "w", encoding="utf-8-sig") as f:
                f.write(textbox.text)
        saved["status"] = True
        event.app.exit(result=textbox.text)

    @kb.add("c-q")
    def exit_app(event):
        saved["status"] = False
        event.app.exit(result=textbox.text)

    @kb.add("enter")
    def _(event):
        buffer = event.app.current_buffer
        document = buffer.document
        current_line = document.current_line_before_cursor
        indentation = ""
        for char in current_line:
            if char in [" ", "\t"]:
                indentation += char
            else:
                break
        if current_line.strip().endswith(":"):
            indentation += "    "
        buffer.insert_text("\n" + indentation)

    root_container = HSplit([header, textbox])

    app = Application(
        layout=Layout(root_container),
        key_bindings=kb,
        full_screen=True,
        style=editor_style,
        mouse_support=True
    )

    text = app.run()

    if saved["status"]:
        print(f"{Fore.GREEN}{filename}.py is saved" if not os.path.exists(f"Storage/{filename}") else f"{Fore.GREEN}{filename} is saved")
    else:
        print(f"{Fore.YELLOW}{filename}.py was not saved" if not os.path.exists(f"Storage/{filename}") else f"{Fore.GREEN}{filename} was not saved")

    return text

def texteditor(filename, initial=""):
    editor_style = PTStyle.from_dict({
        "textarea": "bg:#BFBFBF #404040",
    })

    header_text = f"Text Editor - {filename}.txt / Ctrl+S: Save | Ctrl+Q: Exit"
    header = Window(
        content=FormattedTextControl(header_text),
        height=1,
    )

    # TextArea
    textbox = TextArea(
        text=initial,
        multiline=True,
        wrap_lines=True,
        style="class:textarea",
        scrollbar=True,
    )

    kb = KeyBindings()
    saved = {"status": False}

    @kb.add("c-s")
    def save_text(event):
        if not os.path.exists(f"Storage/{filename}"):
            with open(f"Storage/{filename}.py", "w", encoding="utf-8-sig") as f:
                f.write(textbox.text)
        else:
            with open(f"Storage/{filename}", "w", encoding="utf-8-sig") as f:
                f.write(textbox.text)
        saved["status"] = True
        event.app.exit(result=textbox.text)

    @kb.add("c-q")
    def exit_app(event):
        saved["status"] = False
        event.app.exit(result=textbox.text)

    root_container = HSplit([header, textbox])

    app = Application(
        layout=Layout(root_container),
        key_bindings=kb,
        full_screen=True,
        style=editor_style,
        mouse_support=True
    )

    text = app.run()

    if saved["status"]:
        print(f"{Fore.GREEN}{filename}.txt is saved" if not os.path.exists(f"Storage/{filename}") else f"{Fore.GREEN}{filename} is saved")
    else:
        print(f"{Fore.YELLOW}{filename}.txt was not saved" if not os.path.exists(f"Storage/{filename}") else f"{Fore.GREEN}{filename} was not saved")

    return text

def markdowneditor(filename, initial=""):
    editor_style = PTStyle.from_dict({
        "textarea": "bg:#BFBFBF #404040",
    })

    header_text = f"Markdown Editor - {filename}.md / Ctrl+S: Save | Ctrl+Q: Exit"
    header = Window(
        content=FormattedTextControl(header_text),
        height=1,
    )

    # TextArea
    textbox = TextArea(
        text=initial,
        multiline=True,
        wrap_lines=True,
        style="class:textarea",
        scrollbar=True,
    )

    kb = KeyBindings()
    saved = {"status": False}

    @kb.add("c-s")
    def save_text(event):
        if not os.path.exists(f"Storage/{filename}"):
            with open(f"Storage/{filename}.md", "w", encoding="utf-8-sig") as f:
                f.write(textbox.text)
        else:
            with open(f"Storage/{filename}", "w", encoding="utf-8-sig") as f:
                f.write(textbox.text)
        saved["status"] = True
        event.app.exit(result=textbox.text)

    @kb.add("c-q")
    def exit_app(event):
        saved["status"] = False
        event.app.exit(result=textbox.text)

    root_container = HSplit([header, textbox])

    app = Application(
        layout=Layout(root_container),
        key_bindings=kb,
        full_screen=True,
        style=editor_style,
        mouse_support=True
    )

    text = app.run()

    if saved["status"]:
        print(f"{Fore.GREEN}{filename}.md is saved" if not os.path.exists(f"Storage/{filename}") else f"{Fore.GREEN}{filename} is saved")
    else:
        print(f"{Fore.YELLOW}{filename}.md was not saved" if not os.path.exists(f"Storage/{filename}") else f"{Fore.GREEN}{filename} was not saved")

    return text