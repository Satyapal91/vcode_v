# ---------------------file bug-------------------------
import os

#this function is use to determine file is exists or not. And then return True or False value.
def file_exists(path):
    if os.path.exists(path):
        return True
    else:
        return False

# This function use for creating a file.
def fileMade():
# 	That is use to start and end value for file
    start = int(input("enter the start value"))
    end_of_seq = int(input("enter the end value"))
    for i in range(start, end_of_seq):
# 			file structure 
        name_of_file = f"demo{i}.txt"
# 	corent directory path variable
        path = f"C:/Users/file/PycharmProjects/{name_of_file}"
        if file_exists(path):
            continue
        else:
            f = open(name_of_file, "xt")
            f.close()


try:
    print("This programme is use for fill to storage")
    fileMade()
except ValueError:
    print("Please Enter the valid Numeric value")
    fileMade()
finally:
    print("Programme finish")


# os.remove("vi1.py")
