class Stack:
    def __init__(self, stack=None):
        if stack is None:
            stack = []
        self.stack = stack

    def isEmpty(self):
        if self.stack:
            return False
        else:
            return True

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            last_element = self.stack.pop()
            return last_element

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def size(self):
        return len(self.stack)


def is_string_balanced(string=input()):
    balance_dict = {'(': ')', '{': '}', '[': ']'}
    stack = Stack()
    for i in string:
        if i in balance_dict.values():
            if balance_dict.get(stack.peek()) == i:
                stack.pop()
            else:
                stack.push(i)
        else:
            stack.push(i)
    if stack.isEmpty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'


if __name__ == '__main__':
    print(is_string_balanced())
