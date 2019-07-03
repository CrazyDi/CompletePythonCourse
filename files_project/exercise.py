if __name__ == "__main__":
    questions_file = open('questions.txt', 'r')
    questions = [question.strip() for question in questions_file.readlines()]
    questions_file.close()

    questions = [
        {
            'example': question[:question.index('=') + 1],
            'result': question[question.index('=') + 1:]
         } for question in questions]

    grade = 0
    for question in questions:
        user_result = input(question['example'])
        if user_result == question['result']:
            grade = grade + 1

    result_file = open('result.txt', 'w')
    result_file.write(f'Your final score is {grade}/{len(questions)}.')
    result_file.close()
    print(f'Your final score is {grade}/{len(questions)}.')