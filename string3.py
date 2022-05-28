# Valid Parenthesis
class Partha(object):
    def isValid(self, s):
        if s == []:
            return False
        else:
            stack = []
            balanced = True
            index = 0
            while index < len(s) and balanced:
                symbol = s[index]
                if symbol in "({[":
                    stack.append(symbol)
                else:
                    if stack == []:
                        balanced = False
                    else:
                        top = stack.pop()
                        if not self.matches(top,symbol):
                            balanced = False
                index = index + 1

            if balanced and stack == []:
                return True
            else:
                return False

    def matches(self,open,close):
        openings = "({["
        closings = ")}]"

        return openings.index(open) == closings.index(close)
    
ob1=Partha()
print(ob1.isValid(s = "()"))
print(ob1.isValid(s = "()[]{}"))
print(ob1.isValid(s = "(]"))