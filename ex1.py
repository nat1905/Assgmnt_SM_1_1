import hedgehog as hh
import pandas as pd

bn = hh.BayesNet(
    ('Burglary', 'Alarm'),
    ('Earthquake', 'Alarm'),
    ('Alarm', 'John calls'),
    ('Alarm', 'Mary calls'))

print(bn)

# P(Burglary)
bn.P['Burglary'] = pd.Series({False: .999, True: .001})

# P(Earthquake)
bn.P['Earthquake'] = pd.Series({False: .998, True: .002})

# P(Alarm | Burglary, Earthquake)
bn.P['Alarm'] = pd.Series({
 (True, True, True): .95,
 (True, True, False): .05,

 (True, False, True): .94,
 (True, False, False): .06,

 (False, True, True): .29,
 (False, True, False): .71,

 (False, False, True): .001,
 (False, False, False): .999
})

# P(John calls | Alarm)
bn.P['John calls'] = pd.Series({
 (True, True): .9,
 (True, False): .1,
 (False, True): .05,
 (False, False): .95
})

# P(Mary calls | Alarm)
bn.P['Mary calls'] = pd.Series({
 (True, True): .7,
 (True, False): .3,
 (False, True): .01,
 (False, False): .99
})
bn.prepare()
a = bn.query('Burglary', event={'Mary calls': True, 'John calls': True})
print(a)
a = bn.query('John calls', 'Mary calls', event={'Earthquake': True})
print(a)