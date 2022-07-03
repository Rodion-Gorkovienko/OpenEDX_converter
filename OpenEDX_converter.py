import sourсe_file_parsing
import drop_OLX
import os

while True:
    test_path = input('Enter the full name of the source file (with extension and path): ')

    if os.path.exists(test_path):
        if os.path.isfile(test_path):
            if test_path[-5 : ] == ".docx":
                lib, problems = sourсe_file_parsing.parse_file(test_path)
                #C:\Users\User\Desktop\Сем 6\Практика\Исходники\Auto-Graded Practice Quiz.docx
                #C:\Users\User\Desktop\Сем 6\Практика\test\ВсеТипы.docx
                break
            else:
                print("This is not docx file.")
        else:
            print("This is not file.")
    else:
        print("Path incorrect.")

while lib != "":
    directory_path = input('Enter the path to the directory where the resulting files will be placed: ')

    if os.path.exists(directory_path):
        if os.path.isdir(directory_path):
            drop_OLX.drop_files(directory_path, lib, problems)
            #C:\Users\User\Desktop\Сем 6\Практика\test
            break
        else:
            print("This is not directory.")
    else:
        print("Path incorrect.")

