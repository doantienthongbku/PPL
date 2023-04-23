def hello():
    print("hello")
    def hi():
        print("hi")
    hi()

def hi():
    print("hi")
    
if __name__ == "__main__":
    hello()
    hi()