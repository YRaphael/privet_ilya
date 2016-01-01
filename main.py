import os
import random

alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [chr(i) for i in range(ord('A'), ord('Z') + 1)]
picture = "+**+*+++**+*****++++**+++**+++***+++*+**+***********\
+*++*+*+**+*****+**+*+****+***+*+****+*++***********\
++*+*+*+**+++**+++++*+****+***+*+****++*+***********\
+**+*+**+*+++*+****+**+++**+++***+++*+**+***********\
****************************************************\
****************************************************\
****************************************************"


def get_digest(content):
    return hash(content)


def generate_message():
    return "".join([random.choice(alphabet)] * random.randint(10, 20))


def add_content(content):
    os.system("echo " + content + " >> file.txt")


def git_commit(digest, date):
    os.system("git commit -m \"" + digest + "\" --date=\"" + date + "\"")


def git_add():
    os.system("git add file.txt")


if __name__ == '__main__':
    for i in range(52):
        for j in range(7):
            sym = picture[j * 52 + i]
            if sym == "+":
                print("*", end = "")
            else:
                print(" ", end="")
        print()
    # message = generate_message()
    # add_content(message)
    # digest = get_digest(message)
    # git_add()
    # git_commit(digest)
