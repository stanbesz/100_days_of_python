#FileNotFound
try:
    file = open("a_file.txt")
    a_dict = {"key":"fake"}
    print(a_dict["key"])
except FileNotFoundError:
    file = open("a_file.txt","w")
    print("There was an error")
except KeyError as error_message:
    print(f"Mmmm nonono Fake! Aka key doesn't exist. Error {error_message}")
else:
    content=file.read()
    print("Content:",content)
finally:
    file.close()
    print("File was closed")
    raise TypeError("Random error at the end")