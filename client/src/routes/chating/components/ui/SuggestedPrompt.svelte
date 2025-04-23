<script lang="ts">
    export let text: string;
    export let onClick: () => void;
  </script>
  
  <button 
    on:click={onClick}
    class="bg-blue-50 text-blue-500 hover:bg-blue-100 text-sm font-medium rounded-full px-4 py-2 transition-colors duration-150 focus:outline-none focus:ring-2 focus:ring-blue-300 mr-2 mb-2">
    {text}
  </button>