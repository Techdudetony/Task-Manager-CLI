# 🧠 Task Manager CLI 

A command-line task manager built with Python.
Designed for a clean, interactive experience with persistent task storage and smart features like sorting, editing, tagging, and more.

---

## Features Completed

🧩 Interactive CLI commands using `argparse`
📁 Modular design using `src/` package
💾 Persistent task storage via JSON
🧱 Task model with:  
- Title
- Priority (`Critical`, `High`, `Medium`, `Low`)
- Due Date (YYYY-MM-DD)
- Completion Status
- Optional Tag (`--tag`)

✍️ Interactive `add` and `edit` commands (no flags needed)
🎨 Terminal color-coded output using `colorama`
📅 Overdue task highlighting in red
🔁 Priority-based and due date sorting
🧪 Unit tests using `pytest`
🔐 `.gitignore`, `requirements.txt`, and virtual environment best practices
💻 WSL + VS Code optimized workflow

---

## Installation

```bash
# Clone the repository
git clone https://github.com/Techdudetony/Task-Manager-CLI.git
cd Task-Manager-CLI

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

--- 

# Run Tests
```bash
pytest
# or with coverage:
PYTHONPATH=src pytest --cov=src
```

# How to Use
## ➕ Add a Task
```bash
python3 -m src.main add
```
You'll be prompted to enter:  
- Title
- Priority
- Due Date
- Optional Tag  

## ✏️ Edit a Task
```bash
python3 -m src.main edit <task_id>
```
This will interactively update any field (leave blank to skip)

## 📋 List Tasks
```bash
python3 -m src.main list
```
Here you can show a list of Tasks. Use `--sort priority` or `--sort due_date` to sort the list.

## ✅ Complete a Task
```bash
python3 -m src.main complete <task_id>
```
This is how you change a tasks completion status.

## ❌ Delete a Task
```bash
python3 -m src.main delete <task_id>
```
This is how you can delete a task from your task list. 

# 📃 Example Output
```bash
[ ] 1: Finish this CLI app (Priority: High, Due: 2025-05-01) [Tag: project]
[✔] 2: Turn in assignment (Priority: Critical, Due: 2024-04-10) [Tag: school]
```
In this example:  
- 🟨 `Priority: High` would be highlighted **Yellow** for High Priority.
- 🟥 `Priority: Critical` would be highlighted **Red** for Critical Priority.
- 📅 `2024-04-10` would be highlighted **Red** since this date has passed (overdue).