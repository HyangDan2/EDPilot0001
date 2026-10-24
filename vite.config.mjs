import { resolve } from 'node:path';
import { readdirSync } from 'node:fs';
import { defineConfig } from 'vite';

const root = process.cwd();
function htmlFiles(folder) {
  return readdirSync(resolve(root, folder), { withFileTypes: true }).flatMap((entry) => {
    const path = `${folder}/${entry.name}`;
    return entry.isDirectory()
      ? htmlFiles(path)
      : entry.isFile() && entry.name.endsWith('.html')
        ? [path]
        : [];
  });
}

const pages = [
  ...readdirSync(root, { withFileTypes: true })
    .filter((entry) => entry.isFile() && entry.name.endsWith('.html'))
    .map((entry) => entry.name),
  ...['chapters', 'labs', 'appendix'].flatMap(htmlFiles)
].sort();

if (pages.length !== 17) {
  throw new Error(`Expected 17 public HTML pages, found ${pages.length}`);
}

export default defineConfig({
  base: '/EDPilot0001/',
  publicDir: false,
  build: {
    outDir: 'dist',
    emptyOutDir: true,
    rollupOptions: {
      input: Object.fromEntries(
        pages.map((page) => [page.replaceAll('/', '-').replace(/\.html$/, ''), resolve(root, page)])
      )
    }
  }
});
