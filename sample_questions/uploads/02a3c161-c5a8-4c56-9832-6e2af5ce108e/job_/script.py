import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
import json
import re

def solve_and_save():
    # Load the data
    file_path = 'uploads/02a3c161-c5a8-4c56-9832-6e2af5ce108e/highest_grossing_films.csv'
    df = pd.read_csv(file_path)

    # --- Data Cleaning ---
    def clean_currency(value):
        if isinstance(value, str):
            value = re.sub(r'\[\d+\]', '', value) # Remove citations like [1]
            value = value.replace('$', '').replace(',', '')
        try:
            return float(value)
        except (ValueError, TypeError):
            return np.nan
    
    df['Worldwide gross'] = df['Worldwide gross'].apply(clean_currency)
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
    df['Rank'] = pd.to_numeric(df['Rank'], errors='coerce')
    df['Peak'] = pd.to_numeric(df['Peak'], errors='coerce')
    df.dropna(subset=['Worldwide gross', 'Year', 'Rank', 'Peak'], inplace=True)
    df['Year'] = df['Year'].astype(int)

    # --- Question 1: How many $2 bn movies were released before 2000? ---
    movies_2bn_before_2000 = df[(df['Worldwide gross'] >= 2_000_000_000) & (df['Year'] < 2000)]
    answer1 = len(movies_2bn_before_2000)

    # --- Question 2: Which is the earliest film that grossed over $1.5 bn? ---
    movies_1_5bn = df[df['Worldwide gross'] >= 1_500_000_000]
    earliest_film = movies_1_5bn.sort_values(by='Year').iloc[0]
    answer2 = earliest_film['Title']

    # --- Question 3: What's the correlation between the Rank and Peak? ---
    correlation = df['Rank'].corr(df['Peak'])
    answer3 = correlation

    # --- Question 4: Draw a scatterplot of Rank and Peak ---
    plt.figure(figsize=(10, 6))
    sns.regplot(x='Rank', y='Peak', data=df, line_kws={'color': 'red', 'linestyle': '--'})
    plt.title('Rank vs. Peak of Highest-Grossing Films')
    plt.xlabel('Rank')
    plt.ylabel('Peak')
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    answer4 = f'data:image/png;base64,{image_base64}'
    buf.close()
    plt.close()

    # --- Consolidate and Save Results ---
    results = [answer1, answer2, answer3, answer4]
    with open('uploads/02a3c161-c5a8-4c56-9832-6e2af5ce108e/result.json', 'w') as f:
        json.dump(results, f)

solve_and_save()
