<script lang="ts">
    export let userName: string;
    
    let isMenuOpen = false;
    const toggleMenu = () => isMenuOpen = !isMenuOpen;
  </script>
  
  <header class="bg-white shadow-sm border-b border-gray-200">
    <div class="container mx-auto px-4">
      <div class="flex justify-between items-center py-4">
        <div class="flex items-center">
          <a href="/" class="flex items-center">
            <div class="bg-green-600 text-white p-2 rounded-md mr-2">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
              </svg>
            </div>
            <span class="text-xl font-bold text-green-600">FutureSkills Coach</span>
          </a>
          
          <nav class="hidden md:flex ml-8 space-x-6">
            <a href="/dashboard" class="text-green-700 font-medium">Dashboard</a>
            <a href="/jobs" class="text-gray-600 hover:text-green-600">Green Jobs</a>
            <a href="/skills" class="text-gray-600 hover:text-green-600">Reskilling</a>
            <a href="/hustles" class="text-gray-600 hover:text-green-600">Side Hustles</a>
            <a href="/chat" class="text-gray-600 hover:text-green-600">AI Mentor</a>
          </nav>
        </div>
        
        <div class="flex items-center">
          <div class="hidden md:flex items-center">
            <span class="text-gray-600 mr-2">Welcome,</span>
            <span class="font-medium">{userName}</span>
          </div>
          
          <div class="relative ml-3">
            <button 
              class="bg-gray-100 flex text-sm rounded-full focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500" 
              id="user-menu" 
              aria-expanded="false" 
              aria-haspopup="true"
              on:click={toggleMenu}
            >
              <span class="sr-only">Open user menu</span>
              <div class="h-8 w-8 rounded-full bg-green-600 flex items-center justify-center text-white font-medium">
                {userName.charAt(0)}
              </div>
            </button>
            
            {#if isMenuOpen}
              <div 
                class="origin-top-right absolute right-0 mt-2 w-48 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none" 
                role="menu" 
                aria-orientation="vertical" 
                aria-labelledby="user-menu"
              >
                <div class="py-1" role="none">
                  <a href="/profile" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100" role="menuitem">Your Profile</a>
                  <a href="/settings" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100" role="menuitem">Settings</a>
                  <a href="/signout" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100" role="menuitem">Sign out</a>
                </div>
              </div>
            {/if}
          </div>
          
          <button 
            type="button" 
            class="md:hidden ml-2 bg-white rounded-md p-2 inline-flex items-center justify-center text-gray-500 hover:text-gray-600 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-green-500"
            aria-controls="mobile-menu"
            aria-expanded="false"
            on:click={toggleMenu}
          >
            <span class="sr-only">Open main menu</span>
            <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </button>
        </div>
      </div>
    </div>
    
    {#if isMenuOpen}
      <div class="md:hidden" id="mobile-menu">
        <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3">
          <a href="/dashboard" class="bg-green-50 text-green-700 block px-3 py-2 rounded-md text-base font-medium">Dashboard</a>
          <a href="/jobs" class="text-gray-600 hover:bg-gray-50 hover:text-green-600 block px-3 py-2 rounded-md text-base font-medium">Green Jobs</a>
          <a href="/skills" class="text-gray-600 hover:bg-gray-50 hover:text-green-600 block px-3 py-2 rounded-md text-base font-medium">Reskilling</a>
          <a href="/hustles" class="text-gray-600 hover:bg-gray-50 hover:text-green-600 block px-3 py-2 rounded-md text-base font-medium">Side Hustles</a>
          <a href="/chat" class="text-gray-600 hover:bg-gray-50 hover:text-green-600 block px-3 py-2 rounded-md text-base font-medium">AI Mentor</a>
        </div>
      </div>
    {/if}
  </header>