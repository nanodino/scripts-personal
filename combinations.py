import itertools

GLOBAL_INDEPENDENTS = ['LCRTX', 'NAC', 'ACRTX', 'DMS', 'MCRTX', "DLS", "VM"]
BAR_MOUTHING_INDEPENDENTS_ONLY = [
    'MD', 'VAL', 'SNR', 'STN', 'HOUSING', 'STRAIN']
ROUTE_TRACING_INDEPENDENTS_ONLY = ['NAC', 'ACRTX',
                                   'DMS', 'DLS', 'VM', 'HOUSING', 'STRAIN']

ALL_BAR_MOUTHING = set(GLOBAL_INDEPENDENTS + BAR_MOUTHING_INDEPENDENTS_ONLY)
ALL_ROUTE_TRACING = set(GLOBAL_INDEPENDENTS + ROUTE_TRACING_INDEPENDENTS_ONLY)


def generate_combinations(behaviour_array, filename):
    MODELS = []
    MAX_LENGTH = len(behaviour_array)
    for i in range(MAX_LENGTH):
        modelsOfLength = list(itertools.combinations(behaviour_array, i))
        for model in modelsOfLength:
            MODELS.append(model)

    with open(filename, 'w') as f:
        print(MODELS, file=f)


route_tracing_combinations = generate_combinations(
    ALL_ROUTE_TRACING, 'route_tracing.txt')
bar_mouthing_combinations = generate_combinations(
    ALL_BAR_MOUTHING, 'bar_mouthing.txt')
