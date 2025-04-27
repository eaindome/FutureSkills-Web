<script lang="ts">
    import Navbar from '$lib/components/layouts/Navbar.svelte';
    import PlantGrowth from '$lib/components/animations/PlantGrowth.svelte';
    import { page } from '$app/stores';
    import { onMount } from 'svelte';
    
    // Error status and messages
    let errorTitle = "Page Not Found";
    let errorMessage = "The page you're looking for doesn't exist or is still under development.";
    
    // Animation states
    let animationActive = false;
    
    // Get the referrer to personalize message
    let referrer = '';
    let hasReferrer = false;
    
    // Handle plant interaction
    function handlePlantInteraction(event: CustomEvent<{ stage: number }>) {
      // You can add additional effects when the plant is interacted with
      console.log('Plant growth stage:', event.detail.stage);
    }
    
    onMount(() => {
      // Start entrance animation
      setTimeout(() => {
        animationActive = true;
      }, 100);
      
      // Get referrer
      referrer = document.referrer;
      hasReferrer = referrer.includes('futureskills') || referrer.includes('localhost');
      
      // Customize error message based on status
      if ($page.status === 404) {
        errorTitle = "Page Not Found";
        errorMessage = hasReferrer 
          ? "This feature is still sprouting 🌱 It's coming soon as part of our sustainability journey!" 
          : "Oops! This page couldn't be found or hasn't sprouted yet 🌱";
      } else if ($page.status === 500) {
        errorTitle = "Something Went Wrong";
        errorMessage = "We're experiencing some technical difficulties. Our team has been notified and is working on it.";
      } else {
        errorTitle = `Error ${$page.status}`;
        errorMessage = $page.error?.message || "Something unexpected happened. Please try again.";
      }
    });
  </script>
  
  <svelte:head>
    <title>{errorTitle} - FutureSkills Coach</title>
    <meta name="description" content="Error page for FutureSkills Coach - {errorTitle}">
  </svelte:head>
  
  <div class="min-h-screen bg-gradient-to-b from-gray-50 to-green-50 flex flex-col">
    <Navbar isLoggedIn={false} />
    
    <main class="flex-grow flex items-center justify-center">
      <div class="container mx-auto px-4 py-8 md:py-16 max-w-4xl">
        <div class="text-center mb-8 transition-all duration-700 transform {animationActive ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'}">
          <!-- Plant Growth Animation Component -->
          <div class="mb-6">
            <PlantGrowth 
              autoTransition={true} 
              initialStage={0} 
              windEffect={true}
              on:interaction={handlePlantInteraction}
            />
          </div>
          
          <div class="space-y-4">
            <h1 class="text-4xl font-bold text-green-600 mb-2">{errorTitle}</h1>
            
            <p class="text-xl text-gray-600 mb-4 max-w-2xl mx-auto">
              {errorMessage}
            </p>
            
            <p class="text-gray-500 mb-8">
              Watch the plant grow, or click on it to speed up its growth. Explore our available tools below.
            </p>
          </div>
          
          <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <a 
              href="/" 
              class="bg-green-600 hover:bg-green-700 text-white font-medium py-3 px-6 rounded-lg transition-all duration-300 transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-green-300 focus:ring-opacity-50 shadow-md hover:shadow-lg"
            >
              Back to Dashboard
            </a>
            
            <a 
              href="/chat" 
              class="bg-amber-500 hover:bg-amber-600 text-white font-medium py-3 px-6 rounded-lg transition-all duration-300 transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-amber-300 focus:ring-opacity-50 shadow-md hover:shadow-lg"
            >
              Talk to Your AI Mentor
            </a>
          </div>
        </div>
        
        <!-- Search Section -->
        <div class="max-w-md mx-auto mt-12 mb-8 bg-white p-6 rounded-xl shadow-md border border-green-100 transition-all duration-700 transform {animationActive ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'}">
          <h2 class="text-lg font-semibold text-gray-800 mb-4">Looking for something specific?</h2>
          <div class="flex">
            <input 
              type="text" 
              placeholder="Search our resources..." 
              class="flex-grow px-4 py-2 border border-gray-300 rounded-l-lg focus:outline-none focus:ring-2 focus:ring-green-300 focus:border-transparent"
            />
            <button 
              class="bg-green-600 text-white px-4 py-2 rounded-r-lg hover:bg-green-700 transition-colors duration-300"
              aria-label="Search"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
            </button>
          </div>
        </div>
        
        <!-- Quick Links -->
        <div class="mt-8 transition-all duration-700 delay-100 transform {animationActive ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'}">
          <h2 class="text-xl font-semibold text-center text-gray-700 mb-6">Popular Resources</h2>
          <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
            <a href="/assessment" class="flex items-center p-4 bg-white rounded-lg shadow-sm border border-green-100 hover:shadow-md transition-all duration-300 hover:border-green-200">
              <div class="w-10 h-10 rounded-full bg-green-100 flex items-center justify-center text-green-600 mr-3">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <span>Skills Assessment</span>
            </a>
            
            <a href="/learning-paths" class="flex items-center p-4 bg-white rounded-lg shadow-sm border border-green-100 hover:shadow-md transition-all duration-300 hover:border-green-200">
              <div class="w-10 h-10 rounded-full bg-blue-100 flex items-center justify-center text-blue-600 mr-3">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
                </svg>
              </div>
              <span>Learning Paths</span>
            </a>
            
            <a href="/community" class="flex items-center p-4 bg-white rounded-lg shadow-sm border border-green-100 hover:shadow-md transition-all duration-300 hover:border-green-200">
              <div class="w-10 h-10 rounded-full bg-amber-100 flex items-center justify-center text-amber-600 mr-3">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
                </svg>
              </div>
              <span>Community Forum</span>
            </a>
          </div>
        </div>
      </div>
    </main>
    
    <footer class="py-6 border-t border-gray-200 mt-8">
      <div class="container mx-auto px-4">
        <div class="flex justify-center items-center">
          <p class="text-gray-500 text-sm">© 2025 FutureSkills Coach | Supporting SDG 8: Decent Work and Economic Growth</p>
        </div>
      </div>
    </footer>
  </div>