class Palindrome:

    @staticmethod
    def is_palindrome(word):
        word = word.upper()

        if word == word[::-1]:
            return True
        else:
            return False

print(Palindrome.is_palindrome('Deleveled'))


class FileOwners:

    @staticmethod
    def group_by_owners(files):
        result = {}
        for file, owner in files.items():
            result[owner] = result.get(owner, []) + [file]
        return result

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}

print(FileOwners.group_by_owners(files))


class Print:
    @staticmethod
    def print_integers():
        one = 1
        string =  "Printed out number: %d" % one
        return string

print(Print.print_integers())


class PizzaList:
    def print_out_pizzas(self):
        mylist = []
        mylist.append("margarita")
        mylist.append("romana")
        mylist.append("silicana")

        # prints out 1,2,3
        for x in mylist:
            print(x)


pizza_list = PizzaList()
pizza_list.print_out_pizzas()


class Objects:
    def test_objects(self):
        x = object()
        y = object()

        # TODO: change this code
        x_list = [x] * 10
        y_list = [y] * 10
        big_list = x_list + y_list

        print("x_list contains %d objects" % len(x_list))
        print("y_list contains %d objects" % len(y_list))
        print("big_list contains %d objects" % len(big_list))

        if x_list.count(x) == 10 and y_list.count(y) == 10:
            print("Almost there...")
        if big_list.count(x) == 10 and big_list.count(y) == 10:
            print("Great!")


class Reverse:
    def reverse_string(self, str):
        reversed_str = str[::-1]
        print reversed_str

a = Reverse()
a.reverse_string("Mudilane")


class List():
    def print_unique_list_values(self, list):
        unique_list = []

        for item in list:
            if item not in unique_list:
                unique_list.append(item)

        print unique_list

a = List()
a.print_unique_list_values(list=[1, 1, 2, 2, 3, 4, 5])




