# ⚔️🔗 EmpireChain

⚡ An orchestration framework for all your AI needs ⚡

```
    ███████╗███╗   ███╗██████╗ ██╗██████╗ ███████╗
    ██╔════╝████╗ ████║██╔══██╗██║██╔══██╗██╔════╝
    █████╗  ██╔████╔██║██████╔╝██║██████╔╝█████╗  
    ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║██╔══██╗██╔══╝  
    ███████╗██║ ╚═╝ ██║██║     ██║██║  ██║███████╗
    ╚══════╝╚═╝     ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝
     ██████╗██╗  ██╗ █████╗ ██╗███╗   ██╗
    ██╔════╝██║  ██║██╔══██╗██║████╗  ██║
    ██║     ███████║███████║██║██╔██╗ ██║
    ██║     ██╔══██║██╔══██║██║██║╚██╗██║
    ╚██████╗██║  ██║██║  ██║██║██║ ╚████║
     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
    =============================================
         🔗 Chain Your AI Dreams Together 🔗
    =============================================
```

<p align="center">
  <a href="https://pypi.org/project/empire-chain/">
    <img src="https://img.shields.io/pypi/v/empire-chain" alt="PyPI version">
  </a>
  <a href="https://pypi.org/project/empire-chain/">
    <img src="https://img.shields.io/pypi/dm/empire-chain" alt="PyPI downloads">
  </a>
  <a href="https://github.com/manas95826/empire-chain/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License">
  </a>
  <a href="https://github.com/manas95826/empire-chain/stargazers">
    <img src="https://img.shields.io/github/stars/manas95826/empire-chain" alt="GitHub stars">
  </a>
</p>

## Features

- 🤖 Multiple LLM Support (OpenAI, Anthropic, Groq)
- 📚 Vector Store Integration (Qdrant, ChromaDB)
- 🔍 Advanced Document Processing
- 🎙️ Speech-to-Text Capabilities
- 🌐 Web Crawling with crawl4ai
- 📊 Data Visualization
- 🎯 RAG Applications
- 🤝 PhiData Agent Integration
- 💬 Interactive Chatbots
- 🤖 Agentic Framework

## Installation

```bash
pip install empire-chain
```

## Core Components

### Agent

```python
from empire_chain.agent import Agent
from dotenv import load_dotenv

load_dotenv()

def get_weather(location: str) -> str:
    """Simulated weather function"""
    return f"The weather in {location} is sunny!"

def calculate_distance(from_city: str, to_city: str) -> str:
    """Simulated distance calculator"""
    return f"The distance from {from_city} to {to_city} is 500km"

agent = Agent()
agent.register_function(get_weather)
agent.register_function(calculate_distance)
result = agent.process_query("What's the weather like in New York?")
print(result)
```

### Document Processing

```python
from empire_chain.file_reader import DocumentReader

reader = DocumentReader()
text = reader.read("your_file_path")  # Supports PDF, DOCX, and more
```

### Speech-to-Text

```python
from empire_chain.stt import GroqSTT

stt = GroqSTT()
text = stt.transcribe("audio_file.mp3")
```

### LLM Integration

```python
from empire_chain.llms import OpenAILLM, AnthropicLLM, GroqLLM

openai_llm = OpenAILLM("gpt-4")
anthropic_llm = AnthropicLLM("claude-3-sonnet")
groq_llm = GroqLLM("mixtral-8x7b")
```

### Vector Stores

```python
from empire_chain.vector_stores import QdrantVectorStore, ChromaVectorStore
from empire_chain.embeddings import OpenAIEmbeddings

vector_store = QdrantVectorStore(":memory:")
embeddings = OpenAIEmbeddings("text-embedding-3-small")
```

### Web Crawling

```python
from empire_chain.crawl4ai import Crawler

crawler = Crawler()
data = crawler.crawl("https://example.com")
```

### Data Visualization

```python
from empire_chain.visualizer import DataAnalyzer, ChartFactory

analyzer = DataAnalyzer()
analyzed_data = analyzer.analyze(your_data)
chart = ChartFactory.create_chart('Bar Graph', analyzed_data)
chart.show()
```

### Interactive Chatbots

```python
from empire_chain.streamlit import Chatbot, VisionChatbot, PDFChatbot

# Simple Chatbot
chatbot = Chatbot(llm=OpenAILLM("gpt-4"), title="Empire Chain Chatbot")
chatbot.chat()

# Vision Chatbot
vision_bot = VisionChatbot(title="Vision Assistant")
vision_bot.chat()

# PDF Chatbot
pdf_bot = PDFChatbot(
    title="PDF Assistant",
    llm=OpenAILLM("gpt-4"),
    vector_store=QdrantVectorStore(":memory:"),
    embeddings=OpenAIEmbeddings("text-embedding-3-small")
)
pdf_bot.chat()
```

### PhiData Agents

```python
# cookbooks/phidata/web_agent.py
"""
This is a simple example of how to use the WebAgent class to generate web data.
Please run the following command to install the necessary dependencies and store keys in .env:
!pip install empire-chain phidata duckduckgo-search
"""
from empire_chain.phidata.web_agent import WebAgent

web_agent = WebAgent()
web_agent.generate("What is the price of Tesla?")

# cookbooks/phidata/finance_agent.py
"""
This is a simple example of how to use the PhiFinanceAgent class to generate financial data.
Please run the following command to install the necessary dependencies and store keys in .env:
!pip install empire-chain phidata yfinance
"""
from empire_chain.phidata.finance_agent import PhiFinanceAgent

finance_agent = PhiFinanceAgent()
finance_agent.generate("What is the price of Tesla?")
```

## Example Cookbooks

Check out our cookbooks directory for complete examples:

### RAG Applications
```python
# cookbooks/RAG/empire_rag.py
from empire_chain.vector_stores import QdrantVectorStore
from empire_chain.embeddings import OpenAIEmbeddings
from empire_chain.llms.llms import GroqLLM
from empire_chain.tools.file_reader import DocumentReader
import os
from dotenv import load_dotenv
from empire_chain.stt.stt import GroqSTT

def main(if_audio_input: bool = False):
    load_dotenv()
    
    vector_store = QdrantVectorStore(":memory:")
    embeddings = OpenAIEmbeddings("text-embedding-3-small")
    llm = GroqLLM("llama3-8b-8192")
    reader = DocumentReader()
    
    file_path = "input.pdf"
    text = reader.read(file_path)
    
    text_embedding = embeddings.embed(text)
    vector_store.add(text, text_embedding)
    
    text_query = "What is the main topic of this document?"
    if if_audio_input:
        stt = GroqSTT()
        audio_query = stt.transcribe("audio.mp3")
        query_embedding = embeddings.embed(audio_query)
    else:
        query_embedding = embeddings.embed(text_query)
    relevant_texts = vector_store.query(query_embedding, k=3)
    
    context = "\n".join(relevant_texts)
    prompt = f"Based on the following context, {text_query}\n\nContext: {context}"
    response = llm.generate(prompt)
    print(f"Query: {text_query}")
    print(f"Response: {response}")

if __name__ == "__main__":
    main(if_audio_input=False)
```

### Cool Stuff
```python
# cookbooks/cool_stuff/topic-to-podcast.py
"""
This is a simple example of how to use the GeneratePodcast class to generate a podcast.
Please run the following command to install the necessary dependencies and store keys in .env:
!pip install empire-chain kokoro_onnx (It might take a while to download the model files)
"""
from empire_chain.cool_stuff.podcast import GeneratePodcast

podcast = GeneratePodcast()
podcast.generate(topic="About boom of meal plan and recipe generation apps")

# cookbooks/cool_stuff/visualize_data.py
"""
This is a simple example of how to use the DataAnalyzer and ChartFactory classes to visualize data.
Please run the following command to install the necessary dependencies and store keys in .env:
!pip install empire-chain matplotlib

_chart_types = {
        'Line Chart': LineChart,
        'Pie Chart': PieChart,
        'Bar Graph': BarGraph,
        'Scatter Plot': ScatterChart,
        'Histogram': Histogram,
        'Box Plot': BoxPlot
    }
Please adhere to the naming convention for the chart type.
"""
from empire_chain.cool_stuff.visualizer import DataAnalyzer, ChartFactory

data = """
Empire chain got a fund raise of $100M from a new investor in 2024 and $50M from a new investor in 2023.
"""
    
analyzer = DataAnalyzer()
analyzed_data = analyzer.analyze(data)
        
chart = ChartFactory.create_chart('Bar Chart', analyzed_data)
chart.show()
```

### Tools
```python
# cookbooks/tools/crawler.py
from empire_chain.tools import WebCrawler

crawler = WebCrawler()
data = crawler.crawl("https://example.com")

# cookbooks/tools/docling_md.py
from empire_chain.tools import DocumentProcessor

processor = DocumentProcessor()
processed_text = processor.process("document.pdf")
```

### Chatbots
```python
# cookbooks/chatbots/chat_with_pdf-qdrant.py
"""
This is a simple chatbot that uses the Empire Chain library to create a pdf chatbot.
Please run the following command to install the necessary dependencies and store keys in .env:
!pip install empire-chain streamlit
!streamlit run app.py
"""
from empire_chain.streamlit import PDFChatbot
from empire_chain.llms.llms import OpenAILLM
from empire_chain.vector_stores import QdrantVectorStore
from empire_chain.embeddings import OpenAIEmbeddings

pdf_chatbot = PDFChatbot(title="PDF Chatbot", llm=OpenAILLM("gpt-4o-mini"), vector_store=QdrantVectorStore(":memory:"), embeddings=OpenAIEmbeddings("text-embedding-3-small"))
pdf_chatbot.chat()

# cookbooks/chatbots/chat_with_image.py
"""
This is a simple chatbot that uses the Empire Chain library to create a chatbot.
Please run the following command to install the necessary dependencies and groq key in .env (https://console.groq.com/keys):
!pip install empire-chain streamlit
!streamlit run app.py
"""
from empire_chain.streamlit import VisionChatbot

chatbot = VisionChatbot(title="Empire Chatbot")
chatbot.chat()
```

## Contributing

```bash
git clone https://github.com/manas95826/empire-chain.git
cd empire-chain
pip install -e .
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.