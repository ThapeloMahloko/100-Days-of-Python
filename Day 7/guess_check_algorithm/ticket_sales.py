"""
Ticket Sales Problem

Alyssa, Ben, and Cindy are selling tickets to a fundraiser.
Ben sells 2 fewer than Alyssa.
Cindy sells twice as many as Alyssa.
10 total tickets were sold by the three people.
How many did Alyssa sell?
"""
 
def ticket_sales():
    total_tickets = 10  # Total tickets sold
    for alyssa_tickets in range(total_tickets + 1):  # Possible tickets Alyssa could sell
        ben_tickets = alyssa_tickets - 2  # Ben sells 2 fewer than Alyssa
        cindy_tickets = alyssa_tickets * 2  # Cindy sells twice as many as Alyssa
        
        # Check if the total tickets sold matches the given total
        if ben_tickets >= 0 and cindy_tickets >= 0 and (alyssa_tickets + ben_tickets + cindy_tickets) == total_tickets:
            print(f"Alyssa sold {alyssa_tickets} tickets.")
            print(f"Ben sold {ben_tickets} tickets.")
            print(f"Cindy sold {cindy_tickets} tickets.")
            break  # Stop once the solution is found

if __name__ == "__main__":
    ticket_sales()
