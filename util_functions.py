import os
from contextlib import contextmanager
from enum import Enum
from pathlib import Path
from typing import TextIO

DEFAULT_FILE = "todos.txt"


class Options(Enum):
    add = "add <TODO task>",
    edit = "edit <TODO number>",
    show = "show | display",
    complete = "complete <TODO number>",
    exit = "exit",


options_string = ', '.join([f"'{x.value[0]}'" for x in Options])
user_prompt = f"Type {options_string}:\n"


def print_todos(todos: list[str]) -> None:
    """
    Prints the TODOs
    :param todos:
    :return:
    """
    if not todos:
        return None
    formatted_todos = "\n".join([f"[{index}] {t}" for index, t in enumerate(todos, start=1)])
    print("⎯" * 30)
    print(formatted_todos)
    print("⎯" * 30)


def check_todos_length(todos: list[str]) -> bool:
    if len(todos) < 1:
        return False
    return True


def check_todo_number(todos: list[str], todo_id: int) -> bool:
    if 1 < todo_id > len(todos):
        return False
    return True


@contextmanager
def open_todo_file(mode="r", filename=DEFAULT_FILE) -> TextIO:
    if not os.path.exists(filename):
        Path(filename).touch()

    with open(filename, mode) as file:
        yield file


def read_todos() -> list[str]:
    with open_todo_file(mode="r", filename=DEFAULT_FILE) as file:
        todos = [line.strip("\n") for line in file.readlines()]
    return todos


def save_todos(todos: list[str], filename=DEFAULT_FILE) -> None:
    with open_todo_file(filename=filename, mode="w") as file:
        file.writelines("\n".join(todos))


def get_command(input_str: str) -> tuple[str, str | None] | None:
    result = [command for command in
              [Options.add.name,
               Options.edit.name,
               Options.show.name,
               "DISPLAY",
               Options.complete.name,
               Options.exit.name]
              if input_str.upper().startswith(command.upper())]
    if not len(result):
        return None
    command = result[0]
    try:
        command_str_len = len(command)
        offset = command_str_len + 1
        return command, input_str[offset:]
    except TypeError:
        return command, None
