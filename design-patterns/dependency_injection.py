class NetworkConnection:
    def retrieve(self, data):
        print("retrieving "+data)

class UserData:
    def __init__(self):
        self._connection = NetworkConnection()

    def info_for_username(self, username):
        self._connection.retrieve(username)


ud = UserData()
ud.info_for_username("whatever")


# With DI

class UserDataDI:
    def __init__(self, connection):
        self._connection = connection

    def info_for_username(self, username):
        self._connection.retrieve(username)

ud2 = UserDataDI(NetworkConnection())

ud2.info_for_username("whatever2")
