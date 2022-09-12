def main():
    print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
    print("Welcome to the email slicer \n")

    email_input = input("Input your email address: ")
    (username, domain) = email_input.split("@")

    print("Username: ", username)
    print("Domain: ", domain)
    print('\n')


while True:
    main()
