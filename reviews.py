import pandas as pd

wineData = pd.read_csv('data/winemag-data-130k-v2.csv.zip', index_col=0)

reviewsPerCountry = wineData.country.value_counts()

reviewPoints = wineData.groupby('country')['points'].mean().round(1)

mergedReviews = pd.DataFrame.merge(reviewsPerCountry, reviewPoints, on='country')

mergedReviews.to_csv('data/reviews-per-country.csv')
