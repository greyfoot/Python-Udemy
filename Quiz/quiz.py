file_q = open("questions.txt", "r")
questions = [line.strip() for line in file_q]
file_q.close()
correct_ans = 0
for i in questions:
    q = i.split("=")
    ans = input(f"{q[0]}=")
    if ans == q[1]:
        print(f"{ans} is the correct answer!")
        correct_ans += 1
    else:
        print(f"{ans} is incorrect!!")
file_r = open("result.txt", "w")
file_r.write(f"Your final score is {correct_ans}/{len(questions)}.")
file_r.close()
