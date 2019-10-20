# add-on mixin

class Post:
    def __init__(self, author, title, text):
        super().__init__()
        self.author = author
        self.title = title
        self.text = text


class Comment:
    def __init__(self, author, text):
        super().__init__()
        self.author = author
        self.text = text

class VoteMixin:
    def __init__(self):
        self.votes = 0

    def vote_up(self):
        self.votes += 1


class VoteablePost(Post, VoteMixin):
    pass

class VoteableComment(Comment, VoteMixin):
    pass


p = VoteablePost("me", "a title", "its text")
c = VoteableComment("me", "a comment")

for entry in [p, c]:
    entry.vote_up()

print(p.votes)
print(c.votes)


# ------------------------------
# Participant mixin

from abc import ABCMeta, abstractmethod

class Server(metaclass=ABCMeta):
    def listen(self):
        print("listening on connection "+self.connection())

    @abstractmethod
    def connection(self):
        pass


class TCPConnectionMixin:
    def connection(self):
        return "TCP"


class UDPConnectionMixin:
    def connection(self):
        return "UDP"


class TCPServer(TCPConnectionMixin, Server):
    pass

class UDPServer(UDPConnectionMixin, Server):
    pass


tcp = TCPServer()
udp = UDPServer()

tcp.listen()
udp.listen()




