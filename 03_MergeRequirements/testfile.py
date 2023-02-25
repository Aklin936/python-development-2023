import bullscows


def ask(prompt: str, valid: list[str] = None) -> str:
    if valid == None:
        print(prompt)
        answer = None
    else:
        print(prompt)
        while True:
            answer = input()
            f = False 
            for i in valid:
                if answer == i:
                    f = True
                    break
            if f:
                break
    return(answer)


def inform(format_string: str, bulls: int, cows: int) -> None:
    print("Быки: ", bulls,"Коровы: ", cows)


bullscows.gameplay(ask, inform, ['cat', 'bat', 'let', 'set', 'met'])
