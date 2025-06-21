from summarizer import summarize_text
import streamlit as st

def main():
    # Page config
    st.set_page_config(
        page_title="Text Summarizer",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Title and description
    st.title("Text Summarizer")
    st.markdown("Enter your text on the left and get a summary on the right.")
    
    # Create two columns for input and output
    col1, col2 = st.columns(2)
    
    # Input section
    with col1:
        st.header("Input Text")
        input_text = st.text_area("Enter text to summarize:", height=400)
        
        # Mode selection
        mode = st.radio(
            "Select summary length:",
            ["normal", "short", "very short"],
            captions=["75% of original", "50% of original", "25% of original"]
        )
        
        # Map "very short" option to "v_short" for processing
        mode_key = "v_short" if mode == "very short" else mode
        
        summary_button = st.button("Summarize")
    
    # Output section
    with col2:
        st.header("Summary")
        if summary_button and input_text:
            with st.spinner("Generating summary..."):
                # Calculate max and min lengths based on mode
                normal = 3/4
                short = 1/2
                v_short = 1/4
                len_text = len(input_text.split())
                
                if mode_key == 'normal':
                    max_len = int((len_text)*(normal))
                    min_len = int(len_text*(normal/2))
                elif mode_key == 'short':
                    max_len = int(len_text*short)
                    min_len = int(len_text*(short/2))
                else:  # v_short
                    max_len = int(len_text*v_short)
                    min_len = int(len_text*(v_short/2))
                
                # For debugging (can be removed in production)
                st.caption(f"Text length: {len_text} words")
                st.caption(f"Target summary length: {min_len}-{max_len} words")
                
                # Generate the summary with the specified parameters
                summary = summarize_text(input_text, max_len=max_len, min_len=min_len)
                
                st.success("Summary generated!")
                st.text_area("Summary result:", value=summary, height=400, disabled=True)
        else:
            st.info("Your summary will appear here after you click 'Summarize'")
    
    # Footer
    st.markdown("---")
    st.caption("Powered by TextSummarizer")

if __name__ == "__main__":
    main()
