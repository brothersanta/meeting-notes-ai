import streamlit as st
import requests

st.title("🎙 Meeting Notes Generator")

# Upload audio file (.mp3 or .wav)
audio_file = st.file_uploader("Upload your meeting audio (.mp3 or .wav)", type=["mp3", "wav"])

# If audio file is uploaded
if audio_file:
    st.audio(audio_file)

    # On button click
    if st.button("Generate Notes"):
        with st.spinner("Processing..."):
            response = requests.post(
                "http://localhost:8000/process/",
                files={"file": audio_file.getvalue()}
            )

            if response.status_code == 200:
                output = response.json()

                st.subheader("📝 Summary:")
                st.write(output["summary"])

                st.subheader("✅ Action Items:")
                st.write(output["action_items"])

                with st.expander("📄 Full Transcript"):
                    st.text_area("Transcript", value=output["transcript"], height=300)
            else:
                st.error("Something went wrong. Please try again.")

