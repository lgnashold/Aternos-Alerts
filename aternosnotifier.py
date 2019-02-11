#!/usr/bin/python3
import aternos_scraper
import groupme
import sys

FILENAME = "status.txt"


def main(bot_id):
    old_status = ""
    with open("status.txt") as f:
        old_status = f.readline()
    new_status = aternos_scraper.get_status().lower()

    if new_status != old_status:
        msg = "The server is " + new_status + "."
        groupme.send_message(msg, bot_id)
    with open("status.txt", "w") as f:
        f.write(new_status)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: aternosnotifier.py <bot_id>")
    else:
        main(sys.argv[1])
