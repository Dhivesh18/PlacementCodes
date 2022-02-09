class s:
    def __init__(self):
        self.stack = []
    
    def push(self,data):
        self.stack.append(data)
    
    def pop(self):
        a = self.stack.pop()
        return a

    def BBal(self,e):
        for i in e:
            if i in ["(","{","["]:
                self.push(i)             # If the input is open brackets it will be added to stack.
            else:
                if not self.stack:       # If the stack is Empty, it will return Unbalanced.
                    return "Unbalanced"
                cur_char = self.pop()    # Last element of stack will be popped when there is no open bracket.
                if cur_char == '(':
                    if i != ')':
                        break
                if cur_char == '{':
                    if i != '}':
                        break
                if cur_char == '[':
                    if i!= ']':
                        break
        if self.stack:
            return "Unbalanced"
        else:
            return "Balanced"

a = s()
n = input("Enter the Brackets")
print(a.BBal(n))







