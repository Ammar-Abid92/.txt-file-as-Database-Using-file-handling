
def join():

    file = open('textfile.txt', 'w')
    for i in range(1, 3):
        print('entering a new record')

        file.write(f"\n emp no. : {input('''Number:  ''')},")
        file.write(f" Name: {input('''Name:  ''')},")
        file.write(f"  Gender : {input('''Gender: ''')}, ")
        file.write(f" Gross Salary is : {input('''Gross Salary:  ''')},")
        file.write(f" Designation is: {input('''Designation:  ''')}")
    file.close()


def salary_increase():

    a_file = open("textfile.txt", "r")
    lines = a_file.readlines()
    b = len(lines)
    emp = int(input(f'you have {b - 1} employees in total. Enter number to update: '))
    record = lines[emp].split(",")
    up = input(record)
    a_file.close()
    choice1 = input("Do You want to Change the Gross Salary of any user detail? Yes/No: ")
    if choice1 == "Yes" or choice1 == "yes":
        a_file = open("textfile.txt", "r")
        record[3] = f" New Gross Salary: {input('''New Salary: ''')}"
        update = input(record)
        lines[emp] = update
        new_lines = record
        a_file = open("textfile.txt", "a+")
        new = a_file.readlines()
        if new != new_lines:
            # for line in new_lines:
            a_file.write(f"\n{new_lines}")
            a_file.close()
        else:
            pass


def delete():

    choice = input("Do You want to Delete any user detail? Yes/No: ")
    if choice == "Yes" or choice == "yes":
        del_line = int(input('enter account line to delete: '))
        a_file = open("textfile.txt", "r")
        lines = a_file.readlines()
        a_file.close()
        lines.remove(lines[del_line])

        new_file = open("textfile.txt", "w")
        for line in lines:
            new_file.write(line)
        new_file.close()
        print(f'employee record {del_line} deleted')
    else:
        print("Thank you :)")


join()
salary_increase()
delete()