<script lang="ts">
    import { createEventDispatcher } from 'svelte';
    import SendButton from '../ui/SendButton.svelte';
    import SuggestedPrompt from '../ui/SuggestedPrompt.svelte';
    
    const dispatch = createEventDispatcher();
    
    let message = '';
    let inputElement: HTMLTextAreaElement;
    
    const suggestedPrompts = [
      "What's my career risk?",
      "Suggest a green job",
      "Find a course for me",
      "Suggest a side hustle",
      "How to start in renewable energy?"
    ];
    
    function handleSubmit() {
      if (message.trim()) {
        dispatch('send', message);
        message = '';
        // Focus back on input after sending
        setTimeout(() => {
          if (inputElement) inputElement.focus();
        }, 0);
      }
    }
    
    function handleKeyDown(event: KeyboardEvent) {
      if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        handleSubmit();
      }
    }
    
    function usePrompt(prompt: string) {
      message = prompt;
      if (inputElement) inputElement.focus();
    }
  </script>
  
  <div class="input-area bg-white border-t border-gray-200 p-4">
    <div class="suggested-prompts flex flex-wrap mb-3">
      {#each suggestedPrompts as prompt}
        <SuggestedPrompt text={prompt} onClick={() => usePrompt(prompt)} />
      {/each}
    </div>
    
    <form on:submit|preventDefault={handleSubmit} class="flex items-end gap-2">
      <div class="relative flex-grow">
        <textarea
          bind:this={inputElement}
          bind:value={message}
          on:keydown={handleKeyDown}
          placeholder="Ask a question about your career or green jobs..."
          rows="1"
          class="w-full p-3 pr-12 rounded-lg border border-gray-300 focus:border-green-500 focus:ring focus:ring-green-200 focus:ring-opacity-50 resize-none overflow-auto"
          style="min-height: 44px; max-height: 120px;"
        ></textarea>
      </div>
      <div class="flex-shrink-0">
        <SendButton disabled={!message.trim()} />
      </div>
    </form>
  </div>
  
  <style>
    textarea {
      line-height: 1.5;
    }
  </style>