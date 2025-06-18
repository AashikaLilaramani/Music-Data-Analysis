import sqlite3
import objecttier
import pandas as pd
import matplotlib.pyplot as plt

def plot_rev(total_revenue):
    # Unpack the data
    countries = []
    revenues = []
    
    for country, revenue in total_revenue:
        countries.append(country)
        revenues.append(revenue)
    
    # Create a DataFrame
    df = pd.DataFrame({
        'Country': countries,
        'Revenue': revenues
    })

    # Plot
    plt.figure(figsize=(10, 6))
    plt.bar(df['Country'], df['Revenue'], color='mediumseagreen')
    plt.xticks(rotation=45, ha='right')
    plt.title("Revenue by Country")
    plt.xlabel("Country")
    plt.ylabel("Total Revenue ($)")
    plt.tight_layout()
    plt.show()


def plot_monthly_sales(monthly_data):
    months = []
    revenue = []

    for month, total in monthly_data:
        months.append(month)
        revenue.append(total)

    plt.figure(figsize=(10, 6))
    plt.plot(months, revenue, marker='o', linestyle='-', color='royalblue')
    plt.xticks(rotation=45)
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue ($)")
    plt.tight_layout()
    plt.show()


def plot_tracks_by_genre(genre_data):
    labels = []
    counts = []

    for genre, count in genre_data:
        labels.append(genre.Name)
        counts.append(count)

    plt.figure(figsize=(8, 8))
    plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Tracks by Genre")
    plt.tight_layout()
    plt.show()