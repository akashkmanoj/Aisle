exemptProducts = ["food","chocolates","book", "medicines","headache pills"]

class Item:

    def __init__(self, inputString):
        self.inputString = inputString
        self.name = ""
        self.rate = 0.00
        self.quantity = 0
        self.exempt = False
        self.imported = False
        self.salesTax = 0
        self.itemTotal = 0
        self.basicSalesTax = 0.10
        self.importedSalesTax = 0.05;
        self.checkExempt()
        self.checkImported()
        self.assignValues()
        self.checkSalesTax()
        

    def checkExempt(self):
        if any(x in self.inputString for x in exemptProducts):
            self.exempt = True;

    def checkImported(self):
        if "imported" in self.inputString: 
            self.imported = True
            
    def assignValues(self): 
        splitdWords = self.inputString.split()
        indices = [1, len(splitdWords)-2]
        self.name = " ".join(splitdWords[1:len(splitdWords)-1])
        self.quantity = int(splitdWords[0])
        self.rate = float(splitdWords[len(splitdWords)-1])
        
    def checkSalesTax(self):
        if not self.exempt:
            self.salesTax = self.quantity * self.rate *  self.basicSalesTax
        if self.imported:
            self.salesTax = self.salesTax + (self.quantity * self.rate* self.importedSalesTax)
        self.itemTotal = self.rate + self.salesTax;

class Business:

    def calculateTotal(self,itemList):
        salesTax = 0;
        totalPrice = 0;
        for item in itemList:
            print(item.quantity,"", item.name,":",(item.itemTotal))
            totalPrice = totalPrice + item.itemTotal
            salesTax = salesTax + item.salesTax
            print("Sales Tax: ",round(salesTax,2))
            print("Total: ",round(totalPrice,2))
        
itemList=[]
while True:
    item = input("Enter an item\n");
    if item:
        itemList.append(Item(item));
        del item
    else:
        if len(itemList) <= 0:
            print("No item to process");
        else:
            business = Business()
            business.calculateTotal(itemList);
            itemList.clear()
