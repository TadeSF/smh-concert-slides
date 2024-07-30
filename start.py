#!./.venv/bin/activate

import os
import re
from PyInquirer import prompt
from datetime import datetime

YEAR = 2024
MARKER = "# Hier Konzertdatei einfügen"
MAIN_FILE = "slides.md"
DATE_FORMAT = "%Y-%m-%d_%H"


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
            "choices": [{
                "value": concert,
                "name": f"Concert on {datetime.strptime(concert.replace(".md", ""), DATE_FORMAT).strftime("%A, %Y-%m-%d %H:%M")}"} for concert in concerts],
        }
    ]
    answers = prompt(questions)
    return answers


def update_file(concert):
    modify_next = False

    with open(MAIN_FILE, "r") as file:
        content = file.read()

        for line in content.split("\n"):
            if MARKER in line:
                modify_next = True
                continue
            if modify_next:
                content = content.replace(line, f"src: ./pages/{YEAR}/{concert}")
                break

    with open(MAIN_FILE, "w") as file:
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

    concerts = sorted(get_concerts(), reverse=True)
    concert = choose_concert(concerts)
    concert = concert.get("concert")

    if not concert:
        print("No concert selected. Exiting...")
        return

    print(f"Updating concert {concert}...")
    update_file(concert)
    print("Concert updated.")

    print("Starting the server...")
    print("Press Ctrl+C to stop the server.")

    os.system("npm run dev")


if __name__ == "__main__":
    main()
