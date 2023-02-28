import csv
import datetime
from decorator import *
import pizza
def main():
    # Bir tane sos seçmek zorunzda değil birden fazla sos seçebilir 
    # tekrar bakıcam
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
    main()
