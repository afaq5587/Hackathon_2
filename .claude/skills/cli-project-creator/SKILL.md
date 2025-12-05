---
name: CLI Project Creator
description: A systematic approach to creating command-line interface (CLI) projects with well-structured sections
version: 1.0.0
---

# CLI Project Creator Skill

## When to Use This Skill

Use this skill when you need to:
- Create a new CLI project from scratch
- Structure a CLI application with clear, logical organization
- Ensure your CLI project includes well-written documentation sections
- Apply consistent quality standards across CLI project sections

## Process Steps

1. **Establish Project Foundation**
   - Create a clear project structure with appropriate directories
   - Set up the main entry point for the CLI application
   - Define command-line arguments and options

2. **Design Well-Structured Sections**
   - Write a clear opening that establishes what each section explains
   - Integrate evidence and examples naturally, not tacked on
   - Ensure logical flow from one section to the next
   - Create conclusions that connect back to the project's overall purpose

3. **Implementation Phase**
   - Implement the core CLI functionality
   - Add error handling and user feedback mechanisms
   - Create help and usage documentation

4. **Documentation and Testing**
   - Write comprehensive usage examples
   - Include tests for CLI commands
   - Document command options and parameters

## Output Format

The skill produces:
- Project directory structure with organized components
- Main CLI application file with proper argument parsing
- Well-documented command options and usage examples
- README with clear installation and usage instructions
- Test files to verify CLI functionality

## Example

### Input
Request to create a task management CLI tool called "todo-cli"

### Output
```
todo-cli/
├── README.md
├── todo_cli/
│   ├── __init__.py
│   ├── main.py
│   └── commands/
│       ├── __init__.py
│       ├── add.py
│       ├── list.py
│       └── complete.py
├── tests/
│   ├── __init__.py
│   └── test_todo_cli.py
├── setup.py
└── requirements.txt
```

The main.py file would include:
- Clear opening with what the CLI does
- Well-organized command parsing
- Integration of different functionality modules
- Proper error handling and user feedback

The README.md would follow the same principles:
- Clear introduction that establishes what the CLI tool does
- Installation instructions with supporting evidence
- Usage examples that flow logically
- Conclusion that connects back to the tool's value proposition