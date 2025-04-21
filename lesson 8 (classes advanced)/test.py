from abc import ABC, abstractmethod

class Language(ABC):
    
    @abstractmethod
    def get_text(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

    def language_info(self):
        print(f"Text in {self.get_name()}: {self.get_text()}")


class English(Language):
    def get_text(self):
        return "This is a good sentence!"
    
    def get_name(self):
        return "English"
    
lang = English()
lang.language_info()