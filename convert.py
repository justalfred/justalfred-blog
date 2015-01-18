import os
DOMAIN = 'kwontum.blogspot.com'


fl = os.listdir('.')

for fn in fl:
    if fn.endswith('.py'):
        continue

    with open(fn, 'rb') as f:
        lines = []
        wrote_link = False
        year, month, slug = None, None, None

        for line in f:
            if line.startswith('Date:'):
                year, month = line[6:13].split('-')
                lines.append(line)
            elif line.startswith('Author:'):
                lines.append('Author: Just Alfred\n')
            elif line.startswith('Tags:'):
                lines.append('Tags: The Classical-Kwontum Interface, Music\n')
            elif line.startswith('Slug:'):
                slug = line.rstrip().split(' ')[-1]
                lines.append(line)
            else:
                lines.append(line)

            if line == '\n' and not wrote_link:
                url = 'http://{domain}/{year}/{month}/{slug}.html'.format(
                    domain=DOMAIN,
                    year=year,
                    month=month,
                    slug=slug
                )

                if not slug:
                    slug = fn.split('.')[0]

                lines.append('*Originally published at: '
                             '[{url}]({url})*\n\n'.format(url=url)
                             )
                wrote_link = True

    with open(fn, 'wb') as f:
        for line in lines:
            f.write(line)
