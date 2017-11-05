
'''
Abstract class that defines the behaviour for classes wanting to output message.
'''
class outputter:
    def write(self, message):
        raise NotImplementedError("Please Implement this method")