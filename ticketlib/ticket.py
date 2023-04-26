import random

def generate_ticket():
    ticket_number = f'TICKET-{random.randint(10000, 99999)}'
    return ticket_number