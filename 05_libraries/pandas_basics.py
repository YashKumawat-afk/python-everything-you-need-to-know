# ============================================================
#  Pandas Basics — python-everything-you-need-to-know
# ============================================================

import pandas as pd
import numpy as np

print("=" * 50)
print("  Pandas Basics")
print("=" * 50)

# ------ 1. Creating DataFrames ------
print("\n[1] Creating DataFrames")
data = {
    'Name':    ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan'],
    'Subject': ['Math', 'Science', 'Math', 'English', 'Science'],
    'Score':   [88, 92, 75, 95, 60],
    'Passed':  [True, True, True, True, False]
}
df = pd.DataFrame(data)
print(df)

# ------ 2. Basic Info ------
print("\n[2] Basic Info")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Dtypes:\n", df.dtypes)
print("\nDescribe:\n", df.describe())

# ------ 3. Selecting Data ------
print("\n[3] Selecting Data")
print("Single column:\n", df['Name'])
print("\nMultiple columns:\n", df[['Name', 'Score']])
print("\nRow by iloc:\n", df.iloc[1])
print("\nRow by loc (index 2):\n", df.loc[2])

# ------ 4. Filtering ------
print("\n[4] Filtering")
passed = df[df['Passed'] == True]
high_scorers = df[df['Score'] > 85]
print("Passed students:\n", passed)
print("\nHigh scorers (>85):\n", high_scorers)

# ------ 5. Adding / Modifying Columns ------
print("\n[5] Adding Columns")
df['Grade'] = df['Score'].apply(
    lambda x: 'A' if x >= 90 else ('B' if x >= 80 else ('C' if x >= 70 else 'F'))
)
print(df)

# ------ 6. GroupBy ------
print("\n[6] GroupBy")
subject_avg = df.groupby('Subject')['Score'].mean()
print("Average score per subject:\n", subject_avg)

grade_count = df.groupby('Grade').size()
print("\nCount per grade:\n", grade_count)

# ------ 7. Sorting ------
print("\n[7] Sorting")
sorted_df = df.sort_values(by='Score', ascending=False)
print(sorted_df)

# ------ 8. Handling Missing Data ------
print("\n[8] Missing Data")
df_missing = df.copy()
df_missing.loc[2, 'Score'] = np.nan
print("With NaN:\n", df_missing)
print("Is null:\n", df_missing.isnull().sum())
df_filled = df_missing.fillna(df_missing['Score'].mean())
print("After fillna:\n", df_filled)

# ------ 9. CSV I/O ------
print("\n[9] CSV I/O")
df.to_csv('students.csv', index=False)
df_loaded = pd.read_csv('students.csv')
print("Loaded from CSV:\n", df_loaded.head())

# ------ 10. Merge / Join ------
print("\n[10] Merge / Join")
df_extra = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'City': ['Delhi', 'Mumbai', 'Jaipur']
})
merged = pd.merge(df, df_extra, on='Name', how='left')
print(merged[['Name', 'Score', 'Grade', 'City']])

print("\n✅ Pandas tutorial complete!")
