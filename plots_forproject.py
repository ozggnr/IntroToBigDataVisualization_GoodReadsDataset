import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.style as style
import os
os.makedirs('plotted',exist_ok=True)
data = pd.read_csv('books.csv',error_bad_lines=False)
data.rename(columns={'# num_pages': 'page_number'},inplace=True)
data.rename(columns={'language_code': 'language'},inplace=True)
data.rename(columns={'text_reviews_count': 'text_count'},inplace=True)

df = data.drop('isbn', axis=1)
df.replace(to_replace='J.K. Rowling-Mary GrandPré', value='J.K. Rowling', inplace=True)
df.replace(to_replace='William Shakespeare-Paul Werstine-Barbara A. Mowat', value='William Shakespeare-*', inplace=True)
df.replace(to_replace='Paul Coelho-Alan R. Clarke-Özdemir Ince', value='Paul Coelho-*', inplace=True)
df.replace(to_replace='Charlotte Brontë-Micheal Mason-Joāo Gaspar Rodrigues-Mécia', value='Charlotte Brontë-*', inplace=True)
df.replace(to_replace='Emily Brontë-Richard J. Dunn-David Timson-Charlotte Brontë-Ruth Golding-Robert Heindel', value='Emily Brontë-*', inplace=True)

sns.set(style="white")
df['ratings_count']=df['ratings_count'][df['ratings_count']<3000000]
# sns.set_context("paper")
sns.relplot(x='average_rating',y='language',size='page_number',sizes=(0,750),data=df,alpha=0.4)
plt.savefig(f'plotted/language_average.png')
plt.show()

sns.relplot(x='ratings_count',y='language',size='page_number',sizes=(0,750),data=df,alpha=0.4,color='crimson')
plt.savefig(f'plotted/language_rating.png')
plt.show()
plt.clf()

sns.set(style="darkgrid")
sns.relplot(x='ratings_count',y='page_number',size='average_rating',sizes=(15,200),alpha=0.5,data=df,label='rating_count',color='gold')
plt.xlabel('ratings count')
plt.ylabel('number of pages')
plt.savefig(f'plotted/ratingvspage_average.png')
plt.show()
plt.clf()

sns.set(style="darkgrid")
ax = sns.jointplot(x="average_rating",y='ratings_count', kind='scatter',  data= df,color='limegreen')
ax.set_axis_labels("Average Rating", "Ratings Count")
plt.savefig(f'plotted/ratings_average.png')
plt.show()
plt.clf()

number_books = df[['authors','bookID']].groupby(['authors'],as_index=False).count().sort_values(by=['bookID'],ascending=False).head(20)
number_books['number_of_books'] = number_books['bookID']
sns.set_context('paper')
style.use('ggplot')
sns.barplot(x='number_of_books',y='authors',data=number_books,palette=('rainbow')).set_title('Authors with Most Book')
plt.xlabel('book number')
plt.savefig(f'plotted/authorswithmostbook.png')
plt.show()
plt.clf()

dd = df.sort_values(by=['ratings_count'],ascending=False).head(30)
number_books_most = dd[['authors','bookID']].groupby(['authors'],as_index=False).count().sort_values(by=['bookID'],ascending=False)
sns.barplot(x='average_rating',y='authors',data=dd,palette=("husl")).set_title('Top Rated Authors')
plt.savefig(f'plotted/topratedauthors.png')
plt.show()
plt.clf()

#plot of dd

sns.set_context('paper')
sns.barplot(x='ratings_count',y='authors',data=dd,palette=("husl")).set_title('Most Popular Authors')
plt.savefig(f'plotted/mostpopularauthor.png')
plt.xlabel('ratings count')
plt.show()
plt.clf()


sns.set_color_codes('bright')
sns.set_style("whitegrid")
high_rated = df[['average_rating','authors','bookID']][df['average_rating']>=4].groupby(['authors'],as_index=False).count().sort_values(by=['bookID'],ascending=False).head(20)
sns.barplot(x='bookID',y='authors',data=high_rated,palette=('summer'),label='average rating').set_title('High Rated Authors and Numbers of Books')
plt.xlabel('Number of Books')
most_rated = df[['ratings_count','authors','bookID']][df['ratings_count']>=1000000].groupby(['authors'],as_index=False).count().sort_values(by=['bookID'],ascending=False).head(20)
sns.barplot(x='bookID',y='authors',data=most_rated,palette=("spring"),label='ratings count').set_title('Most Popular Authors with average rating >= 4 and ratings count >= 1000000')
plt.xlabel('Number of Books')
plt.legend(ncol = 2, loc = 'lower right', fontsize='x-small')
plt.savefig(f'plotted/topratedmostpopular.png')
plt.show()
plt.clf()




normalized_df=dd[['average_rating','ratings_count']]/dd[['average_rating','ratings_count']].max()
normalized_df['authors']=dd['authors']
# normalized_df
f, ax = plt.subplots()
sns.set_color_codes('muted')
sns.barplot(x = 'ratings_count', y = 'authors', data = normalized_df,
            label = 'ratings count', color = 'r', edgecolor = 'w')
# sns.set_color_codes('hot')
sns.barplot(x = 'average_rating', y = 'authors', data = normalized_df,
            label = 'average rating', color = 'b',alpha=0.6, edgecolor = 'w')
plt.xlabel('normalized count')
ax.legend(ncol = 2, loc = 'lower right', fontsize='x-small')
plt.savefig(f'plotted/normalized_authors.png')
plt.show()
plt.clf()

df['ratings_count']=df['ratings_count'][df['ratings_count']<3000000]
df['text_count']=df['text_count'][df['text_count']<60000]
sns.set(style="darkgrid")
sns.relplot(x='text_count',y='ratings_count',size='average_rating',sizes=(15,200),alpha=0.5,data=df,label='rating_count',color='orchid')
plt.xlabel('text review count')
plt.ylabel('ratings count')
plt.savefig(f'plotted/Textvsrating_average.png')
plt.show()
plt.clf()