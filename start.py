import os
import re
from PyInquirer import prompt

YEAR = 2024


def get_concerts():
    concerts = []
    for file in os.listdir(f"pages/{YEAR}"):
        if re.match(r"\d{4}-\d{2}-\d{2}_\d+", file):
            concerts.append(file)
    return concerts


def choose_concert(concerts):
    questions = [
        {
            "type": "list",
            "name": "concert",
            "message": "Select a concert:",
            "choices": concerts,
        }
    ]
    answers = prompt(questions)
    return answers


def update_file(concert_file):
    update_line = False

    with open(f"pages/{YEAR}/{concert_file}", "r") as file:
        content = file.read()

        for line in content.split("\n"):
            if "# Update" in line:
                update_line = True
                continue

            if update_line:
                content = content.replace(line, f"src: ./pages/{YEAR}/{concert_file}")

    with open(f"pages/{YEAR}/{concert_file}", "w") as file:
        file.write(content)


def main():

    print("Updating the repository...")
    update_process = os.system("git pull")
    if update_process != 0:
        print("Error updating the repository.")
        if prompt(
            [
                {
                    "type": "confirm",
                    "name": "reset",
                    "message": "Do you want to reset the repository and continue?",
                }
            ]
        )["reset"]:
            reset_process = os.system("git reset --hard origin/main")
            update_again_process = os.system("git pull")
            if reset_process != 0 or update_again_process != 0:
                print("Fatal Error resetting the repository.")
                return
        else:
            print("Exiting...")
            return

    print("\nRepository updated.\n\n")

    concert = choose_concert(get_concerts())
    concert = concert.get("concert")

    if not concert:
        print("No concert selected. Exiting...")
        return

    print(f"Updating concert {concert}...")
    update_file(concert)
    print("Concert updated.")

    print("Pushing changes to the repository...")
    push_process = os.system("git add .")
    push_process += os.system("git commit -m 'Automatic concert update'")
    push_process += os.system("git push")

    if push_process != 0:
        print("Error pushing changes to the repository.")
        return

    print("Changes pushed to the repository.")

    print("Starting the server...")
    print("Press Ctrl+C to stop the server.")

    os.system("npm run dev")


if __name__ == "__main__":
    main()
