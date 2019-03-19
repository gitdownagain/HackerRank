class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    # implement this function from the base class
    def divisorSum(self, n):
        divisor_list = []
        for x in range(1,n+1): # 6 = 1,2,3,6
            if n % x == 0:
                divisor_list.append(x)
        return sum(divisor_list)
                
# https://www.geeksforgeeks.org/sum-of-all-proper-divisors-of-a-natural-number/

# number 20 has 5 proper divisors: 1, 2, 4, 5, 10

# Objective 
#Today, we're learning about Interfaces. Check out the Tutorial tab for learning materials and an instructional video!

#Task 
#The AdvancedArithmetic interface and the method declaration for the abstract divisorSum(n) method are provided for you in the editor below.

#Complete the implementation of Calculator class, which implements the AdvancedArithmetic interface. The implementation for the divisorSum(n) method must return the sum of all divisors of "n".

# NOTE: __bases__ == The tuple of base classes of a class object.



n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
