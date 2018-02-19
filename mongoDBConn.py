import pymongo

class DBConn:
    conn = None
    servers = "mongodb://106.15.224.237:27017"

    def connect(self):
        self.conn = pymongo.Connection(self.servers)

