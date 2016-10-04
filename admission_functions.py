SPECIAL_CASE_SCHOOL_1 = 'Fort McMurray Composite High'
SPECIAL_CASE_SCHOOL_2 = 'Father Mercredi High School'
SPECIAL_CASE_YEAR = '2016'

# Add other constants here
NO_EXAM = 'NE'

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
    """ (str, str, str) -> float
    
    >>> get_final_mark('Jacqueline Smith,Fort McMurray Composite High,2016,MAT,90,94,ENG,92,88,CHM,80,85,BArts','90','95')
    92.5
    >>> get_final_mark('Jacqueline Smith,Fort McMurray Composite High,2016,MAT,90,94,ENG,92,88,CHM,80,85,BArts','90','NE')
    90.0
    >>> get_final_mark('Jacqueline Smith,McDonald High,2014,MAT,90,94,ENG,92,88,CHM,80,85,BArts','90','NE')
    45.0
    """
    
    if NO_EXAM in exam_mark and is_special_case:
        return float(coursework_mark)
    elif NO_EXAM in exam_mark:
        return (int(coursework_mark) + 0)/2
    else:
        return (int(coursework_mark)+int(exam_mark))/2
    
    
    

def get_both_marks(course_record,course_code):
    """ (str, str) -> str
    
    >>> get_both_marks('MAT,90,85','MAT')
    '90 85'
    >>> get_both_marks('MAT,90,85','CHM')
    ''
    """
    
    if course_record[:3] == course_code:
        return course_record[4:6] + ' ' + course_record[7:9]
    else:
        return ''
    
    
    
    
def extract_course(transcript,extracted_course):
    """ (str, int) -> str
    
    >>> extract_course('BIO,90,94,ENG,92,NE,CHM,80,85',1)
    'BIO,90,94'
    >>> extract_course('BIO,90,94,ENG,92,NE,CHM,80,85',3)
    'CHM,80,85'
    """

    if extracted_course == 1 :
        return transcript[:9]
    elif extracted_course == 2:
        return transcript[10:19]
    else:
        return transcript[20:]
    
    
    

def applied_to_degree(record,degree):
    """ (str,str) -> bool
    
    >>> applied_to_degree('Jacqueline Smith,Fort McMurray Composite High,2016,MAT,90,94,ENG,92,88,CHM,80,85,BArts','BArts')
    True
    >>> applied_to_degree('Jacqueline Smith,Fort McMurray Composite High,2016,MAT,90,94,ENG,92,88,CHM,80,85,BArts','BCom')
    False
    >>> applied_to_degree('Arthur,Fort McMurray Composite High,2016,MAT,90,94,ENG,92,88,CHM,80,85,BCom','Art')
    False
    """
    return degree in record.split(",")[-1].strip()




def decide_admission(student_average,degree_cutoff):
    """(number,number) -> str
    
    >>>decide_admission(80,80)
    'accept'
    >>>decide_admission(86,80)
    'accept with scholarship'
    >>>decide_admission(76,80)
    'reject'
    """
    
    if student_average - degree_cutoff >= 5:
        return 'accept with scholarship'
    elif student_average < degree_cutoff:
        return 'reject'
    else:
        return 'accept'



    