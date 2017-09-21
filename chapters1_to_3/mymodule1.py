myage = 24
year = 2016
print("My name is", __name__)

if __name__ == "__main__":
    print("This won't run if I'm imported.")
else:
    print("Another program is using this file")