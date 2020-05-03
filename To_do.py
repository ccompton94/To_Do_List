#Simple To Do List
def print_todos(todos): #Print to do list
    if len(todos) == 0:
        print("You have nothing to do.")
    else:
        index = 0
        for todo in todos:
            print(f"{index}: {todo}")
            index += 1
    return

def add_todo(todos, new): #Add a to do to the list
    todos.append(new)
    return todos

def delete_todo(todos, index): #Delete a to do from the list
    try:
        del todos[index]
        deleted = 0
    except IndexError:
        print("That todo does not exist.")
        deleted = 1
    return todos,deleted

def print_menu():
    message = """
    Todo App
==================
0. Quit App
1. Display Todo List
2. Add a New Todo to the List
3. Check Off a Todo from the List 
==================
"""
    return print(message)

def get_choice(prompt="Choose one: "):
    while True:
        try:    
            choice = int(input(prompt))
            if choice < 0 or choice > 3:
                print('Invalid choice. Please try again.')
                print_menu()
                continue
            break
        except ValueError:
            print("Please enter a number.")
    return choice
    
def main_function():
    todo_list = []
    while True:
        print_menu()
        choice = get_choice()
        if choice == 0:
            print("Have a good day!")
            break
        elif choice == 1:
            print_todos(todo_list)
        elif choice == 2:
            new_todo = input("Enter a todo: ")
            todo_list = add_todo(todo_list, new_todo)
        elif choice == 3:            
            print_todos(todo_list)
            index_to_delete = get_choice("Choose one: ")
            todo_list,deleted = delete_todo(todo_list, index_to_delete)
            if deleted == 0:
                print('\nCongradulations on finishing something from your Todo List!')
    return

main_function()