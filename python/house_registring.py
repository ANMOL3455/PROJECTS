#-------------------------------------
#this program is designed to register 
#house andsearch for if registerd or not
#hope you like it
#-------------------------------------
def file_opener(opener,mode):
 with open(opener,mode)as f:
    try:
     house_number=int(input("enter the house number: "))
    except ValueError:
        print("please enter the valid house number")
        op=opener
        md=mode
        file_opener(op,md)
    your_name=input("enter your name: ")
    if mode=="a":
     f.write("\n")
     f.write(str(house_number))
     f.write(your_name)
     print("registered sucessfully")
    else:
       data=house_number+your_name
       for line in f:
        if line== data:
            res=1
        else:
            res=0
       if res==1:
           print("your data was found")
       else:
           print("you need to register")
           chm=input("wanna register (y,n): ")
           if chm.isdigit():
               print("please enter the valid choice")
           else:
            if chm=="y":
               choice_validation(1)
            elif chm=="n":
               print(":: thanks for using our program ::")
def choice_validation(cho):
    match cho:
        case 1:
            print(":: HERE WE WEILL REGGiSTER UR HOUSE ::")
            file_opener(opener="register.txt",mode="a")     
        case 2:
            print(":: HERE WE WEILL SEARCH  FOR UR HOUSE ::")
            file_opener(opener="register.txt",mode="r")   
                                  
def main():
    print("1: register house \n 2: search for validation")
    try:
     cho=int(input("enter the choice:"))
     return choice_validation(cho)
    except ValueError:
        print(":: PLEASE ENTER THE VALID CHOICE ::")
        main() 
main()
