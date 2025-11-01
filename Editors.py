from prompt_toolkit import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import Layout, HSplit
from prompt_toolkit.widgets import TextArea
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style as PTStyle
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.styles.pygments import style_from_pygments_cls
from pygments.style import Style as PygmentsStyle
from pygments.token import Keyword, Name, Comment, String, Number, Operator
from pygments.lexers import PythonLexer
from colorama import Fore, init
import re
import os

init(autoreset=True)

class SyntaxHighlighter(PygmentsStyle):
    default_style = ""
    styles = {
        Keyword: 'bold #bf0000',
        Keyword.Constant: '#bf0040',
        Operator.Word: 'bold #bf00bf',
        Name.Function: '#bf4000',
        Name.Builtin: '#bf8000',
        Name.Namespace: '#404040',
        Name.Decorator: '#4000bf',
        Comment: 'italic #808080',
        String: '#00bf00',
        String.Doc: '#00bf40',
        Number.Integer: '#0040bf',
        Number.Float: '#0000bf',
        Operator: '#808080',
    }

app_style = PTStyle.from_dict({
    "textarea": "bg:#BFBFBF #404040",
})

def pythoneditor(filename, initial=""):
    python_keywords = [
        "False", "True", "None", "and", "as", "assert", "async", "await", "break",
        "class", "continue", "def", "del", "elif", "else", "except", "finally",
        "for", "from", "global", "if", "import", "in", "is", "lambda", "nonlocal",
        "not", "or", "pass", "raise", "return", "try", "while", "with", "yield",
        "print", "input", "len", "range", "open", "list", "dict", "set", "int", "str"
    ]

    completer = WordCompleter(python_keywords, ignore_case=True)

    header = Window(
        content=FormattedTextControl(f"Python Editor - {filename} / Ctrl+S: Save | Ctrl+Q: Exit | Tab: Auto complete"),
        height=1,
    )

    textbox = TextArea(
        text=initial,
        multiline=True,
        wrap_lines=True,
        scrollbar=True,
        line_numbers=True,
        style="class:textarea",
        completer=completer,
        complete_while_typing=True,
        lexer=PygmentsLexer(PythonLexer),
    )

    kb = KeyBindings()
    saved = {"status": False}

    @kb.add("c-s")
    def save_text(event):
        with open(f"Storage/{filename}", "w", encoding="utf-8", errors="replace") as f:
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
    
    from prompt_toolkit.styles import Style, merge_styles
    from prompt_toolkit.styles.pygments import style_from_pygments_cls

    final_style = merge_styles([
        app_style,
        style_from_pygments_cls(SyntaxHighlighter)
    ])

    app = Application(
        layout=Layout(root_container),
        key_bindings=kb,
        full_screen=True,
        mouse_support=True,
        style=final_style,
        color_depth=None
)

    text = app.run()

    if saved["status"]:
        print(f"{Fore.CYAN} İ {filename} is saved")
    else:
        print(f"{Fore.YELLOW} X {filename} was not saved")

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
        with open(f"Storage/{filename}", "w", encoding="utf-8", errors="replace") as f:
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
        print(f"{Fore.CYAN} İ {filename} is saved")
    else:
        print(f"{Fore.YELLOW} X {filename} was not saved")

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
        with open(f"Storage/{filename}", "w", encoding="utf-8", errors="replace") as f:
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
        print(f"{Fore.CYAN} İ {filename} is saved")
    else:
        print(f"{Fore.YELLOW} X {filename} was not saved")

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
        with open(f"Storage/{filename}", "w", encoding="utf-8", errors="replace") as f:
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

        current_indent = re.match(r"\s*", line).group(0)

        if line.strip().endswith(("{", "[", "(")):
            buffer.newline(copy_margin=False)
            buffer.insert_text(current_indent + " " * 4)

        elif line.strip().startswith(("}", "]", ")")):
            buffer.newline(copy_margin=False)
            buffer.insert_text(current_indent)
        else:

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
        print(f"{Fore.CYAN} İ{filename} is saved.")
    else:
        print(f"{Fore.YELLOW} X {filename} was not saved.")

    return text