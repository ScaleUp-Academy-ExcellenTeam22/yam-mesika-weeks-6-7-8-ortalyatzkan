class User:
    """
    A class containing user details.
    """
    def __init__(self, user_name, user_password, type_of_user):
        self.user_name = user_name
        self.password = user_password
        self.type = type_of_user


class File:
    """
    A class that contains details of a general file.
    """
    def __init__(self, name_of_file):
        self.name_of_file = name_of_file
        self.type = "file"

    def __str__(self):
        return f"name:{self.name_of_file}"


class VisualFiles(File):
    """
    A class that contains details of a visual file.
    """
    def __init__(self, name_of_file, weight, content, user):
        super().__init__(name_of_file=name_of_file)
        self.weight = weight
        self.content = content
        self.user = user

    def read(self, user: User) -> [str, None]:
        """
        A function that gets a user, if the user it gets is an administrator or the creator of the file,
        it returns the contents of the file, otherwise it returns None.
        :param user: User details.
        :return: If the user it gets is an administrator or the creator of the file,
        it returns the contents of the file, otherwise it returns None.
        """
        if user.type == "system administrator" or self.user.user_name == user.user_name:
            return self.content
        return None


class Text(VisualFiles):
    """
    Class of text file.
    """
    def __init__(self, name_of_file, weight, content, user):
        super().__init__(name_of_file=name_of_file, weight=weight, content=content, user=user)
        self.type = "Text"

    def count(self, string: str) -> int:
        """
        Count the number of times you sub-string in the content.
        :param string:substring for count.
        :return: The number of times the sub-string appears.
        """
        return self.content.count(string)

    def __str__(self):
        return f"{self.name_of_file}.svg"


class Binary(VisualFiles):
    """
    Class of Binary file.
    """
    def __init__(self, name_of_file, weight, content, user):
        super().__init__(name_of_file=name_of_file, weight=weight, content=content, user=user)


class Image(Binary):
    """
    Class of (Binary) Image file.
    """
    def __init__(self, name_of_file, length_image, width_image, weight, content, user):
        super().__init__(name_of_file=name_of_file, weight=weight, content=content, user=user)
        self. type = "Images"
        self.length = length_image
        self.width = width_image

    def get_dimensions(self) -> list:
        """
        A function that returns the dimensions of the image.
        :return:Length and width of the image in list.
        """
        return[self.length, self.width]

    def __str__(self):
        return f"{self.name_of_file}.img"


class Directory(File):
    """
       Class of Directory file.
       """
    def __init__(self, name_of_directory: str, *files: File):
        super().__init__(name_of_file=name_of_directory)
        self.list_of_file = list(files)

    def __str__(self):
        string = " "
        for i in self.list_of_file:
            string += f"{self.name_of_file}/{i.type}/{i}/\n"
        return string


if __name__ == '__main__':
    first_user = User("Ortal", "1234", "system administrator")
    second_user = User("Or", "12345678", "system administrator")

    first_file = Image("Flower", 10, 9, 4, "The contect of first file", first_user)
    text_file = Text("text_file", 10, "Once upon a time there was a dear little girl, Once", first_user)

    print(first_file.read(first_user))
    print(first_file.get_dimensions())
    print(text_file.count("Once"))
    second_file = Image("apple", 5, 4, 6,  "The contect of second file", second_user)
    directory_of_files = Directory("first_directory", first_file, second_file)
    print(directory_of_files)
