import readline, shlex, cmd, sys, cowsay


class cow_chat(cmd.Cmd):
    intro = 'Welcome to the cow_chat.   Type help or ? to list commands.\n'
    prompt = '(cow_chat) '

    # cowsay commands
    def do_cowsay(self, arg):
        'print cow saying something'
        if '-l' in parse(arg):
            print (cowsay.list_cows())
        else:
            print(cowsay.cowsay(*parse(arg)))
#list_cows, make_bubble, cowsay и cowthink

    def do_list_cows(self, arg):
        'Lists all cow file names in the given directory'
        print(cowsay.list_cows(*parse(arg)))

    def do_make_bubble(self, arg):
        'Wraps text if wrap_text is true, then pads text and sets inside\
a bubble. This is the text that appears above the cows'
        print(cowsay.make_bubble(*parse(arg)))
        """
    def do_make_bubble(self, arg):
        'Wraps text if wrap_text is true, then pads text and sets inside\
a bubble. This is the text that appears above the cows'
        assumption = [None,
        cowsay.Bubble(stem='\\', l='<', r='>', tl='/', tr='\\', ml='|', mr='|', bl='\\', br='/'),
        40, True]
        args = check_assumption(assumption, parse(arg))
        print(cowsay.make_bubble(*args))
        """

    def do_cowthink(self, arg):
        'Cow think about wise things'
        print(cowsay.cowthink(*parse(arg)))

    #promt commands
    def do_exit(self, arg):
        'Exit command'
        print('Exit')
        return True

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return shlex.split(arg)

def check_assumption(assumption, args):
    for i in range(len(args), len(assumption)):
        if assumption[i] == None:
            print('Error need more parameters')
        else:
            args.append(assumption[i])
    return args

if __name__ == '__main__':
    cow_chat().cmdloop()
