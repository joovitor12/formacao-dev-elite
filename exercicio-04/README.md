# Exercício 04 — Refatoração multi-arquivo com agente (Cursor)

## Contexto

Este projeto é uma landing page fictícia da **Vendinha do Seu Zé**: mercearia de bairro com lista de produtos em destaque. Hoje quase tudo vive em um único arquivo (`app/page.tsx`): dados em linha, marcação repetida de seções e textos de contato espalhados no JSX.

Esse formato é comum no começo de um protótipo, mas dificulta evolução, testes e trabalho em equipe. O objetivo deste exercício é **reorganizar o código em vários arquivos com responsabilidades claras**, usando o **Agente do Cursor** para executar a maior parte das mudanças (você dirige; o agente implementa).

## Objetivo de aprendizagem

- Praticar **extração de módulos**: tipos, dados estáticos e componentes de UI.
- Ganhar fluência em **pedidos ao agente** (escopo, passos, critérios de aceite).
- Manter **paridade visual e de comportamento** antes e depois da refatoração.

## Enunciado (o que fazer)

Refatore a aplicação para que `app/page.tsx` **apenas componha** a página: importar dados constantes, importar componentes de seção e montar a árvore com pouca lógica e pouco JSX “denso”.

Implemente, no mínimo, a seguinte organização (nomes podem variar um pouco, mas as responsabilidades devem existir):

| Responsabilidade | Onde colocar (sugestão) |
| ---------------- | ------------------------ |
| Tipo do item de produto (título, descrição, preço) | `types/produto.ts` (ou `lib/types/produto.ts`) |
| Lista `produtos` (array exportado) | `lib/data/produtos.ts` (ou `data/produtos.ts`) |
| Textos reutilizáveis da loja (nome, endereço, horário, telefone fictício, etc.) | `lib/site.ts` ou `config/site.ts` — objeto ou constantes nomeadas |
| Cabeçalho (título, subtítulo, botões WhatsApp / Ligar) | `components/landing/site-header.tsx` |
| Seção “Quem somos” | `components/landing/secao-quem-somos.tsx` |
| Seção “Destaques de hoje” (título, texto auxiliar, grid de cards) | `components/landing/secao-destaques.tsx` |
| Rodapé | `components/landing/site-footer.tsx` |

Regras:

1. **Não altere o significado** dos textos nem o layout esperado (classes Tailwind e estrutura visual devem permanecer equivalentes).
2. O **componente de página** (`app/page.tsx`) deve ficar **enxuto**: idealmente só imports, o `export default function Home` e JSX de alto nível (header, main com seções, footer).
3. **Imports** devem usar o alias `@/` já configurado no projeto, como no código atual.
4. **Não** mova os componentes prontos de `components/ui/*` (Card, Button, etc.) — continue usando-os nos novos componentes de landing.

## Como usar o agente do Cursor

1. Abra o **Chat do Agent** (modo que pode editar arquivos), não só o chat de pergunta/resposta.
2. Comece com um pedido **estruturado**, por exemplo:
   - “Leia `app/page.tsx`. Extraia o array `produtos` para `lib/data/produtos.ts` com tipo em `types/produto.ts`. Atualize os imports. Não mude classes CSS nem textos.”
3. Depois, em **passos menores** (um ou dois por vez): extrair cabeçalho, depois seções, depois rodapé, depois constantes do site.
4. Sempre peça explicitamente: **“rode o linter / corrija erros de TypeScript”** se algo quebrar.
5. Se o agente sugerir renomear demais ou “melhorar” UI, **recuse** o que foge do escopo — o foco é arquitetura de arquivos, não redesign.

Boas práticas de prompt: citar caminhos de arquivo, pedir lista de arquivos criados/alterados ao final, e pedir que a página continue compilando.

## Definição de concluído (DoD)

O exercício está **concluído** quando **todos** os itens abaixo forem verdadeiros:

### Estrutura e arquivos

- [ ] Existem os arquivos de **tipo**, **dados** e **site/config** conforme a tabela do enunciado (ou equivalente documentado no PR/commit).
- [ ] Existem **pelo menos quatro** componentes em `components/landing/` (ou pasta equivalente) cobrindo header, “Quem somos”, destaques e footer.
- [ ] `app/page.tsx` **não** contém mais o array `produtos` inline nem blocos grandes de JSX de seção — apenas composição.

### Qualidade e paridade

- [ ] A página, ao rodar em desenvolvimento, está **visualmente e funcionalmente equivalente** à versão original (mesmos textos, mesmos links `tel:` e botões, mesma grade de cards).
- [ ] **TypeScript** sem erros nos arquivos tocados.
- [ ] **ESLint** do projeto passa (`npm run lint` ou o comando equivalente do seu `package.json`).

### Processo (entrega pedagógica)

- [ ] Você registrou **em 3–5 linhas** (no corpo do PR, comentário da entrega ou arquivo indicado pelo instrutor) **como** usou o agente: 1) primeiro prompt; 2) principal dificuldade; 3) o que ajustou manualmente, se houver.

---

**Observação para o instrutor:** o repositório local deste exercício deve incluir `package.json` e scripts de lint/build usuais de Next.js; se estiverem ausentes, restaure-os antes da turma começar, para que o DoD de lint/build seja verificável.
