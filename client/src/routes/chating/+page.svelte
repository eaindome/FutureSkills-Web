<script lang="ts">
    import { onMount } from 'svelte';
    // @ts-ignore
    import { v4 as uuidv4 } from 'uuid';
    import ChatContainer from './components/layout/ChatContainer.svelte';
    import InputArea from './components/layout/InputArea.svelte';
    
    // Mock data for the chat history
    let messages = [
      {
        id: uuidv4(),
        content: "Hi there! I'm your FutureSkills AI Coach. I can help you navigate career transitions, find green jobs, suggest courses, and recommend side hustles for extra income. What would you like to know today?",
        isUser: false,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      }
    ];
    
    let isTyping = false;
    
    // Mock AI response function - In production, this would call your actual API
    async function getAIResponse(userMessage: string) {
      isTyping = true;
      
      // Simulate API delay
      await new Promise(resolve => setTimeout(resolve, 1000));
      
      let response = "";
      
      // Mock responses based on user query
      if (userMessage.toLowerCase().includes("risk")) {
        response = "Based on automation trends, cashier roles have about 75% risk of displacement by 2030. However, your customer service skills could transfer well to sustainable retail or clean energy customer success roles.";
      } else if (userMessage.toLowerCase().includes("green job")) {
        response = "Here are some green jobs that might match your skills:\n\n1. Solar Panel Installer (Growth: +52% by 2030)\n2. Sustainability Coordinator (+25%)\n3. Green Building Consultant (+15%)\n\nWhich one interests you most?";
      } else if (userMessage.toLowerCase().includes("course")) {
        response = "Based on your interest in sustainability, I recommend:\n\n• Coursera: Green Supply Chain Management ($49, 4 weeks)\n• EdX: Introduction to Solar Energy (Free, 6 weeks)\n• LinkedIn Learning: ESG Fundamentals ($29.99, self-paced)";
      } else if (userMessage.toLowerCase().includes("hustle") || userMessage.toLowerCase().includes("side")) {
        response = "Here are some eco-friendly side hustles that could earn you $200-500/month while you reskill:\n\n• Upcycled Product Creator on Etsy\n• Energy Efficiency Consultant for small businesses\n• Virtual Assistant for sustainable brands";
      } else if (userMessage.toLowerCase().includes("renewable energy")) {
        response = "To start in renewable energy without prior experience:\n\n1. Take an intro online course like 'Solar Energy Basics'\n2. Earn the Entry Level NABCEP Certification\n3. Apply for installer assistant roles or internships\n4. Network at renewable energy meetups and job fairs";
      } else {
        response = "Thanks for your question! I'm here to help with career transitions to green jobs, risk assessment, training paths, and sustainable side hustles. Could you tell me more about what specific aspect you're interested in?";
      }
      
      isTyping = false;
      
      return response;
    }
    
    async function handleMessageSend(event: CustomEvent<string>) {
      const userMessage = event.detail;
      
      // Add user message to chat
      messages = [...messages, {
        id: uuidv4(),
        content: userMessage,
        isUser: true,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      }];
      
      // Get AI response
      const aiResponse = await getAIResponse(userMessage);
      
      // Add AI response to chat
      messages = [...messages, {
        id: uuidv4(),
        content: aiResponse,
        isUser: false,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      }];
    }
  </script>
  
  <div class="chat-page flex flex-col h-screen bg-gray-50">
    <header class="bg-green-600 text-white p-4 shadow-md">
      <div class="container mx-auto flex items-center justify-between">
        <div class="flex items-center">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 mr-2" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-3a1 1 0 00-.867.5 1 1 0 11-1.731-1A3 3 0 0113 8a3.001 3.001 0 01-2 2.83V11a1 1 0 11-2 0v-1a1 1 0 011-1 1 1 0 100-2zm0 8a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" />
          </svg>
          <h1 class="text-xl font-bold">AI Career Mentor</h1>
        </div>
        <a href="/dashboard" class="flex items-center text-white hover:text-green-100 transition-colors">
          <span class="mr-1">Back to Dashboard</span>
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
          </svg>
        </a>
      </div>
    </header>
    
    <main class="flex-grow flex flex-col overflow-hidden">
      <div class="container mx-auto flex-grow flex flex-col max-w-3xl px-4">
        <ChatContainer {messages} />
        
        {#if isTyping}
          <div class="typing-indicator ml-4 mb-3">
            <span class="dot"></span>
            <span class="dot"></span>
            <span class="dot"></span>
          </div>
        {/if}
        
        <InputArea on:send={handleMessageSend} />
      </div>
    </main>
  </div>
  
  <style>
    .typing-indicator {
      display: flex;
      align-items: center;
    }
    
    .dot {
      display: inline-block;
      width: 8px;
      height: 8px;
      background-color: #2E7D32;
      border-radius: 50%;
      margin-right: 3px;
      opacity: 0.7;
      animation: dot-pulse 1.5s infinite ease-in-out;
    }
    
    .dot:nth-child(2) {
      animation-delay: 0.2s;
    }
    
    .dot:nth-child(3) {
      animation-delay: 0.4s;
    }
    
    @keyframes dot-pulse {
      0%, 60%, 100% {
        transform: scale(1);
        opacity: 0.7;
      }
      30% {
        transform: scale(1.5);
        opacity: 1;
      }
    }
  </style>