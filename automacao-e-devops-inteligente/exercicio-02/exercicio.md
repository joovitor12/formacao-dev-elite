# Exercício integrador — Containerização com IA

## Contexto

O time expõe `metrics_exporter.py` via Docker. O **baseline** traz um Dockerfile que **builda e roda**, mas concentra falhas de **revisão, estrutura, geração assistida, multistage, otimização e segurança**.

Sua missão é percorrer o **ciclo completo de containerização profissional** com IA como parceira — e entregar imagem endurecida + **dossiê integrado**.

## Estrutura


| Caminho                    | Quem usa        | Papel                                                      |
| -------------------------- | --------------- | ---------------------------------------------------------- |
| **Raiz** (`exercicio-02/`) | **Facilitador** | Mesmo baseline.                                            |
| `**pre-changes/`**         | **Alunos**      | Cópia idêntica no início — **único lugar para trabalhar**. |


## Onde trabalhar

- **Alunos:** somente `pre-changes/`.
- **Facilitador:** demonstra na **raiz** no mesmo roteiro.

## Objetivo técnico

1. Revisar o baseline e inventariar achados (§1 do dossiê).
2. Reorganizar estrutura do Dockerfile (§2).
3. Usar IA com `especificacao_app.md` para gerar/refinar trechos (§3).
4. Aplicar multistage (§4).
5. Otimizar tamanho e camadas (§5).
6. Endurecer segurança e boas práticas (§6).
7. Validar com `python example.py`, `docker build`, `curl /health` e `python verificar_entrega.py`.

---

 Trabalhe em `pre-changes/` (alunos).

1. Documente cada fase no dossiê **antes** de pular para a próxima.
2. Não commitar segredos em `ENV`/`ARG` no Dockerfile final.
3. Imagem final deve: multistage, USER não-root, HEALTHCHECK, tag fixa slim.

## Critérios de aceite

- [x] `python example.py` verde na pasta de trabalho.
- [x] `docker build` + `curl /health` verdes.
- [ ] Dossiê §1–§6 preenchido.
- [ ] Checklist de entrega com todos `[x]`.
- [ ] `python verificar_entrega.py` retorna **0**.

## Comandos úteis

**Alunos (`pre-changes/`):**

```bash
cd automacao-e-devops-inteligente/exercicio-02/pre-changes
python example.py
python verificar_entrega.py
```

**Docker:**

```bash
docker build -t metrics-exporter:integrador .
docker run --rm -p 8080:8080 metrics-exporter:integrador
curl http://127.0.0.1:8080/health
docker images metrics-exporter:integrador
```

