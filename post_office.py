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
        }
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
        return [{self.boxes[user_name][i]['title']: self.boxes[user_name][i]['body']}
                for i in range(0, len(self.boxes[user_name]) if n is None else n)]

    def search_inbox(self, user_name: str, string: str) -> list:
        """
        A function that returns a list of messages that contain the string it gets for the user it gets.
        :param user_name:Username for searching his messages.
        :param string:Search string in body and title of messages.
        :return:A list of messages in which the string appears.
        """
        return [{i['title']:i['body']} for i in self.boxes[user_name]if string in i['title'] or string in i['body']]


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
