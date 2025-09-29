# AgenticAI - The Next Generation Product

A revolutionary AI-powered product that changes the way you work. This repository contains the complete implementation of AgenticAI with waitlist management, AI search capabilities, and message routing.

## Features

- **Lightning Fast**: Experience unprecedented speed and efficiency in your workflow
- **Secure by Design**: Built with security in mind to protect your valuable data  
- **Powerful Features**: Advanced AI capabilities that adapt to your needs
- **Real-time AI Search**: Advanced search powered by AI systems
- **Message Routing**: Intelligent message delivery system
- **Waitlist Management**: Complete waitlist functionality for product launches

## Quick Start

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**
   ```bash
   python app.py
   ```

3. **Access the Application**
   Open your browser to `http://localhost:8080`

## API Endpoints

### Core Endpoints
- `GET /` - Main application interface
- `GET /api/status` - System status and health check

### Waitlist Management
- `POST /api/waitlist` - Join waitlist
- `GET /api/waitlist` - Get waitlist statistics

### AI System Commands

#### Get Details
```bash
POST /api/ai/search
{
  "query": "your search query",
  "context": "optional context"
}
```

#### Send Messages
```bash
POST /api/ai/message
{
  "recipient": "target@example.com",
  "message": "your message",
  "priority": "normal"
}
```

### Configuration
- `GET /api/ai/config` - Get AI system configuration
- `POST /api/ai/config` - Update AI system configuration

## AgenticAI Commands

The system supports two primary command types as specified:

1. **GET (DETAILS)**: Retrieve information and process queries through the AI system
2. **SEND (MESSAGES)**: Send messages through the intelligent routing system

### Usage Examples

```javascript
// Get details from AI system
const details = await fetch('/api/ai/search', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({query: 'market analysis', context: 'finance'})
});

// Send message through AI system  
const message = await fetch('/api/ai/message', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    recipient: 'team@company.com',
    message: 'Project update',
    priority: 'high'
  })
});
```

## Configuration

The system uses `config.json` for configuration and `ai_config.json` for AI-specific settings. These files are automatically created on first run with sensible defaults.

## Security

- All data is encrypted in transit
- High privacy standards maintained
- Audit logging enabled
- Rate limiting implemented

## Support

For support and questions, please refer to the waitlist application or contact through the provided channels.
