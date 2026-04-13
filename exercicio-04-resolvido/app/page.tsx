import { SecaoDestaques } from "@/components/landing/secao-destaques";
import { SecaoQuemSomos } from "@/components/landing/secao-quem-somos";
import { SiteFooter } from "@/components/landing/site-footer";
import { SiteHeader } from "@/components/landing/site-header";

export default function Home() {
  return (
    <div className="min-h-svh bg-muted/40">
      <SiteHeader />
      <main className="mx-auto max-w-3xl space-y-10 px-4 py-10">
        <SecaoQuemSomos />
        <SecaoDestaques />
      </main>
      <SiteFooter />
    </div>
  );
}
