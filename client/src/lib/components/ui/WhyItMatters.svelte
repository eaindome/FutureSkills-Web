<script lang="ts">
  import { fade, fly } from 'svelte/transition';
  import { onMount } from 'svelte';
  
  const stats = [
    {
      value: "60%",
      label: "Of current jobs will be impacted by automation by 2030",
      icon: "robot",
      description: "AI and automation are reshaping industries from manufacturing to services"
    },
    {
      value: "24M+",
      label: "New green jobs expected globally by 2030",
      icon: "leaf",
      description: "Sustainable sectors like renewable energy, green construction, and eco-tourism are growing rapidly"
    },
    {
      value: "73%",
      label: "Of workers need guidance on transitioning to sustainable careers",
      icon: "compass",
      description: "Bridging the skills gap requires personalized career pathways and training"
    }
  ];
  
  let visible = false;
  
  onMount(() => {
    const observer = new IntersectionObserver((entries) => {
      if (entries[0].isIntersecting) {
        visible = true;
      }
    }, { threshold: 0.2 });
    
    const section = document.getElementById('why-it-matters');
    if (section) observer.observe(section);
    
    return () => {
      if (section) observer.unobserve(section);
    };
  });
</script>

<section id="why-it-matters" class="bg-gradient-to-br from-green-700 to-teal-800 text-white py-24 px-4 sm:px-6 lg:px-8 relative overflow-hidden">
  <!-- Background pattern -->
  <div class="absolute inset-0 opacity-10">
    <svg width="100%" height="100%" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
      <pattern id="grid" width="10" height="10" patternUnits="userSpaceOnUse">
        <path d="M 10 0 L 0 0 0 10" fill="none" stroke="white" stroke-width="0.5"/>
      </pattern>
      <rect width="100%" height="100%" fill="url(#grid)" />
    </svg>
  </div>
  
  <div class="max-w-7xl mx-auto relative">
    <!-- SDG 8 Badge -->
    <div class="absolute top-0 right-0 -mt-10 mr-6 hidden lg:block">
      <div class="bg-amber-500 rounded-full w-20 h-20 flex items-center justify-center shadow-lg">
        <span class="text-white font-bold text-2xl">SDG 8</span>
      </div>
    </div>
    
    <div class="text-center mb-16">
      <h2 class="text-4xl font-bold mb-4">Why It Matters</h2>
      <div class="w-24 h-1 bg-amber-500 mx-auto mb-6"></div>
      <p class="text-xl max-w-3xl mx-auto opacity-90">
        Supporting UN Sustainable Development Goal 8: Promoting decent work and economic growth in a changing world
      </p>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      {#each stats as stat, i}
        {#if visible}
          <div
            class="bg-white/10 backdrop-blur-lg rounded-xl p-8 shadow-xl border border-white/20 hover:bg-white/15 hover:transform hover:scale-105 transition-all duration-300"
            in:fly={{ y: 40, duration: 800, delay: 200 + (i * 150) }}
          >
            <div class="flex flex-col items-center">
              <div class="bg-gradient-to-br from-teal-600 to-green-500 w-20 h-20 rounded-full flex items-center justify-center mb-6 shadow-lg">
                {#if stat.icon === "robot"}
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                  </svg>
                {:else if stat.icon === "leaf"}
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                {:else}
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7" />
                  </svg>
                {/if}
              </div>
              <span class="text-5xl font-bold mb-3 bg-clip-text text-transparent bg-gradient-to-r from-amber-300 to-amber-500">{stat.value}</span>
              <p class="text-center text-lg mb-4">{stat.label}</p>
              <p class="text-center text-sm text-white/80">{stat.description}</p>
            </div>
          </div>
        {/if}
      {/each}
    </div>
    
    <div class="mt-16 max-w-3xl mx-auto text-center">
      <p class="text-xl mb-8">
        By connecting skills, sustainable jobs, and side hustle opportunities, 
        we're building a more inclusive and resilient workforce for the future green economy.
      </p>
      
      <a href="https://www.globalgoals.org/goals/8-decent-work-and-economic-growth/" target="_blank" class="group inline-flex items-center px-6 py-3 text-lg font-medium rounded-lg bg-amber-500 text-white hover:bg-amber-600 transition-all shadow-lg hover:shadow-xl">
        <span>Learn more about SDG 8</span>
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2 group-hover:translate-x-1 transition-transform" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
        </svg>
      </a>
    </div>
  </div>
</section>