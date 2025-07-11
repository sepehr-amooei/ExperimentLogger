class MailcatObject:
    def __init__(self, idName, mailAddress, listItems=None):
        self.idNum = None
        self.idName = idName
        self.mailAddress = mailAddress
        self.listItems = listItems if listItems else []

class MailcatCollection:
    def __init__(self):
        self.mailcat = {}
        self.indexCounter = 0

    def add(self, mailcatObject):
        self.indexCounter += 1
        mailcatObject.idNum = self.indexCounter
        self.mailcat[self.indexCounter] = mailcatObject

class CreateCatalog:
    def __init__(self, records):
        self.data = MailcatCollection()
        for name, email, items in records:
            self.data.add(MailcatObject(name, email, items))

    def serialize(self):
        header = ["Name", "Mail_address", "Label", "Birthdate", "Start", "End", "Age", "Duration", "W_Start", "W_End"]
        output = [header]
        for obj in self.data.mailcat.values():
            row = [obj.idName, obj.mailAddress] + list(map(str, obj.listItems))
            output.append(row)
        return output
