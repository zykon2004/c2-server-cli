"""
Main Menu:
    Server Status
    Client
        Status
        Kill
    Command
        Send Command
            Choose: Client, All
            Choose: Payload
            Input: Args (separated by space)
        View Status
"""
# import subprocess
# from pathlib import Path
# from subprocess import PIPE, Popen
# from typing import Any, Iterable

# gum = str((Path(__file__).parents[1] / "bin" / "gum").absolute())
# p1 = Popen(["ip", "a"], stdout=PIPE)
# p2 = Popen(["sed", "/^$/d"], stdin=p1.stdout, stdout=PIPE)
# p3 = Popen(["awk", "NR > 1 { print $2 }"], stdin=p2.stdout, stdout=PIPE)
# p4 = Popen(f"{gum} filter".split(), stdin=p3.stdout, stdout=PIPE, text=True)
# stdout, _ = p4.communicate()
# print(stdout)


# def run_command(args: Iterable[str]) -> Any:
#     result = subprocess.run([*args], stdout=subprocess.PIPE, text=True)
#     return result.stdout.split()


# # run_command(f'{gum} spin --spinner dot --title "Buying Bubble Gum..." -- sleep 5'.split())
# print("What's your favorite language?")

from server_status import server_status

server_status()
