class GradeSchool:

    def __init__(self, school_name):

        self.first_grade_students = []
        self.second_grade_students = []
        self.third_grade_students = []
        self.fourth_grade_students = []
        self.fifth_grade_students = []
        self.sixth_grade_students = []
        self.seventh_grade_students = []
        self.eight_grade_students = []
        self.ninth_grade_students = []

        self.student_dict = {1: self.first_grade_students,
                        2: self.second_grade_students,
                        3: self.third_grade_students,
                        4: self.fourth_grade_students,
                        5: self.fifth_grade_students,
                        6: self.sixth_grade_students,
                        7: self.seventh_grade_students,
                        8: self.eight_grade_students,
                        9: self.ninth_grade_students
                        }

        print "This is " + school_name

    def add_student(self, grade, name):
        self.student_dict[grade].append(name)

    def get_students_from_grade(self, grade):
        sorted_student_list = sorted(self.student_dict[grade])
        print str(grade) + "th class students are: "
        for student in sorted_student_list:
            print student

    def get_all_students(self):
        print "List of all the students in this school: "
        for grade in self.student_dict.values():
            for student in sorted(grade):
                print student

school = GradeSchool('Reaalkool')
school.add_student(3, 'Timmo')
school.add_student(3, 'Tammo')
school.add_student(3, 'Aadamson')
school.add_student(5, 'Tarmo')
school.get_students_from_grade(3)
school.get_students_from_grade(5)
school.get_all_students()
