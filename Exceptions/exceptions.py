try:
    f = open("Exceptions\\corrupt_file.txt")

    # if f.name == "Exceptions\\corrupt_file.txt":
    #     raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing finally")
