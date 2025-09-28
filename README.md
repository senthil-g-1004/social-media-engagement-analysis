# Social Media Engagement Analysis 📊

This project analyzes engagement metrics across different social media platforms, content types, and posting times to derive insights for better content strategy.  

## 🚀 Dataset
- **File:** `social_media_engagement_dataset.csv`
- **Columns:**
  - `Platform` → Instagram, YouTube, Twitter, LinkedIn
  - `ContentType` → Image, Video, Text, Reel
  - `Likes, Comments, Shares, Impressions`
  - `PostedTime` → Morning, Afternoon, Evening, Night
  - `EngagementRate` (calculated)

## 🛠️ Steps Performed
1. **Data Cleaning** → handled 0 impressions.
2. **Feature Engineering** → added Engagement Rate.
3. **Analysis** → average engagement by platform, content type, posting time.
4. **Visualizations** → bar charts showing results.

## 📌 Insights
- Instagram had the **highest engagement**.
- **Videos/Reels** perform better than text or static images.
- **Evening posts** generate more engagement.

## 📂 Files
- `social_media_engagement_dataset.csv` → dataset
- `social_media_engagement_analysis.ipynb` → Jupyter notebook
- `requirements.txt` → dependencies

## 📦 Requirements
Install required libraries:
```bash
pip install -r requirements.txt
```

## 🖥️ How to Run
1. Clone this repository  
   ```bash
   git clone https://github.com/yourusername/social-media-engagement-analysis.git
   ```
2. Open Jupyter Notebook  
   ```bash
   jupyter notebook social_media_engagement_analysis.ipynb
   ```

---
✨ Made with Python (Pandas, Matplotlib)
