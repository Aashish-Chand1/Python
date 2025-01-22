#Accept marks of three subjects. Print total and average along with whether a candidate has passed or fail. If student secures <= 39 marks in any subject, consider him as fail. Also assigned a subject wise grade based on the following table
s1 = float(input("Enter the marks of 1st subject: "))
s2 = float(input("Enter the marks of 2nd subject: "))
s3 = float(input("Enter the marks of 3rd subject: "))


def get_grade(marks):
    if marks <= 39:
        return "F"
    elif 40 <= marks <= 44:
        return "P"
    elif 45 <= marks <= 49:
        return "C"
    elif 50 <= marks <= 54:
        return "B"
    elif 55 <= marks <= 59:
        return "B+"
    elif 60 <= marks <= 69:
        return "A"
    elif 70 <= marks <= 79:
        return "A+"
    elif 80 <= marks <= 100:
        return "O"
    else:
        return "Invalid marks"


def calculate_results(s1, s2, s3):
    
    if s1 <= 39 or s2 <= 39 or s3 <= 39:
        print("Result: Fail")
    else:
        total = s1 + s2 + s3
        average = total / 3
        print(f"Result: Pass")
        print(f"Total Marks: {total}")
        print(f"Average Marks: {average:.2f}")
    
    
    print("Subject-wise Grades:")
    print(f"1st Subject Grade: {get_grade(s1)}")
    print(f"2nd Subject Grade: {get_grade(s2)}")
    print(f"3rd Subject Grade: {get_grade(s3)}")


calculate_results(s1, s2, s3)
