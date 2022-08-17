import imp
import pandas as pd
import sqldf
import numpy as np
import itertools
from collections import defaultdict

pd.set_option('display.max_columns', 20)

df_raw = pd.read_csv('marketing.csv')

df_raw.columns

df_raw.info()

df_raw.head()

df_selected = df_raw[['user_id', 'date_served',
                      'marketing_channel', 'date_subscribed', 'converted']]
df_selected = df_selected.dropna()
df_selected['converted'] = df_selected['converted'].astype('int')

df_selected.groupby(['marketing_channel']).size()

df_selected.groupby(['user_id']).size().sort_values()

df_selected.loc[df_selected['user_id'] == 'a100000879']

# 1. select columns in need
query1 = """
SELECT user_id, marketing_channel, converted
FROM df_selected
ORDER BY user_id, marketing_channel
"""

df_view1 = sqldf.run(query1)
df_view1

# 2. concat channels and mark if converted
query2 = """
SELECT user_id, GROUP_CONCAT(DISTINCT(marketing_channel)) as channel_subset, max(converted) as conversion
FROM df_view1
GROUP BY user_id
"""
df_view2 = sqldf.run(query2)

# 3. sum up channels successfully converted, if fail to convert then 0, sum up will ignore this record
query3 = """
SELECT channel_subset, sum(conversion) as conversion_sum
FROM df_view2
GROUP BY channel_subset
"""
df_view3 = sqldf.run(query3)


# some functions
def power_set(List):
    PS = [list(j) for i in range(len(List)) for j in itertools.combinations(List, i+1)]
    return PS

def subsets(s):
    '''
    This function returns all the possible subsets of a set of channels.
    input :
            - s: a set of channels.
    '''
    if len(s)==1:
        return s
    else:
        sub_channels=[]
        for i in range(1,len(s)+1):
            sub_channels.extend(map(list,itertools.combinations(s, i)))
    return list(map(",".join,map(sorted,sub_channels)))


def v_function(A,C_values):
    '''
    This function computes the worth of each coalition.
    inputs:
            - A : a coalition of channels.
            - C_values : A dictionnary containing the number of conversions that each subset of channels has yielded.
    '''
    subsets_of_A = subsets(A)
    #print(subsets_of_A)
    #exit()
    worth_of_A=0
    for subset in subsets_of_A:
        #print("subset:", subset)
        if subset in C_values:
            #print("subset:", subset, "; Value:", C_values[subset])
            worth_of_A += C_values[subset]
    return worth_of_A


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# convert coalitions into dictionary format, true values
c_values = dict(zip(df_view3['channel_subset'], df_view3['conversion_sum']))
#  get unique channels from all colisions (this line might be tidious, but secured and trustworthy) 
unique_channels = df_view3['channel_subset'].apply(lambda x: x if len(x.split(',')) == 1 else np.nan).dropna().unique()

itertools.combinations(unique_channels, 2)

# the length of S lost should be 31
# 31 = 5 (one) + 10 (two) + 10(three) + 5(four) + 1(five)??? why 1 is five conlision? shouldn't it be 0?
S_list = [list(j) for i in range(len(unique_channels)) for j in itertools.combinations(unique_channels, i+1)]

v_values = {}
for A in S_list:
    v_values[','.join(sorted(A))] = v_function(A,c_values)

print(len(list(itertools.combinations(unique_channels, 2))))


n = len(unique_channels)
shapley_values = defaultdict(int)

for channel in unique_channels:
    for A in v_values.keys():
        #print(A)
        if channel not in A.split(","):
            #print(channel)
            cardinal_A=len(A.split(","))
            A_with_channel = A.split(",")
            A_with_channel.append(channel)            
            A_with_channel=",".join(sorted(A_with_channel))
            # Weight = |S|!(n-|S|-1)!/n!
            weight = (factorial(cardinal_A)*factorial(n-cardinal_A-1)/factorial(n))
            # Marginal contribution = v(S U {i})-v(S)
            contrib = (v_values[A_with_channel]-v_values[A]) 
            shapley_values[channel] += weight * contrib
    # Add the term corresponding to the empty set
    shapley_values[channel]+= v_values[channel]/n