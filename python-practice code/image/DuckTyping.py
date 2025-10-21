# ...existing code...
class Pycharm:
    def execute(self):
        print("compiling")
        print("running")
class Myeditor:
    def execute(self):
        print("Spell check")
        print("convention check")
        print("compiling")
        print("Running")
class Laptop:
    def code(self, ide):
        ide.execute()
ide = Myeditor()
lap1 = Laptop()
# ...existing code...
lap1.code(ide)          # call the method to execute Myeditor
lap1.code(Pycharm())    # optional: call with Pycharm     
                        