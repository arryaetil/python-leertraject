import sys, io, json
src, out = sys.argv[1], sys.argv[2]
cards = io.open(f"{src}/cards.js", encoding="utf-8").read()
ex = json.load(io.open(f"{src}/explain.json", encoding="utf-8"))
explain = "const EXPLAIN=" + json.dumps(ex, ensure_ascii=False) + ";\nCARDS.forEach(c=>{c.x=EXPLAIN[c.id]||\"\"});"
page = io.open(f"{src}/shell.html", encoding="utf-8").read().replace("/*CARDS*/", cards).replace("/*EXPLAIN*/", explain)
page = page.replace("\u2013", "-").replace("\u2014", "-")
io.open(out, "w", encoding="utf-8").write(page)
io.open(out.replace(".html", "-preview.html"), "w", encoding="utf-8").write('<!doctype html>\n<html lang="en">\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n' + page + "</html>\n")
print("ok", len(page))
