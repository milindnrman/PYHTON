def calculate_gpa(grades):
    total_grade_points=sum(grades.values())
    total_courses=len(grades)

    if total_courses==0:
        return 0
    
    return total_grade_points/total_courses