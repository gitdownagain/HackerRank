class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = None # instance variable
    
# instead of the private integer array we have a list of __elements that are "private" in Python

	# Add your code here (method inside Difference class)
    def computeDifference(self):
        # check if the list has all the same elements
        # elements backwards using a shallow copy
        if self.__elements == self.__elements[::-1]:
            self.maximumDifference = 0
            return self.maximumDifference

        difference = []
        for a in self.__elements:
            for b in self.__elements:
                if b == a:
                    continue # skip this item
                difference.append(abs(a - b))
                #print("DEBUG - difference:", difference)
                self.maximumDifference = max(difference)

        return self.maximumDifference

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
