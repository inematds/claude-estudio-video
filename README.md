# O Claude vira seu estúdio de vídeo: 7 repositórios grátis

Vídeo do INEMA.CLUB, com avatar e voz do Nei Maldaner, sobre sete repositórios gratuitos do GitHub que mostram como fazer
vídeo pedindo para o Claude escrever o vídeo como código: motion graphics, desenho animado, explicativos e clipes de música.

**Assistir:** https://inematds.github.io/claude-estudio-video/videos/ (16:9 e 9:16) · YouTube: [16:9](https://www.youtube.com/watch?v=xkAzBrdUVhA) · [9:16](https://www.youtube.com/watch?v=c4xoc26xFEU)

## Como funciona

O Claude não gera arquivo de vídeo. Ele escreve uma **página web que desenha cada quadro**; o **Chrome** tira uma foto de
cada quadro e o **FFmpeg** junta tudo num MP4. Como cada quadro é desenhado por código, o texto sai nítido e qualquer coisa
muda só pedindo.

```
seu prompt → Claude Code → página web (HTML + JS) → Chrome (quadro a quadro) → FFmpeg → MP4
```

Você precisa de Node, Chrome e FFmpeg (grátis) e do Claude Code (plano pago do Claude). Os repositórios são grátis.

## Os 7 repositórios

Estrelas e licença conferidas em 22/10/2026.

| # | Repositório | O que tem | ★ | Licença |
|---|---|---|---|---|
| 1 | [yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos) | 703 prompts de vídeos reais, cada um com o link do post original (motion graphics, explicativos, 3D, joguinhos) | 9,2 mil | MIT |
| 2 | [joeseesun/opus-video-prompts](https://github.com/joeseesun/opus-video-prompts) | 54 casos e 18 prompts completos; página em chinês, prompts em inglês. Tem o prompt de uma linha | 690 | não informada |
| 3 | [Vincentwei1021/mg-styles-15](https://github.com/Vincentwei1021/mg-styles-15) | 15 estilos de motion graphics: filme de 10 s + prompt + código. Troque só o `Creative seed`; revise com `rubric.md` | 1,8 mil | MIT |
| 4 | [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) | Skill do Claude Code com 59 estilos de filme (aquarela, nanquim, giz de cera, xilogravura…) | 5,5 mil | MIT |
| 5 | [JohnHeibel/ClaudeAnimationBase](https://github.com/JohnHeibel/ClaudeAnimationBase) | Kit de desenho animado com o Clawd e 31 emoções, guia de animação para o modelo | 1,6 mil | MIT |
| 6 | [JohnHeibel/PDoomVideo](https://github.com/JohnHeibel/PDoomVideo) + [mexicat/pdoom-video](https://github.com/mexicat/pdoom-video) | Dois clipes para a mesma música: pinceladas × karaokê neon em 4K 60 fps | 2,5 mil + 3,3 mil | não informada + MIT |
| 7 | [athemeroy/awesome-claude-5-5-videos](https://github.com/athemeroy/awesome-claude-5-5-videos) | 424 posts de origem (Opus, Sonnet, Haiku); tabela "sua tarefa → exemplo para copiar" | 721 | CC-BY-4.0 |

## Prompts para começar

- **Uma linha** (repositório 2): `make a modern slick and punchy video for a modern startup that works on inference`
  (o criador relata ~1 min e ~US$ 2). Troque pelo seu tema.
- **Instalar o lemo-opuscar** (repositório 4):
  ```bash
  claude plugin marketplace add lemomo-ai/lemo-opuscar
  claude plugin install lemo-opuscar@lemolab
  ```
  Depois: *"Faça um filme de 45 s, em aquarela, sobre a fazenda de café da minha família."* Um filme leva de 30 a 60 min
  e gasta bastante token: comece curto.
- **Desenho animado** (repositório 5): *"Read ANIMATION_GUIDE.md, then make a 15-second video of Clawd trying to catch a butterfly."*

## Limites

- Ótimo para motion graphics, desenho animado, explicativos e clipes com letra. **Não** é para pessoas realistas (aí entra um
  modelo de vídeo).
- O mesmo prompt gera um filme diferente a cada vez: conte com 2 ou 3 rodadas.
- Custo: um criador relata a mesma cena por US$ 2,19 no Haiku e US$ 3,04 no Opus. Teste antes o modelo mais barato.
- **Por onde começar:** um estilo do lemo-opuscar, menos de 30 s, sobre algo que você vende ou ensina.

## O processo, do início ao fim

Como este vídeo foi feito (🧠 sessão com o Nei · ⚙️ script · 🤖 agente):

1. 🧠 Pedido do Nei: link de referência + "crie um repo, 16:9 e 9:16, lives4, INEMA.VIDEOS".
2. ⚙️ Legenda da referência (`yt-dlp --write-auto-subs`) e download (inemavox `baixar_v1.py`).
3. 🧠 Números conferidos nos repositórios pela API do GitHub; roteiro em português (`roteiro/pt.json`, 10 cenas).
4. ⚙️ Avatar e voz do Nei pelo estúdio HeyGen (`explicavideos/engine/heygen-studio.mjs`), 1 bloco.
5. 🤖 Artes de capa e de abertura de cada repositório pelo Codex (`image_gen`).
6. 🧠 Roteiro visual (`visual/gerar_visual.py`): trechos animados da referência + diagrama, prints do GitHub, terminal e contadores.
7. ⚙️ Render no Explicavideos v2 (HyperFrames: página → Chrome → FFmpeg, o mesmo caminho do vídeo).
8. ⚙️ Versão 9:16: visual do 16:9 em cima, avatar embaixo.
9. ⚙️ `scripts/publica.py`: release com os MP4 e o player em `videos/`.
10. ⚙️ YouTube (canal INEMA Tec, via yt-pubx) e Telegram INEMA.VIDEOS.

Conteúdo aberto e gratuito do [INEMA.CLUB](https://inema.club).
