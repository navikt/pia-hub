pia-hub
================

# Hva er dette?

Inngangsport for alle ting Pia.

Repoet benytter seg av [meta](https://github.com/mateodelnorte/meta).

# Kom i gang med pia-hub

Forhåndskrav: `node` og `npm` [installert](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).
README er skrevet med utgangspunkt i et Mac oppsett.

## Meta

### Installer meta: 
```bash
npm i -g meta
```

### Klon alle repoer:
```bash
meta git update
```


### Legg til nye repoer:

For å legge til nytt repo i pia-hub bruker man:
```bash
meta project import pia-nytt-repo git@github.com:navikt/pia-nytt-repo.git
```

## Python

### Opprett virtuelt miljø, og installer poetry:
```bash
python3.12 -m venv python_scripts/.venv && python_scripts/.venv/bin/pip install -U pip setuptools && python_scripts/.venv/bin/pip install poetry
```

### Ta i bruk miljø:
```bash
source python_scripts/.venv/bin/activate
```

### Installer avhengigheter:
```bash
poetry install
```

### Kjør tester
```bash
pytest
```


### Deaktiver miljø med: 
```bash
deactivate
```
# Hvordan ta i bruk
Endel av dette krever et kjørende docker / docker-compose miljø.

## Bash scripts
### Bygger bun/next prosjekter
```bash
./scripts/bunBuild
```

### Bygger gradle prosjekter
```bash
./scripts/gradleBuild
```

## Python scripts
### Nytt innhold i spørreundersøkelse
Generer migreringsskript for nytt innhold til spørreundersøkelse i [lydia-api](https://github.com/navikt/lydia-api)

```bash
python ./python_scripts/legg_til_nye_temaer.py
```

### TODO: Migreringsscript for databaseendringer i Fia


### TODO: nye testvirksomheter i Fia

# Henvendelser

Spørsmål knyttet til koden eller prosjektet kan stilles som issues her på GitHub

## For NAV-ansatte

Interne henvendelser kan sendes via Slack i kanalen #team-pia-utvikling
