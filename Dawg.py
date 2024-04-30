

from textx import metamodel_from_file
Dawg_mm = metamodel_from_file('Dawg.tx')
Dawg_model = Dawg_mm.model_from_file('program.Dawg')

locDic = dict()

class Dawg:
    
    def assignment(self,var,val):    
        locDic[var] = val
    
    def print_this(self, targetVar):
        if targetVar in locDic:
            
            print(locDic[targetVar])
        else:
            print(targetVar)

    def for_Loop(self,minVal,maxVal,statements):
        for i in range(minVal,maxVal):
                self.intepreter(statements)
            
    def comparison(self,minVal,maxVal,statements,compare):
        tempVal = minVal.val
        tempLocValue = 0
        if tempVal in locDic:
             tempLocValue = locDic[tempVal]

        if '<' == compare:
            if tempLocValue < maxVal:
                self.intepreter(statements)
        if '>' == compare:
            if tempLocValue > maxVal:
                self.intepreter(statements)
        if '!=' == compare:
            if tempLocValue != maxVal:
                self.intepreter(statements)
        
        if '==' == compare:
            if tempLocValue == maxVal:
                
                self.intepreter(statements)

    def math_Operations(self,expressions,sumVariable):

        tempValue1 = expressions.var1
        tempValue2 = expressions.var3
        tempOperand = expressions.varop
        tempSum = 0
        if not sumVariable in locDic:
            locDic[sumVariable] = 0
        
        if tempValue1 in locDic:
            tempValue1 = locDic[tempValue1]

        if tempValue2 in locDic:
            tempValue2 = locDic[tempValue2]
        
        if tempOperand == '-':
            tempSum = tempValue1 - tempValue2

        if tempOperand == '+':
            tempSum = tempValue1 + tempValue2
        
        if tempOperand == '*':
            tempSum = tempValue1 * tempValue2

        if tempOperand == '/':
            tempSum = tempValue1 / tempValue2
        
        if tempOperand == '%':
            tempSum = tempValue1 % tempValue2
        
        locDic[sumVariable] = tempSum

    def while_loop(self,iteration, statements):
        i = 1
        while i < iteration:
            self.intepreter(statements)
            iteration-=1
    def intepreter(self,model):

        for dogLines in model.statements:
            if dogLines.__class__.__name__ == "AssignmentStatement":
                self.assignment(dogLines.var,dogLines.expr)
            if dogLines.__class__.__name__ == "PrintStatement":
                self.print_this(dogLines.var)
            if dogLines.__class__.__name__ == "ForLoopStatement":
                self.for_Loop(dogLines.val1,dogLines.val2,dogLines)
            if dogLines.__class__.__name__ == "if_statment":
                self.comparison(dogLines.comparison,dogLines.var1,dogLines,dogLines.compareOperator) 
            if dogLines.__class__.__name__ == "MathAssignment":
                self.math_Operations(dogLines.expr,dogLines.var) 
            if dogLines.__class__.__name__ == "WhileLoop":
                self.while_loop(dogLines.val1,dogLines) 
                
dawg = Dawg()
dawg.intepreter(Dawg_model)

#This works
# Begin
    # Name is "Moka"
    # Age is 5
    # BARK Name
    # BARK Age
    # Name1 is "Max"
    # BARK Name1
    # BARK sfdsfd
# end
#This works
# Begin
#     Name is "Moka"
#     Age is 5
#     Dom is "The greatest professor alive"
#     RollOver 6,10(BARK Dom)
#     RollOver 1,5(BARK Age BARK Name )
# end

# Begin
    # Name is "Max"
    # Name2 is "Andrew"
    # Name3 is "Kitty"
    # Age is 2
    # RollOver 1,5(BARK Age BARK Name)
    # Confused Age<5(BARK Name BARK Name2)
# end

# I am not sure if this would work
# MathAssignment: 
#     'Paw' var=ID '=' expr=mathExpression;
# mathExpression: 
#     val=Sum;
# Sum: 
#     base=Product terms*=ExtraTerm;
# ExtraTerm: 
#     operator=Operator value=Product;
# Operator: 
#     '+' | '-' | '/';
# Product: 
#     base=Value factors*=ExtraFactor;
# ExtraFactor: 
#     operator='*' value=Value;
# Value: 
#     ID | INT | ID ('(' mathExpression ')');





# Program:
#     'Begin'
#         statements*=Statements
#     'end';

# Statements:
#    PrintStatement | AssignmentStatement | ForLoopStatement | 
#    commparsionStatement  | WhileLoop| MathStatment;

# PrintStatement: 
#     'BARK' var=ID;

# AssignmentStatement: 
#     var=ID 'is' expr=Expression;

# Expression:
#     BASETYPE;
 
# ForLoopStatement: 
#     'RollOver' val1=INT ',' val2=INT ('('statements*=Statements')')?;


# commparsionStatement:
#     'Confused' comparison=compareValue compareOperator=CompareOperator var1=INT ('('statements*=Statements')')?;

# compareValue:
# val=ID;

# CompareOperator:
# '<' | '>' | '==';

# WhileLoop: 
#     'Sit' val1=INT ('('statements*=Statements')')?;

# MathStatment:
#     'Paw' val=ID '=' mathExpr=MathExpression;

# MathExpression:
#     firstExpression=Operand Operator=Operation (nextOperation*=findNext)?;

# Operand:
# thisIdentifier=ID | thisNumber=INT;

# Operation:
# '+' | '-' | '*' | '/';

# findNext:
#     Operand | Operation;


# Begin
#     BARK PRINT_THIS
#     Name is "Max"
#     BARK Name
#     Name2 is "Andrew"
#     Name3 is "Kitty"
#     Age is 2
#     Hello is "sdfjksdlfkdsfklds"
#     RollOver 1,5(BARK Age BARK Name)
#     Confused Age<5(BARK Name3 BARK Name2 BARK Age)
#     phrase is "Hello DOM"
#     Sit 5(BARK phrase)
#     Paw Age = Age - 3
#     Paw newVar = 20 - 3
#     BARK newVar
#      Paw newVar = Age - 3
# end

#Sit 100(Confused Age==0(BARK Age Paw Age=Age-1))

# Begin
#     Name is "Doggy"
#     Name2 is "Style"
#     Name3 is "DoggyStyle"
#     Age is 101
#     Age1 is 0
#     Age2 is 0
#     Age3 is 0

#     Sit 101(
#     Paw Age1=Age%3 
#     Paw Age2=Age%5
#     Paw Age3=Age%15
#     Confused Age3==0(BARK Name3) 
#     Confused Age1==0(BARK Name)
#     Confused Age2==0(BARK Name2)
#     Paw Age=Age-1 
#     BARK Age)
# end

# Begin
#     Name is "Doggy"
#     Name2 is "Style"
#     Name3 is "DoggyStyle"
#     Age is 100
#     Age1 is 0
#     Age2 is 0
#     Age3 is 0
#     Sit 101(
#     Paw Age1=Age%3 
#     Paw Age2=Age%5
#     Paw Age3=Age%15
#     Confused Age3==0(BARK Name3)
#     Confused Age1==0(BARK Name)
#     Confused Age2==0(BARK Name2)
#     Confused Age3!=0(Confused Age2!=0(Confused Age1!=0(BARK Age)))
#     Paw Age=Age-1 
#     )
# end