import os
import webbrowser

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
dataset_path = os.path.join(os.getcwd(), "../data/flavors_of_cacao.csv")
chocodata = pd.read_csv(dataset_path)

# Rename the columns to better manage them
new_colnames = ['company', 'bean_origin', 'ref', 'review_date', 'cocoa_percent',
                'company_location', 'rating', 'bean_type', 'bean_origin']
chocodata = chocodata.rename(columns=dict(zip(chocodata.columns, new_colnames)))

# Get a list of all the unique values of the Company column (that are overall 416)
companies = chocodata.company.unique()

# Create a dataframe in which to save the companies and their average evaluations
d = {'company': [],
     'avg_rating': []}
avg_companies = pd.DataFrame(d)

# Foreach company save its average evaluation in a dataframe
for c in companies:
    company = chocodata[chocodata.company == c]
    mean_rating = company['rating'].mean()
    d = pd.DataFrame(
        {'company': [c],
         'avg_rating': [mean_rating]})
    tmp = [avg_companies, d]
    avg_companies = pd.concat(tmp)

# Extract the ten better companies in term of average chocolate rating
ten_better_companies = avg_companies.nlargest(10, columns=['avg_rating'])

# Plot them through a horizontal barplot
sns.set_theme(style='whitegrid')
sns.set(font_scale = 2)
fig_dims = (23, 18)
fig, ax = plt.subplots(figsize=fig_dims)
ax = sns.barplot(data=ten_better_companies, ax=ax, x='avg_rating', y='company')
ax.set(xlabel='Average Bar Rating', ylabel='Company')
plt.savefig('images/best_companies.pdf')
