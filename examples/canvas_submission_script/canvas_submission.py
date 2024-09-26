import os
import requests
import csv

def get_canvas_api_token():
    return os.getenv('CANVAS_API_TOKEN')

def get_canvas_domain():
    return os.getenv('CANVAS_DOMAIN')

def get_courses(api_token, domain):
    url = f"https://{domain}/api/v1/courses"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Authentication-Provider": "canvas"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_students_in_course(api_token, course_id, domain):
    url = f"https://{domain}/api/v1/courses/{course_id}/students"
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_assignments_in_course(api_token, course_id, domain):
    url = f"https://{domain}/api/v1/courses/{course_id}/assignments"
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def update_student_grade(api_token, course_id, assignment_id, student_id, grade, domain):
    url = f"https://{domain}/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{student_id}"
    headers = {"Authorization": f"Bearer {api_token}", "Content-Type": "application/json"}
    data = {"submission": {"posted_grade": grade}}
    response = requests.put(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()
def create_csv_for_students(courses, api_token, domain):
    with open('students_list.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Course Name', 'Student Name', 'Email'])

        for course in courses:
            course_id = course['id']
            course_name = course['name']
            students = get_students_in_course(api_token, course_id, domain)
            for student in students:
                writer.writerow([course_name, student['name'], student['email']])

def update_grades_for_students(courses, api_token, domain):
    for course in courses:
        course_id = course['id']
        assignments = get_assignments_in_course(api_token, course_id, domain)
        students = get_students_in_course(api_token, course_id, domain)
        
        for assignment in assignments:
            assignment_id = assignment['id']
            for student in students:
                student_id = student['id']
                # Example: Assign a grade of 85 to each student for each assignment
                update_student_grade(api_token, course_id, assignment_id, student_id, 85, domain)
def main():
    api_token = get_canvas_api_token()
    domain = get_canvas_domain()
    if not api_token or not domain:
        raise EnvironmentError("CANVAS_API_TOKEN or CANVAS_DOMAIN environment variable not set.")
    
    courses = get_courses(api_token, domain)
    create_csv_for_students(courses, api_token, domain)
    update_grades_for_students(courses, api_token, domain)

if __name__ == "__main__":
    main()
