const servicos = [
  {
    titulo: "Corte Masculino",
    descricao:
      "Corte personalizado de acordo com seu estilo e formato de rosto.",
    preco: "R$ 35,00",
  },
  {
    titulo: "Barba Completa",
    descricao: "Modelagem, alinhamento e acabamento com navalha.",
    preco: "R$ 30,00",
  },
  {
    titulo: "Corte + Barba",
    descricao: "Pacote completo para sair no estilo e economizar.",
    preco: "R$ 60,00",
  },
  {
    titulo: "Sobrancelha",
    descricao: "Acabamento discreto e natural para destacar seu olhar.",
    preco: "R$ 15,00",
  },
];

export default function Home() {
  return (
    <>
      <header>
        <h1>Barbearia do Seu Ze</h1>
        <p>Tradição, estilo e atendimento de primeira no coração do bairro.</p>
      </header>

      <main>
        <section>
          <h2>Quem somos</h2>
          <p>
            A Barbearia do Seu Ze oferece cortes modernos e clássicos com
            qualidade, bom atendimento e aquele café parceiro enquanto você
            espera.
          </p>
        </section>

        <section>
          <h2>Nossos serviços</h2>
          <div className="servicos">
            {servicos.map((s) => (
              <article key={s.titulo} className="card">
                <h3>{s.titulo}</h3>
                <p>{s.descricao}</p>
                <p className="preco">{s.preco}</p>
              </article>
            ))}
          </div>
        </section>
      </main>

      <footer>
        <p>
          Barbearia do Seu Ze - Rua do Estilo, 123 - Aberto de seg a sab, das
          9h as 19h
        </p>
      </footer>
    </>
  );
}
