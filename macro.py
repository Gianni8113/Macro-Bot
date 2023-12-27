import re
import pyautogui

# Global variables to store the current mouse position
current_x, current_y = pyautogui.position()

def perform_mouse_action(action):
    global current_x, current_y

    # Use regular expressions to extract the movement distance (if provided)
    match = re.match(r"([A-Z.]+)\((\d*)\)", action)
    if match:
        movement, distance = match.groups()
        distance = int(distance) if distance else 1

        if "MOUSE.UP" in movement:
            current_y -= distance
        elif "MOUSE.DOWN" in movement:
            current_y += distance
        elif "MOUSE.LEFT" in movement:
            current_x -= distance
        elif "MOUSE.RIGHT" in movement:
            current_x += distance

        # Ensure the new position is within the screen bounds
        current_x = max(0, min(current_x, pyautogui.size().width - 1))
        current_y = max(0, min(current_y, pyautogui.size().height - 1))

        # Move the mouse to the new position
        pyautogui.moveTo(current_x, current_y, duration=0.25)
    elif action.startswith("KEYBOARD(") and action.endswith(")"):
        key = action[len("KEYBOARD("):-1]
        pyautogui.typewrite(key)
    else:
        print(f"Error: Invalid command format - {action}. Did you mean something like 'MOUSE.DOWN(100)' or 'KEYBOARD(A)'?")

def main():
    file_path = "commands.txt"  # Change this to the actual name of your text file

    try:
        with open(file_path, "r") as file:
            for line in file:
                command = line.strip()
                perform_mouse_action(command)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
