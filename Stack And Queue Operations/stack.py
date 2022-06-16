def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack) == 0

def push(stack):
    item=int(input('Enter Item to push'))
    stack.append(item)
    print("pushed item: ",item)

def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"

    return stack.pop()

stack = create_stack()
while(1):
    print('Menu\n\t1.Create Stack'
      '\n\t2.Push()'
      '\n\t3.Pop()'
      '\n\t4.Display'
      '\n\t5.Exit')

    match ch:=int(input('Enter Your Choice:')):
        case 1:
            create_stack()
            print(ch)
        case 2: push(stack)
        case 3: pop(stack)
        case 4: print(stack)
        case 5: exit()
        case _:
            print('Wrong Choice')


