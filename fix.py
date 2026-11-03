from pathlib import Path 
files = [ 
    Path('c:/Users/SHANTO/Videos/xnnews/apkxxx/lama/test/video-viral-video-xxx-vira-liv-en.html'), 
    Path('c:/Users/SHANTO/Videos/xnnews/apkxxx/lama/test/video-viral-video-xxx-vira-liv-en-01.html'), 
    Path('c:/Users/SHANTO/Videos/xnnews/apkxxx/lama/test/video-viral-video-xxx-vira-liv-en-02.html'), 
    Path('c:/Users/SHANTO/Videos/xnnews/apkxxx/lama/test/video-watch-full-video-vir-liv-en.html'), 
    Path('c:/Users/SHANTO/Videos/xnnews/apkxxx/lama/test/video-watch-now-viral-vide-liv-en.html'), 
    Path('c:/Users/SHANTO/Videos/xnnews/apkxxx/lama/test/video-xxx-exclusive-video-liv-en.html'), 
] 
for p in files: 
    text = p.read_text(encoding='utf-8') 
    out = [] 
    in_conflict = False 
    keep_head = False 
    for line in text.splitlines(True): 
"        if line.startswith('<<<<<<< '):" 
            in_conflict = True 
            keep_head = True 
            continue 
"        if line.startswith('======='):" 
            in_conflict = True 
            keep_head = False 
            continue 
"        if line.startswith('>>>>>>> '):" 
            in_conflict = False 
            keep_head = False 
            continue 
        if not in_conflict or keep_head: 
            out.append(line) 
    p.write_text(''.join(out), encoding='utf-8') 
    print(f'fixed {p.name}') 
