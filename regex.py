import re
    from operator import truediv

    #string = "Lach- und Sachgeschichten"
    #pattern = r"ach"

    #list_found = re.findall(pattern, string)

    #print(list_found)

    #split_text = string.split("ch")

    #print(split_text)


def simple_password_check(password)
    pattern = r"\w{8,25}"

    if re.fullmatch(pattern, password):
        return True
    else:
        return False

def test_password():
    liste_passwords = [
        "admin123456",
        "password0815",
        "12345",
        "0815",
        "'*+#.,_",
        " ad",
    ]

    for pwd in liste_password:
        print(f"{pwd} ist {simple_password_check(pwd)}")


