import sys
#バリデーションしてないけど
def reverse(contents, output):
    reversed_contents = list(reversed(contents))
    output.write(''.join(reversed_contents))

def copy(contents, output):
    output.write(contents)

def duplicate(contents,count,input):
  input.write(contents * count)

def replace(contents,input):
  input.truncate(0)
  input.write(contents.replace("needle", "newstring"))

def main():
    command = sys.argv[1]
    inputpath = sys.argv[2]

    with open(inputpath, "r+") as input:
        contents = input.read()

        if command == 'reverse':
            outputpath = sys.argv[3]
            with open(outputpath, "w") as output:
                reverse(contents, output)

        elif command == "copy":
            outputpath = sys.argv[3]
            with open(outputpath, "w") as output:
                copy(contents,output)
        
        elif command == "duplicate":
            count = int(sys.argv[3])
            duplicate(contents, count,input)
        
        elif command == "replace":
            replace(contents,input)
    sys.exit(0)

if __name__ == "__main__":
    main()