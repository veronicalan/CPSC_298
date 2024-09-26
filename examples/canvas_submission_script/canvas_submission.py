import os
import requests
import csv

def get_canvas_api_token():
    return os.getenv('CANVAS_API_TOKEN')

def get_courses(api_token):
    url = "https://canvas.instructure.com/api/v1/courses"
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_students_in_course(api_token, course_id):
    url = f"https://canvas.instructure.com/api/v1/courses/{course_id}/students"
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def create_csv_for_students(courses, api_token):
    with open('students_list.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Course Name', 'Student Name', 'Email'])

        for course in courses:
            course_id = course['id']
            course_name = course['name']
            students = get_students_in_course(api_token, course_id)
            for student in students:
                writer.writerow([course_name, student['name'], student['email']])

def main():
    api_token = get_canvas_api_token()
    if not api_token:
        raise EnvironmentError("CANVAS_API_TOKEN environment variable not set.")
    
    courses = get_courses(api_token)
    create_csv_for_students(courses, api_token)

if __name__ == "__main__":
    main()
