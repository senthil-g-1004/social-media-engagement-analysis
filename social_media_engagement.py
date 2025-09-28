# 📊 Social Media Engagement Analysis Project

# Step 1: Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Show plots inline (for Jupyter)
%matplotlib inline

# Step 2: Create Dummy Dataset
data = {
    "Post_ID": range(1, 11),
    "User": ["Alice", "Bob", "Charlie", "David", "Eva",
             "Alice", "Bob", "Charlie", "David", "Eva"],
    "Likes": [120, 340, 560, 230, 150, 430, 210, 300, 90, 600],
    "Comments": [15, 45, 60, 20, 10, 35, 25, 30, 5, 70],
    "Shares": [12, 30, 40, 15, 8, 20, 10, 25, 4, 50]
}

df = pd.DataFrame(data)
df["Total_Engagement"] = df["Likes"] + df["Comments"] + df["Shares"]

# Save dataset to CSV
df.to_csv("social_media_dataset.csv", index=False)

print("✅ Dataset created and saved as social_media_dataset.csv")
print(df.head())

# Step 3: Summary Statistics
print("\n📈 Summary Statistics:")
print(df.describe())

# Step 4: Average Engagement per User
print("\n👥 Average Engagement per User:")
user_avg = df.groupby("User")[["Likes", "Comments", "Shares", "Total_Engagement"]].mean()
print(user_avg)

# Step 5: Find the Most Engaging Post
print("\n🔥 Most Engaging Post:")
print(df.loc[df["Total_Engagement"].idxmax()])

# Step 6: Visualizations

## Total Likes by User
sns.barplot(x="User", y="Likes", data=df, estimator=sum)
plt.title("Total Likes by User")
plt.show()

## Total Comments by User
sns.barplot(x="User", y="Comments", data=df, estimator=sum)
plt.title("Total Comments by User")
plt.show()

## Total Shares by User
sns.barplot(x="User", y="Shares", data=df, estimator=sum)
plt.title("Total Shares by User")
plt.show()

## Total Engagement per Post
plt.figure(figsize=(10,5))
sns.barplot(x="Post_ID", y="Total_Engagement", data=df)
plt.title("Total Engagement per Post")
plt.show()

# Step 7: Save Final Results
user_avg.to_csv("user_average_engagement.csv")
print("\n💾 Results saved to user_average_engagement.csv")
