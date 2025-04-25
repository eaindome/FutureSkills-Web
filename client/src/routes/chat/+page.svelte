<!-- src/routes/chat/+page.svelte -->
<script lang="ts">
  import { onMount } from 'svelte';
  import { fade, fly, slide } from 'svelte/transition';
  import Navbar from '$lib/components/layouts/Navbar.svelte';
  import ChatMessage from './components/ui/ChatMessage.svelte';
  import SuggestedPrompts from './components/ui/SuggestedPrompts.svelte';
  import ChatInput from './components/ui/ChatInput.svelte';
  import InChatGuide from './components/ui/InChatGuide.svelte';
  
  type Message = {
    id: string;
    content: string;
    isAI: boolean;
    timestamp: Date;
  };

  let messages: Message[] = [];
  let isTyping = false;
  let chatContainer: HTMLElement;
  let showScrollButton = false;
  let initialLoad = true;
  let showGuide = true;
  let showShareButton = false;
  
  // First visit detection (in a real app, this would be persisted in localStorage)
  let isFirstVisit = true;

  const suggestedPrompts = [
    "What's the future of data entry jobs in Kenya?",
    "Are there low-risk AI-proof jobs in energy?",
    "How can I transition from manufacturing to green tech?",
    "What skills will be most valuable in 2030?",
    "Sustainable careers in construction?"
  ];

  onMount(() => {
    // Add a welcome message from the AI
    messages = [
      {
        id: '1',
        content: "👋 Welcome to FutureSkills Coach! I'm here to help you navigate career transitions, explore green jobs, and find sustainable opportunities. What would you like to know today?",
        isAI: true,
        timestamp: new Date()
      }
    ];
    
    // Add scroll event listener
    if (chatContainer) {
      chatContainer.addEventListener('scroll', handleScroll);
    }
    
    // Hide initial load state after animation
    setTimeout(() => {
      initialLoad = false;
      
      // Show the share button after a delay (only after some conversation)
      setTimeout(() => {
        showShareButton = messages.length > 2;
      }, 2000);
    }, 800);

    // Always scroll to bottom on first load
    setTimeout(scrollToBottom, 200);
  });

  function handleScroll() {
    if (chatContainer) {
      const { scrollTop, scrollHeight, clientHeight } = chatContainer;
      showScrollButton = scrollHeight - scrollTop - clientHeight > 100;
    }
  }

  function scrollToBottom() {
    if (chatContainer) {
      chatContainer.scrollTo({
        top: chatContainer.scrollHeight,
        behavior: 'smooth'
      });
    }
  }

  function handleSendMessage(event: CustomEvent<string>) {
    const userMessage = event.detail;
    
    if (!userMessage.trim()) return;
    
    // Add user message
    const userMsg: Message = {
      id: Date.now().toString(),
      content: userMessage,
      isAI: false,
      timestamp: new Date()
    };
    
    messages = [...messages, userMsg];
    isTyping = true;
    
    // Scroll to bottom immediately after user sends message
    setTimeout(scrollToBottom, 100);
    
    // Simulate AI response (replace with actual API call)
    setTimeout(() => {
      const aiResponse: Message = {
        id: (Date.now() + 1).toString(),
        content: simulateAIResponse(userMessage),
        isAI: true,
        timestamp: new Date()
      };
      
      messages = [...messages, aiResponse];
      isTyping = false;
      
      // Show share button after conversation develops
      if (messages.length > 2) {
        showShareButton = true;
      }
      
      // Scroll to bottom after AI responds
      setTimeout(scrollToBottom, 100);
    }, 1500);
  }

  function handlePromptClick(event: CustomEvent<string>) {
    handleSendMessage(new CustomEvent('message', { detail: event.detail }));
  }
  
  function handleGuideComplete() {
    showGuide = false;
    isFirstVisit = false;
  }
  
  function shareConversation() {
    // In a real app, this would generate a shareable link or export functionality
    alert('This feature would let you share insights from this conversation!');
  }
  
  function clearConversation() {
    // Keep only the welcome message
    messages = [
      {
        id: Date.now().toString(),
        content: "👋 Welcome back to FutureSkills Coach! How can I help you today?",
        isAI: true,
        timestamp: new Date()
      }
    ];
    showShareButton = false;
  }

  // Temporary function to simulate AI responses (replace with actual backend)
  function simulateAIResponse(userMessage: string): string {
    const lowercaseMsg = userMessage.toLowerCase();
    
    if (lowercaseMsg.includes('data entry') || lowercaseMsg.includes('kenya')) {
      return "Data entry jobs are facing high automation risk globally, including in Kenya. By 2030, an estimated 70% of traditional data entry roles could be automated. However, Kenya's growing tech sector offers opportunities in data analysis, interpretation, and management that require human skills.\n\nConsider exploring data science courses or learning data visualization tools for a more secure career path.";
    }
    
    if (lowercaseMsg.includes('low-risk') || lowercaseMsg.includes('energy')) {
      return "The renewable energy sector offers several low-automation-risk careers! Solar installation technicians, wind turbine maintenance specialists, and energy efficiency consultants all require hands-on skills that are difficult to automate.\n\nThese green energy jobs are projected to grow by 15-20% annually through 2030, with starting salaries between $40-60K depending on location.";
    }
    
    if (lowercaseMsg.includes('manufacturing') || lowercaseMsg.includes('green tech')) {
      return "Transitioning from manufacturing to green tech is an excellent move! Your mechanical knowledge and attention to detail are transferable.\n\nConsider a certification in renewable energy systems (8-12 weeks) or green manufacturing processes. Many companies like Tesla and Siemens have programs specifically designed to retrain manufacturing workers for green tech roles.\n\nWould you like me to suggest some specific training programs?";
    }
    
    if (lowercaseMsg.includes('skills') || lowercaseMsg.includes('2030')) {
      return "By 2030, the most valuable skills for the green economy will include:\n\n1. Renewable energy systems knowledge\n2. Sustainable materials expertise\n3. Carbon accounting and management\n4. Circular economy design principles\n5. Climate adaptation planning\n\nThese skills are projected to command 15-25% salary premiums across industries. Would you like to learn more about any specific skill area?";
    }
    
    if (lowercaseMsg.includes('construction') || lowercaseMsg.includes('sustainable')) {
      return "The construction industry is being transformed by sustainability requirements! Emerging green construction careers include sustainable building consultants, green materials specialists, and energy efficiency retrofitters.\n\nThese roles typically require certifications like LEED or Passive House, and pay 10-20% above traditional construction roles. Many community colleges now offer green building programs that take 3-6 months to complete.";
    }
    
    // Default response
    return "That's an interesting question about future careers! The green economy is creating opportunities across multiple sectors, from renewable energy to sustainable agriculture and eco-tourism.\n\nWould you like me to explore specific green job paths related to your skills or interests? I can help you identify growing fields with strong long-term prospects.";
  }
</script>

<svelte:head>
  <title>AI Assistant | FutureSkills Coach</title>
  <meta name="description" content="Get personalized career guidance for sustainable jobs and skills development">
</svelte:head>

<div class="flex flex-col h-screen bg-gray-50">
  <Navbar isLoggedIn={true}/>
  
  <main class="flex-1 flex flex-col overflow-hidden">
    <!-- Chat container -->
    <div 
      bind:this={chatContainer} 
      class="flex-1 overflow-y-auto px-4 py-6 scroll-smooth"
    >
      <div class="max-w-3xl mx-auto space-y-1">
        {#if initialLoad}
          <div in:fly={{ y: 20, duration: 400 }}>
            <!-- Display loading if needed -->
          </div>
        {/if}
        
        <!-- Guide component -->
        {#if isFirstVisit && showGuide}
          <InChatGuide on:complete={handleGuideComplete} />
        {/if}
        
        <!-- Messages -->
        {#each messages as message (message.id)}
          <div in:fly={{ y: 10, duration: 300 }}>
            <ChatMessage {message} />
          </div>
        {/each}
        
        <!-- Typing indicator -->
        {#if isTyping}
          <div class="flex items-center space-x-2 py-2 px-4 max-w-max rounded-full bg-teal-50 border border-teal-200 text-teal-800"
               in:fade={{ duration: 200 }}
          >
            <div class="flex space-x-1">
              <div class="w-2 h-2 rounded-full bg-teal-500 animate-pulse" style="animation-delay: 0ms"></div>
              <div class="w-2 h-2 rounded-full bg-teal-500 animate-pulse" style="animation-delay: 300ms"></div>
              <div class="w-2 h-2 rounded-full bg-teal-500 animate-pulse" style="animation-delay: 600ms"></div>
            </div>
            <span class="text-sm font-medium">Thinking...</span>
          </div>
        {/if}
      </div>
    </div>
    
    <!-- Scroll to bottom button -->
    {#if showScrollButton}
      <button 
        on:click={scrollToBottom}
        class="absolute bottom-32 right-6 bg-white p-2.5 rounded-full shadow-lg border border-gray-200 text-gray-600 hover:text-teal-600 transition-all hover:shadow-md transform hover:scale-105 z-20"
        in:fade={{ duration: 200 }}
        out:fade={{ duration: 150 }}
        aria-label="Scroll to bottom"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M14.707 12.293a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 111.414-1.414L9 14.586V3a1 1 0 012 0v11.586l2.293-2.293a1 1 0 011.414 0z" clip-rule="evenodd" />
        </svg>
      </button>
    {/if}
    
    <!-- Action buttons -->
    {#if showShareButton}
      <div class="fixed top-20 right-4 md:right-8 flex flex-col space-y-2 z-20">
        <button 
          on:click={shareConversation}
          class="bg-white p-2.5 rounded-full shadow-md border border-gray-200 text-gray-600 hover:text-amber-500 transition-all hover:shadow-lg transform hover:scale-105"
          in:fly={{ x: 20, duration: 300 }}
          aria-label="Share conversation"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
            <path d="M15 8a3 3 0 10-2.977-2.63l-4.94 2.47a3 3 0 100 4.319l4.94 2.47a3 3 0 10.895-1.789l-4.94-2.47a3.027 3.027 0 000-.74l4.94-2.47C13.456 7.68 14.19 8 15 8z" />
          </svg>
        </button>
        <button 
          on:click={clearConversation}
          class="bg-white p-2.5 rounded-full shadow-md border border-gray-200 text-gray-600 hover:text-red-500 transition-all hover:shadow-lg transform hover:scale-105"
          in:fly={{ x: 20, duration: 300, delay: 100 }}
          aria-label="Clear conversation"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
          </svg>
        </button>
      </div>
    {/if}
    
    <!-- Input area -->
    <div class="sticky bottom-0 bg-gradient-to-t from-gray-50 to-transparent pt-4 pb-6 px-4">
      <div class="max-w-3xl mx-auto">
        <!-- Suggested prompts -->
        {#if messages.length <= 2}
          <SuggestedPrompts 
            prompts={suggestedPrompts} 
            on:promptClick={handlePromptClick} 
          />
        {/if}
        
        <!-- Chat input -->
        <ChatInput on:sendMessage={handleSendMessage} />
      </div>
    </div>
  </main>
</div>