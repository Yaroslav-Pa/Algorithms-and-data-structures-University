import math
from variables1 import exchange_rates
def arbitrage_opportunity(graph):
    currencies = list(graph.keys())
    distances = {currency: 0 for currency in currencies}
    predecessor = {currency: None for currency in currencies}

    for _ in range(len(currencies) - 1):
        for source in currencies:
            for target, rate in graph[source].items():
                if distances[source] + math.log(rate) < distances[target]:
                    distances[target] = distances[source] + math.log(rate)
                    predecessor[target] = source

    for source in currencies:
        for target, rate in graph[source].items():
            if distances[source] + math.log(rate) < distances[target]:
                path = [target, source]
                while predecessor[source] not in path:
                    source = predecessor[source]
                    path.append(source)
                path.reverse()
                return path

    return None

arbitrage_path = arbitrage_opportunity(exchange_rates)

if arbitrage_path:
    print("Можливий арбітражній маршрут:", ' -> '.join(arbitrage_path))
else:
    print("Арбітраж неможливий.")
