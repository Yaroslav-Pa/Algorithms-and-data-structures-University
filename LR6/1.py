import math

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


exchange_rates = {
    'USD': {'EUR': 0.9, 'GBP': 0.8, 'JPY': 110, 'AUD': 1.3, 'CAD': 1.2},
    'EUR': {'USD': 1.1, 'GBP': 0.9, 'JPY': 120, 'AUD': 1.4, 'CAD': 1.3},
    'GBP': {'USD': 1.2, 'EUR': 1.1, 'JPY': 130, 'AUD': 1.5, 'CAD': 1.4},
    'JPY': {'USD': 0.009, 'EUR': 0.008, 'GBP': 0.0077, 'AUD': 0.011, 'CAD': 0.01},
    'AUD': {'USD': 0.77, 'EUR': 0.71, 'GBP': 0.67, 'JPY': 90, 'CAD': 0.91},
    'CAD': {'USD': 0.83, 'EUR': 0.77, 'GBP': 0.73, 'JPY': 100, 'AUD': 1.1},
}



arbitrage_path = arbitrage_opportunity(exchange_rates)

if arbitrage_path:
    print("Можливий арбітражній маршрут:", ' -> '.join(arbitrage_path))
else:
    print("Арбітраж неможливий.")
