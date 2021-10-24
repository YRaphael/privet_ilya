import os
import random
from datetime import timedelta, date

alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [chr(i) for i in range(ord('A'), ord('Z') + 1)]
picture = "+**+**+++*+*****++++**+++**+++***+++*+**+***********\
+*++**+*+*+*****+**+*+****+***+*+****+*++***********\
++*+**+*+*+++***++++*+****+***+*+****++*+***********\
+**+*+**+*+++*++***+**+++**+++***+++*+**+***********\
****************************************************\
****************************************************\
****************************************************"


def get_digest(content):
    return hash(content)


def generate_message():
    return "".join([random.choice(alphabet) for i in range(random.randint(10, 20))])


def add_content(content):
    os.system("echo " + content + " >> file.txt")


def git_commit(digest, date):
    os.system("git commit -m \"" + str(digest) + "\" --date=\"" + str(date) + "T12:00:00+0300\"")


def git_add():
    os.system("git add file.txt")


def fill_point(delta):
    message = generate_message()
    digest = get_digest(message)
    add_content(message)
    git_add()
    git_commit(digest, date.today().replace(2017, 1, 1) + timedelta(days=delta))


if __name__ == '__main__':
    for i in range(52):
        for j in range(7):
            sym = picture[j * 52 + i]
            if sym == "+":
                fill_point(j+i*7)
