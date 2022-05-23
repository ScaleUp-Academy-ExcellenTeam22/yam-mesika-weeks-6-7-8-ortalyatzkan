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
        message_details = {
            'id': self.message_id,
            'title': title_of_message,
            'body': message_body,
            'sender': sender,
            'is_read': False,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_message(self, user_name, message):
        """
        A function that returns a message and updates that a message has been read.
        :param user_name:Name of the user who received the message.
        :param message:The message to read.
        :return:The message.
        """
        self.boxes[user_name][message]['is_read'] = True
        return {self.boxes[user_name][message]['title']: self.boxes[user_name][message]['body']}

    def amount_of_messages_read(self, user_name):
        """
        A function that returns the amount of messages that have already been read.
        :param user_name: Name of the user who received the messages.
        :return: The amount of messages that have already been read.
        """
        return sum(1 for message in range(0, len(self.boxes[user_name]))if self.boxes[user_name][message]['is_read'])

    def read_inbox(self, user_name: str, n: int = None) -> list:
        """
        A function that returns the list of messages according to the name it gets.
        :param user_name:
        :param n:The number of first messages returned, if not passed to a function will return all user messages.
        :return:List of messages
        """
        if n >= len(self.boxes[user_name]):
            return[{self.boxes[user_name][message]['title']: self.boxes[user_name][message]['body']}
                   for message in range(0, len(self.boxes[user_name]))]
        return [self.read_message(user_name, message)
                for message in range(0, len(self.boxes[user_name]) if n is None
                else n+self.amount_of_messages_read(user_name))
                if not self.boxes[user_name][message]['is_read'] or n is None]

    def search_inbox(self, user_name: str, text_message: str) -> list:
        """
        A function that returns a list of messages that contain the string it gets for the user it gets.
        :param user_name:Username for searching his messages.
        :param text_message:Search string in body and title of messages.
        :return:A list of messages in which the string appears.
        """
        return [{message['title']:message['body']} for message in self.boxes[user_name]if text_message in message['title'] or text_message in message['body']]


if __name__ == '__main__':
    new_post_office = PostOffice(['Ortal', 'Dana', 'Shir', 'Dan'])
    new_post_office.send_message('Ortal', 'Dana', "Question", "How are you today?", urgent=False)
    new_post_office.send_message('Dana', 'Ortal', "Answer", "I'm feeling good", urgent=False)
    new_post_office.send_message('Ortal', 'Dana', "Question", "Where are you?", urgent=False)
    new_post_office.send_message('Dana', 'Ortal', "Answer", "I'm home", urgent=False)
    new_post_office.send_message('Ortal', 'Dana', "Fire engine location", "Fire station", urgent=False)
    new_post_office.send_message('Dana', 'Ortal', "Answer", "Bye", urgent=False)

    print(new_post_office.read_inbox('Ortal', 1))
    print(new_post_office.read_inbox('Ortal', 2))
    print(new_post_office.read_inbox('Ortal', 10))
