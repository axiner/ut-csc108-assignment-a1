SPECIAL_CASE_SCHOOL_1 = 'Fort McMurray Composite High'
SPECIAL_CASE_SCHOOL_2 = 'Father Mercredi High School'
SPECIAL_CASE_YEAR = '2016'

# Add other constants here
NO_EXAM = 'NE'
DESIRED_COURSE = input("Enter the course code of the desired course: ")

def is_special_case(record):
    """ (str) -> bool

    Return True iff the student represented by record is a special case.

    >>> is_special_case('Jacqueline Smith,Fort McMurray Composite High,2016,MAT,90,94,ENG,92,88,CHM,80,85,BArts')
    True
    >>> is_special_case('Jacqueline Smith,Father Something High School,2016,MAT,90,94,ENG,92,88,CHM,80,85,BArts')
    False
    >>> is_special_case('Jacqueline Smith,Fort McMurray Composite High,2015,MAT,90,94,ENG,92,88,CHM,80,85,BArts')
    False
    """

    # Complete the body of the function here
    return SPECIAL_CASE_SCHOOL_1 in record and SPECIAL_CASE_YEAR in record
    return SPECIAL_CASE_SCHOOL_2 in record and SPECIAL_CASE_YEAR in record


# Complete the rest of the functions here

def get_final_mark(record,coursework_mark,exam_mark):
    
    if NO_EXAM in exam_mark and is_special_case:
        return float(coursework_mark)
    elif NO_EXAM in exam_mark:
        return (int(coursework_mark) + 0)/2
    else:
        return (int(coursework_mark)+int(exam_mark))/2
    

def get_both_marks(course_record,course_code):
    
    if DESIRED_COURSE == course_code:
        return int
    
    

