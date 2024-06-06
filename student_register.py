# We create an input to ask user the total students registering.
students_num = int(input("How many students are registering ?:"))

# The for loop runs from 0 to the range of num_students,
# and it uses to iterate that many times.

for x in range(students_num):
    # Prompt and read student's ID.
    ID = input("Please enter your student's ID:")

    # This script uses the with statement to open the file in append mode
    # to add each student's ID to the existing content of the file.

    with open("reg_form.txt", "a") as file:
        # Write the ID in file.
        file.write('ID: ' + ID + "\n")
        # Including dotted line after each student ID.
        file.write("------------------\n")

# Close the file.
file.close()
