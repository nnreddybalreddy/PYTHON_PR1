import os 


def main():
    req_path=input("Enter the dir name:::")
    try:
        os.chdir(req_path)
        print("current workdir:::",os.getcwd())
    except FileNotFoundError:
        print("File not found error:::")
    except NotADirectoryError:
        print("Not a dir error:::::")
    except PermissionError:
        print("Permission error....")
    except Exception as e:
        print(e)    
    return None


if __name__=="__main__":
    main()