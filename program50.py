# inheritance

# parent/super/base class
class Phone:
    def call(self):
        print("You can call")

    def message(self):
        print("You can message")


# sub/child/derived class
class Samsung(Phone):
    # call, message
    def photo(self):
        print("You can take photo")


s = Samsung()
s.message()
s.call()
s.photo()
print(issubclass(Samsung, Phone))
