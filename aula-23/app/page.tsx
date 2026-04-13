import {
  Card,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Separator } from "@/components/ui/separator";
import { Button, buttonVariants } from "@/components/ui/button";
import { cn } from "@/lib/utils";

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
    <div className="min-h-svh bg-muted/40">
      <header className="border-b border-border/60 bg-primary text-primary-foreground">
        <div className="mx-auto flex max-w-3xl flex-col items-center px-4 py-12 text-center">
          <h1 className="font-heading text-3xl font-semibold tracking-tight md:text-4xl">
            Barbearia do Seu Ze
          </h1>
          <p className="mt-3 max-w-lg text-sm text-primary-foreground/85 md:text-base">
            Tradição, estilo e atendimento de primeira no coração do bairro.
          </p>
          <div className="mt-8 flex flex-wrap items-center justify-center gap-3">
            <Button variant="secondary" size="lg">
              Agendar horário
            </Button>
            <a
              href="tel:+5500000000000"
              className={cn(
                buttonVariants({ variant: "outline", size: "lg" }),
                "border-primary-foreground/40 bg-transparent text-primary-foreground hover:bg-primary-foreground/10 hover:text-primary-foreground"
              )}
            >
              Ligar
            </a>
          </div>
        </div>
      </header>

      <main className="mx-auto max-w-3xl space-y-10 px-4 py-10">
        <section className="rounded-xl border bg-card p-6 text-card-foreground shadow-sm ring-1 ring-foreground/5">
          <h2 className="font-heading text-xl font-semibold tracking-tight">
            Quem somos
          </h2>
          <Separator className="my-4" />
          <p className="text-sm leading-relaxed text-muted-foreground md:text-base">
            A Barbearia do Seu Ze oferece cortes modernos e clássicos com
            qualidade, bom atendimento e aquele café parceiro enquanto você
            espera.
          </p>
        </section>

        <section>
          <h2 className="font-heading text-xl font-semibold tracking-tight">
            Nossos serviços
          </h2>
          <p className="mt-1 text-sm text-muted-foreground">
            Valores e combinações para você escolher com calma.
          </p>
          <div className="mt-6 grid gap-4 sm:grid-cols-2">
            {servicos.map((s) => (
              <Card key={s.titulo}>
                <CardHeader>
                  <CardTitle>{s.titulo}</CardTitle>
                  <CardDescription>{s.descricao}</CardDescription>
                </CardHeader>
                <CardFooter className="justify-end border-t font-medium text-emerald-700 dark:text-emerald-400">
                  {s.preco}
                </CardFooter>
              </Card>
            ))}
          </div>
        </section>
      </main>

      <footer className="border-t py-8 text-center text-sm text-muted-foreground">
        <p>
          Barbearia do Seu Ze — Rua do Estilo, 123 — Aberto de seg a sáb, das
          9h às 19h
        </p>
      </footer>
    </div>
  );
}
