
class Transaction:
    def tipCalc(self, cost, tipPercentage):
        percentage = tipPercentage *  0.01
        tip = cost * percentage
        total = tip + cost
        print("Cost: {}".format (cost))
        print("Tip: {}".format (round(tip, 2)))
        print("Total: {}".format (round(total, 2)))

# transaction.tipCalc()
transaction = Transaction()
print("Test 1")
test1 = transaction.tipCalc(51.25, 25)
print("Test 2")
test2 = transaction.tipCalc(11.25, 15)
print("Test 3")
test3 = transaction.tipCalc(69.69, 69)
print("Test 4")
test4 = transaction.tipCalc(80.08, 21)

