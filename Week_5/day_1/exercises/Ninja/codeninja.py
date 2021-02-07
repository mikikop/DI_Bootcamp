class Phone:
    """docstring for Phone"""
    def __init__(self, number):
        super(Phone, self).__init__()
        self.number = number
        self.call_history = []
        self.messages = []
        self.message_dict = {}
    
    def call(self, other_phone):
        self.call_history.append(other_phone)
    
    def show_call_history(self):
        print("here the list of the call history: \n")
        for call in call_history:
            print(call)

def send_messages(self,to,fromwho, content):
    self.message_dict = {"to":to,"fromwho":fromwho,"content":content}
        print(self.message_dict)

    def show_outgoing_messages(self):
        print(self.message_dict)

def show_incoming_messages(self):
    print(self.messages)
    
    def show_messages_from(self, number):
        print(f"here the list of the message from the number {number}")
        for message in self.message_dict:
            if message["fromwho"] == number:
                print(self.message_dict["content"])
            else:
                print("there are no message from this number")


number1 = Phone("0526226956")
number2 = Phone("0543331226")

number1.send_messages("0543331226","0526226956","Hello")

number2.show_messages_from("0526226956")

