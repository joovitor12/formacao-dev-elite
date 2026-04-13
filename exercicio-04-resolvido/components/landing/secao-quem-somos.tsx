import { Separator } from "@/components/ui/separator";

export function SecaoQuemSomos() {
  return (
    <section className="rounded-xl border bg-card p-6 text-card-foreground shadow-sm ring-1 ring-foreground/5">
      <h2 className="font-heading text-xl font-semibold tracking-tight">
        Quem somos
      </h2>
      <Separator className="my-4" />
      <p className="text-sm leading-relaxed text-muted-foreground md:text-base">
        Há anos o Zé abre cedo pra quem vai pro trabalho e fecha tarde pra quem
        esqueceu o sal na hora do jantar. Aqui tem de tudo um pouco, fiado na
        confiança pra quem mora perto e sempre um banquinho pra tomar um café.
      </p>
    </section>
  );
}
