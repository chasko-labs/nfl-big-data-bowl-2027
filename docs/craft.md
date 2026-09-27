# craft: how to win

judging, formats, and advice from the people who grade. bracketed
numbers are sources in [references](references.md).

## the rubric

football 30 / data science 30 / report 20 / visualization 20 -
documented for 2025 [37] and 2026 analytics [37b]. assume it holds
until the new rules say otherwise.

two hard constraints found in the 2025 mirror [37]:

- judges are analytics staffers from nfl teams and tracking vendors.
  they know more football than you.
- entries not using player tracking data are not scored. the tracking
  file must matter to the result, not decorate it.

## format limits (verify against the current year)

- metric / undergrad notebooks: 2000 words max, under 10 figures,
  code in appendix [37].
- coaching track: pdf slide deck, max 20 slides, plus a public kaggle
  dataset [37]. coaching pairs teams with real coaches (cmu worked
  with coach larsen in 2024) [41b].
- 2026 split into leaderboard + data visualization tracks, with
  university-only and broadcast-viz sub-tracks [30][31].

## patton's 20 tips (verbatim, condensed lightly)

andrew patton, nfl director of analytical research and governance,
posted this advice jan 13 2024 [53] (the single highest-signal doc
in this repo - preserved verbatim since x blocks fetches):

1. answer the prompt. don't solve all of football or stray outside
   the year's bounds. tackling year != fourth down model.
2. graders do this at night and weekends on top of day jobs. format
   so they can see you did good work. help them help you.
3. graders know more football than you. no "what is football"
   introductions, no novice narratives.
4. flowery prose is not your friend. concise and direct. (good
   creative example: the kendrick lamar submission by
   @deceptivespeed\_.)
5. you never need 17 decimal points.
6. size figures correctly. zooming 27 times to read a legend kills
   you.
7. don't spend 200 hours on tech and 30 minutes on the writeup.
   half-assed explanations never get through.
8. have a friend proofread. grammar and spelling are easy points.
9. humility. you did not revolutionize football; team analysts are
   not stupid.
10. pick better chart colors. your submission should look expensive.
11. use correct football terminology. a wrong basic term, in the
    graders' expertise, is a bad look.
12. don't submit in the last hour then send panic emails begging
    1:1 support.
13. enter the correct track. think hard about whether coaching-track
    work is really coaching-appropriate.
14. state limitations. don't overclaim on a narrow data slice and a
    short window.
15. have a conclusion - a paragraph or table wrapping up.
16. have better spelling and grammar than the thread.
17. pick a memorable, informative title.
18. check whether someone already did your idea publicly. if so,
    innovate on it.
19. make it easy and fun to read. (worth repeating - his emphasis.)
20. it isn't life or death.

aws's builder center guide [54] highlights a subset of these (1, 2,
4, 6-8, 10, 11, 14, 17) - same message from the sponsor side.

## yurko's method discipline

costa yurko (cmu, stat thinks) on what separates entries [39]:

- always report base rates next to model accuracy.
- compare complex models to a simple lasso-logistic baseline.
- report cross-validated accuracy with standard errors, not one split.
- the data is small - win on downstream use of the predictions, not
  the fit itself.

## stacks that won

- 2022 winners: r + ggplot2/gganimate + shiny + bigquery +
  sportsdataverse [45].
- 2025: sumersports sports tracking transformer aided multiple
  winners [47] - transformers on tracking are now baseline for
  prediction years.
- 2026 preprint: lstm seq2seq + z-score + hyperband [35].
- 2020: crps over a yards cdf - probabilistic framing, not point
  estimates [6].
- gap: detailed winner stacks for 2023-2026 prediction work are thin
  beyond the above.

## support ecosystem

- cmu cmsac football workshop: invited talks + advanced modeling
  tutorial (~$50) [47]; 2019 edition taught tidyverse nfl data + elo
  in r [48]; annual conference tracks the field [48b].
- aws: slack/discord community, builder center guide, up to $200
  free tier credits [31][54]. sagemaker demo notebooks exist for
  past years [54].
- posit's getting-started guide, written with the 2022 winners [45].
- career context: 50+ entrants hired into sports analytics [51].
