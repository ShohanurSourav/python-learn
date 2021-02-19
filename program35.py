# xargs

def student(*details):
    print(details)
    print(details[1])


student(101, "Sourav", "Rangpur")


def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)


add(10, 20)
add(10, 30)
add(10, 40, 30)


# xxargs

def student(**details):
    print(details)
    print(details["id"])


student(id=101, name="Sourav", address="Rangpur")
