# Django Frontend Application

PySide6-based desktop application frontend for the Django backend.

## Features
- Connection monitoring to Django backend
- Real-time status updates
- Modern Qt interface with qt-material styling

## Development
```bash
# Install dependencies
uv sync

# Run application
uv run frontend
```

## UI Development
Generated UI files (`src/ui/*.py`) are ignored in `.gitignore`. To modify the UI:

1. Edit `ui/MainWindows.ui` using Qt Designer
2. Regenerate Python code:
   ```bash
   # Install UI tools (first time)
   uv add pyside6-tools

   # Generate UI Python files
   pyside6-uic ui/MainWindows.ui -o src/ui/main_windows.py
   ```

    Or use the task runner:
    ```bash
    go-task frontend:ui-generate
    ```

3. To clean generated UI files:
    ```bash
    go-task frontend:ui-clean
    ```

4. The generated files will be ignored by Git, so you need to regenerate them after cloning the repository.
