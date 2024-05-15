class NoteTwo:
    def __init__(self, text, iscomplete):
        self.text = text
        self.count = 0
        self.iscompleted = iscomplete

    def upd_count(self, gob):
        self.count += gob

    def res_count(self):
        self.count = 0


note1 = NoteTwo('arbuz', False)

print(note1.text)
print(note1.count)
print(note1.iscompleted)
print(note1.count)
note1.upd_count(3)
print(note1.count)
note1.res_count()
print(note1.count)
print(note1.__dict__)