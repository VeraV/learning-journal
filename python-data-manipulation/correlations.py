import pandas as pd

data = pd.read_csv("data_cor.csv")

## Relationship btw the columns
#  1   - perfect correlation
#  0.9 - good rel., increases 1 probably another also increses
# -0.9 - good rel., increases 1 probably DEcreases another
#  0.2 - NOT a good rel. => if 1 goes UP doesn't mean the other will
# A GOOD Relationship is AT LEAST 0.6 (-0.6)

print(data.corr()) # relationship btw the columns (ignores not numeric)

