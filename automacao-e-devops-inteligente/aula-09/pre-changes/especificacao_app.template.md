# Especificação da app — template

> **Como usar:** copie este arquivo para `especificacao_app.md`, preencha cada seção com dados **reais** da sua aplicação e referencie-o nos prompts de geração do Dockerfile (`@especificacao_app.md`).

## Identificação

- Nome do serviço: <!-- ex.: metrics-exporter -->
- Descrição em uma linha: <!-- ex.: HTTP mínimo de health e métricas -->

## Runtime

- Linguagem / versão: <!-- ex.: Python 3.12+ -->
- Entry point: <!-- ex.: python app.py — módulo/função principal -->
- Variáveis de ambiente relevantes: <!-- ex.: PORT, HOST, LOG_LEVEL — ou "nenhuma" -->

## Rede

- Porta padrão: <!-- ex.: 8080 -->
- Porta configurável? <!-- sim (env `___`) / não -->
- Host de bind: <!-- ex.: 0.0.0.0 em container -->
- Protocolo: <!-- ex.: HTTP -->

## Endpoints / contrato (se aplicável)

| Método | Rota | Resposta esperada |
|--------|------|-------------------|
| | | |
| | | |

<!-- Serviços sem HTTP: descreva fila, job, CLI ou health check alternativo. -->

## Dependências

- Arquivo de deps: <!-- ex.: requirements.txt, package.json, go.mod -->
- Pacotes principais: <!-- liste ou "stdlib / nenhum externo" -->
- Comando de instalação: <!-- ex.: pip install -r requirements.txt -->

## Restrições desejadas na imagem

Preencha o que o time exige — a IA usa isto como critério de aceite.

- Imagem base: <!-- ex.: python:3.12.x-slim — tag fixa, sem latest -->
- Usuário do processo: <!-- ex.: não-root -->
- Forma do `CMD` / `ENTRYPOINT`: <!-- ex.: exec form (JSON array) -->
- Health check: <!-- rota/comando — use ferramenta já presente na imagem -->
- Estratégia de `COPY`: <!-- seletivo — listar o que entra e o que fica de fora -->
- Segredos: <!-- ex.: nunca em ENV/ARG do Dockerfile; injetar no deploy -->
- Outras políticas: <!-- ex.: multi-stage, tamanho máximo, distroless -->

## Contexto de build

Arquivos **incluir** na imagem:

- 
- 

Arquivos **excluir** da imagem (smoke test, docs, configs locais):

- 
- 

Diretório de build: <!-- ex.: raiz do serviço / subpasta api/ -->

## Validação esperada

Como confirmar que a imagem está correta após `docker build`:

```bash
# Cole os comandos que você rodará (build, run, curl, testes)
```

## Observações para a IA (opcional)

<!-- Restrições extras, ambientes (dev/staging/prod), orquestrador (K8s, ECS), etc. -->
