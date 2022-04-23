class File:
    def __init__(self, name_of_file):
        self.name_of_file = name_of_file

    def __str__(self):
        return f"name:{self.name_of_file}"


class VisualFiles(File):
    def __init__(self, weight, content, user,type_of_file):
        self.weight = weight
        self.content = content
        self.user = user
        self.type = type_of_file

    def read(self, user):
        if user.type == "system administrator" or user.type == "file creator":
            return self.content
        return None


class Text(VisualFiles):
    def __init__(self, weight, content, user, type_of_file):
        super().__init__(weight=weight, content=content, user=user, type_of_file=type_of_file)

    def count(self, string):
        return self.content.count(0, len(self.content))

    def __str__(self):
        return f"name:{self.name_of_file}.svg"


class Binary(VisualFiles):
    def __init__(self,weight, content, user, type_of_file):
        super().__init__(weight=weight, content=content, user=user, type_of_file=type_of_file)


class Image(Binary):
    def __init__(self,length_image, width_image,weight, content, user, type_of_file):
        super().__init__( weight=weight, content=content, user=user, type_of_file=type_of_file)
        self.length = length_image
        self.width = width_image

    def get_dimensions(self):
        return[self.length,self.width]

    def __str__(self):
        return f"name:{self.name_of_file}.img"


class User:
    def __init__(self,user_name, user_password,type_of_user):
        self.user = user_name
        self.password = user_password
        self.type = type_of_user


class Directory(File):
    def __init__(self, name_of_directory: str, content, user, type_of_file, *files: File):
        super().__init__(content=content, user=user, type_of_file=type_of_file)
        self.list_of_file = list(files)
        self.name = name_of_directory

    def __str__(self):
        str = f"{self.name}\n"
        for i in self.list_of_file:
            str += f"|\n|\n--{i}"
        return str

if __name__ == '__main__':
    first_user = User("Ortal","1234","system administrator")
    second_user = User("Shira","12345678","system administrator")

    first_file = Image(3,10,9,"ddddd",first_user,"img")
    second_file=Image(10,5,4,"ppppp",second_user,"img")
    directory_of_files = Directory("first_directory","kkkk",first_user,"dir",first_file,second_file)
    print(directory_of_files)

