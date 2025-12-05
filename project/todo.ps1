#!/usr/bin/env pwsh
# ToDo CLI - PowerShell Wrapper
# Usage: todo add "Task title"
#        todo list
#        todo update 1 "New title"
#        todo delete 1
#        todo complete 1

param(
    [Parameter(ValueFromRemainingArguments=$true)]
    [string[]]$Arguments
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$pythonScript = Join-Path $scriptDir "src\todo.py"

# Call Python script with all arguments
python $pythonScript @Arguments
