import {
  Card,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { produtos } from "@/lib/data/produtos";

export function SecaoDestaques() {
  return (
    <section>
      <h2 className="font-heading text-xl font-semibold tracking-tight">
        Destaques de hoje
      </h2>
      <p className="mt-1 text-sm text-muted-foreground">
        Preços de exemplo — na loja o Zé confirma o valor e a promoção do dia.
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
  );
}
