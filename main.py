import task
import shlex

def parse_command(command_str):
    try:
        tokens = shlex.split(command_str)
    except ValueError:
        return ("invalid", None)

    if not tokens:
        return ("invalid", None)

    cmd = tokens[0].lower()
    args = tokens[1:]

    if cmd == "add":
        return ("add", " ".join(args))
    elif cmd == "update":
        if len(args) < 2:
            return ("invalid", command_str)
        return ("update", (args[0], " ".join(args[1:])))  # (task_id, new_title)
    elif cmd == "mark-in-progress":
        return ("mark-in-progress", args[0])
    elif cmd == "mark-done":
        return ("mark-done", args[0])
    elif cmd == "delete":
        return ("delete", args[0])
    elif cmd == "list":
        return ("list", None)
    elif cmd == "todo":
        return ("todo", None)
    elif cmd == "in-progress":
        return ("in-progress", None)
    elif cmd == "done":
        return ("done", None)
    elif cmd == "exit":
        return ("exit", None)
    else:
        return ("invalid", command_str)
    

all_tasks = []
todo_tasks = []
in_progress_tasks = []
done_tasks = []

def run_cli():
    while True:
        cmd = input("task-cli ")
        action, data = parse_command(cmd)
    
        if action == "add":
            taskT = task.Task(description=data)
            
            all_tasks.append(taskT)
            todo_tasks.append(taskT)
            
        elif action == "update":
            try:
                task_id, new_description = data
                task_id = int(task_id)
                exist = False
                for t in all_tasks:
                    if t.id == task_id:
                        t.set_description(new_description)
                        exist = True
                if not exist:
                    print(f"Task (id: {task_id}) not found")
            except ValueError:
                print(f"{task_id} is not a valid ID")
            
        elif action == "mark-in-progress":
            try:
                data = int(data)
                exist = False
                for t in all_tasks:
                    if t.id == data:
                        t.set_in_progress()
                        in_progress_tasks.append(t)
                        exist = True
                        break
                if not exist:
                    print(f"Task (id: {data}) not found")
            except ValueError:
                print(f"{data} is not a valid ID")
                
        elif action == "mark-done":
            try:
                data = int(data)
                exist = False
                for t in all_tasks:
                    if t.id == data:
                        t.set_done()
                        done_tasks.append(t)
                        exist = True
                        break
                if not exist:
                    print(f"Task (id: {data}) not found")
            except ValueError:
                print(f"{data} is not a valid ID")
                
        elif action == "delete":
            try:
                data = int(data)
                exist = False
                
                for t in all_tasks:
                    if t.id == data:
                        all_tasks.remove(t)
                        exist = True
                        
                        
                        # Delete the following task from one of the other lists
                        if t.status.value == "To Do":
                            todo_tasks.remove(t)
                        elif t.status.value == "In Progress":
                            in_progress_tasks.remove(t)
                        elif t.status.value == "Done":
                            done_tasks.remove(t)
                        break
                if not exist:
                    print(f"Task (id: {data}) not found")
            except ValueError:
                print(f"{data} is not a valid ID")   
                
        elif action == "list":
            for t in all_tasks:
                print(t.get_details())
        elif action == "todo":
            for t in todo_tasks:
                print(t.get_details())
        elif action == "in-progress":
            for t in in_progress_tasks:
                print(t.get_details())
        elif action == "done":
            for t in done_tasks:
                print(t.get_details())
                
        elif action == "invalid":
            print(f"Unknown command: {data}")
            
if __name__ == "__main__":
    run_cli()

    
