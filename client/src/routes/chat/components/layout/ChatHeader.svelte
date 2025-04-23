<!-- src/lib/components/layout/ChatHeader.svelte -->
<script lang="ts">
  import { onMount } from 'svelte';
  import { fade, fly } from 'svelte/transition';
  import { page } from '$app/stores';
  
  let isMobileMenuOpen = false;
  let isScrolled = false;
  let showNotification = true;
  
  function toggleMobileMenu() {
    isMobileMenuOpen = !isMobileMenuOpen;
  }
  
  function dismissNotification() {
    showNotification = false;
  }
  
  onMount(() => {
    const handleScroll = () => {
      isScrolled = window.scrollY > 10;
    };
    
    window.addEventListener('scroll', handleScroll);
    
    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  });
</script>

<header class="relative z-30">
  <!-- Main navigation header -->
  <div class="bg-gradient-to-r from-teal-600 to-green-600 text-white shadow-md transition-all duration-300 {isScrolled ? 'shadow-lg' : ''}">
    <div class="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between">
      <div class="flex items-center">
        <a href="/" class="flex items-center group">
          <div class="bg-white p-1.5 rounded-full shadow-md mr-2 transform transition group-hover:scale-110 duration-300">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7 text-teal-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9" />
            </svg>
          </div>
          <div>
            <span class="text-xl font-bold tracking-tight">FutureSkills</span>
            <span class="text-xl font-light tracking-tight">Coach</span>
          </div>
        </a>
      </div>
      
      <nav class="hidden md:flex items-center space-x-6">
        <a href="/dashboard" class="text-white hover:text-amber-200 transition-colors font-medium py-2 px-1 relative group">
          <span>Dashboard</span>
          <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-amber-300 rounded-full transition-all duration-300 group-hover:w-full"></span>
        </a>
        <a href="/chat" class="text-amber-200 font-medium relative py-2 px-1 group">
          <span>AI Assistant</span>
          <span class="absolute bottom-0 left-0 w-full h-0.5 bg-amber-300 rounded-full"></span>
        </a>
        <a href="/resources" class="text-white hover:text-amber-200 transition-colors font-medium py-2 px-1 relative group">
          <span>Resources</span>
          <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-amber-300 rounded-full transition-all duration-300 group-hover:w-full"></span>
        </a>
      </nav>
      
      <!-- Mobile menu button with animation -->
      <button 
        type="button" 
        on:click={toggleMobileMenu} 
        class="md:hidden rounded-md p-2 text-white hover:bg-green-700 transition-colors focus:outline-none focus:ring-2 focus:ring-white focus:ring-opacity-50" 
        aria-label={isMobileMenuOpen ? 'Close mobile menu' : 'Open mobile menu'}
      >
        <svg 
          xmlns="http://www.w3.org/2000/svg" 
          class="h-6 w-6 transition-transform duration-300 {isMobileMenuOpen ? 'rotate-90' : 'rotate-0'}" 
          fill="none" 
          viewBox="0 0 24 24" 
          stroke="currentColor"
        >
          {#if isMobileMenuOpen}
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          {:else}
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
          {/if}
        </svg>
      </button>
    </div>
  </div>
  
  <!-- Mobile menu dropdown with animation -->
  {#if isMobileMenuOpen}
    <div 
      class="md:hidden bg-green-700 shadow-lg"
      transition:fly={{ y: -10, duration: 200 }}
    >
      <div class="px-4 pt-2 pb-3 space-y-1">
        <a 
          href="/dashboard" 
          class="block text-white hover:bg-green-800 px-3 py-2 rounded-md text-base font-medium my-1 transition-colors"
          in:fly={{ y: 5, delay: 50, duration: 200 }}
        >
          Dashboard
        </a>
        <a 
          href="/chat" 
          class="block bg-green-800 text-amber-200 px-3 py-2 rounded-md text-base font-medium my-1 transition-colors"
          in:fly={{ y: 5, delay: 100, duration: 200 }}
        >
          AI Assistant
        </a>
        <a 
          href="/resources" 
          class="block text-white hover:bg-green-800 px-3 py-2 rounded-md text-base font-medium my-1 transition-colors"
          in:fly={{ y: 5, delay: 150, duration: 200 }}
        >
          Resources
        </a>
        <button 
          class="w-full mt-2 bg-amber-500 hover:bg-amber-600 text-white font-medium px-3 py-2 rounded-md transition-colors shadow-sm"
          in:fly={{ y: 5, delay: 200, duration: 200 }}
        >
          Get Started
        </button>
      </div>
    </div>
  {/if}
  
  <!-- Notification banner -->
  <!-- {#if showNotification}
    <div 
      class="bg-blue-50 p-2 border-b border-blue-100"
      transition:fly={{ y: -20, duration: 300 }}
    >
      <div class="max-w-7xl mx-auto px-4 flex items-center justify-between">
        <div class="flex items-center text-sm text-blue-700">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2 flex-shrink-0" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd" />
          </svg>
          <span>Join our <span class="font-medium">Green Skills Workshop</span> on May 15th!</span>
        </div>
        <button 
          on:click={dismissNotification}
          class="text-blue-500 hover:text-blue-700 focus:outline-none"
          aria-label="Dismiss notification"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>
    </div>
  {/if} -->
</header>