class Message:
    def __init__(self, message_id: int, sender: str, title_of_message: str, message_body: str):
        """
        The constructor of Message class.
        :param message_id:The id of message.
        :param sender:The name of sender.
        :param title_of_message:The title of message.
        :param message_body:The body of message.
        """
        self.id = message_id
        self.title = title_of_message
        self.body = message_body
        self.sender = sender

    def __str__(self):
        """
        A function that returns the title and body of the message for the print function.
        :return: The title and body of the message.
        """
        return f'title: {self.title}, body: {self.body}'

    def __len__(self) -> int:
        """
        A function that returns the length of the string of the message body.
        :return:The length of the string of the message body.
        """
        return len(self.body)

    __repr__ = __str__


class PostOffice:
    """A Post Office class. Allows users to message each other.
    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.
    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, title_of_message, message_body, urgent=False):
        """Send a message to a recipient.
        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param title_of_message:The title of the message.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = Message(self.message_id, title_of_message, message_body, sender)
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, user_name: str, n: int = None) -> list:
        """
        A function that returns the list of messages according to the name it gets.
        :param user_name:
        :param n:The number of first messages returned, if not passed to a function will return all user messages.
        :return:List of messages
        """
        return [{self.boxes[user_name][i]}
                for i in range(0, len(self.boxes[user_name]) if n is None else n)]

    def search_inbox(self, user_name: str, string: str) -> list:
        """
        A function that returns a list of messages that contain the string it gets for the user it gets.
        :param user_name:Username for searching his messages.
        :param string:Search string in body and title of messages.
        :return:A list of messages in which the string appears.
        """
        return [str(i) for i in self.boxes[user_name]if string in i.title or string in i.body]


if __name__ == '__main__':
    new_post_office = PostOffice(['Ortal', 'Dana', 'Shir', 'Dan'])
    new_post_office.send_message('Ortal', 'Dana', "Question", "How are you today?", urgent=False)
    new_post_office.send_message('Dana', 'Ortal', "Answer", "I'm feeling good", urgent=False)
    new_post_office.send_message('Ortal', 'Dana', "Question", "Where are you?", urgent=False)
    new_post_office.send_message('Dana', 'Ortal', "Answer", "I'm home", urgent=False)
    new_post_office.send_message('Ortal', 'Dana', "Fire engine location", "Fire station", urgent=False)

    print(new_post_office.read_inbox('Ortal', 1))
    print(new_post_office.read_inbox('Dana'))
    print(new_post_office.search_inbox('Dana', 'tion'))
    new_message = Message(0, "Ortal", "Title", "Hello world!")
    print(len(new_message))
    print(new_message)
