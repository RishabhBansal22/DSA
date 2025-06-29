
class Pattern:
    def __init__(self, n: int):
        self.n = n

    def print_nums(self):
        for i in range(0,self.n):
            for j in range(0,self.n):
                print(j+1, end=" ")
            print()

    def print_sym(self, sym):
        for i in range(0, self.n):
            for j in range(0, self.n):
                print(sym, end=" ")

            print()

    def print_character(self):
        for i in range(0, self.n):
            num = 0
            char: str = "A"
            while num<self.n:
                print(char, end=" ")
                num+=1
                char = chr(ord(char)+1)
            print()

    def print_num_continue(self):
        num = 1
        for i in range(0, self.n):
            for j in range(0, self.n):
                print(num, end=" ")
                num+=1
            print()

    def print_char_continue(self):
        char: str = "A"
        for i in range(0, self.n):
            for j in range(0, self.n):
                print(char, end=" ")
                char = chr(ord(char)+1)
        
            print()

    def triangle(self):
        for i in range(self.n):
            for j in range(i+1):
                print("*", end=" ")
                
            print()
            

n = 3
pattern = Pattern(n)
pattern.triangle()
