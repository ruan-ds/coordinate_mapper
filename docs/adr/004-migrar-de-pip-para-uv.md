# ADR-004: Migrar de pip para uv

- Status: Aceito
- Data: 2026-07-31

## Contexto

O projeto precisava de um fluxo de desenvolvimento mais simples e consistente para gerenciar dependências e ambientes Python. O uso de pip, embora funcional, exigia mais passos manuais e não oferecia uma experiência tão integrada para instalação, sincronização e execução do projeto.

## Decisão

Adotar uv como ferramenta principal para gestão de dependências e execução do ambiente do projeto.

A migração inclui:

- substituir o fluxo baseado em venv e pip por comandos com uv;
- usar uv sync para criar e sincronizar o ambiente a partir do arquivo de configuração do projeto;
- executar a aplicação com uv run, reduzindo a necessidade de ativação manual de ambientes virtuais.

## Consequências

- O processo de configuração do ambiente fica mais rápido e menos propenso a erros manuais.
- O projeto passa a ter um fluxo mais moderno e padronizado para desenvolvimento e execução.
- A manutenção futura se torna mais simples, especialmente em ambientes compartilhados ou em integração contínua.
