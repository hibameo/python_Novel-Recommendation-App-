import streamlit as st
import requests

# App ka title
st.title("Novel Recommendation App")

# Genre selection ke liye dropdown
genre = st.selectbox("Select a Genre", 
                     ["Romance", "Mystery", "Fantasy", "Sci-Fi", "Thriller", "Historical", "Non-fiction"])

# Button dabane par recommendations fetch karna
if st.button("Get Recommendations"):
    # Google Books API ke liye query banayein (genre ke sath 'novel' add kar rahe hain)
    query = f"{genre} novel"
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults=10"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        books = data.get("items", [])
        
        if books:
            for book in books:
                info = book.get("volumeInfo", {})
                title = info.get("title", "No Title")
                authors = info.get("authors", ["Unknown"])
                description = info.get("description", "Description not available.")
                
                st.subheader(title)
                st.write("Author(s):", ", ".join(authors))
                st.write(description)
                st.markdown("---")
        else:
            st.write("No books found for this genre!")
    else:
        st.write("Error fetching data from Google Books API.")

