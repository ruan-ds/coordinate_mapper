# ADR-010: Regras de escrita para ADRs do projeto

- Status: Aceito
- Data: 2026-08-05

## Contexto

O projeto utiliza ADRs como documentação técnica de mudança, não como tutoriais. É essencial que qualquer ADR posterior siga um padrão consistente para que seja possível entender rapidamente por que a decisão foi tomada e como ela se conecta à arquitetura existente.

## Decisão

Definir regras fixas para a escrita de ADRs neste repositório:

- O título do arquivo deve ser numerado e descritivo, por exemplo `ADR-010: Regras de escrita para ADRs do projeto`.
- O documento deve começar com um título único em `#`.
- Usar apenas os cabeçalhos `##` para as seções principais: `Contexto`, `Decisão` e `Consequências`.
- Usar `###` apenas para subtópicos dentro dessas seções.
- Evitar `####` ou níveis adicionais em ADRs normais, mas permitir `####` no `ADR-000: Ideias futuras e TODO` para títulos de funcionalidades já implementadas ou sugeridas.
- Registrar somente informações técnicas de mudança e motivação, evitando linguagem de tutorial ou fluxo de usuário passo a passo.
- Incluir, quando apropriado, referências a arquivos de código implementados e outras ADRs relacionadas.
- Manter o estilo conciso e orientado a decisão: `por quê`, `o que mudou`, `impacto`.

## Consequências

- A leitura das ADRs fica mais rápida e previsível.
- Fica mais fácil revisitar decisões antigas e entender o motivo de cada mudança.
- Novas ADRs manterão uma forma consistente, facilitando a manutenção da documentação técnica.
- O repositório terá melhor rastreabilidade entre decisões arquiteturais e implementação de código.

### Observação

Esta ADR também serve como base para revisar e corrigir ADRs existentes que não sigam o padrão. Arquivos fora do padrão devem ser normalizados ao serem atualizados ou sempre que uma mudança de decisão relevante for registrada.
