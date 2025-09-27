import numpy as np
import pandas as pd

# linear range search #
# given input value in int/float form, linearly check whether each trial is disqualified 
def check_valid_num_range(input, dataframe, cname1, cname2):
    mask = (dataframe[cname1] <= input) & (dataframe[cname2] >= input)
    return dataframe[mask]

# check whether the criteria was originally inclusion or exclusion 
# no edge cases where l = r because of continuous correction, including with +-1e7 for inf and -inf
def check_in_ex(l, r):
    if l > r:
        return "exclusion"
    if l < r:
        return "inclusion"

# check whether the input satisfies the criteria, handles both inclusion and exclusion criterias
def check_satisfiability_criteria(criteria, input):
    low, up = criteria
    if check_in_ex(low, up) == 'inclusion':
        if (input >= low) & (input <= up):
            return True
        else:
            return False
    else:
        if (input < low) | (input > up):
            return True
        else:
            return False

# map for inclusion and exclusion
def map_in_ex(criteria, type):
    if type == 'exclusion':
        low, up = criteria
    #     temp = low
    #     low = up
    #     up = temp
    # result = (low, up)
    # return result
        return (up, low)

###### Demo on How To Use Below ####### 
np.random.seed(42)
min_age = np.random.randint(18, 50, size=5)
max_age = np.random.randint(50, 65, size=5)
min_age = np.minimum(min_age, max_age - 1)

feature_1 = [(np.random.randint(1, 50), np.random.randint(51, 100)) for _ in range(5)]
feature_2 = [(np.random.randint(1, 50), np.random.randint(51, 100)) for _ in range(5)]

df1 = pd.DataFrame({
    'min age': min_age,
    'max age': max_age,
    'feature 1': feature_1,
    'feature 2': feature_2
})

feature_1_value = np.random.choice(['inclusion', 'exclusion'])  # Either all inclusion or all exclusion for feature 1
feature_2_value = np.random.choice(['inclusion', 'exclusion'])  # Either all inclusion or all exclusion for feature 2

df2 = pd.DataFrame({
    'feature 1': [feature_1_value] * 5,
    'feature 2': [feature_2_value] * 5
})

print("DataFrame 1 (random values):")
print(df1)
print("\nDataFrame 2 (inclusion/exclusion):")
print(df2)

print(check_valid_num_range(29, df1, "min age", "max age"))

for criteria in df1['feature 2']:
    mapped_criteria = map_in_ex(criteria, feature_2_value)
    print(f"Original criteria: {criteria}, Mapped criteria: {mapped_criteria}")

for criteria in df1['feature 1']:
    input = 12
    is_satisfiable = check_satisfiability_criteria(criteria, input)
    print(f"Satisfiable: {is_satisfiable}")


    