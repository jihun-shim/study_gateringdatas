import get_classes

temp = 'temp message'
def main(message):
    count = 0
    while True:
        print(f'{message} : count - {count}')
        # call function
        get_classes.getfunctions.message_print()
        get_classes.getfunctions.job_print()
        print(f'message : {get_classes.getfunctions.message}')
        count = count + 1
        pass
    return True

if __name__ == '__main__':
    main('task forever!')
    pass