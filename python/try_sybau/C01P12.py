filename = input("Enter file name: ")

parts = filename.split(".")

if len(parts) > 1:
    print("File extension:", parts[-1])
else:
    print("No extension found")
