@echo off
REM ToDo CLI - Windows Batch Wrapper
REM Usage: todo add "Task title"
REM        todo list
REM        todo update 1 "New title"
REM        todo delete 1
REM        todo complete 1

setlocal enabledelayedexpansion

REM Get the directory where this script is located
set "SCRIPT_DIR=%~dp0"

REM Call the Python CLI with all arguments passed through
python "%SCRIPT_DIR%src\todo.py" %*

endlocal
