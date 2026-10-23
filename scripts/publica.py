"""Publica o vídeo "O Claude vira seu estúdio de vídeo" (explicavideos v2, refazvideo) em inematds/claude-estudio-video.
Release video-v1.0.0 (MP4 16:9 + SRT + MP4 9:16) + Pages: videos/index.html com os 2 players, capítulos e legendas VTT.
Uso: python3 scripts/publica.py   (idempotente: sobe só o que mudou; commit só se houver diff). Molde: ai-harness."""
import html, json, re, subprocess, sys, time, urllib.request
from pathlib import Path

ID = 'claude-estudio-video'
OUT = Path.home() / 'projetos/output/explica-p-7yeArMIQ0'
REPO = Path(__file__).resolve().parent.parent
GH = f'inematds/{ID}'
TAG = 'video-v1.0.0'
BASE = f'https://github.com/{GH}/releases/download/{TAG}/'
PAGES = f'https://inematds.github.io/{ID}/'
TITLE = 'O Claude vira seu estúdio de vídeo: 7 repositórios grátis'
H1 = 'O Claude vira seu <b>estúdio de vídeo</b>'
LEAD = ('Sete repositórios gratuitos do GitHub mostram como fazer motion graphics, desenho animado, explicativos e clipes '
        'pedindo para o Claude escrever o vídeo como código: uma página web desenha cada quadro, o Chrome fotografa e o FFmpeg '
        'junta. Os prompts, os estilos, o código e por onde começar.')
FINAL = OUT / 'v2/final'
V916 = FINAL / '9x16' / f'{ID}-pt-9x16.mp4'


def sh(*a, **kw):
    return subprocess.run(a, check=True, text=True, capture_output=True, **kw).stdout


def dur(p):
    return float(sh('ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(p)))


def mmss(d):
    return f'{int(d // 60)}min{int(d % 60):02d}s'


def main():
    V2 = OUT / 'v2'
    rec = json.loads((V2 / 'verification/assembled-pt.json').read_text())
    full = Path(rec['file'])
    assert full.stat().st_size == rec['bytes']
    assert V916.exists(), V916
    scenes = json.loads((V2 / 'docs/lesson-pt.json').read_text())
    chapters = [(int(c['time']), scenes[c['scene'] - 1]['title']) for c in rec['chapters']]
    stage = OUT / 'release'; stage.mkdir(exist_ok=True)
    folder = REPO / 'videos'; folder.mkdir(exist_ok=True)
    pares = [(full, f'{ID}-16x9.mp4'), (full.with_suffix('.srt'), f'{ID}-16x9.srt'), (V916, f'{ID}-9x16.mp4')]
    assets = []
    for src, nome in pares:
        dst = stage / nome
        if not dst.exists() or dst.stat().st_size != src.stat().st_size:
            dst.write_bytes(src.read_bytes())
        assets.append(dst)
    vtt = 'WEBVTT\n\n' + re.sub(r'(\d\d:\d\d:\d\d),(\d{3})', r'\1.\2', full.with_suffix('.srt').read_text())
    (folder / 'pt.vtt').write_text(vtt)
    caps = ''.join(f'<button type="button" data-time="{s}">{s // 60:02d}:{s % 60:02d} · {html.escape(c)}</button>' for s, c in chapters)
    d1, d2 = dur(full), dur(V916)
    cards = [
        f'''<section class="card"><h2>Vídeo completo 16:9 <span>{mmss(d1)}</span></h2>
<video controls preload="metadata" playsinline><source src="{BASE}{ID}-16x9.mp4" type="video/mp4"><track default kind="subtitles" src="pt.vtt" srclang="pt" label="Português"></video>
<p><a href="{BASE}{ID}-16x9.mp4">Baixar MP4</a> · <a href="{BASE}{ID}-16x9.srt">Baixar legendas</a></p>
<details><summary>Capítulos</summary>{caps}</details></section>''',
        f'''<section class="card vert"><h2>Versão vertical 9:16 <span>{mmss(d2)}</span></h2>
<video controls preload="metadata" playsinline><source src="{BASE}{ID}-9x16.mp4" type="video/mp4"><track default kind="subtitles" src="pt.vtt" srclang="pt" label="Português"></video>
<p><a href="{BASE}{ID}-9x16.mp4">Baixar MP4</a></p></section>''']
    delivery = {'16x9': {'url': BASE + f'{ID}-16x9.mp4', 'srt': BASE + f'{ID}-16x9.srt', 'duration': round(d1, 2)},
                '9x16': {'url': BASE + f'{ID}-9x16.mp4', 'duration': round(d2, 2)}}
    if subprocess.run(['gh', 'release', 'view', TAG, '--repo', GH], capture_output=True).returncode:
        notes = stage / 'RELEASE.md'
        notes.write_text(f'{TITLE} — vídeo com avatar e voz do Nei, 16:9 e 9:16, legendas em português.\n\n'
                         f'Assistir: {PAGES}videos/\n\nProdução: Explicavideos v2 (https://inematds.github.io/explicavideos/guia/)')
        sh('gh', 'release', 'create', TAG, '--repo', GH, '--draft', '--title', f'{TITLE} (vídeo)', '--notes-file', str(notes))
    have = {a['name']: a['size'] for a in json.loads(sh('gh', 'release', 'view', TAG, '--repo', GH, '--json', 'assets'))['assets']}
    for f in assets:
        if have.get(f.name) != f.stat().st_size:
            print('upload', f.name, flush=True)
            sh('gh', 'release', 'upload', TAG, str(f), '--repo', GH, '--clobber')
    page = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)} · INEMA.CLUB</title><meta name="description" content="{html.escape(LEAD)}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Sora:wght@700;800&family=Inter:wght@400;600&display=swap" rel="stylesheet">
<style>:root{{color-scheme:dark;--bg:#0c0c10;--card:#15151c;--line:#2a2a35;--tx:#ededf2;--mut:#a3a3b2;--am:#FACC15}}*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--tx);font:17px/1.6 Inter,system-ui,sans-serif}}main{{max-width:1100px;margin:auto;padding:32px 16px}}
a{{color:var(--am)}}h1{{font:800 clamp(1.9rem,5vw,3rem)/1.12 Sora,sans-serif;margin:.4em 0}}h1 b{{color:var(--am)}}.lead{{color:var(--mut);max-width:760px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:20px;margin:28px 0}}.card h2{{font:700 1.25rem Sora,sans-serif;margin:0 0 8px}}.card h2 span{{color:var(--mut);font:500 .95rem Inter,sans-serif}}
video{{width:100%;aspect-ratio:16/9;background:#000;border-radius:12px}}.vert video{{aspect-ratio:9/16;max-width:420px;display:block;margin:auto}}
summary{{cursor:pointer;color:var(--am);margin-top:8px}}button{{display:block;background:var(--bg);color:var(--tx);border:1px solid var(--line);border-radius:10px;padding:10px 12px;margin:6px 0;text-align:left;cursor:pointer;width:100%;font:inherit}}
.repos li{{margin:.35em 0}}:focus-visible{{outline:3px solid var(--am);outline-offset:3px}}footer{{color:var(--mut);font-size:15px;margin-top:40px}}</style></head>
<body><main><nav><a href="https://inema.club">INEMA.CLUB</a> · <a href="https://github.com/{GH}">GitHub</a></nav>
<h1>{H1}</h1><p class="lead">{html.escape(LEAD)}</p>
{cards[0]}
<section class="card"><h2>Os 7 repositórios</h2><ol class="repos">
<li><a href="https://github.com/yihui-dev/awesome-opus5-5-videos">awesome-opus5-5-videos</a> — 703 prompts com o post original</li>
<li><a href="https://github.com/joeseesun/opus-video-prompts">opus-video-prompts</a> — 54 casos, 18 prompts e o prompt de uma linha</li>
<li><a href="https://github.com/Vincentwei1021/mg-styles-15">mg-styles-15</a> — 15 estilos de motion com filme, prompt e código</li>
<li><a href="https://github.com/lemomo-ai/lemo-opuscar">lemo-opuscar</a> — skill do Claude Code com 59 estilos de filme</li>
<li><a href="https://github.com/JohnHeibel/ClaudeAnimationBase">ClaudeAnimationBase</a> — desenho animado com o Clawd e 31 emoções</li>
<li><a href="https://github.com/JohnHeibel/PDoomVideo">PDoomVideo</a> + <a href="https://github.com/mexicat/pdoom-video">pdoom-video</a> — mesma música, dois diretores</li>
<li><a href="https://github.com/athemeroy/awesome-claude-5-5-videos">awesome-claude-5-5-videos</a> — 424 posts com Opus, Sonnet e Haiku</li></ol>
<p>Prompts, comandos e limites no <a href="https://github.com/{GH}#readme">README</a>.</p></section>
{cards[1]}
<footer>Produzido com o <a href="https://inematds.github.io/explicavideos/guia/">Explicavideos v2</a>. Conteúdo aberto e gratuito do <a href="https://inema.club">INEMA.CLUB</a>.</footer></main>
<script>document.querySelectorAll('[data-time]').forEach(b=>b.addEventListener('click',()=>{{const v=b.closest('.card').querySelector('video');v.currentTime=Number(b.dataset.time);v.play();}}));</script></body></html>
'''
    (folder / 'index.html').write_text(page)
    (REPO / 'index.html').write_text(f'<!doctype html><meta charset="utf-8"><title>{html.escape(TITLE)}</title><meta http-equiv="refresh" content="0; url=videos/"><a href="videos/">Assistir</a>\n')
    (folder / 'delivery.json').write_text(json.dumps(delivery, indent=2) + '\n')
    g = lambda *a: sh('git', '-c', 'user.name=inematds', '-c', 'user.email=inematds@gmail.com', *a, cwd=REPO)
    g('add', '-A')
    if subprocess.run(['git', 'diff', '--cached', '--quiet'], cwd=REPO).returncode:
        g('commit', '-m', f'feat: player do vídeo (16:9 e 9:16)\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>')
        g('push', '-q', 'origin', 'HEAD:main')
    sh('gh', 'release', 'edit', TAG, '--repo', GH, '--draft=false')
    if subprocess.run(['gh', 'api', f'repos/{GH}/pages'], capture_output=True).returncode:
        sh('gh', 'api', '-X', 'POST', f'repos/{GH}/pages', '-f', 'source[branch]=main', '-f', 'source[path]=/')
    for n in delivery.values():
        with urllib.request.urlopen(urllib.request.Request(n['url'], method='HEAD'), timeout=60) as r:
            assert r.status == 200
    for _ in range(40):
        try:
            with urllib.request.urlopen(PAGES + 'videos/delivery.json?v=' + str(int(time.time())), timeout=30) as f:
                if '9x16' in f.read().decode():
                    break
        except Exception:
            pass
        time.sleep(30)
    else:
        sys.exit('push e release feitos; Pages ainda não respondeu')
    print('OK', PAGES + 'videos/')


if __name__ == '__main__':
    main()
