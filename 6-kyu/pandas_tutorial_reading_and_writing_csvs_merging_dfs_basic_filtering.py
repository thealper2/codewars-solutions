import pandas as pd

def export_csv_with_name_and_grade(
    student_name: str, 
    grade: str
):
    students_df = pd.read_csv('files/students.csv')
    grades_df = pd.read_csv('files/grades.csv')
    student_ids = students_df.loc[students_df['Name'] == student_name, 'Student_ID']
    if student_ids.empty:
        empty = pd.DataFrame(columns=['Student_ID', 'Class'])
        empty.to_csv('files/output.csv', index=False)
        return
    
    result_df = grades_df[(grades_df['ID'].isin(student_ids)) & (grades_df['Grade'] == grade)]
    result_df = result_df[['ID', 'Class']].rename(columns={'ID': 'Student_ID'})
    result_df.to_csv('files/output.csv', index=False)
