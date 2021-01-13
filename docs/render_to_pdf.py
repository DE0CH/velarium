import subprocess
import os

for filename in os.listdir('.'):
    if filename.endswith('.md'):
        subprocess.run(['pandoc',
                        '--listings',
                        '-H', 'formatting.tex',
                        filename,
                        '-o', os.path.join('prod', filename[:-3] + '.pdf')]
                       )
