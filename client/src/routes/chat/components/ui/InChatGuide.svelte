<!-- src/lib/components/ui/InChatGuide.svelte -->
<script lang="ts">
    import { createEventDispatcher, onMount } from 'svelte';
    import { fade, fly, slide } from 'svelte/transition';
    
    export let showGuide = true;
    const dispatch = createEventDispatcher();
    
    let currentStep = 0;
    const totalSteps = 3;
    const steps = [
      {
        title: "Welcome to FutureSkills Coach!",
        content: "I'll help you discover green job opportunities, assess your skills, and find your sustainable career path.",
        icon: "💼"
      },
      {
        title: "How It Works",
        content: "Ask me about job risks, green careers, training opportunities, or side hustles. I'll provide personalized guidance based on your situation.",
        icon: "🔍"
      },
      {
        title: "Try These Examples",
        content: "Ask about careers in renewable energy, transitioning from your current role, or skills that will be valuable in the future green economy.",
        icon: "🌱"
      }
    ];
    
    function nextStep() {
      if (currentStep < totalSteps - 1) {
        currentStep++;
      } else {
        completeGuide();
      }
    }
    
    function prevStep() {
      if (currentStep > 0) {
        currentStep--;
      }
    }
    
    function completeGuide() {
      dispatch('complete');
    }
    
    function skipGuide() {
      dispatch('complete');
    }
  </script>
  
  {#if showGuide}
    <div 
      class="bg-gradient-to-r from-teal-50 to-green-50 rounded-xl border border-teal-200 shadow-md mb-6 overflow-hidden"
      in:fly={{ y: 20, duration: 400 }}
      out:fade={{ duration: 200 }}
    >
      <div class="p-4">
        <!-- Progress indicator -->
        <div class="flex justify-between items-center mb-4">
          <div class="flex space-x-1.5">
            {#each Array(totalSteps) as _, i}
              <div 
                class="w-2.5 h-2.5 rounded-full transition-all duration-300 {i === currentStep ? 'bg-teal-500 scale-125' : i < currentStep ? 'bg-teal-400' : 'bg-teal-200'}"
              ></div>
            {/each}
          </div>
          <button 
            on:click={skipGuide}
            class="text-xs text-gray-500 hover:text-gray-700 underline"
          >
            Skip intro
          </button>
        </div>
        
        <!-- Content -->
        <div class="h-[120px] relative">
          {#each steps as step, i}
            {#if i === currentStep}
              <div 
                class="flex flex-col items-center text-center"
              >
                <div class="text-3xl mb-2">{step.icon}</div>
                <h3 class="text-lg font-medium text-teal-800 mb-1.5">{step.title}</h3>
                <p class="text-gray-700">{step.content}</p>
              </div>
            {/if}
          {/each}
        </div>
        
        <!-- Navigation buttons -->
        <div class="flex justify-between mt-4">
          <button 
            on:click={prevStep}
            class="px-3 py-1.5 text-gray-600 hover:text-gray-800 disabled:opacity-50 disabled:cursor-not-allowed transition-colors text-sm flex items-center"
            disabled={currentStep === 0}
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-1" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clip-rule="evenodd" />
            </svg>
            Back
          </button>
          <button 
            on:click={nextStep}
            class="px-4 py-1.5 bg-gradient-to-r from-teal-500 to-green-500 hover:from-teal-600 hover:to-green-600 text-white rounded-lg shadow-sm hover:shadow transition-all text-sm flex items-center"
          >
            {currentStep < totalSteps - 1 ? 'Next' : 'Get Started'}
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 ml-1" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
            </svg>
          </button>
        </div>
      </div>
    </div>
  {/if}