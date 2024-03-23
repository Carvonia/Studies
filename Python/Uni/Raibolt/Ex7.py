# Por: Matheus Cunha Nogueira - 06004493
TicketsTotal = 0
TotalTicketsSold = 0
Tickets90P = 0
TotalGames = 4

for Game in range(1, TotalGames + 1):
    AvailableTickets = int(input(f"Informe o total de ingressos disponíveis para o jogo{Game}: "))
    SoldTickets = int(input(f"Agora, informe o número de ingressos que foram vendidos para o mesmo jogo: "))

    TicketsTotal += AvailableTickets
    TotalTicketsSold += SoldTickets

    if SoldTickets >= 0.9 * AvailableTickets:
        Tickets90P += 1


NotSold = TicketsTotal - TotalTicketsSold

print("Total de ingressos disponíveis durante a Copa:", TicketsTotal)
print("Total de ingressos que foram vendidos durante a Copa:", TotalTicketsSold)
print("Total de ingressos que não foram vendidos durante a Copa:", NotSold)
print("Total de jogos com a venda de ingressos acima de 90%:", Tickets90P)