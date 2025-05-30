Absolutely! Below is your **fully updated `README.md` file**, with:

* ✅ Correct `get_details()` output in the Example Output section
* ✅ `command_parser.py` removed from the project structure
* ✅ Everything in one copy-paste block, ready for GitHub

---

````markdown
# 📝 Task Tracker CLI

A simple, user-friendly command-line task manager written in Python. Manage your to-dos directly from the terminal — add tasks, update them, track progress, and view them in a clean, readable format.

---

## 🚀 Features

- Create tasks with a title, optional description, and due date
- Track task status: `To Do`, `In Progress`, `Completed`
- Mark tasks as completed or in progress
- Update task titles by ID
- List all tasks in a clean, formatted view
- Detect overdue tasks
- Display due dates and timestamps in 12-hour AM/PM format
- Optional task list size limit

---

## 📦 Requirements

- Python 3.7 or higher
- No external libraries required (uses only Python standard library)

---

## 🖥️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/task-tracker-cli.git
cd task-tracker-cli
````

2. Run the CLI:

```bash
python main.py
```

---

## 💡 Available Commands

Use these commands after running `main.py`:

### ➕ `add "task title"`

Creates a new task with the given title.

```bash
add "Buy groceries"
```

---

### 🛠️ `update <task_id> "new title"`

Updates the title of a task using its ID.

```bash
update 1 "Buy groceries and cook dinner"
```

---

### 🔄 `mark-in-progress <task_id>`

Marks a task as **In Progress**.

```bash
mark-in-progress 1
```

---

### ✅ `mark-done <task_id>`

Marks a task as **Completed**.

```bash
mark-done 1
```

---

### 📋 `list`

Lists all tasks with full details.

```bash
list
```

---

> 🔢 **Note:** Task IDs are automatically assigned starting from 1.

---

## 🧾 Example Output

```text
Description: Finish homework
    Status: In Progress - Created: 05/29/2025 02:15 PM - Updated: 05/29/2025 03:10 PM - Task ID: 1
```

---

## 📁 Project Structure

```
task-tracker-cli/
├── main.py             # Entry point and command loop
├── task.py             # Task class and status enum
└── README.md           # This file
```

---

## 🧠 Future Improvements

* Add support for descriptions and due dates via CLI
* Save/load tasks to a file (JSON/CSV)
* Sort/filter tasks by status or due date
* Add priority levels or tags
* Support recurring or repeating tasks

---

## 📝 License

This project is licensed under the MIT License — free to use, modify, and share.

---

## 🙋‍♂️ Author

Created with 🧠 and 🐍 by IDevelopBits
