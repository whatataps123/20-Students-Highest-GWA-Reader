# Joshua Lemuel Z. Centina BS CPE 1-4
# 20 Students Highest GWA

# Write a Python program that read a file containing the name of 20 students together with their GWA. 
# The program will outputs the name of the student who got the highest GWA (including the GWA).

def student():
# open studentgwa.txt (read)
    with open("studentgwa.txt", "r") as input_gwa:
        student_data = {}
        # read the file line by line
        for line in input_gwa:
            name, gwa = line.strip().split(",")
            gwa = float(gwa)
            student_data[name] = gwa
            # find the min gwa(lesser is better) of the student
            low_gwa_student = min(student_data, key = student_data.get)
            low_gwa = student_data[low_gwa_student]
        # print name of student and gwa
        print("The student who got the highest GWA:", "\033[1m" + low_gwa_student + "\033[0m", "Their GWA:", "\033[1m" + str(low_gwa) + "\033[0m")

student()