import { siteFooterLine } from "@/lib/site";

export function SiteFooter() {
  return (
    <footer className="border-t py-8 text-center text-sm text-muted-foreground">
      <p>{siteFooterLine}</p>
    </footer>
  );
}
