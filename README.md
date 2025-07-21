# Deep Research Clone - Streamlit App

An AI-powered research assistant that conducts comprehensive web research using OpenAI's API. This Streamlit application converts the original Jupyter notebook into a modular, user-friendly web interface.

## Features

- 🔍 **Interactive Research Process**: Step-by-step research workflow
- 🤖 **AI-Powered Questions**: Dynamic clarifying questions based on research topic
- 🌐 **Web Search Integration**: Automated web searches using OpenAI's tools
- 📊 **Progress Tracking**: Real-time progress indicators during research
- 📄 **Report Generation**: Comprehensive research reports with citations
- 💾 **Download Reports**: Export research reports in Markdown format

## Project Structure

```
├── app.py                 # Main Streamlit application
├── research_engine.py     # Core research logic module
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore file
├── README.md             # Project documentation
└── .env                  # Environment variables (create this)
```

## Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd deep-research-clone
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

### Running the Application
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

### Research Workflow

1. **Enter Research Topic**: Input the topic you want to research
2. **Answer Clarifying Questions**: Respond to 5 AI-generated questions to refine your research scope
3. **Automatic Research**: The app conducts web searches and evaluates data quality
4. **Generate Report**: Receive a comprehensive research report with citations
5. **Download Results**: Export your research report in Markdown format

## Technical Details

### Dependencies
- **Streamlit 1.32.0**: Web application framework
- **OpenAI 1.78.1**: OpenAI API client
- **python-dotenv 1.0.0**: Environment variable management

### Architecture
- **Modular Design**: Core research logic separated into `research_engine.py`
- **Session Management**: Streamlit session state for multi-step workflow
- **Error Handling**: Graceful fallbacks for API failures
- **Progress Tracking**: Real-time updates during research process

### API Integration
The application uses OpenAI's API for:
- Generating clarifying questions
- Creating research goals and search queries
- Conducting web searches
- Evaluating research completeness
- Generating final reports

## Configuration

### OpenAI Models
- **Primary Model**: `gpt-4o` for complex tasks
- **Secondary Model**: `gpt-4o-mini` for simpler tasks
- **Tools**: Web search integration

### Research Parameters
- **Initial Queries**: 5 search queries per research session
- **Max Iterations**: 3 additional search rounds if needed
- **Evaluation Criteria**: AI-determined research completeness

## Development

### Adding New Features
1. Modify `research_engine.py` for core logic changes
2. Update `app.py` for UI/UX improvements
3. Test with different research topics
4. Update requirements.txt if adding new dependencies

### Testing
```bash
# Run the application
streamlit run app.py

# Test with different research topics
# Verify API key configuration
# Check error handling
```

## Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure `.env` file exists with `OPENAI_API_KEY`
   - Verify API key is valid and has sufficient credits

2. **Import Errors**
   - Activate virtual environment
   - Install dependencies: `pip install -r requirements.txt`

3. **Web Search Failures**
   - Check OpenAI API status
   - Verify web search tool availability
   - Review API rate limits

### Error Handling
The application includes fallback mechanisms for:
- API failures
- Network issues
- Invalid responses
- Rate limiting

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Original Jupyter notebook implementation
- OpenAI API for AI capabilities
- Streamlit for the web interface framework 