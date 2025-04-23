<!-- src/lib/components/ui/ChatInput.svelte -->
<script lang="ts">
  import { createEventDispatcher, onMount } from 'svelte';
  import { fade, fly } from 'svelte/transition';
  
  const dispatch = createEventDispatcher();
  let message = '';
  let inputElement: HTMLTextAreaElement;
  let isFocused = false;
  let showEmojiPicker = false;
  
  // Common emojis for quick insertion
  const quickEmojis = ['🌱', '💼', '🔍', '📊', '📚', '💡', '🌍', '⚡'];
  
  function handleSubmit() {
    if (message.trim()) {
      dispatch('sendMessage', message);
      message = '';
      // Reset textarea height
      if (inputElement) {
        inputElement.style.height = 'auto';
      }
      // Focus back to input after sending
      setTimeout(() => {
        if (inputElement) inputElement.focus();
      }, 0);
    }
  }
  
  function handleKeyDown(event: KeyboardEvent) {
    // Submit on Enter without Shift key
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault();
      handleSubmit();
    }
    // Close emoji picker on Escape
    if (event.key === 'Escape' && showEmojiPicker) {
      showEmojiPicker = false;
    }
  }
  
  function toggleEmojiPicker() {
    showEmojiPicker = !showEmojiPicker;
  }
  
  function insertEmoji(emoji: string) {
    message += emoji;
    if (inputElement) {
      inputElement.focus();
      adjustHeight();
    }
  }
  
  // Auto-resize textarea
  function adjustHeight() {
    if (inputElement) {
      inputElement.style.height = 'auto';
      inputElement.style.height = `${inputElement.scrollHeight}px`;
    }
  }
  
  onMount(() => {
    if (inputElement) {
      inputElement.focus();
    }
    
    // Add global event listener to close emoji picker when clicking outside
    const handleClickOutside = (event: MouseEvent) => {
      const target = event.target as HTMLElement;
      if (showEmojiPicker && !target.closest('.emoji-container') && !target.closest('.emoji-button')) {
        showEmojiPicker = false;
      }
    };
    
    document.addEventListener('click', handleClickOutside);
    
    return () => {
      document.removeEventListener('click', handleClickOutside);
    };
  });
</script>

<form on:submit|preventDefault={handleSubmit} class="relative">
  <div class="relative">
    <textarea
      bind:this={inputElement}
      bind:value={message}
      on:input={adjustHeight}
      on:keydown={handleKeyDown}
      on:focus={() => isFocused = true}
      on:blur={() => isFocused = false}
      placeholder="Ask about future jobs, skills, or career transitions..."
      class="w-full border-2 {isFocused ? 'border-teal-500 shadow-md' : 'border-gray-200'} focus:border-teal-500 focus:ring focus:ring-teal-200 focus:ring-opacity-50 rounded-xl py-3.5 px-4 pr-16 resize-none overflow-hidden transition-all"
      rows="1"
      style="min-height: 56px; max-height: 180px;"
    ></textarea>
    
    <div class="absolute right-2 bottom-2.5 flex items-center space-x-2">
      <!-- Emoji button -->
      <button
        type="button"
        class="emoji-button rounded-full p-2 text-gray-400 hover:text-amber-500 hover:bg-amber-50 transition-all"
        on:click={toggleEmojiPicker}
        aria-label="Add emoji"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM7 9a1 1 0 100-2 1 1 0 000 2zm7-1a1 1 0 11-2 0 1 1 0 012 0zm-7.536 5.879a1 1 0 001.415 0 3 3 0 014.242 0 1 1 0 001.415-1.415 5 5 0 00-7.072 0 1 1 0 000 1.415z" clip-rule="evenodd" />
        </svg>
      </button>
      
      <!-- Send button with animation -->
      <button
        type="submit"
        class="rounded-full p-2.5 {message.trim() ? 'bg-gradient-to-r from-teal-500 to-green-500 hover:from-teal-600 hover:to-green-600' : 'bg-gray-300'} text-white transition-all flex items-center justify-center shadow-sm transform hover:scale-105 active:scale-95 duration-300"
        disabled={!message.trim()}
        aria-label="Send message"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 {message.trim() ? 'animate-pulse' : ''}" viewBox="0 0 20 20" fill="currentColor">
          <path d="M10.894 2.553a1 1 0 00-1.788 0l-7 14a1 1 0 001.169 1.409l5-1.429A1 1 0 009 15.571V11a1 1 0 112 0v4.571a1 1 0 00.725.962l5 1.428a1 1 0 001.17-1.408l-7-14z" />
        </svg>
      </button>
    </div>
    
    <!-- Emoji picker dropdown -->
    {#if showEmojiPicker}
      <div 
        class="emoji-container absolute right-0 bottom-16 bg-white rounded-lg shadow-lg border border-gray-200 p-2 z-50"
        in:fly={{ y: 10, duration: 200 }}
        out:fade={{ duration: 150 }}
      >
        <div class="grid grid-cols-4 gap-2">
          {#each quickEmojis as emoji}
            <button 
              type="button"
              on:click={() => insertEmoji(emoji)}
              class="w-8 h-8 flex items-center justify-center text-xl hover:bg-gray-100 rounded transition-colors"
            >
              {emoji}
            </button>
          {/each}
        </div>
      </div>
    {/if}
  </div>
  
  <!-- Character hint -->
  <div class="flex justify-between mt-1.5">
    <p class="text-xs text-gray-500">Voice your career questions</p>
    <p class="text-xs text-gray-500 mr-2">Shift + Enter for new line</p>
  </div>
</form>