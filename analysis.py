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