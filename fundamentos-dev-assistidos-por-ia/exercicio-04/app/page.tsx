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

const produtos = [
  {
    titulo: "Café do dia",
    descricao: "Café coado na hora, forte do jeito que o bairro gosta.",
    preco: "R$ 3,00",
  },
  {
    titulo: "Pão francês (unidade)",
    descricao: "Sai quentinho de manhã e volta à tarde — acaba rápido.",
    preco: "R$ 1,20",
  },
  {
    titulo: "Refrigerante 350 ml",
    descricao: "Gelado na hora, das marcas que a galera sempre pede.",
    preco: "R$ 6,50",
  },
  {
    titulo: "Kit básico do mês",
    descricao: "Arroz, feijão, açúcar e óleo — monte seu kit com o Zé.",
    preco: "A partir de R$ 45,00",
  },
];

export default function Home() {
  return (
    <div className="min-h-svh bg-muted/40">
      <header className="border-b border-border/60 bg-primary text-primary-foreground">
        <div className="mx-auto flex max-w-3xl flex-col items-center px-4 py-12 text-center">
          <h1 className="font-heading text-3xl font-semibold tracking-tight md:text-4xl">
            Vendinha do Seu Zé
          </h1>
          <p className="mt-3 max-w-lg text-sm text-primary-foreground/85 md:text-base">
            Mercearia de bairro: produto fresco, preço justo e aquele papo bom
            na porta.
          </p>
          <div className="mt-8 flex flex-wrap items-center justify-center gap-3">
            <Button variant="secondary" size="lg">
              Pedir pelo WhatsApp
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
            Há anos o Zé abre cedo pra quem vai pro trabalho e fecha tarde pra
            quem esqueceu o sal na hora do jantar. Aqui tem de tudo um pouco,
            fiado na confiança pra quem mora perto e sempre um banquinho pra
            tomar um café.
          </p>
        </section>

        <section>
          <h2 className="font-heading text-xl font-semibold tracking-tight">
            Destaques de hoje
          </h2>
          <p className="mt-1 text-sm text-muted-foreground">
            Preços de exemplo — na loja o Zé confirma o valor e a promoção do
            dia.
          </p>
          <div className="mt-6 grid gap-4 sm:grid-cols-2">
            {produtos.map((p) => (
              <Card key={p.titulo}>
                <CardHeader>
                  <CardTitle>{p.titulo}</CardTitle>
                  <CardDescription>{p.descricao}</CardDescription>
                </CardHeader>
                <CardFooter className="justify-end border-t font-medium text-amber-800 dark:text-amber-400">
                  {p.preco}
                </CardFooter>
              </Card>
            ))}
          </div>
        </section>
      </main>

      <footer className="border-t py-8 text-center text-sm text-muted-foreground">
        <p>
          Vendinha do Seu Zé — Rua das Flores, 45 — Aberto todos os dias, das
          6h30 às 21h
        </p>
      </footer>
    </div>
  );
}
