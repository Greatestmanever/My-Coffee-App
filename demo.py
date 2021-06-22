def age_in_seconds():
    user_age = input("Enter your age: ")
    age_seconds = int(user_age) * 365 * 24 * 60 *60
    print("")
    print("You have lived for {} seconds.".format(age_seconds))