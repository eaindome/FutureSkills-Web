<script lang="ts">
    export let isUser: boolean = false;
    export let content: string = "";
    export let timestamp: string = "";
  </script>
  
  <div class={`chat-bubble flex flex-col max-w-xs md:max-w-md lg:max-w-lg rounded-2xl p-3 mb-3 ${
    isUser ? 'ml-auto bg-blue-100 text-gray-800' : 'mr-auto bg-green-100 text-gray-700'
  }`}>
    <div class="message text-sm md:text-base">
      {#if content.includes("\n")}
        {#each content.split("\n") as line}
          <p class="mb-1">{line}</p>
        {/each}
      {:else}
        <p>{content}</p>
      {/if}
    </div>
    <span class="timestamp text-xs text-gray-500 mt-1 {isUser ? 'text-right' : ''}">{timestamp}</span>
  </div>
  
  <style>
    .chat-bubble {
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
      word-wrap: break-word;
    }
  </style>