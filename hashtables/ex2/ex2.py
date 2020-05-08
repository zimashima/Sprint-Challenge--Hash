#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    hash_ticket = { i.source: i.destination for i in tickets}
    route = ['NONE'] * (length+1)
    
    for i in range(0,length):
        if route[i] in hash_ticket:
            route[i+1] = hash_ticket[route[i]]

    route.pop(0)
    
    return route
