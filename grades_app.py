from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_grade(n1, n2, n3):
    return 24 * max(n1, n2) + 28 * max(n3, n2) + 48 * max(n3, (0.3 * n1 + 0.7 * n2))

def get_result(test1, test2):
    already_earned_grades = []  # List to store earned grades

    curr_grade = calculate_grade(test1, test2, 0)
    grade_dict = {'C': 40, 'C+': 54, 'B-': 60, 'B': 66, 'B+': 80, 'A-': 85, 'A': 90, 'A+': 100}

    for letter_grade, grade_value in grade_dict.items():
        if curr_grade >= grade_value:
            already_earned_grades.append(letter_grade)

    result = f"You have already earned the following grades: "
    for earned_grade in already_earned_grades:
        result += f"{earned_grade}, "

    return result

@app.route('/grades/', methods=['GET', 'POST'])
def grades():
    if request.method == 'POST':
        test1 = float(request.form['test1'])
        test2 = float(request.form['test2'])
        result = get_result(test1, test2)
        return render_template('result.html', result=result)

    return render_template('grades.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
