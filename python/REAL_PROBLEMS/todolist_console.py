#incomplete [on-going project]
#-----------
#TO DO LIST
#-----------
def task_adder():
    print("\n WELCOME TO TASK ADDER")
    try:
     no_of_task=int(input("\nenter the number of task you want add: "))
     if no_of_task <=0:
         print("if you dont wanna add task then why are you here: ")
         option()
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
     at_end()

#this left
def task_remover():
 print("\n WELCOME TO TASK REMOVER")
 with open("tasks.txt","r") as f:
    for line in f:
       print(line.strip())
       
       
       
       
       
def task_viewer():
  print("\n WELCOME TO TASK VIEWER:")
  print("\n:: These are the task you have to do ::")
  with open("tasks.txt","r") as f:
    i=0
    for line in f:
          if line.strip()!=None:
           i+=1
           print(f"{i} > {line.strip()}")
       
       
       
       
def exit_message():
    print("""
          << 😊 THANK YOU FOR USING MY PROGRAM 😊 >>
          \n
                    << HAVE A NICE DAY >>
          """)
    
    
    
    
def option():
   exiting=input("do you wanna exit (y/n): ")
   if exiting=="y":
    exit_message()
   elif exiting=="n":
    main()
   else: 
     print("enter the valid reason: ")
     option()
     
def at_end():
    again=input("do you want to do something else or exit (y/n) ?")
    if again=="n":
     exit_message()
    elif again=="y":
     main()  
    else:
     exit_message()
    






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