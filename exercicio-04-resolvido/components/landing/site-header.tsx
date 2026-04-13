import { Button, buttonVariants } from "@/components/ui/button";
import { site } from "@/lib/site";
import { cn } from "@/lib/utils";

export function SiteHeader() {
  return (
    <header className="border-b border-border/60 bg-primary text-primary-foreground">
      <div className="mx-auto flex max-w-3xl flex-col items-center px-4 py-12 text-center">
        <h1 className="font-heading text-3xl font-semibold tracking-tight md:text-4xl">
          {site.name}
        </h1>
        <p className="mt-3 max-w-lg text-sm text-primary-foreground/85 md:text-base">
          {site.headerTagline}
        </p>
        <div className="mt-8 flex flex-wrap items-center justify-center gap-3">
          <Button variant="secondary" size="lg">
            Pedir pelo WhatsApp
          </Button>
          <a
            href={`tel:${site.phoneTelHref}`}
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
  );
}
