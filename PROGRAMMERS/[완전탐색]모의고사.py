def solution(answers):
    answers_1 = [1,2,3,4,5] #5
    answers_2 = [2,1,2,3,2,4,2,5] #8
    answers_3 = [3,3,1,1,2,2,4,4,5,5] #10
    k = len(answers)
    while len(answers_1) < k:
        answers_1.extend(answers_1)
    while len(answers_2) < k:
        answers_2.extend(answers_2)
    while len(answers_3) < k:
        answers_3.extend(answers_3)

    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0

    for i in range(k):
        if answers_1[i] == answers[i]:
            cnt_1 += 1
        if answers_2[i] == answers[i]:
            cnt_2 += 1
        if answers_3[i] == answers[i]:
            cnt_3 += 1

    scores = [cnt_1, cnt_2, cnt_3]
    max_score = max(scores)
    result = []

    for i, score in enumerate(scores):
        if score == max_score:
            result.append(i + 1)
    return result
