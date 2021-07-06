import sys

print("测试开始")
def main(arg):
    if arg:
        print("The arg detail:",arg)
    else:
        print("This")

if __name__ == "__main__":
   main(sys.argv[1:])