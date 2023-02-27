def main():
    path="menu.txt"
    file=open(path,mode='r')
    content=file.readlines()
    for element in content:
        print(f"{element}",end="")
    file.close()
    base,sauce=input("\n").split(" ")
    print(f"Pizza base is {base} and your favorite sauce is {sauce}")
    return base,sauce
if __name__ == "__main__":
    choice = main()
    print(f"{choice}")