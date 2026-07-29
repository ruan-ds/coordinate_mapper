# ADR-002: Separar módulos por responsabilidade

- Status: Aceito
- Data: 2026-07-28

## Contexto

O projeto começou com uma lógica simples, mas precisava de organização para permanecer compreensível e fácil de evoluir.

## Decisão

Separar a aplicação em módulos independentes:

- main.py para o ponto de entrada
- canvas.py para a interface e interação
- models.py para os modelos de dados
- storage.py para persistência

## Consequências

- Melhora a legibilidade do código.
- Facilita a manutenção e testes futuros.
- Torna a aplicação mais reutilizável em novas features.
