class MainClass:
    def __init__(self, text=""):
        self._text = text

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

    def set_text(self, text=None):
        if text is None:
            self._text = "Default Text"
        else:
            self._text = text

class SubClass(MainClass):
    def __init__(self, text="", number=0):
        super().__init__(text)
        self._number = number

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number
if __name__ in "__main__":
    main_obj = MainClass("Initial Text")
    print(main_obj.text)  
    main_obj.set_text()
    print(main_obj.text)
    main_obj.set_text("New Text")
    print(main_obj.text)

    sub_obj = SubClass("Sub Initial Text", 42)
    print(sub_obj.text)
    print(sub_obj.number)
    sub_obj.set_text("Sub New Text")
    sub_obj.number = 99
    print(sub_obj.text)
    print(sub_obj.number)