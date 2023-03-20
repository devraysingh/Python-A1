SPECIAL_CASE_SCHOOL_1 = 'Fort McMurray'
SPECIAL_CASE_SCHOOL_2 = 'Father Mercredi'
SPECIAL_CASE_YEAR = '2016'

# Add other constants here
SCHOLARSHIP = 5
ACCEPT = 'accept'
ACCEPT_SCH = 'accept with scholarship'
REJECT = 'reject'
NE = 'NE'

def is_special_case(record):
    """ (str) -> bool
    
    Return True iff the student represented by record is a special case.
    
    >>> is_special_case('1,Jacqueline Smith,Fort McMurray Composite,2016,MAT,90,94,ENG,92,88,Bachelor of Arts')
    True
    >>> is_special_case('2,Jacqueline Smith,Father Something School,2016,MAT,90,94,ENG,92,88,Bachelor of Arts')
    False
    >>> is_special_case('1,Jacqueline Smith,Fort McMurray Composite,2015,MAT,90,94,ENG,92,88,Bachelor of Arts')
    False
    """
    
    return ((SPECIAL_CASE_SCHOOL_1 in record) or (SPECIAL_CASE_SCHOOL_2 in record)) and (SPECIAL_CASE_YEAR in record)
    
    
def get_final_mark(record, specific_coursework_mark, specific_exam_mark):
    """(str, str, str) -> float

    Return the final mark of the student in the course, while considering the special cases.

    >>> get_final_mark('1,Jacqueline Smith,Fort McMurray Composite,2016,MAT,90,94,ENG,92,88,Bachelor of Arts', '90', 'NE')
    90.0
    >>> get_final_mark('2,Jacqueline Smith,Father Something School,2016,MAT,90,94,ENG,92,88,Bachelor of Arts', '94', '90')
    92.0
    >>> get_final_mark('1,Jacqueline Smith,Fort McMurray Composite,2015,MAT,90,94,ENG,92,88,Bachelor of Arts', '90', '94')
    92.0
    """
   
    if is_special_case(record) == True and (specific_exam_mark == NE):
        return float(specific_coursework_mark)
    else:
        return ((float(specific_coursework_mark) + float(specific_exam_mark)) / 2)

def get_both_marks(course_record, course_code):
    """(str, str) -> str

    Return the specefic course and exam mark to the user when given the course code of that specefic course.

    >>> get_both_marks('MAT,90,94', 'MAT')
    90 94
    >>> get_both_marks('MAT,90,94', 'ENG')
    ""
    """
    
    if (course_code in course_record):
        return course_record[-5:-3] + " " + course_record[-2:]
    else:
        return ''
    


def extract_course(transcript, course_code):
    """(str, int) -> str

    Return the infromation of the course wanted from the user, using second parameter and
    extracting inforamation from the student transcript
    
    >>> extract_course('MAT,90,94,ENG,92,88,BIO,98,67', 1)
    'MAT,90,94'
    >>> extract_course('MAT,40,94,ENG,92,88,BIO,98,67', 2)
    'ENG,92,88'
    >>> extract_course('MAT,40,94,ENG,92,88,BIO,98,67', 5)
    ''    
    """

    
    if (course_code == 1):
        course_code = course_code - 1
        return transcript[course_code:(course_code + 9)]
    elif(course_code == 2):
        course_code = (course_code - 1) * 10
        return transcript[course_code: (course_code + 9)]
    elif(course_code == 3):
        course_code = (course_code - 1) * 10
        return transcript[course_code: (course_code + 9)]
    elif(course_code > 3):
        return ''
    


def applied_to_degree(record, applied_degree):
    '''(str, str) -> bool

    Return a statment iff the degree applied to by the student matches the student record.
    
    >>> applied_to_degree('1,Jacqueline Smith,Fort McMurray Composite,2016,MAT,90,94,ENG,92,88,Bachelor of Arts', 'Bachelor of Arts')
    True
    >>> applied_to_degree('1,Jacqueline Smith,Fort McMurray Composite,2016,MAT,90,94,ENG,92,88,Bachelor of Arts', 'Bachelor of Science')
    False
    
    '''
    return applied_degree in record
    

def decide_admission(total_course_average, cutoff_average):
    """(number, number) -> st

    Return the decision of acceptance or rejection in the area of study depending on meeting the cutoff_average, 
    and if the student recevies scholarship with it or not.
    
    >>> decide_admission(85, 90)
    'reject'
    >>> decide_admission(90, 90)
    'accept'
    >>> decide_admission(95, 90)
    'accept with scholarship'
    """

    
    if (total_course_average >= (cutoff_average + SCHOLARSHIP)):
        return ACCEPT_SCH
    elif(total_course_average >= cutoff_average):
        return ACCEPT
    else:
        return REJECT
