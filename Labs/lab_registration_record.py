# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: B. Schoen-Phelan
# date: 13-11-2020
# purpose: A solution to the word games lab exercise


class Student:
    """
    This class contains the students details i.e. their firstname, lastname and their study type.

    ...

    Attributes:
    -----

        UNDERGRADUATE AND POSTGRADUATE are class variables. They are used to determine the student's study level
        UNDERGRADUATE is assigned the value 0 and POSTGRADUATE is assigned the value 1.

        study_type: range(2)
        study_type is only allowed the predefined Student.UNDERGRADUATE and Student.POSTGRADUATE class variables

        f_name : str
        Firstname of the student

        l_name : str
        Lastname of the student

        course : list
        This variable is used to put the names of the students courses into a list by appending them into the
        empty list.

    ...

    Methods:
    -----
        student_name : property
            Returns self.firstname, self.lastname
            available as a setter that expects the first and last name as a list. The first element being
            the first name and the second element being the last name

        courses : property


    """

    UNDERGRADUATE, POSTGRADUATE = range(2)

    def __init__(self, study_type, f_name, l_name):
        # YOUR CODE GOES HERE
        self.study_type = study_type
        self.firstname = f_name
        self.lastname = l_name
        self.course = []

    # YOUR CODE GOES HERE
    @property  # getter method
    def student_name(self):
        return self.firstname, self.lastname  # getting the first name of the student

    @student_name.setter
    def student_name(self, s_name):
        self.firstname = s_name[0]
        self.lastname = s_name[1]

    @property
    def courses(self):
        return self.course

    @courses.setter
    def courses(self, new_course):
        self.course.append(new_course)


class RegistrationData:
    """
    This class is the composite class. It creates a

    ...

    Attributes:



    """

    def __init__(self, address, registration_fee, study_type, f_name, l_name, s_id="NA"):
        # YOUR CODE GOES HERE
        self.study_type = study_type
        self.address = address
        self.registration_fee = registration_fee
        self.student_id = s_id
        self.student_object = Student(study_type, f_name, l_name)

    # YOUR CODE GOES HERE

    # using get method to get the registration details of student

    # def set_name(self, new_name):  # giving a new value for the variable f_name
    #     self.firstname = new_name

    @property
    def student_address(self):  # getting the address
        return self.address

    @property
    def student_reg_fee(self):  # getting the registration fee
        return self.registration_fee

    def study_type(self):  # getting study type
        return self.study_type

    @property
    def student_ID(self): # getting student ID
        return self.student_id

    # def set_student_ID(self, new_id): # setting a new student ID
    #     self.student_id = new_id

    def get_student_object(self):
        return self.student_object

    def display_student_data(self):
        print("Student Info: " + str(self.student_object.student_name) + ", " + str(self.study_type) + ", " + self.student_id + ", " + str(r.student_object.course))
        print("Address: ", self.address)
        print("Registration fee: ", str(self.registration_fee))


r = RegistrationData("8 Lower Kevin Street, Dublin 8, Ireland", 1500,
                     Student.POSTGRADUATE, "Bianca", "Phelan")
r.display_student_data()
r.student_id = "C12345"
r.display_student_data()
for course in ("OOP", "Advanced Databases", "Environmental Analytics"):
    r.student_object.courses = course
r.display_student_data()

# ### MY OWN PRACTICE - GETTER & SETTER METHODS ### #
# print(r.get_name())
# print(r.get_lastname())
# r.set_name("Lina")
# print(r.get_name())

# print(RegistrationData.__doc__)
