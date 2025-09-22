#incomplete [on-hoing project]
#-----------
#TO DO LIST
#-----------
def task_adder():
    print("\n WELCOME TO TASK ADDER")
    try:
     no_of_task=int(input("\nenter the number of task you want add: "))
     if no_of_task <=0:
         print("if you dont wanna add task then why are you here: ")
         task_adder()
    except ValueError:
     print("enter the vaklid data")
     task_adder()
    else:
        for i in range(no_of_task):
         task=input(f"\n Enter the task you want to as task {i}: ")
         with open("tasks.txt","a") as f:
          f.write("\n")
          f.write(task)
    if no_of_task == 1:
     print(f" {no_of_task} task has been added sucessfully ")
     cont=int(input("do you wanna continue:"))
    else:
     print(f" {no_of_task} tasks has been added sucessfully ")

def task_remover():
    print("hello")
def task_viewer():
    print("hello")
    
def exit_message():
    print("bye")






def choice_trapper_and_analyzer(choice):
 match choice:
     case 1:
         task_adder()
     case 2:
         task_remover()
     case 3:
         task_viewer()
     case 4:
         exit_message()
     case default:
         print("::check your eyes and run the program again::")
         



def main():
 try:
  print("this is a TO-DO list")
  print("Waht do you want to do ?")
  print("1> Add the task: ")
  print("2> Remove the task:  ")
  print("3> View tasks: ")
  print("4> Exit: ")
  choice=int(input("Enter ur choice"))
  return choice_trapper_and_analyzer(choice)
 except ValueError:
  print("enter the valid choice")
  


main()