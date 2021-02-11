class Node(object):
    def __init__(self, data = None, next = None):
        self.data_ = data
        self.next_ = next
    
    def set_data(self):
        self.data_ = data

    def get_data(self):
        return self.data_

    def set_next(self):
        self.next_ = next
    
    def get_next(self):
        return self.next_

    def __str__(self):
        return str(self.data_)