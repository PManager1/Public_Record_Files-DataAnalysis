# https://www.youtube.com/watch?v=ODNMNwgtehk&t=295s

import re
import pandas as pd


df = pd.read_html('https://fastestlaps.com/tracks/le-mans-bugatti')
print(df)