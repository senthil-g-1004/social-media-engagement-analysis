# 📊 Social Media Engagement Analysis Project


# --------------------------
# Step 1: Import Libraries
# --------------------------
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------
# Step 2: Load Dataset
# --------------------------
df = pd.read_csv("social_media_engagement_dataset.csv")

# Quick look at the dataset
print("First 5 rows:")
print(df.head())

# --------------------------
# Step 3: Data Cleaning
# --------------------------
# Replace 0 impressions with median to avoid divide by zero
df["Impressions"] = df["Impressions"].replace(0, df["Impressions"].median())

# --------------------------
# Step 4: Feature Engineering - Engagement Rate
# --------------------------
# Formula = (Likes + Comments + Shares) / Impressions * 100
df["EngagementRate"] = ((df["Likes"] + df["Comments"] + df["Shares"]) / df["Impressions"]) * 100

# --------------------------
# Step 5: Analysis using GroupBy
# --------------------------
# Average engagement per platform
avg_platform = df.groupby("Platform")["EngagementRate"].mean().sort_values(ascending=False)
print("\nAverage Engagement Rate by Platform:")
print(avg_platform)

# Average engagement per content type
avg_content = df.groupby("ContentType")["EngagementRate"].mean().sort_values(ascending=False)
print("\nAverage Engagement Rate by Content Type:")
print(avg_content)

# Best posting time
avg_time = df.groupby("PostedTime")["EngagementRate"].mean().sort_values(ascending=False)
print("\nAverage Engagement Rate by Posting Time:")
print(avg_time)

# --------------------------
# Step 6: Visualizations
# --------------------------
# Platform performance
plt.figure(figsize=(6,4))
avg_platform.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Average Engagement Rate by Platform")
plt.ylabel("Engagement Rate (%)")
plt.xlabel("Platform")
plt.show()

# Content type performance
plt.figure(figsize=(6,4))
avg_content.plot(kind="bar", color="lightgreen", edgecolor="black")
plt.title("Average Engagement Rate by Content Type")
plt.ylabel("Engagement Rate (%)")
plt.xlabel("Content Type")
plt.show()

# Posting time performance
plt.figure(figsize=(6,4))
avg_time.plot(kind="bar", color="salmon", edgecolor="black")
plt.title("Average Engagement Rate by Posting Time")
plt.ylabel("Engagement Rate (%)")
plt.xlabel("Time of Day")
plt.show()

# --------------------------
# Step 7: Export Insights
# --------------------------
avg_platform.to_csv("avg_platform.csv")
avg_content.to_csv("avg_content.csv")
avg_time.to_csv("avg_time.csv")

print("\nAnalysis complete! Charts displayed and results saved to CSV files.")

