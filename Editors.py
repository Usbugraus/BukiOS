from prompt_toolkit import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import Layout, HSplit
from prompt_toolkit.widgets import TextArea
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style as PTStyle
from colorama import Fore, init
import re
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

    header_text = f"Python Editor - {filename} / Ctrl+S: Save | Ctrl+Q: Exit | Tab: Auto complete"

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

    header_text = f"Text Editor - {filename} / Ctrl+S: Save | Ctrl+Q: Exit"
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

    header_text = f"Markdown Editor - {filename} / Ctrl+S: Save | Ctrl+Q: Exit"
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

def jsoneditor(filename, initial=""):
    editor_style = PTStyle.from_dict({
        "textarea": "bg:#BFBFBF #404040",
    })

    header_text = f"Json Editor - {filename} / Ctrl+S: Save | Ctrl+Q: Exit"
    header = Window(
        content=FormattedTextControl(header_text),
        height=1,
    )

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
        with open(f"Storage/{filename}", "w", encoding="utf-8") as f:
            f.write(textbox.text)
        saved["status"] = True
        event.app.exit(result=textbox.text)

    @kb.add("c-q")
    def exit_app(event):
        saved["status"] = False
        event.app.exit(result=textbox.text)

    # Otomatik girinti ve tablama
    @kb.add("enter")
    def auto_indent(event):
        buffer = event.current_buffer
        line = buffer.document.current_line_before_cursor

        # Mevcut satırın girintisini hesapla
        current_indent = re.match(r"\s*", line).group(0)

        # Eğer satır { [ ( ile bitiyorsa yeni satırda bir seviye fazla girinti yap
        if line.strip().endswith(("{", "[", "(")):
            buffer.newline(copy_margin=False)
            buffer.insert_text(current_indent + " " * 4)
        # Eğer satır } ] ) ile bitiyorsa aynı girintiyi koru
        elif line.strip().startswith(("}", "]", ")")):
            buffer.newline(copy_margin=False)
            buffer.insert_text(current_indent)
        else:
            # Sadece aynı girintiyi koru
            buffer.newline(copy_margin=False)
            buffer.insert_text(current_indent)

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
        print(f"{Fore.GREEN}{filename} kaydedildi.")
    else:
        print(f"{Fore.YELLOW}{filename} kaydedilmedi.")

    return text