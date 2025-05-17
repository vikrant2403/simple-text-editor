# simple-text-editor
print("Hello, welcome to the simple text editor.\nCreated by Mr. Vikrant Sheokand")
ask_user = input("enter the filename to open or create: ")
try:
    with open(f"{ask_user}.txt","r") as f:
        print(f"file found. opening\n{ask_user}.txt")
except FileNotFoundError:
    print("file not found. opening a new file for you.")

with open(f"{ask_user}.txt","w") as f:
    print("enter your text(type SAVE on a new line to save and exit): ")
    while True:
        line = input()
        if line.strip().upper()== "SAVE":
            print("file saved successfully.\n------------")
            break




