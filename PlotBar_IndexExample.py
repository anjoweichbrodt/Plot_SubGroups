import xlwings as xw
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib

# Generate the data
ix = pd.MultiIndex.from_arrays([
    ['35', '35', '35', '36', '36', '36',
    '37', '37', '37', '38', '38', '38',
    '39', '39', '39', '40', '40', '40',
    '41', '41', '41', '42', '42', '42',
    '43', '43', '43', '45', '45', '45'],
    ['SableCEN', 'SableCEN', 'SableCEN', 'SableCEN', 'SableCEN', 'SableCEN',
    'GrèsBleu', 'GrèsBleu', 'GrèsBleu', 'GrèsBleu', 'GrèsBleu', 'GrèsBleu',
    'GrèsBleu', 'GrèsBleu', 'GrèsBleu', 'GrèsBleu', 'GrèsBleu', 'GrèsBleu',
    'GrèsBleu', 'GrèsBleu', 'GrèsBleu', 'GrèsBleu', 'GrèsBleu', 'GrèsBleu',
    'GrèsBleu', 'GrèsBleu', 'GrèsBleu', 'GrèsBleu', 'GrèsBleu', 'GrèsBleu'],
    ['Aer5-16', 'Aer5-16', 'Aer5-16', 'None', 'None', 'None',
    'None', 'None', 'None', 'Aer5-16', 'Aer5-16', 'Aer5-16',
    'Aer5-16', 'Aer5-16', 'Aer5-16', 'Solid-10', 'Solid-10', 'Solid-10',
    'Solid-20', 'Solid-20', 'Solid-20', 'Aer10-16', 'Aer10-16', 'Aer10-16',
    'Aer10-24', 'Aer10-24', 'Aer10-24', 'None', 'None', 'None', ]],
    names=['Melange_ID', 'Melange', 'Fluidifiant'])

df = pd.DataFrame({'data1': [91.7355,100.986, 92.2203, 85.5049,89.2162,82.5723,
    101.376,98.3238,96.1542,87.2135,96.8933,91.6958,
    125.647,124.272,118.407,93.8892,85.8784,84.7499,
    84.6386,87.0387,91.2666,92.419,102.313,92.6813,
    99.9371,113.471,104.3,100,100,100]}, index=ix)
