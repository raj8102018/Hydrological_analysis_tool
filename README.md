# README: Hydrological Analysis Streamlit App  

## Overview  

This project is a **hydrological analysis tool** built using `dspy` and deployed with **Streamlit**. It utilizes **Ollama's Llama 3.2 (1B model)** for generating concise assessments based on groundwater levels, location, and criticality. The model provides **recommendations, potential risks, causes of water scarcity, and mitigation measures** considering urbanization and water demand.

## Features  

- **AI-powered analysis** for groundwater conditions.  
- **User input fields**: Location, Groundwater Level, Criticality.  
- **Insights** on water scarcity, risks, and mitigation strategies.  
- **Streamlit-based UI** for easy interaction.  

## Installation  

### Prerequisites  

Ensure you have the following installed:  

- **Python 3.8+**  
- **Streamlit** (`pip install streamlit`)  
- **dspy** (`pip install dspy`)  
- **Ollama** ([Install Ollama](https://ollama.com))  or **groq**
- **Llama 3.2 model (1B parameter version)**  

### Setup  

1. Clone the repository:  
   ```sh
   git clone <repo-url>
   cd <repo-folder>
   ```  

2. Install dependencies:  
   ```sh
   pip install -r requirements.txt
   ```  

3. Start **Ollama** locally:  
   ```sh
   ollama run llama3.2:1b
   ```
   or instead you can set up your groq api key in the environment variables

4. Run the Streamlit app:  
   ```sh
   streamlit run app.py
   ```  

## Usage  

1. Open the Streamlit app in your browser.  
2. Enter the required inputs:
   - **Location** (e.g., "Warangal, Telangana, India")
   - **Groundwater Level** (e.g., "6.4 - 8 ft below ground")
   - **Criticality** (e.g., "Low for water scarcity")  
3. Click **Analyze** to generate insights.  
4. View recommendations, potential risks, and mitigation measures.  
---
