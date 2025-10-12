import streamlit as st
from news_fetcher import search_news  # We only need 'search_news'
from analyzer import summarize_text, analyze_sentiment

# Page setup
st.set_page_config(page_title="GenAI News Analyst", page_icon="🔍")

st.title("🔍 GenAI News Analyst")
st.write("""
Welcome! Enter a topic below to find, summarize, and analyze the latest news.
From 'AI advancements' to 'global market trends', what are you curious about today?
""")

# --- Step 1: Get user input for the topic ---
user_topic = st.text_input("👇 Enter a news topic to search for:")

# --- Step 2: Search for news when the button is clicked ---
if st.button("Search & Analyze News ✨"):
    if user_topic:
        with st.spinner(f"Searching for articles about '{user_topic}'..."):
            # Call our new, API-powered search function
            articles, error = search_news(user_topic)

            if error:
                # Display the error from the news_fetcher
                st.error(f"Oh no! We couldn't fetch the news. Reason: {error}")
            elif not articles:
                st.warning(f"We couldn't find any recent articles on '{user_topic}'. Try another topic!")
            else:
                st.success(f"Found {len(articles)} articles! Now, pick one to analyze.")
                # Use session state to store the fetched articles
                st.session_state.articles = articles

    else:
        st.warning("Please enter a topic to search for.")

# --- Step 3: Display results and allow user to select an article for analysis ---
# This part only runs if articles have been successfully fetched and stored
if 'articles' in st.session_state and st.session_state.articles:
    
    # Create a list of article titles for the selectbox
    article_titles = [article['title'] for article in st.session_state.articles]
    selected_title = st.selectbox("👇 Choose an article to get the AI summary:", article_titles)

    # Find the full article data that matches the selected title
    selected_article = next((article for article in st.session_state.articles if article['title'] == selected_title), None)

    if selected_article:
        # Display a preview of the article
        st.subheader(selected_article['title'])
        st.write(f"**Source:** {selected_article['source']['name']} | **Published on:** {selected_article['publishedAt'].split('T')[0]}")
        st.write(selected_article.get('description', 'No description available.'))
        st.markdown(f"[Read Full Article]({selected_article['url']})", unsafe_allow_html=True)
        
        # The AI analysis part
        text_to_analyze = selected_article.get('content', selected_article.get('description', ''))

        if text_to_analyze and len(text_to_analyze) > 50:
             with st.spinner("Our AI is reading and generating insights..."):
                st.write("---")
                st.subheader("💡 AI-Generated Insights")
                
                # Call our analyzer functions
                sentiment = analyze_sentiment(text_to_analyze)
                st.write(f"**Sentiment Analysis:** {sentiment}")
                
                summary = summarize_text(text_to_analyze)
                st.subheader("📜 Executive Summary")
                st.info(summary)
        else:
            st.warning("The content from the source was too short for a detailed analysis.")

st.markdown("---")
st.write("Built with ❤️ using Streamlit and NewsAPI.org.")
