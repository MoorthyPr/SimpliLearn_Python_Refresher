class Operations:
    def __init__(self,a,b,operation,*args):
        self.a = a
        self.b = b
        self.operation = operation 
        self.args = args if args else None
    def operate(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "subtract":
            return self.a - self.b
        elif self.operation == "multiply":
            return self.a * self.b
        elif self.operation == "divide":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero is not allowed."
        else:
            return "Error: Invalid operation."
        
    def display_result(self):
        result = self.operate()
        print(f"Result of {self.operation} operation on {self.a} and {self.b} is: {result}")    


    def multi_args(self,*args):
        if self.operation == "add":
            return sum(args)
        elif self.operation == "multiply":
            result = 1
            for arg in args:
                result *= arg
            return result
        else:
            return "Error: Invalid operation."

class Calculator(Operations):
    def __init__(self,a,b,operation):
        super().__init__(a,b,operation)

    def display_result(self):
        result = self.operate()
        print(f"Result of {self.operation} operation on {self.a} and {self.b} is: {result}")



cal1 = Calculator(10,5,"add")
cal1.display_result()

result_multi_args = cal1.multi_args(1,2,3,4,5)
print(f"Result of muliple arguments for {cal1.operation} operation is: {result_multi_args}")








