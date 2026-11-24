# The Funniest Toaster Error Message

[![make.fun bounty](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/Takoyaki061/make-fun-funniest-toaster-error/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/Takoyaki061/make-fun-funniest-toaster-error/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)

One line, under 120 characters — the funniest error message a kitchen toaster would show its owner, written by `main.py` (standard library only, deterministic) to `/output/entry.txt`:

> You never pressed the lever. There is no record of it. Are you feeling alright?

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

The program writes exactly one error message (79 characters), checks it against the gate (1–120 characters, not only whitespace), and exits non-zero if the check fails.
