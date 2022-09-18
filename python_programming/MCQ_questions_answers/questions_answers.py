from questions import questions

real_question = ["Taste of mango is:: \na) Sweet \nb)Sower \nc)bitter\n\n",
                 "Taste of apple is:: \na) Sweet \nb)Sower \nc)bitter\n\n"]

Questions_list = [questions(real_question[0], "a"),
                  questions(real_question[1], "b")]


def run_test(Questions_list):
    score = 0
    for Question in Questions_list:
        answer = input(Question.prompt)
        if answer == Question.answer:
            score += 1
    print("you got " + str(score) + "/" + str(len(Questions_list)) + " correct")


run_test(Questions_list)
