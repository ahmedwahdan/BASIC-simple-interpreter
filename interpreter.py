INTEGER, PLUS, MINUS, PROD, DIV, EOF = 'INTEGER', 'PLUS', 'MINUS' , 'PROD', 'DIV', 'EOF'

class Token():
    def __init__(self,type,value):
        self.type = type
        self.value = value
        
    def __str__(self):
        return 'Token({type},{value})'.format(type = self.type, value = self.value)
    
    def __repr__(self):
        return self.__str__()
    
class Interpreter():
    def __init__(self,text):
        # user operation "3+5"
        self.text  = text
        self.pos   = 0
        self.current_token = None
        self.current_char = self.text[self.pos]
        
    def error(self):
        raise Exception("Error parsing input")
        
        
    def advance(self):
        #print("advanve pos : ", self.pos)
        self.pos += 1
        if (self.pos > len(self.text) - 1):
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]
     
    def skip_whitespace(self):
        pass
    
    def integer(self):
        
        # gather the integer digits as string, then convert to integer
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            #print("Integer")
            #print("current integer : ", self.current_char)
            self.advance()
        #print("integer result : ", int(result))    
        return int(result)    
    
    def get_next_token(self):
        
        # continue parsing as long as there is data
        while self.current_char is not None:
            #print("Get next token")
            #print("current char : ", self.current_char)
            
            # handle white spaces before and after digits
            if self.current_char.isspace():
                #self.skip_whitespace()
                self.advance()
                #print("White space")
                continue
                
            # handle integers (multiple digits)
            if self.current_char.isdigit():
                integer_val = self.integer()
                return Token(INTEGER, integer_val)
            
            # handle operations
            if self.current_char == '+':
                self.advance()
                return Token(PLUS, None)
            
            if self.current_char == '-':
                self.advance()
                return Token(MINUS, None)
            
            if self.current_char == '*':
                self.advance()
                return Token(PROD, None)
        
            if self.current_char == '/':
                self.advance()
                return Token(DIV, None)
            # rasie exception if the data is neither integer nor operation
            self.error()
            
        # return EOF token if we reached the end of user input    
        return Token(EOF, None)
    
    def eat(self, token_type):
        #print("eat type: ",token_type)
        #print("toke type: ",self.current_token.type)
        if(self.current_token.type == token_type):
            self.current_token = self.get_next_token()
        else:
            self.error()
    
    def expr(self):
        
        self.current_token = self.get_next_token()
        
        left = self.current_token
        self.eat(INTEGER)
    
        op = self.current_token   
        if(op.type == PLUS):
            self.eat(PLUS)
        elif(op.type == MINUS):
            self.eat(MINUS)
        elif(op.type == PROD):
            self.eat(PROD)
        elif(op.type == DIV):
            self.eat(DIV)    
            
        right = self.current_token
        self.eat(INTEGER)
        
        if(op.type == PLUS):
            result = left.value + right.value
        elif(op.type == MINUS):
            result = left.value - right.value
        elif(op.type == PROD):
            result = left.value * right.value
        elif(op.type == DIV):
            if(right.value is not 0):
                result = left.value / right.value 
            else:
                raise Exception("Divided by zero")
        return result
    
    
   
