---
description: "Task list for Todo CLI Intermediate Level Upgrade"
---

# Tasks: Todo CLI - Intermediate Level Upgrade

**Input**: Design documents from `/specs/001-todo-cli-upgrade/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

**Tests**: Unit tests are explicitly requested in the feature specification.

**Organization**: Tasks are grouped by logical components and user stories to enable independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

---

## Phase 1: Project Structure & Task Model (Foundational) 🎯 MVP Preparation

**Purpose**: Establish the core project structure and define the Task data model. This phase is foundational for all other features.

- [ ] T000 Create the project's root `src/` directory.
- [ ] T001 Create `src/models/`, `src/storage/`, `src/services/`, `src/cli/` directories.
- [ ] T002 Implement `Task` dataclass in `src/models/task.py` with `id`, `title`, `status`, `created_at`.
- [ ] T003 Add validation to `Task` dataclass for `title` (required, non-empty) and `status` (enum: `pending`, `completed`).

---

## Phase 2: Implement Persistent Storage (US1) 🎯 MVP

**Purpose**: Replace in-memory list with JSON file-based persistence.

**Goal**: Tasks must persist between program runs.

- [ ] T004 Implement `JsonStorage` class in `src/storage/json_storage.py` with `load_tasks()` and `save_tasks(tasks)` methods.
- [ ] T005 Integrate `JsonStorage` into the application's main flow to load tasks on startup and save on exit/changes.

---

## Phase 3: Enhance CLI Commands (US2)

**Purpose**: Add new command functionalities.

- [ ] T006 Implement `search <keyword>` command in `src/cli/commands.py` (case-insensitive).
- [ ] T007 Implement `filter <status>` command in `src/cli/commands.py` (`completed` / `pending`).
- [ ] T008 Implement `clear` command in `src/cli/commands.py` to delete all completed tasks.
- [ ] T009 Improve error handling and input validation across all CLI commands.

---

## Phase 4: Improve CLI User Experience (US3)

**Purpose**: Enhance the user interface and readability.

- [ ] T010 Add a detailed help menu with examples for all commands in `src/cli/cli.py`.
- [ ] T011 Implement optional colored output for better readability (e.g., using `colorama`) in `src/cli/display.py`.
- [ ] T012 Add table-style formatting for displaying tasks (ID, Title, Status, Created At) using `tabulate` in `src/cli/display.py`.

---

## Phase 5: Add Unit Tests

**Purpose**: Ensure core functionalities are robust and reliable.

- [ ] T013 Create unit tests for `Task` dataclass validation in `tests/unit/test_task.py`.
- [ ] T014 Create unit tests for `JsonStorage` (load/save operations) in `tests/unit/test_storage.py`.
- [ ] T015 Create unit tests for `search` functionality in `tests/unit/test_cli_commands.py`.
- [ ] T016 Create unit tests for `filter` functionality in `tests/unit/test_cli_commands.py`.

---

## Phase 6: Deliver Final Output

**Purpose**: Final review and packaging.

- [ ] T017 Consolidate and review all code in the `src/` directory.
- [ ] T018 Provide clear instructions on how to run the CLI application.
- [ ] T019 Ensure the complete codebase meets production-grade quality.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Project Structure & Task Model)**: No dependencies - can start immediately.
- **Phase 2 (Persistent Storage)**: Depends on Phase 1 completion.
- **Phase 3 (CLI Command Enhancements)**: Depends on Phase 1 and Phase 2 completion.
- **Phase 4 (CLI User Experience)**: Depends on Phase 1, Phase 2, and Phase 3 completion.
- **Phase 5 (Unit Tests)**: Can be integrated throughout development, but full execution depends on respective feature completion.
- **Phase 6 (Final Output)**: Depends on completion of all previous phases.

### Within Each Phase

- Tasks within each phase should generally be completed in the order listed, respecting dependencies.
- Unit tests (Phase 5) should be written *before* or *concurrently with* the implementation they validate.

### Parallel Opportunities

- Tasks within Phase 1 that involve creating separate files (`models`, `storage`, `services`, `cli` directories) can be done in parallel if working with a team.
- Writing unit tests for different components can be done in parallel once the component specifications are clear.
