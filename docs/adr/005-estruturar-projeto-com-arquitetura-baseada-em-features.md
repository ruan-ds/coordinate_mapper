# ADR-005: Estruturar o projeto com uma arquitetura baseada em features

- Status: Aceito
- Data: 2026-07-31

## Contexto

O projeto passou por uma fase de crescimento em que a organização inicial começou a ficar pouco clara para manutenção e evolução. Com o aumento da complexidade, tornou-se mais difícil localizar responsabilidades, entender o fluxo de funcionamento e introduzir novas funcionalidades sem impactar partes já existentes.

## Decisão

Reestruturar o projeto para uma arquitetura baseada em features, organizando o código em módulos mais coesos e com responsabilidades mais claras.

A nova organização passou a separar a aplicação em camadas e agrupamentos temáticos, como:

- app para a camada de interface e entrada da aplicação;
- features para encapsular funcionalidades específicas do domínio;
- módulos menores e mais focados, facilitando a compreensão e a evolução incremental.

Essa mudança foi adotada com o objetivo de reduzir o acoplamento entre partes do sistema e tornar o projeto mais sustentável a longo prazo.

A refatoração do `Canvas` em mixins especializados é um exemplo dessa estratégia, transformando-o em um agregador de comportamentos enquanto cada funcionalidade passa a residir em um módulo específico.

## Consequências

- A estrutura do projeto fica mais intuitiva para novos desenvolvedores.
- A manutenção se torna mais simples, pois cada feature possui responsabilidades mais bem definidas.
- A evolução do sistema fica mais segura, porque mudanças podem ser feitas de forma mais localizada.
- O projeto passa a estar melhor preparado para crescer com novas funcionalidades sem perder organização.
