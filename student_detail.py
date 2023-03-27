import csv
file = open("student_information.csv","w+",newline="")
write_file = csv.writer(file)
header = ["Name","Department","Roll","Session"]
write_file.writerow(header)
student_data = []
while True:
    try:
        student = int(input("How many students data do you want to entry: "))
        break
    except ValueError:
        print("Please enter correct number")
        continue
for i in range(student):
    print("")
    print(f"Record {i+1}")
    name = input("Student name: ")
    deparment = input("Department: ")
    session = input("Session : ")
    while True:
        try:
            roll = int(input("Roll: "))
            break
        except:
            print("Enter correct roll")
            continue
    record = [name.capitalize(),deparment.capitalize(),roll,session]
    student_data.append(record)

write_file.writerows(student_data)
file.close()

new_file = open("student_information.csv","r")
read_file = csv.reader(new_file)
print("______________________________________________All Data of Students____________________________________________________")
print(header)
for j in student_data:
    print(j)
