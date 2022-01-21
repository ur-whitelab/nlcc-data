# nlcc-data

## Contribution instructions
- First, make sure you're in the main branch with `git checkout main`, and update with `git pull origin`
- Then, make a branch with `git checkout -b <name>`
- After preparing your prompt/test following the example in smoke, push with `git push origin <name>`
- Go to the repo URL and open a PR from pull requests tab
- You will see a report with the result (did it pass), responses, and prompts after combining with context

## Categories of Prompts

- Topic: cheminf, spectroscopy, qm, md, bio, genchem, numerics, other, stats, thermo, vis
- Eval: code, human
- Special: disabled

### Special variables
Files can be accessed by the test scripts relative to the example `yml` file directory using the `_FILE_DIR_` variable. For example (from `dipole`):

```
import numpy as np
import os
coordinates = np.loadtxt(os.path.join(_FILE_DIR_,"water.xyz"),usecols=(1,2,3))
```

### Papermill

```sh
papermill -f output.yml human_eval_template.ipynb test.ipynb
jupyter-nbconvert --to=html --no-input test.ipynb
```
