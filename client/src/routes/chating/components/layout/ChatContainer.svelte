<script lang="ts">
    import { onMount, afterUpdate } from 'svelte';
    import ChatBubble from '../ui/ChatBubble.svelte'
    
    export let messages: Array<{
      id: string;
      content: string;
      isUser: boolean;
      timestamp: string;
    }> = [];
  
    let chatContainer: HTMLElement;
  
    onMount(() => {
      scrollToBottom();
    });
  
    afterUpdate(() => {
      scrollToBottom();
    });
  
    function scrollToBottom() {
      if (chatContainer) {
        chatContainer.scrollTop = chatContainer.scrollHeight;
      }
    }
  </script>
  
  <div 
    bind:this={chatContainer}
    class="chat-container flex flex-col p-4 overflow-y-auto flex-grow" 
    role="log" 
    aria-live="polite" 
    aria-label="Chat messages">
    {#if messages.length === 0}
      <div class="flex items-center justify-center h-full">
        <p class="text-gray-500 text-center">Ask the AI Mentor a question about green jobs, career risks, or side hustles.</p>
      </div>
    {:else}
      {#each messages as message (message.id)}
        <ChatBubble isUser={message.isUser} content={message.content} timestamp={message.timestamp} />
      {/each}
    {/if}
  </div>
  
  <style>
    .chat-container {
      scroll-behavior: smooth;
      height: calc(100vh - 200px);
    }
  
    @media (max-width: 640px) {
      .chat-container {
        height: calc(100vh - 180px);
      }
    }
  </style>