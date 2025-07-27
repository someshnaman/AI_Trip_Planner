# AI Trip Planner

AI Trip Planner is an intelligent assistant that helps users plan trips by leveraging advanced AI models, real-time data, and web search/crawling capabilities.

## Features

- AI-powered travel itinerary generation
- Real-time weather and place information
- Integration with multiple APIs (OpenAI, Tavily, Google Places, Foursquare, OpenWeatherMap, etc.)
- Modular agentic workflow for extensibility
- Web interface with Streamlit and FastAPI

## Project Structure

```
.
├── app.py
├── main.py
├── requirements.txt
├── setup.py
├── pyproject.toml
├── .env
├── agent/
│   ├── __init__.py
│   ├── Agent_bot.py
│   └── agentic_workflow.py
├── config/
│   ├── __init__.py
│   └── config.yaml
├── utils/
├── tools/
├── promtp_library/
├── logger/
├── experment/
└── env/
```

## Getting Started

### 1. Clone the repository

```sh
git clone <your-repo-url>
cd AI_Trip_Planner
```

### 2. Set up the environment

Create a virtual environment and activate it:

```sh
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```

### 4. Configure environment variables

Edit the `.env` file and add your API keys:

```env
OPENAI_API_KEY="your-openai-key"
TAVILY_API_KEY="your-tavily-key"
GOOGLE_API_KEY="your-google-key"
EURI_API_KEY="your-euri-key"
...
```

### 5. Run the application

For the FastAPI server:

```sh
uvicorn app:app --reload
```

For the Streamlit interface:

```sh
streamlit run main.py
```

## Usage

- Access the web UI to interact with the AI Trip Planner.
- Use the API endpoints for programmatic access.

## Development

- Modular codebase for easy extension.
- Add new tools in the `tools/` directory.
- Update prompts in `promtp_library/`.

## License

MIT

---

**Contributors:**  
Somesh Chitranshi

---

> Powered by OpenAI, Tavily, Google, and more.