from sys import stdin as s

ticket_number = int(s.readline().strip())
tickets = sorted(map(int, s.readline().split()))

def get_my_ticket_number(tickets):
    expected = 1
    for ticket in tickets:
        if ticket == expected:
            expected += 1
        else:
            return expected
    return expected

print(get_my_ticket_number(tickets))