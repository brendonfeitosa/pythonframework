def calc_media(*args):
    return sum(args) / len(args)

def calc_media_pond(notas, pesos):
    return sum(n * p for n, p in zip(notas, pesos)) / sum(pesos)