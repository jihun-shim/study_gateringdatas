import codes.schedulers.get_classes as gf

temp = 'temp message'
def main(message):
    count = 0
    while True:
        print(f'{message} : count - {count}')
        # call function
        gf.message_print()
        gf.job_print()
        print(f'{gf.message}')
        
        count = count + 1
        pass
    return True

if __name__ == '__main__':
    main('task forever!')
    pass