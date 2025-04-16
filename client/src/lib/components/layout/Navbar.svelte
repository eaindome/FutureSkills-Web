<script lang="ts">
  import { onMount } from 'svelte';
  import { fly } from 'svelte/transition';
 
  let isMenuOpen = false;
  let scrolled = false;
  let prevScrollPos = 0;
  let visible = true;
 
  function toggleMenu() {
    isMenuOpen = !isMenuOpen;
  }
 
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
 
 <nav class={`fixed w-full z-30 transition-all duration-300 ${scrolled ? 'bg-white/95 backdrop-blur-sm shadow-lg py-2' : 'bg-transparent py-4'} 
   ${visible ? 'translate-y-0' : '-translate-y-full'}`}>
   <div class="container mx-auto px-4">
     <div class="flex justify-between items-center">
       <div class="flex items-center">
         <a href="/" class="flex items-center group">
           <div class="w-10 h-10 rounded-full bg-gradient-to-br from-green-600 to-teal-500 flex items-center justify-center mr-2 shadow-md group-hover:shadow-lg transition-all duration-300 group-hover:scale-105">
             <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6 text-white">
               <path d="M11.584 2.376a.75.75 0 01.832 0l9 6a.75.75 0 11-.832 1.248L12 3.901 3.416 9.624a.75.75 0 01-.832-1.248l9-6z" />
               <path fill-rule="evenodd" d="M20.25 10.332v9.918H21a.75.75 0 010 1.5H3a.75.75 0 010-1.5h.75v-9.918a.75.75 0 01.634-.74A49.109 49.109 0 0112 9c2.59 0 5.134.202 7.616.592a.75.75 0 01.634.74zm-7.5 2.418a.75.75 0 00-1.5 0v6.75a.75.75 0 001.5 0v-6.75zm3-.75a.75.75 0 01.75.75v6.75a.75.75 0 01-1.5 0v-6.75a.75.75 0 01.75-.75zM9 12.75a.75.75 0 00-1.5 0v6.75a.75.75 0 001.5 0v-6.75z" clip-rule="evenodd" />
             </svg>
           </div>
           <div>
             <span class="text-xl font-bold bg-gradient-to-r from-green-700 to-teal-600 bg-clip-text text-transparent">FutureSkills</span>
             <span class="text-xl font-medium text-gray-700">Coach</span>
           </div>
         </a>
       </div>
       
       <!-- Desktop Navigation -->
       <div class="hidden md:flex items-center space-x-1">
         {#each ['Home', 'Dashboard', 'AI Mentor', 'About'] as item, i}
           <a 
             href={item === 'Home' ? '/' : `/${item.toLowerCase().replace(' ', '-')}`} 
             class="text-gray-700 hover:text-green-600 font-medium px-3 py-2 rounded-lg hover:bg-green-50 transition-all duration-200"
           >
             {item}
           </a>
         {/each}
         <button class="ml-4 bg-gradient-to-r from-green-600 to-teal-500 hover:from-green-700 hover:to-teal-600 text-white py-2 px-5 rounded-lg transition-all duration-300 shadow-md hover:shadow-lg transform hover:-translate-y-0.5">
           Get Started
         </button>
       </div>
       
       <!-- Mobile menu button -->
       <div class="md:hidden">
         <button
           on:click={toggleMenu}
           class="text-gray-700 hover:text-green-600 focus:outline-none p-2 rounded-lg hover:bg-green-50"
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
       <div class="md:hidden mt-4 pb-4 bg-white rounded-lg shadow-lg" transition:fly={{ y: -20, duration: 300 }}>
         <div class="flex flex-col space-y-1 px-2">
           {#each ['Home', 'Dashboard', 'AI Mentor', 'About'] as item, i}
             <a 
               href={item === 'Home' ? '/' : `/${item.toLowerCase().replace(' ', '-')}`} 
               class="text-gray-700 hover:text-green-600 hover:bg-green-50 py-3 px-4 rounded-lg font-medium transition-colors duration-200"
             >
               {item}
             </a>
           {/each}
           <div class="pt-2 px-2">
             <button class="w-full bg-gradient-to-r from-green-600 to-teal-500 hover:from-green-700 hover:to-teal-600 text-white py-3 px-4 rounded-lg mt-2 transition-colors duration-300 font-medium shadow-md">
               Get Started
             </button>
           </div>
         </div>
       </div>
     {/if}
   </div>
 </nav>
 
 <!-- Spacer to prevent content from being hidden under the fixed navbar -->
 <div class={`${scrolled ? 'h-16' : 'h-20'}`}></div>