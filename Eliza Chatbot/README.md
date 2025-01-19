
# 🤖 Eliza Chatbot

Eliza is an interactive chatbot inspired by the original program created by Joseph Weizenbaum in the 1960s. It simulates a conversation by using pattern matching and simple substitutions to provide engaging responses to user inputs. This version of Eliza has been enhanced with modern Python techniques and custom substitution patterns.

## ✨ Features
- 💬 Simulates natural language conversations.
- 🔍 Recognizes and responds to keywords and phrases dynamically.
- 🤝 Offers context-aware responses based on user inputs.
- 🎮 Covers a range of topics, including gaming, emotions, and casual questions.

## 🛠️ How It Works
1. **🔗 Pattern Matching**: 
   - User inputs are matched against predefined regular expressions.
   - Patterns include cases like:
     - 🗣️ Introducing oneself (e.g., "My name is Aymane").
     - 😢 Expressing emotions (e.g., "I feel sad").
     - 🎮 Asking for recommendations (e.g., "Can you suggest a survival game?").

2. **🔄 Dynamic Substitutions**:
   - Captured keywords (using regex groups) are inserted into template responses.
   - For example:
     - Input: *"My name is Aymane."*
     - Response: *"Hello, Aymane! How can I assist you today?"*

3. **⚙️ Fallback Handling**:
   - If no pattern matches, Eliza responds with a generic message, encouraging the user to elaborate: 
     - *"I'm not sure I understand. Could you elaborate?"*

## ▶️ Usage
To start the chatbot:
1. Run the Python script:
   ```bash
   python eliza.py

2. Eliza will prompt you to start the conversation.
3. 🛑 Make sure your inputs are in lower case.
4. Continue the conversation by typing your responses.
5. To exit, type bye or goodbye. 
## 🗨️ Example Conversation  
Eliza: Welcome to Eliza Chatbot! What's your name?  

  
You: my name is Aymane.  

  
Eliza: Hello, Aymane! How can I assist you today?  

  

You: i like gaming.  

  
Eliza: What kind of video games do you enjoy?  

  
You: i feel sad.  

  
Eliza: I'm sorry to hear that you're feeling sad. Would you like to talk more about it?  

  

You: goodbye.  

  
Eliza: Bye! Take care!




