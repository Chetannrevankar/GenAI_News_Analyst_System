<p align="center">
  <h1 align="center">🤖 GenAI News Analyst System 📰</h1>
</p>

## 🚀 Introduction and Objective

**GenAI News Analyst System** is an AI-powered web application that fetches, summarizes, and analyzes the latest news articles on any topic you choose. Its primary goal is to provide quick, concise news summaries along with sentiment insights, helping users stay informed efficiently and effectively.

---

## ✨ Features

* 📰 Fetches the latest news based on user-input topics using NewsAPI.
* 🤖 Summarizes articles using advanced Hugging Face transformers.
* 📊 Analyzes sentiment for quick understanding of news tone.
* 💻 Streamlit-based user interface for seamless interaction.
* ⚠️ Handles errors robustly and provides helpful messages.

---

## 🛠 Workflow Diagram

![Workflow Diagram](https://github.com/Chetannrevankar/GenAI_News_Analyst_System/blob/main/workflow_diagram.png)
*Elegant workflow diagram showing data flow from user input to AI summary and sentiment display.*

---

## 🧰 Tech Stack & Tools Used

* 🐍 Python 3.7+
* 🌐 Streamlit - Frontend interface
* 🗞 NewsAPI - Fetching news articles
* 🤗 Transformers (Hugging Face) - Summarization & sentiment analysis
* 🔥 Torch - Backend model computations
* 📡 Requests - Web requests to fetch data
* 🍲 BeautifulSoup4 - Parsing HTML data
* 📰 Feedparser - Parsing RSS feeds
* 🔐 python-dotenv - Secure API key management

---

## 📖 How to Use

1. **Clone or download the repository:**

```bash
git clone https://github.com/Chetannrevankar/GenAI_News_Analyst_System.git
cd GenAI_News_Analyst_System
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Add your NewsAPI key in `.env` file:**

```bash
NEWS_API_KEY="your_actual_api_key"
```

4. **Launch the app:**

```bash
streamlit run app.py
```

5. Enter your desired topic, click **Search**, and explore AI-generated summaries and sentiment insights.

---

## ❓ Why Use This App

* ⚡ Save time with automatic summaries of long and complex news stories.
* 🔍 Quickly understand the sentiment behind trending news.
* 🌍 Stay updated on topics of interest without information overload.

---

## 🎯 Target Users

* Business executives & market analysts tracking trends.
* Researchers & students seeking quick insights.
* News followers who prefer concise summaries.
* Developers & AI enthusiasts exploring NLP capabilities.

---

## 📸 Sample Screenshots

| Screenshot                                                                                                                                                   | Description                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------- |
| ![Backend Architecture](https://github.com/Chetannrevankar/GenAI_News_Analyst_System/blob/main/Snapshots/Backend.png)                                        | 🏗 Backend architecture showing data flow.    |
| ![Frontend Input](https://github.com/Chetannrevankar/GenAI_News_Analyst_System/blob/main/Snapshots/Frontend.png)                                             | 🖥 User input interface.                      |
| ![No Input Warning](https://github.com/Chetannrevankar/GenAI_News_Analyst_System/blob/main/Snapshots/NoInput.png)                                            | ⚠️ Warning when the input field is empty.     |
| ![Redirect to Article](https://github.com/Chetannrevankar/GenAI_News_Analyst_System/blob/main/Snapshots/Redirect_Microsoft_article.png)                      | 🔗 Redirect to full web article.              |
| ![Topic AI India](https://github.com/Chetannrevankar/GenAI_News_Analyst_System/blob/main/Snapshots/TopicAI_India.png)                                        | 🌏 Example of a selected news topic.          |
| ![Summary & Sentiment](https://github.com/Chetannrevankar/GenAI_News_Analyst_System/blob/main/Snapshots/TopicAI_India_article_EthicalFrameworks_summary.png) | 💡 AI-generated summary & sentiment analysis. |

---

## ✍️ Authors

**Chetan N Revankar**

<p>
    <a href="https://github.com/Chetannrevankar" target="_blank">GitHub</a> | 
    <a href="https://www.linkedin.com/in/chetannrevankar/" target="_blank">LinkedIn</a>
  </p>

---


## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
