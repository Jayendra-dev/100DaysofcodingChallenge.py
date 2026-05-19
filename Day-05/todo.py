# 1. TASKS STORE KARNE KE LIYE KHALI LIST BANAYI
tasks = []  # Ye ek dabba hai jisme hum saare tasks string ke form me rakhenge

# 2. INFINITE LOOP - PROGRAM BAND NA HO JAB TAK USER BOLE
while True:  # Jab tak 'break' na mile, ye chalta rahega
     
    # 3. MENU DIKHANA USER KO
    print("\n1. Add Task  2. View Tasks  3. Exit")  # \n se ek line ka gap aata hai
     
    # 4. USER SE INPUT LENA
    choice = input("Choose: ")  # input() hamesha string deta hai, "1" ya "2" type ka
     
    # 5. AGAR USER NE "1" DABAYA = NAYA TASK ADD KARNA
    if choice == "1":  # == matlab check kar raha hai barabar hai ya nahi
        task = input("Enter task: ")  # User se task ka naam poocha
        tasks.append(task)  # .append() se list ke end me naya task add ho gaya
        print("Task added!")  # Confirmation diya
     
    # 6. AGAR USER NE "2" DABAYA = SAARE TASKS DIKHANA  
    elif choice == "2":  # elif = else if, matlab doosra option check karo
        # enumerate(tasks, 1) ka matlab: list ke har item ko 1,2,3... number do
        for i, task in enumerate(tasks, 1):  
            print(f"{i}. {task}")  # f-string: i ki value aur task print karo. Example: "1. Git Seekho"
     
    # 7. AGAR USER NE "3" DABAYA = PROGRAM BAND KARO
    elif choice == "3":  
        break  # while loop ko tod do, program yahi khatam ho jayega
     
    # 8. AGAR USER GALAT NUMBER DAALE
    else:  # Upar wale 1,2,3 me se kuch nahi hai to ye chalega
        print("Invalid choice! 1, 2 ya 3 dabao")