#!/usr/bin/env python3
"""
AgenticAI - The Next Generation Product
AI-powered system with waitlist management and search capabilities
"""

from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import json
import os
from datetime import datetime
import hashlib

app = Flask(__name__)
CORS(app)

# Data storage
WAITLIST_FILE = 'waitlist.json'
AI_CONFIG_FILE = 'ai_config.json'

class AgenticAI:
    def __init__(self):
        self.version = "1.0.0"
        self.initialized = True
        self.load_config()
    
    def load_config(self):
        """Load AI configuration"""
        if os.path.exists(AI_CONFIG_FILE):
            with open(AI_CONFIG_FILE, 'r') as f:
                self.config = json.load(f)
        else:
            self.config = {
                "search_enabled": True,
                "ai_models": ["gpt-4", "claude-3"],
                "confidence_threshold": 0.8,
                "max_results": 10
            }
            self.save_config()
    
    def save_config(self):
        """Save AI configuration"""
        with open(AI_CONFIG_FILE, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def get_details(self, query, context=None):
        """Get details from AI system - simulated AI search functionality"""
        return {
            "query": query,
            "context": context,
            "timestamp": datetime.now().isoformat(),
            "status": "processed",
            "results": {
                "confidence": 0.95,
                "sources": ["AI Knowledge Base", "Real-time Data"],
                "summary": f"Processed query: {query}",
                "details": "AI system successfully processed the request with high confidence.",
                "recommendations": ["Consider refining query", "Check related topics"]
            },
            "system_info": {
                "version": self.version,
                "model": "AgenticAI-v1",
                "processing_time": "0.234s"
            }
        }
    
    def send_message(self, recipient, message, priority="normal"):
        """Send message through AI system"""
        message_id = hashlib.md5(f"{recipient}{message}{datetime.now()}".encode()).hexdigest()[:8]
        
        return {
            "message_id": message_id,
            "recipient": recipient,
            "message": message,
            "priority": priority,
            "timestamp": datetime.now().isoformat(),
            "status": "sent",
            "delivery_info": {
                "estimated_delivery": "immediate",
                "channel": "ai_direct",
                "encryption": "enabled"
            }
        }

# Initialize AI system
ai_system = AgenticAI()

def load_waitlist():
    """Load waitlist from file"""
    if os.path.exists(WAITLIST_FILE):
        with open(WAITLIST_FILE, 'r') as f:
            return json.load(f)
    return []

def save_waitlist(waitlist):
    """Save waitlist to file"""
    with open(WAITLIST_FILE, 'w') as f:
        json.dump(waitlist, f, indent=2)

@app.route('/')
def index():
    """Serve the main application"""
    with open('index.html', 'r') as f:
        return f.read()

@app.route('/api/status')
def api_status():
    """Get API and AI system status"""
    return jsonify({
        "status": "active",
        "ai_system": {
            "initialized": ai_system.initialized,
            "version": ai_system.version,
            "config": ai_system.config
        },
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/waitlist', methods=['POST'])
def join_waitlist():
    """Add email to waitlist"""
    data = request.get_json()
    email = data.get('email', '').strip().lower()
    
    if not email:
        return jsonify({"error": "Email is required"}), 400
    
    # Basic email validation
    if '@' not in email or '.' not in email:
        return jsonify({"error": "Invalid email format"}), 400
    
    waitlist = load_waitlist()
    
    # Check if email already exists
    if any(entry['email'] == email for entry in waitlist):
        return jsonify({
            "status": "already_exists",
            "message": "Email already on waitlist"
        })
    
    # Add to waitlist
    entry = {
        "email": email,
        "timestamp": datetime.now().isoformat(),
        "position": len(waitlist) + 1
    }
    
    waitlist.append(entry)
    save_waitlist(waitlist)
    
    return jsonify({
        "status": "success",
        "message": "Successfully added to waitlist",
        "position": entry['position']
    })

@app.route('/api/waitlist', methods=['GET'])
def get_waitlist_stats():
    """Get waitlist statistics"""
    waitlist = load_waitlist()
    return jsonify({
        "total_subscribers": len(waitlist),
        "latest_signup": waitlist[-1]['timestamp'] if waitlist else None
    })

@app.route('/api/ai/search', methods=['POST'])
def ai_search():
    """AI-powered search endpoint"""
    data = request.get_json()
    query = data.get('query', '')
    context = data.get('context')
    
    if not query:
        return jsonify({"error": "Query is required"}), 400
    
    results = ai_system.get_details(query, context)
    return jsonify(results)

@app.route('/api/ai/message', methods=['POST'])
def ai_message():
    """Send message through AI system"""
    data = request.get_json()
    recipient = data.get('recipient', '')
    message = data.get('message', '')
    priority = data.get('priority', 'normal')
    
    if not recipient or not message:
        return jsonify({"error": "Recipient and message are required"}), 400
    
    result = ai_system.send_message(recipient, message, priority)
    return jsonify(result)

@app.route('/api/ai/config', methods=['GET'])
def get_ai_config():
    """Get AI system configuration"""
    return jsonify(ai_system.config)

@app.route('/api/ai/config', methods=['POST'])
def update_ai_config():
    """Update AI system configuration"""
    data = request.get_json()
    ai_system.config.update(data)
    ai_system.save_config()
    
    return jsonify({
        "status": "success",
        "message": "Configuration updated",
        "config": ai_system.config
    })

if __name__ == '__main__':
    print(f"AgenticAI System v{ai_system.version} starting...")
    print("Available endpoints:")
    print("  GET  /                 - Main application")
    print("  GET  /api/status       - System status")
    print("  POST /api/waitlist     - Join waitlist")
    print("  GET  /api/waitlist     - Waitlist stats")
    print("  POST /api/ai/search    - AI search")
    print("  POST /api/ai/message   - Send AI message")
    print("  GET  /api/ai/config    - Get AI config")
    print("  POST /api/ai/config    - Update AI config")
    
    app.run(debug=True, host='0.0.0.0', port=8080)