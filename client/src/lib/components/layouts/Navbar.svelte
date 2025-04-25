<!-- src/lib/components/layout/Navbar.svelte -->
<script lang="ts">
    import { onMount } from 'svelte';
    import { fly } from 'svelte/transition';
    import { page } from '$app/stores';
    
    // Props with defaults
    export let userName: string = ''; // Pass username when user is logged in
    export let isLoggedIn: boolean = false; // Control navbar state based on auth
    export let pageType: keyof typeof navItems | undefined = undefined;
    
    // Reactive state
    let isMenuOpen = false;
    let scrolled = false;
    let prevScrollPos = 0;
    let visible = true;
    
    // Dynamically determine active page first
    $: currentPath = $page?.url?.pathname || '/';
    $: isActive = (path: string) => currentPath === path || currentPath.startsWith(path + '/');
    
    function toggleMenu() {
      isMenuOpen = !isMenuOpen;
    }

    // Calculate pageType based on currentPath
    $: pageType = getPageType(currentPath);

    function getPageType(path: string): 'chat' | 'input' | 'loggedIn' | 'public' {
    if (pageType) return pageType; // Use the prop if provided
    if (path === '/chat') return 'chat';
    if (path === '/input') return 'input';
    if (isLoggedIn) return 'loggedIn';
    return 'public';
}

    $: navItems = {
        'chat': [
            { href: '/dashboard', label: 'Dashboard' },
            { href: '/chat', label: 'AI Assistant' },
            { href: '/resources', label: 'Resources' }
        ],
        'input': [
            { href: '/', label: 'Home' },
            { href: '/about', label: 'About' },
            { href: '/resources', label: 'Resources' }
        ],
        'loggedIn': [
            { href: '/dashboard', label: 'Dashboard' },
            { href: '/jobs', label: 'Green Jobs' },
            { href: '/skills', label: 'Reskilling' },
            { href: '/hustles', label: 'Side Hustles' },
            { href: '/chat', label: 'AI Mentor' }
        ],
        'public': [
            { href: '/', label: 'Home' },
            { href: '/about', label: 'About' },
            { href: '/resources', label: 'Resources' }
        ]
    };
    
    onMount(() => {
      prevScrollPos = window.scrollY;
      
      const handleScroll = () => {
        const currentScrollPos = window.scrollY;
        scrolled = currentScrollPos > 10;
        
        // Hide navbar on scroll down, show on scroll up
        visible = prevScrollPos > currentScrollPos || currentScrollPos < 10 || isMenuOpen;
        prevScrollPos = currentScrollPos;
      };
      
      window.addEventListener('scroll', handleScroll);
      return () => {
        window.removeEventListener('scroll', handleScroll);
      };
    });
</script>
  
<nav class={`fixed w-full z-30 transition-all duration-300 
    ${scrolled ? 'bg-white/95 backdrop-blur-sm shadow-lg py-2' : 'bg-gradient-to-r from-teal-600 to-green-600 py-4'} 
    ${visible ? 'translate-y-0' : '-translate-y-full'}`}>
    <div class="container mx-auto px-4">
      <div class="flex justify-between items-center">
        <div class="flex items-center">
          <a href="/" class="flex items-center group">
            <div class={`w-10 h-10 rounded-full flex items-center justify-center mr-2 shadow-md 
              group-hover:shadow-lg transition-all duration-300 group-hover:scale-105
              ${scrolled ? 'bg-gradient-to-br from-green-600 to-teal-500' : 'bg-white'}`}>
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" 
                class={`w-6 h-6 ${scrolled ? 'text-white' : 'text-teal-600'}`}>
                <path d="M11.584 2.376a.75.75 0 01.832 0l9 6a.75.75 0 11-.832 1.248L12 3.901 3.416 9.624a.75.75 0 01-.832-1.248l9-6z" />
                <path fill-rule="evenodd" d="M20.25 10.332v9.918H21a.75.75 0 010 1.5H3a.75.75 0 010-1.5h.75v-9.918a.75.75 0 01.634-.74A49.109 49.109 0 0112 9c2.59 0 5.134.202 7.616.592a.75.75 0 01.634.74z" clip-rule="evenodd" />
              </svg>
            </div>
            <div>
              <span class={`text-xl font-bold ${scrolled ? 'bg-gradient-to-r from-green-700 to-teal-600 bg-clip-text text-transparent' : 'text-white'}`}>
                FutureSkills
              </span>
              <span class={`text-xl font-medium ${scrolled ? 'text-gray-700' : 'text-white/90'}`}>
                Coach
              </span>
            </div>
          </a>
        </div>
        
        <!-- Desktop Navigation -->
        <div class="hidden md:flex items-center space-x-1">
          {#if isLoggedIn}
            <!-- Logged-in navigation -->
            {#each navItems[pageType] || [] as item}
              <a 
                href={item.href}
                class="relative group py-2 px-3 rounded-lg transition-all duration-200 font-medium"
              >
                <span class={`${isActive(item.href) 
                  ? (scrolled ? 'text-green-600' : 'text-amber-200') 
                  : (scrolled ? 'text-gray-700 group-hover:text-green-600' : 'text-white group-hover:text-amber-200')}`}>
                  {item.label}
                </span>
                <span class={`absolute bottom-0 left-0 w-0 h-0.5 transition-all duration-300 rounded-full
                  ${scrolled ? 'bg-green-500' : 'bg-amber-300'} 
                  ${isActive(item.href) ? 'w-full' : 'group-hover:w-full'}`}>
                </span>
              </a>
            {/each}
            
            <!-- User profile -->
            <div class="relative ml-3">
              <button 
                class={`flex items-center focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500 rounded-full ${scrolled ? 'text-gray-700' : 'text-white'}`}
                on:click={toggleMenu}
              >
                <span class="mr-1 font-medium text-sm">{userName}</span>
                <div class={`h-8 w-8 rounded-full flex items-center justify-center text-white font-medium
                    ${scrolled 
                      ? 'bg-green-600' 
                      : 'bg-green-600 ring-2 ring-white/80 shadow-lg'}`}>
                    {userName ? userName.charAt(0).toUpperCase() : 'U'}
                </div>
              </button>
              
              {#if isMenuOpen}
                <div 
                  class="origin-top-right absolute right-0 mt-2 w-48 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none" 
                  transition:fly={{ y: -5, duration: 200 }}
                  role="menu" 
                  aria-orientation="vertical"
                >
                  <div class="py-1" role="none">
                    <a href="/profile" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100" role="menuitem">Your Profile</a>
                    <a href="/settings" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100" role="menuitem">Settings</a>
                    <a href="/signout" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100" role="menuitem">Sign out</a>
                  </div>
                </div>
              {/if}
            </div>
          {:else}
            <!-- Public navigation -->
            {#each navItems[pageType] || [] as item}
              <a 
                href={item.href}
                class="relative group py-2 px-3 rounded-lg transition-all duration-200 font-medium"
              >
                <span class={`${isActive(item.href) && (item.href !== '/' || currentPath === '/') 
                  ? (scrolled ? 'text-green-600' : 'text-amber-200') 
                  : (scrolled ? 'text-gray-700 group-hover:text-green-600' : 'text-white group-hover:text-amber-200')}`}>
                  {item.label}
                </span>
                <span class={`absolute bottom-0 left-0 w-0 h-0.5 transition-all duration-300 rounded-full
                  ${scrolled ? 'bg-green-500' : 'bg-amber-300'} 
                  ${isActive(item.href) && (item.href !== '/' || currentPath === '/') ? 'w-full' : 'group-hover:w-full'}`}>
                </span>
              </a>
            {/each}
            
            <button 
              class={`ml-4 py-2 px-5 rounded-lg transition-all duration-300 shadow-md hover:shadow-lg transform hover:-translate-y-0.5 font-medium
              ${scrolled 
                ? 'bg-gradient-to-r from-green-600 to-teal-500 hover:from-green-700 hover:to-teal-600 text-white' 
                : 'bg-amber-500 hover:bg-amber-600 text-white'}`}
            >
              Get Started
            </button>
          {/if}
        </div>
        
        <!-- Mobile menu button -->
        <div class="md:hidden">
          <button
            on:click={toggleMenu}
            class={`p-2 rounded-lg focus:outline-none
              ${scrolled 
                ? 'text-gray-700 hover:text-green-600 hover:bg-green-50' 
                : 'text-white hover:bg-green-700'}`}
            aria-label="Toggle menu"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              {#if isMenuOpen}
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
              {:else}
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path>
              {/if}
            </svg>
          </button>
        </div>
      </div>
      
      <!-- Mobile Navigation -->
      {#if isMenuOpen}
        <div 
          class="md:hidden mt-4 pb-4 rounded-lg shadow-lg"
          class:bg-white={scrolled} 
          class:bg-green-700={!scrolled}
          transition:fly={{ y: -20, duration: 300 }}
        >
          <div class="flex flex-col space-y-1 px-2">
            {#if isLoggedIn}
              <!-- Logged-in mobile navigation -->
              <a 
                href="/dashboard" 
                class={`py-3 px-4 rounded-lg font-medium transition-colors duration-200
                  ${isActive('/dashboard')
                    ? (scrolled ? 'bg-green-50 text-green-600' : 'bg-green-800 text-amber-200')
                    : (scrolled ? 'text-gray-700 hover:text-green-600 hover:bg-green-50' : 'text-white hover:bg-green-800')}`}
              >
                Dashboard
              </a>
              <a 
                href="/jobs" 
                class={`py-3 px-4 rounded-lg font-medium transition-colors duration-200
                  ${isActive('/jobs')
                    ? (scrolled ? 'bg-green-50 text-green-600' : 'bg-green-800 text-amber-200')
                    : (scrolled ? 'text-gray-700 hover:text-green-600 hover:bg-green-50' : 'text-white hover:bg-green-800')}`}
              >
                Green Jobs
              </a>
              <a 
                href="/skills" 
                class={`py-3 px-4 rounded-lg font-medium transition-colors duration-200
                  ${isActive('/skills')
                    ? (scrolled ? 'bg-green-50 text-green-600' : 'bg-green-800 text-amber-200')
                    : (scrolled ? 'text-gray-700 hover:text-green-600 hover:bg-green-50' : 'text-white hover:bg-green-800')}`}
              >
                Reskilling
              </a>
              <a 
                href="/hustles" 
                class={`py-3 px-4 rounded-lg font-medium transition-colors duration-200
                  ${isActive('/hustles')
                    ? (scrolled ? 'bg-green-50 text-green-600' : 'bg-green-800 text-amber-200')
                    : (scrolled ? 'text-gray-700 hover:text-green-600 hover:bg-green-50' : 'text-white hover:bg-green-800')}`}
              >
                Side Hustles
              </a>
              <a 
                href="/chat" 
                class={`py-3 px-4 rounded-lg font-medium transition-colors duration-200
                  ${isActive('/chat')
                    ? (scrolled ? 'bg-green-50 text-green-600' : 'bg-green-800 text-amber-200')
                    : (scrolled ? 'text-gray-700 hover:text-green-600 hover:bg-green-50' : 'text-white hover:bg-green-800')}`}
              >
                AI Mentor
              </a>
              <div class="border-t border-gray-200 my-2"></div>
              <a 
                href="/profile" 
                class={`py-3 px-4 rounded-lg font-medium transition-colors duration-200
                  ${scrolled ? 'text-gray-700 hover:text-green-600 hover:bg-green-50' : 'text-white hover:bg-green-800'}`}
              >
                Your Profile
              </a>
              <a 
                href="/signout" 
                class={`py-3 px-4 rounded-lg font-medium transition-colors duration-200
                  ${scrolled ? 'text-gray-700 hover:text-green-600 hover:bg-green-50' : 'text-white hover:bg-green-800'}`}
              >
                Sign out
              </a>
            {:else}
              <!-- Public mobile navigation -->
              <a 
                href="/" 
                class={`py-3 px-4 rounded-lg font-medium transition-colors duration-200
                  ${isActive('/') && currentPath === '/'
                    ? (scrolled ? 'bg-green-50 text-green-600' : 'bg-green-800 text-amber-200')
                    : (scrolled ? 'text-gray-700 hover:text-green-600 hover:bg-green-50' : 'text-white hover:bg-green-800')}`}
              >
                Home
              </a>
              <a 
                href="/about" 
                class={`py-3 px-4 rounded-lg font-medium transition-colors duration-200
                  ${isActive('/about')
                    ? (scrolled ? 'bg-green-50 text-green-600' : 'bg-green-800 text-amber-200')
                    : (scrolled ? 'text-gray-700 hover:text-green-600 hover:bg-green-50' : 'text-white hover:bg-green-800')}`}
              >
                About
              </a>
              <a 
                href="/resources" 
                class={`py-3 px-4 rounded-lg font-medium transition-colors duration-200
                  ${isActive('/resources')
                    ? (scrolled ? 'bg-green-50 text-green-600' : 'bg-green-800 text-amber-200')
                    : (scrolled ? 'text-gray-700 hover:text-green-600 hover:bg-green-50' : 'text-white hover:bg-green-800')}`}
              >
                Resources
              </a>
              <div class="pt-2 px-2">
                <button 
                  class={`w-full py-3 px-4 rounded-lg mt-2 font-medium shadow-md
                  ${scrolled 
                    ? 'bg-gradient-to-r from-green-600 to-teal-500 hover:from-green-700 hover:to-teal-600 text-white' 
                    : 'bg-amber-500 hover:bg-amber-600 text-white'}`}
                >
                  Get Started
                </button>
              </div>
            {/if}
          </div>
        </div>
      {/if}
    </div>
  </nav>
  
  <!-- Spacer to prevent content from being hidden under the fixed navbar -->
<div class={`${scrolled ? 'h-16' : 'h-20'}`}></div>