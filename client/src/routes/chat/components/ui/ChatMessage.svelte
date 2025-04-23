<!-- src/lib/components/ui/ChatMessage.svelte -->
<script lang="ts">
  export let message: {
    id: string;
    content: string;
    isAI: boolean;
    timestamp: Date;
  };
  
  // Function to format the timestamp
  function formatTime(date: Date): string {
    return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  }
  
  // Generate AI avatar with logo animation
  const aiAvatar = `
    <div class="relative flex items-center justify-center w-10 h-10 rounded-full bg-gradient-to-br from-teal-500 to-green-600 shadow-md transform transition-transform hover:scale-105 group">
      <div class="absolute inset-0 rounded-full bg-gradient-to-br from-teal-500 to-green-600 opacity-50 animate-pulse group-hover:opacity-0"></div>
      <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
      </svg>
    </div>
  `;
  
  // Generate user avatar with subtle hover effect
  const userAvatar = `
    <div class="flex items-center justify-center w-10 h-10 rounded-full bg-gradient-to-br from-blue-500 to-sky-600 shadow-md transform transition-transform hover:scale-105">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
      </svg>
    </div>
  `;

  // Split content into paragraphs for better formatting
  const paragraphs = message.content.split('\n').filter(p => p.trim() !== '');
</script>

<div class="flex flex-col space-y-1 mb-6">
  <div class="flex {message.isAI ? 'justify-start' : 'justify-end'}">
    <div class="flex max-w-3xl {message.isAI ? 'items-start' : 'items-end'} {message.isAI ? 'flex-row' : 'flex-row-reverse'}">
      <!-- Avatar -->
      <div class="flex-shrink-0 {message.isAI ? 'mr-3' : 'ml-3'} mt-1">
        {@html message.isAI ? aiAvatar : userAvatar}
      </div>
      
      <!-- Message bubble -->
      <div class="
        {message.isAI 
          ? 'bg-gradient-to-br from-teal-50 to-green-100 border-l-4 border-l-teal-500' 
          : 'bg-gradient-to-br from-blue-50 to-sky-100 border-r-4 border-r-blue-500'} 
        px-5 py-3.5 rounded-2xl max-w-xl shadow-sm 
        transition-all duration-300 transform hover:shadow-md
        relative z-10
      ">
        <!-- Message content with paragraph support -->
        <div class="whitespace-pre-wrap">
          {#each paragraphs as paragraph, i}
            <p class="leading-relaxed {i < paragraphs.length - 1 ? 'mb-3' : ''}">{paragraph}</p>
          {/each}
        </div>
      </div>
    </div>
  </div>
  
  <!-- Timestamp with subtle fade-in effect -->
  <div class="flex {message.isAI ? 'justify-start pl-14' : 'justify-end pr-14'}">
    <span class="text-xs text-gray-500 font-light px-2 py-0.5 rounded-full hover:bg-gray-100 transition-colors">
      {formatTime(message.timestamp)}
    </span>
  </div>
</div>