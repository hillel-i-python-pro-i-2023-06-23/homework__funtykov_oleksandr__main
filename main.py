if __name__ == '__main__':
    n = int(input())
    if n < 2 or n > 10:
        print("Invalid number")
        exit

    arr = list(map(int, input().split()))
    for score in arr:
        if score < -100 or score > 100:
            print("Invalid value")
            exit

    unique_scores = sorted(set(arr), reverse=True)

    if len(unique_scores) > 1:
        runner_up_scores = unique_scores[1]
        print(runner_up_scores)
    else:
        print("There is no score")
