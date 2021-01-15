import subprocess
import os

if __name__ == '__main__':
    os.makedirs('prod', exist_ok=True)
    for filename in os.listdir('.'):
        if filename.endswith('.md'):
            subprocess.run(['pandoc',
                            '--listings',
                            '-H', 'formatting.tex',
                            filename,
                            '-o', os.path.join('prod', filename[:-3] + '.pdf')]
                           )
