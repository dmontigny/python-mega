reps = []

def ask():
    while True:
        ans = input("Say something: ").strip()
        if not ans:
            break
        reps.append(add_ans(ans).capitalize())
    end_app()


def add_ans(t):
    q = ['who', 'what', 'why', 'where', 'when', 'how', 'are', 'did', "didn't", 'is', "isn't"]
    if t.split()[0] in q:
        punc = "?"
    else:
        punc = "."
    return t + punc


def end_app():
    print(' '.join(reps))


ask()

