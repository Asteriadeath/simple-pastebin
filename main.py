import os
import uuid

def create_paste(content):
    paste_id = str(uuid.uuid4())
    with open(f"pastes/{paste_id}.txt", "w") as f:
        f.write(content)
    return paste_id

def get_paste(paste_id):
    try:
        with open(f"pastes/{paste_id}.txt", "r") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return None

if __name__ == "__main__":
    if not os.path.exists("pastes"):
        os.makedirs("pastes")
    while True:
        action = input("What do you want to do? (create/get/exit): ")
        if action == "create":
            content = input("Enter your content: ")
            paste_id = create_paste(content)
            print(f"Paste created: {paste_id}")
        elif action == "get":
            paste_id = input("Enter paste ID: ")
            content = get_paste(paste_id)
            if content:
                print(content)
            else:
                print("Paste not found.")
        elif action == "exit":
            break
        else:
            print("Invalid action.")