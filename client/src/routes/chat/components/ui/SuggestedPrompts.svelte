<!-- src/lib/components/ui/SuggestedPrompts.svelte -->
<script lang="ts">
  import { createEventDispatcher, onMount } from 'svelte';
  import { fade, fly } from 'svelte/transition';
  
  export let prompts: string[] = [];
  const dispatch = createEventDispatcher();
  
  function handlePromptClick(prompt: string) {
    dispatch('promptClick', prompt);
  }
  
  let container: HTMLElement;
  let showLeftShadow = false;
  let showRightShadow = true;
  let isScrolling = false;
  let touchStartX = 0;
  let touchEndX = 0;
  
  function checkScrollShadows() {
    if (container) {
      showLeftShadow = container.scrollLeft > 20;
      showRightShadow = container.scrollLeft < (container.scrollWidth - container.clientWidth - 20);
    }
  }
  
  function scrollContainer(direction: 'left' | 'right') {
    if (container) {
      const scrollAmount = container.clientWidth * 0.6;
      const targetScroll = container.scrollLeft + (direction === 'left' ? -scrollAmount : scrollAmount);
      
      isScrolling = true;
      container.scrollTo({
        left: targetScroll,
        behavior: 'smooth'
      });
      
      // Reset isScrolling after animation completes
      setTimeout(() => {
        isScrolling = false;
        checkScrollShadows();
      }, 300);
    }
  }
  
  function handleTouchStart(e: TouchEvent) {
    touchStartX = e.touches[0].clientX;
  }
  
  function handleTouchEnd(e: TouchEvent) {
    touchEndX = e.changedTouches[0].clientX;
    const swipeDistance = touchEndX - touchStartX;
    
    // If the swipe distance is significant (more than 50px), scroll
    if (Math.abs(swipeDistance) > 50) {
      scrollContainer(swipeDistance > 0 ? 'left' : 'right');
    }
  }
  
  onMount(() => {
    if (container) {
      checkScrollShadows();
      
      // Add resize observer to recheck shadows when window size changes
      const resizeObserver = new ResizeObserver(() => {
        checkScrollShadows();
      });
      
      resizeObserver.observe(container);
      
      return () => {
        resizeObserver.disconnect();
      };
    }
  });
</script>

<div class="relative mb-4">
  <h3 class="text-sm font-medium text-gray-700 mb-2 px-1">Suggested Topics:</h3>
  
  <div class="relative">
    <!-- Left scroll button -->
    {#if showLeftShadow}
      <button 
        on:click={() => scrollContainer('left')}
        class="absolute left-0 top-1/2 -translate-y-1/2 z-20 bg-white/80 hover:bg-white rounded-full p-1.5 shadow-md text-teal-600 hover:text-teal-700 transition transform hover:scale-105 backdrop-blur-sm"
        disabled={isScrolling}
        aria-label="Scroll left"
        in:fade={{ duration: 150 }}
        out:fade={{ duration: 100 }}
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clip-rule="evenodd" />
        </svg>
      </button>
    {/if}
    
    <!-- Right scroll button -->
    {#if showRightShadow}
      <button 
        on:click={() => scrollContainer('right')}
        class="absolute right-0 top-1/2 -translate-y-1/2 z-20 bg-white/80 hover:bg-white rounded-full p-1.5 shadow-md text-teal-600 hover:text-teal-700 transition transform hover:scale-105 backdrop-blur-sm"
        disabled={isScrolling}
        aria-label="Scroll right"
        in:fade={{ duration: 150 }}
        out:fade={{ duration: 100 }}
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
        </svg>
      </button>
    {/if}
    
    <!-- Left shadow -->
    {#if showLeftShadow}
      <div class="absolute left-0 top-0 bottom-0 w-12 bg-gradient-to-r from-white to-transparent z-10 pointer-events-none"></div>
    {/if}
    
    <!-- Prompt container -->
    <div
      bind:this={container}
      on:scroll={checkScrollShadows}
      on:touchstart={handleTouchStart}
      on:touchend={handleTouchEnd}
      class="overflow-x-auto px-4 py-2 flex snap-x snap-mandatory scroll-smooth scrollbar-none"
    >
      <div class="flex space-x-3 px-2">
        {#each prompts as prompt, i}
          <div in:fly|local={{ x: 20, y: 5, delay: i * 100, duration: 300 }}>
            <button
              on:click={() => handlePromptClick(prompt)}
              class="snap-start whitespace-nowrap text-sm bg-gradient-to-r from-teal-50 to-green-100 
                text-gray-700 px-4 py-2.5 rounded-full transition-all flex-shrink-0 border border-teal-200 
                hover:border-teal-300 hover:shadow-md transform hover:-translate-y-0.5 
                hover:bg-gradient-to-r hover:from-teal-100 hover:to-green-200 group"
            >
              <!-- Icon for each prompt type -->
              <span class="inline-flex items-center">
                {#if prompt.toLowerCase().includes('kenya') || prompt.toLowerCase().includes('data entry')}
                  <span class="mr-1.5 text-teal-600 group-hover:scale-110 transition-transform">🌍</span>
                {:else if prompt.toLowerCase().includes('energy') || prompt.toLowerCase().includes('ai-proof')}
                  <span class="mr-1.5 text-teal-600 group-hover:scale-110 transition-transform">⚡</span>
                {:else if prompt.toLowerCase().includes('manufacturing') || prompt.toLowerCase().includes('green tech')}
                  <span class="mr-1.5 text-teal-600 group-hover:scale-110 transition-transform">🏭</span>
                {:else if prompt.toLowerCase().includes('skills') || prompt.toLowerCase().includes('2030')}
                  <span class="mr-1.5 text-teal-600 group-hover:scale-110 transition-transform">🚀</span>
                {:else if prompt.toLowerCase().includes('construction') || prompt.toLowerCase().includes('sustainable')}
                  <span class="mr-1.5 text-teal-600 group-hover:scale-110 transition-transform">🏗️</span>
                {:else}
                  <span class="mr-1.5 text-teal-600 group-hover:scale-110 transition-transform">💡</span>
                {/if}
                {prompt}
              </span>
            </button>
          </div>
        {/each}
      </div>
    </div>
    
    <!-- Right shadow -->
    {#if showRightShadow}
      <div class="absolute right-0 top-0 bottom-0 w-12 bg-gradient-to-l from-white to-transparent z-10 pointer-events-none"></div>
    {/if}
  </div>
</div>