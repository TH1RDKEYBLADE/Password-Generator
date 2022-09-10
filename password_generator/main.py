# Made by TH1RDKEYBLADE
# Main.py

# Files
from password import Password

# Modules
from time import sleep


def main():
    # Main Password Loop
    while True:

        Password.get_char_amount(Password)
        Password.no_character_detection(Password)

        Password.get_file_name(Password)

        Password.get_amount_lower(Password)
        Password.get_amount_upper(Password)
        Password.get_amount_special(Password)
        Password.get_amount_numbers(Password)

        Password.get_random_password(Password)
        Password.write_password_file(Password)

        sleep(3)

if __name__ == '__main__':
    main()
