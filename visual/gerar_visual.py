#!/usr/bin/env python3
"""refazvideo p-7yeArMIQ0 (22/10/2026): "7 repositórios grátis que fazem do Claude um estúdio de vídeo".
Modo clipes + visual melhorado: capa Codex, diagrama próprio do "como funciona", abertura por repositório
(imagem Codex + REPO n DE 7), prints atuais do GitHub, terminal/chat/contador nossos.
Trechos do autor (propaganda 228–247 s, inscreva-se 288–294 s, PDF 396 s+) ficam de fora.
Grava visual/pt-b01.json e clips/lista.json."""
import json
from pathlib import Path

O = Path(__file__).resolve().parent.parent
CL = O / "clips"
M = O / "media"
LISTA = []


def c(at, a, b, **kw):
    nome = f"c_{a:06.1f}_{b:06.1f}.mp4"
    LISTA.append([a, b, nome])
    d = {"type": "media", "at": at, "src": str(CL / nome), "focus": [0.5, 0.5], "zoom": [1.0, 1.0]}
    d.update(kw)
    return d


def st(at, txt, **kw):
    d = {"type": "statement", "at": at, "text": txt}
    d.update(kw)
    return d


def hook(at, n, titulo, sub=None):
    d = {"type": "hook", "at": at, "kicker": f"REPO {n} DE 7", "text": titulo, "src": str(M / f"rp{n}.png"), "size": 84}
    if sub:
        d["sub"] = sub
    return d


def gh(at, n, label, hl=None, **kw):
    d = {"type": "media", "at": at, "src": str(M / "gh" / f"r{n}.png"), "focus": [0.5, 0.35], "zoom": [1.0, 1.12],
         "label": label, "calm": True}
    if hl:
        d["highlights"] = hl
    d.update(kw)
    return d


S = {
 "1": [
   {"type": "hook", "at": "@start", "src": str(M / "capa.png"), "scrim": False},
   c("Aqueles vídeos", 0.5, 9),
   c("Muita gente fez", 24, 32.5),
   c("então o texto", 32.5, 36),
   c("E está tudo", 37.5, 47.5),
   {"type": "etapas", "at": "Neste vídeo eu", "titulo": "OS 7 REPOSITÓRIOS",
    "itens": ["awesome-opus5-5-videos", "opus-video-prompts", "mg-styles-15", "lemo-opuscar",
              "ClaudeAnimationBase", "dupla P(doom)", "awesome-claude-5-5-videos"],
    "atual": 1, "sub": "no fim: por onde eu começaria", "sub_at": "e no fim"},
 ],
 "2": [
   {"type": "diagrama", "at": "Primeiro, como funciona",
    "nos": [
      {"id": "pr", "label": "SEU PROMPT", "icon": "chat", "sub": "uma frase", "x": 0.1, "y": 0.22, "at": "Primeiro, como funciona"},
      {"id": "cc", "label": "CLAUDE CODE", "forma": "nucleo", "x": 0.42, "y": 0.22, "at": "O Claude não gera"},
      {"id": "pg", "label": "PÁGINA WEB", "icon": "code", "sub": "desenha cada quadro", "x": 0.8, "y": 0.22, "at": "uma página web"},
      {"id": "ch", "label": "CHROME", "icon": "image", "sub": "foto de cada quadro", "x": 0.8, "y": 0.78, "at": "O Chrome tira"},
      {"id": "ff", "label": "FFMPEG", "icon": "gear", "sub": "junta os quadros", "x": 0.42, "y": 0.78, "at": "o FFmpeg"},
      {"id": "mp4", "label": "MP4", "icon": "video", "x": 0.1, "y": 0.78, "at": "num MP4"}],
    "ligacoes": [
      {"de": "pr", "para": "cc", "at": "O Claude não gera"},
      {"de": "cc", "para": "pg", "at": "uma página web"},
      {"de": "pg", "para": "ch", "at": "O Chrome tira"},
      {"de": "ch", "para": "ff", "at": "o FFmpeg"},
      {"de": "ff", "para": "mp4", "at": "num MP4"}],
    "passos": [
      {"at": "arquivo de vídeo", "estado": {"cc": "ativo"}, "nota": {"no": "cc", "texto": "não sai vídeo: sai **código**"}},
      {"at": "desenha cada quadro", "pacote": {"de": "cc", "para": "pg", "texto": "HTML + JS"}},
      {"at": "uma foto de", "pacote": {"de": "pg", "para": "ch", "texto": "quadro a quadro"}},
      {"at": "junta tudo", "pacote": {"de": "ch", "para": "ff", "texto": "PNGs"}},
      {"at": "num MP4", "estado": {"mp4": "ok"}},
      {"at": "Você precisa de", "foco": ["ch", "ff"], "nota": {"no": "ff", "texto": "Node, Chrome e FFmpeg: **grátis**"}},
      {"at": "do Claude Code", "foco": "cc", "nota": {"no": "cc", "texto": "Claude Code: **plano pago**"}},
      {"at": "E aqui no", "foco": "todos", "nota": {"no": "mp4", "texto": "nossos vídeos: **o mesmo caminho**"}}]},
 ],
 "3": [
   hook("Número um", 1, "**awesome**-opus5-5-videos", "a maior coleção"),
   gh("Passa de nove", 1, "github · **awesome-opus5-5-videos**"),
   {"type": "counter", "at": "setecentos e três",
    "items": [{"value": 703, "label": "prompts", "at": "setecentos e três"},
              {"value": 9.2, "decimals": 1, "suffix": " mil", "label": "estrelas", "at": "cada um com"}]},
   c("separados em", 84, 93),
   c("O uso é", 96, 102),
 ],
 "4": [
   hook("Número dois", 2, "**opus**-video-prompts", "o prompt de uma linha"),
   c("A página é", 103, 109.5),
   c("São cinquenta e", 111, 114.5),
   {"type": "terminal", "at": "E tem o", "title": "um prompt, uma linha",
    "lines": [{"type": "comment", "text": "o prompt inteiro:", "at": "E tem o"},
              {"type": "cmd", "text": "make a modern slick and punchy video", "at": "de uma linha"},
              {"type": "cmd", "text": "for a modern startup that works on inference", "at": "uma startup de"},
              {"type": "out", "text": "≈ 1 min · ≈ US$ 2 (relato do criador)", "at": "O criador relata"}]},
   st("Então comece assim", "**Uma frase** + o seu tema"),
 ],
 "5": [
   hook("Número três", 3, "**15** estilos de motion", "filme + prompt + código"),
   c("Cada um é", 132.3, 140),
   c("Cidade isométrica", 140, 147),
   c("Para deixar com", 152, 158.5),
   c("O resto segura", 158.5, 161),
   c("E a melhor dica", 162, 169.5),
 ],
 "6": [
   hook("Número quatro", 4, "**lemo**-opuscar", "o que eu usaria primeiro"),
   gh("É uma skill", 4, "github · **lemo-opuscar**"),
   c("Aquarela, nanquim", 221.5, 227.5),
   {"type": "terminal", "at": "Você instala com", "title": "instalar a skill",
    "lines": [{"type": "cmd", "text": "claude plugin marketplace add lemomo-ai/lemo-opuscar", "at": "Você instala com"},
              {"type": "cmd", "text": "claude plugin install lemo-opuscar@lemolab", "at": "dois comandos"}]},
   {"type": "chat", "at": "Por exemplo", "title": "Claude Code",
    "messages": [{"role": "user", "text": "Faça um filme de 45 s, em aquarela, sobre a fazenda de café da minha família.",
                  "at": "Por exemplo"}]},
   c("Aí trabalha como", 199.5, 206),
   {"type": "counter", "at": "Um filme leva",
    "items": [{"value": 60, "prefix": "30–", "suffix": " min", "label": "por filme", "at": "Um filme leva"}]},
   st("então comece curto", "Plano menor? **Comece curto**"),
 ],
 "7": [
   hook("Número cinco", 5, "Claude**Animation**Base", "desenho animado"),
   c("É um kit", 249, 254.5),
   c("trinta e uma", 257, 261),
   {"type": "chat", "at": "Abra no Claude", "title": "Claude Code",
    "messages": [{"role": "user", "text": "Leia o guia de animação.", "at": "peça para ler"},
                 {"role": "user", "text": "Faça um vídeo de 15 s do Clawd tentando pegar uma borboleta.", "at": "e depois um"}]},
   {"type": "steps", "at": "Ele planeja", "goal": "o que ele faz sozinho",
    "steps": [{"title": "Planeja as cenas", "at": "Ele planeja"}, {"title": "Desenha", "at": "desenha"},
              {"title": "Confere os quadros", "at": "confere os quadros"}, {"title": "Entrega o MP4", "at": "entrega o MP4"}]},
   c("Dica do criador", 276, 287),
 ],
 "8": [
   hook("Número seis", 6, "A dupla **P(doom)**", "mesma música, dois diretores"),
   c("Duas pessoas fizeram", 296.3, 306),
   c("Um é pintado", 309, 316),
   c("O outro é", 317.5, 321.3),
   c("Abra os dois", 327, 335),
   st("é a melhor aula", "A **sua direção** muda o resultado"),
 ],
 "9": [
   hook("Número sete", 7, "awesome-**claude**-5-5-videos", "a pesquisa"),
   c("São quatrocentos e", 340, 347),
   {"type": "counter", "at": "Um criador deu",
    "items": [{"value": 2.19, "decimals": 2, "prefix": "US$ ", "label": "Haiku", "at": "dois dólares"},
              {"value": 3.04, "decimals": 2, "prefix": "US$ ", "label": "Opus", "at": "três dólares"}]},
   st("Então, se o", "Teste antes o **modelo mais barato**"),
 ],
 "10": [
   {"type": "compare", "at": "Agora, os limites",
    "left": {"title": "Ótimo para", "tone": "good", "at": "ótimo para",
             "lines": [{"text": "motion graphics", "at": "motion graphics"}, {"text": "desenho animado", "at": "desenho animado"},
                       {"text": "explicativos", "at": "explicativos"}, {"text": "clipes com letra", "at": "clipes com letra"}]},
    "right": {"title": "Não é para", "tone": "bad", "at": "Não é para",
              "lines": [{"text": "pessoas realistas", "at": "pessoas realistas"}]},
    "verdict": {"text": "Mesmo prompt, outro filme: **2 ou 3 rodadas**", "at": "duas ou três"}},
   st("Por onde eu", "**1 estilo** · menos de **30 s** · o que você vende ou ensina", src=str(M / "comecar.png")),
   {"type": "keyword", "at": "Os sete links", "text": "**inema.club**", "sub": "os 7 links no repositório do vídeo"},
   st("Me conta nos", "Qual você vai **testar primeiro**?"),
 ],
}

out = {"block": "pt-b01", "scenes": {n: {"shots": S[n]} for n in S}}
(O / "visual").mkdir(exist_ok=True)
(O / "visual" / "pt-b01.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
CL.mkdir(exist_ok=True)
(CL / "lista.json").write_text(json.dumps(LISTA))
print("ok", len(LISTA), "clipes")
