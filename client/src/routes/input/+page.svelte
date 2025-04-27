<script lang="ts">
    import { goto } from '$app/navigation';
    import Navbar from '$lib/components/layouts/Navbar.svelte';
    import UserInputForm from '$lib/components/ui/UserInputForm.svelte';
    import { fade } from 'svelte/transition';
    
    let isFormProcessing = false;
    let errorMessage = '';
    let successMessage = '';
    
    function handleFormSubmit(event: CustomEvent) {
      const formData = event.detail;
      console.log('Form submitted:', formData);
      
      // Validate necessary fields
      if (!formData.jobTitle || !formData.experience) {
        errorMessage = 'Please fill in all required fields';
        return;
      }
      
      // Reset error if any
      errorMessage = '';
      isFormProcessing = true;
      
      // Mock API call - would be a real API call in production
      setTimeout(() => {
        // Store form data in session/local storage or global store
        localStorage.setItem('futureSkillsData', JSON.stringify(formData));
        
        isFormProcessing = false;
        successMessage = 'Analysis complete!';
        
        // Wait a moment to show success message before redirecting
        setTimeout(() => {
          goto('/dashboard');
        }, 1000);
      }, 2000);
    }
  </script>
  <svelte:head>
    <title>Input - FutureSkills Coach</title>
  </svelte:head>
  
  <div class="min-h-screen bg-gradient-to-br from-green-50 to-blue-50" in:fade={{ duration: 300 }}>
    <Navbar isLoggedIn={true}/>
  
    <!-- Hero Section -->
    <div class="container mx-auto px-4 py-12 md:py-20 -mb-32">
      <div class="max-w-5xl mx-auto">
        <div class="text-center mb-12">
          <h1 class="text-3xl md:text-4xl lg:text-5xl font-bold text-gray-800 mb-4">
            Future-Proof Your Career
          </h1>
          <p class="text-lg md:text-xl text-gray-600 max-w-3xl mx-auto">
            Discover sustainable career paths, assess automation risks, and find green job opportunities that match your skills.
          </p>
        </div>
      </div>
    </div>
    
    <!-- Error/Success Messages -->
    {#if errorMessage}
      <div class="max-w-3xl mx-auto px-4 mb-6">
        <div class="bg-red-50 border-l-4 border-red-500 p-4 rounded" role="alert" transition:fade>
          <div class="flex">
            <div class="flex-shrink-0">
              <svg class="h-5 w-5 text-red-500" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
              </svg>
            </div>
            <div class="ml-3">
              <p class="text-sm text-red-700">{errorMessage}</p>
            </div>
          </div>
        </div>
      </div>
    {/if}
    
    {#if successMessage}
      <div class="max-w-3xl mx-auto px-4 mb-6">
        <div class="bg-green-50 border-l-4 border-green-500 p-4 rounded" role="alert" transition:fade>
          <div class="flex">
            <div class="flex-shrink-0">
              <svg class="h-5 w-5 text-green-500" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
              </svg>
            </div>
            <div class="ml-3">
              <p class="text-sm text-green-700">{successMessage}</p>
            </div>
          </div>
        </div>
      </div>
    {/if}
    
    <!-- Main Form Component -->
    <UserInputForm on:formSubmit={handleFormSubmit} />
    
    <!-- Features Section -->
    <div class="container mx-auto px-4 py-16 -mt-10 -mb-10">
      <div class="max-w-5xl mx-auto">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- Feature 1 -->
          <div class="bg-white p-6 rounded-xl shadow-md border border-green-100">
            <div class="w-12 h-12 rounded-full bg-green-100 flex items-center justify-center text-green-600 mb-4">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
              </svg>
            </div>
            <h3 class="font-semibold text-lg text-gray-800 mb-2">Career Risk Analysis</h3>
            <p class="text-gray-600">Understand your job's automation risk and prepare for the future of work.</p>
          </div>
          
          <!-- Feature 2 -->
          <div class="bg-white p-6 rounded-xl shadow-md border border-green-100">
            <div class="w-12 h-12 rounded-full bg-blue-100 flex items-center justify-center text-blue-600 mb-4">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9" />
              </svg>
            </div>
            <h3 class="font-semibold text-lg text-gray-800 mb-2">Green Job Matching</h3>
            <p class="text-gray-600">Discover sustainable career opportunities that align with your skills and passions.</p>
          </div>
          
          <!-- Feature 3 -->
          <div class="bg-white p-6 rounded-xl shadow-md border border-green-100">
            <div class="w-12 h-12 rounded-full bg-amber-100 flex items-center justify-center text-amber-600 mb-4">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            <h3 class="font-semibold text-lg text-gray-800 mb-2">Side Hustle Generator</h3>
            <p class="text-gray-600">Find supplemental income opportunities while transitioning to your new career path.</p>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Footer -->
    <footer class="bg-white border-t border-gray-200 mt-16">
      <div class="container mx-auto px-4 py-8">
        <div class="text-center text-gray-500 text-sm">
          <p>© 2025 FutureSkills Coach. Created for Call for Code Hackathon.</p>
          <p class="mt-2">Supporting UN Sustainable Development Goal 8: Decent Work and Economic Growth</p>
        </div>
      </div>
    </footer>
  </div>