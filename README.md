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

# Komme i gang (Poetry)
## Installasjon

Poetry kan installeres via [homebrew](https://formulae.brew.sh/formula/poetry)
```bash
brew install poetry
```

Andre alternativer finnes også i Poetry sin [dokumentasjon](https://python-poetry.org/docs/#installation)

## Opprette virtuelt miljø i prosjektet
Anbefaler å konfigurere poetry til å lage virtuelt miljø i prosjektmappen så det ikke legges i cache, det gjør man ved å bruke kommandoen:

```bash
poetry config virtualenvs.in-project true
```

Deretter kan man opprette virtuelt miljø med kommandoen:

```bash
poetry install
```
Denne lager virtuelt miljø basert på `pyproject.toml`-filen i prosjektet.

For å få informasjon om hvilken python versjon som brukes og hvor den ligger (det virtuelle miljøet) kan du skrive: `poetry env info`

## Ta i bruk virtuelt miljø:


### Shell
For å åpne et shell i det virtuelle miljøet bruker du kommandoen:

```bash
poetry shell
```

Fra shell i virtuelt miljø kan du f.eks. kjøre tester med:
```bash
pytest
```

eller lage notebooks med:

```bash
jupyter notebook
```

For å komme deg ut av shell for det virtuelle miljøet bruker du:
```bash
exit
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
### Åpne shell:
```bash
poetry shell
```

### Nytt innhold i spørreundersøkelse
Generer migreringsskript for nytt innhold til spørreundersøkelse i [lydia-api](https://github.com/navikt/lydia-api)

```bash
python python_scripts/legg_til_nye_temaer.py
```

### Nye testdata fra tenor
Generer SQL scripts som legger til testvirksomheter for lokal kjøring og dev-miljø

```bash
python python_scripts/testdata_tenor.py
```

# Henvendelser

Spørsmål knyttet til koden eller prosjektet kan stilles som issues her på GitHub

## For NAV-ansatte

Interne henvendelser kan sendes via Slack i kanalen #team-pia-utvikling
