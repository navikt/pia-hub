pia-hub
================

## Hva er dette?

Inngangsport for alle ting Pia.

Repoet benytter seg av [meta](https://github.com/mateodelnorte/meta).

## Kom i gang med pia metarepo

Forhåndskrav: `node` og `npm` [installert](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).
README er skrevet med utgangspunkt i et Mac oppsett.

Installer meta: 
```bash
npm i -g meta
```

Klon alle repoer:
```bash
meta git update
```

## Ok, hva nå?

Endel av dette krever et kjørende docker / docker-compose miljø.

### Bygg gradle prosjekter:
```bash
scripts/gradleBuild.sh
```

### Bygg bun/next prosjekter:
```bash
scripts/bunBuild.sh
```

# Henvendelser

Spørsmål knyttet til koden eller prosjektet kan stilles som issues her på GitHub

## For NAV-ansatte

Interne henvendelser kan sendes via Slack i kanalen #team-pia-utvikling
