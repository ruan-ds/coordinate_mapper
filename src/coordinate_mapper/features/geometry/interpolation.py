def interpolate_points(
    start,
    end,
    count,
    density=100
):
    """
    Gera pontos interpolados entre dois pontos.

    Args:
        start: ponto inicial
        end: ponto final
        count: quantidade de pontos internos
        density:
            100 = distribuição normal
            <100 = aproxima pontos do centro
            >100 = afasta pontos do centro

    Returns:
        Lista de tuplas (x, y)
    """

    if count <= 0:
        return []


    # limita densidade para evitar extrapolação excessiva
    density = max(
        1,
        density
    )


    points = []


    for i in range(1, count + 1):

        # interpolação normal
        factor = i / (count + 1)


        # distância relativa ao centro (0.5)
        offset = factor - 0.5


        # aplica densidade simetricamente
        offset *= density / 100


        # retorna ao eixo normalizado
        factor = 0.5 + offset


        # impede sair dos limites
        factor = max(
            0,
            min(1, factor)
        )


        x = int(
            start.x +
            (end.x - start.x) * factor
        )

        y = int(
            start.y +
            (end.y - start.y) * factor
        )


        points.append(
            (x, y)
        )


    return points