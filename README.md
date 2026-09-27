# nfl big data bowl 2027

bryan chasko's personal collection of big data bowl resources to prep
for this year's contest. unofficial - just one builder's notes on the
annual nfl football operations contest (powered by aws) where
contestants turn next gen stats player tracking data into new stats.
eight editions run so far (2019-2026). the 2027 edition has not been
announced yet - this collection exists to be ready the day it drops.

## status

- research: complete for 2019-2026 (topics, datasets, winners, tv lineage)
- 2027: not announced. see [2027 prediction](docs/2027-prediction.md)
- talk prep: presenting tomorrow, start at [talk notes](docs/talk-notes.md)

## repo map

- `docs/history.md` - year-by-year: topic, dataset, winners, what reached tv
- `docs/winners.md` - hall of fame + how each win worked
- `docs/data-guide.md` - next gen stats spec, file layouts, how to download
- `docs/craft.md` - judging rubric, format limits, patton 20 tips, yurko method
- `docs/2027-prediction.md` - topic forecast + prep checklist
- `docs/references.md` - every source url, grouped
- `docs/talk-notes.md` - one-page cheat sheet for the presentation
- `data/` - local tracking data (gitignored, see `data/README.md`)
- `notebooks/` - starter analysis notebooks (see `notebooks/README.md`)

## the one-paragraph version

since 2019 the bowl has marched through open innovation, rushing, pass
defense, special teams, pass rush, tackling, pre-snap motion, and (2026)
player movement prediction. winning entries keep escaping the contest:
expected rushing yards, rushing yards over expected, pressure probability,
tackle probability, and coverage responsibility all went from entries to
national tv and team analytics departments. 50+ entrants have been hired
into sports analytics off the back of it. prize pool runs about $100k,
finalists present at the combine.

## quickstart

1. read [talk notes](docs/talk-notes.md) for the shape of the thing
2. pull a past dataset per [data README](data/README.md)
3. open the starter notebooks in `notebooks/`
4. when 2027 is announced, work the [prediction checklist](docs/2027-prediction.md)

sources for every claim live in `docs/references.md`. research compiled
2026-09-27 from nfl, aws, kaggle, cmu, and winner writeups.
