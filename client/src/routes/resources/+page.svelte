<script lang="ts">
  import { onMount } from 'svelte';
  import { fade } from 'svelte/transition';
  import Navbar from '$lib/components/layouts/Navbar.svelte';
  import Footer from '$lib/components/layout/Footer.svelte';
  
  interface Resource {
    id: string;
    title: string;
    description: string;
    link: string;
    type: 'pdf' | 'article' | 'tool' | 'faq' | 'ai';
    isNew?: boolean;
    isFeatured?: boolean;
  }
  
  interface ResourceCategory {
    id: string;
    title: string;
    icon: string;
    description: string;
    resources: Resource[];
    expanded: boolean;
  }
  
  let categories: ResourceCategory[] = [
    {
      id: 'toolkits',
      title: '🛠️ Toolkits & Guides',
      icon: 'tools',
      description: 'Essential tools and guides to help you navigate your green career journey',
      expanded: true,
      resources: [
        {
          id: 'transition-guide',
          title: 'How to Transition to a Green Job',
          description: 'Comprehensive guide with step-by-step instructions for pivoting to sustainable careers',
          link: '/resources/guides/green-job-transition.pdf',
          type: 'pdf',
          isFeatured: true
        },
        {
          id: 'resume-templates',
          title: 'Resume Builder Templates for Eco Roles',
          description: 'Customizable templates optimized for green industry applications',
          link: '/resources/tools/green-resume-templates',
          type: 'tool'
        },
        {
          id: 'interview-prep',
          title: 'Interview Prep Tips for Green Jobs',
          description: 'Common questions and winning strategies for sustainable role interviews',
          link: '/resources/guides/green-interview-prep.pdf',
          type: 'pdf'
        },
        {
          id: 'skills-assessment',
          title: 'Green Skills Self-Assessment Tool',
          description: 'Evaluate your current skills and identify gaps for green careers',
          link: '/tools/skills-assessment',
          type: 'tool',
          isNew: true
        }
      ]
    },
    {
      id: 'articles',
      title: '📖 Informational Articles & Blogs',
      icon: 'book-open',
      description: 'Stay informed with the latest insights on green careers and future work trends',
      expanded: true,
      resources: [
        {
          id: 'top-green-careers',
          title: 'Top 10 Green Careers in 2025',
          description: 'Explore the most promising sustainable jobs with growth potential',
          link: '/resources/articles/top-green-careers-2025',
          type: 'article',
          isFeatured: true
        },
        {
          id: 'understanding-risk',
          title: 'Understanding Job Risk in the AI Era',
          description: 'Learn how automation is reshaping industries and how to adapt',
          link: '/resources/articles/job-risk-ai-era',
          type: 'article'
        },
        {
          id: 'green-economy',
          title: 'The Green Economy: Trends and Opportunities',
          description: 'Overview of how sustainability is creating new economic models',
          link: '/resources/articles/green-economy-trends',
          type: 'article'
        },
        {
          id: 'success-stories',
          title: 'Success Stories: Career Transitions to Green Jobs',
          description: 'Real-world examples of successful pivots to sustainable careers',
          link: '/resources/articles/green-transition-stories',
          type: 'article',
          isNew: true
        }
      ]
    },
    {
      id: 'ai-and-faq',
      title: '🤖 AI Chat Links & FAQs',
      icon: 'message-circle',
      description: 'Get answers to your questions and personalized guidance',
      expanded: true,
      resources: [
        {
          id: 'ai-reskilling',
          title: 'Ask the AI About Reskilling Paths',
          description: 'Get personalized learning recommendations based on your background',
          link: '/ai-chat?topic=reskilling',
          type: 'ai'
        },
        {
          id: 'ai-job-risk',
          title: 'Analyze Your Job Risk with AI',
          description: 'Understand how automation might impact your current role',
          link: '/ai-chat?topic=job-risk',
          type: 'ai',
          isFeatured: true
        },
        {
          id: 'ai-side-hustles',
          title: 'Discover Side Hustles with AI Guidance',
          description: 'Find supplementary income sources aligned with your skills',
          link: '/ai-chat?topic=side-hustles',
          type: 'ai'
        },
        {
          id: 'faq-sdg8',
          title: 'FAQs on SDG 8 and Green Economy',
          description: 'Common questions about sustainable development and green growth',
          link: '/resources/faqs/sdg8-green-economy',
          type: 'faq'
        }
      ]
    }
  ];
  
  let searchQuery = '';
  let filterType: string | null = null;
  let activeResource: Resource | null = null;
  let showResourceModal = false;
  
  $: filteredCategories = categories.map(category => {
    const filteredResources = category.resources.filter(resource => {
      const matchesSearch = searchQuery === '' || 
        resource.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
        resource.description.toLowerCase().includes(searchQuery.toLowerCase());
      
      const matchesType = filterType === null || resource.type === filterType;
      
      return matchesSearch && matchesType;
    });
    
    return {
      ...category,
      resources: filteredResources,
      hasMatches: filteredResources.length > 0
    };
  }).filter(category => category.hasMatches);
  
  function toggleCategory(id: string) {
    categories = categories.map(cat => 
      cat.id === id ? { ...cat, expanded: !cat.expanded } : cat
    );
  }
  
  function viewResourceDetails(resource: Resource) {
    activeResource = resource;
    showResourceModal = true;
  }
  
  function closeModal() {
    showResourceModal = false;
  }
  
  function setFilter(type: string | null) {
    filterType = type === filterType ? null : type;
  }
  
  onMount(() => {
    // Simulate loading resources from an API
    setTimeout(() => {
      // Resources already loaded in the initial state
    }, 300);
  });
</script>

<svelte:head>
  <title>Resources - FutureSkills Coach</title>
</svelte:head>

<!-- Main Content -->
<div class="min-h-screen bg-gradient-to-br from-green-50 to-blue-50" in:fade={{ duration: 300 }}>
  <Navbar />
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <div class="mb-8">
      <h1 class="text-3xl font-bold text-teal-700 mb-2">Resources</h1>
      <p class="text-gray-600 max-w-3xl">
        Discover tools, guides, and knowledge to help you transition to sustainable careers 
        and navigate the changing job landscape in the green economy.
      </p>
    </div>
    
    <!-- Search and Filter Bar -->
    <div class="bg-white rounded-lg shadow-md mb-8 p-4 flex flex-col md:flex-row gap-4 items-center">
      <div class="relative flex-grow">
        <input 
          type="text" 
          placeholder="Search resources..." 
          bind:value={searchQuery}
          class="w-full pl-10 pr-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition"
        />
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400 absolute left-3 top-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
        </svg>
      </div>
      
      <div class="flex flex-wrap gap-2">
        <button 
          class={`px-3 py-1 text-sm rounded-full transition ${filterType === 'pdf' ? 'bg-teal-600 text-white' : 'bg-gray-200 text-gray-600 hover:bg-gray-300'}`}
          on:click={() => setFilter('pdf')}
        >
          Guides
        </button>
        <button 
          class={`px-3 py-1 text-sm rounded-full transition ${filterType === 'tool' ? 'bg-teal-600 text-white' : 'bg-gray-200 text-gray-600 hover:bg-gray-300'}`}
          on:click={() => setFilter('tool')}
        >
          Tools
        </button>
        <button 
          class={`px-3 py-1 text-sm rounded-full transition ${filterType === 'article' ? 'bg-teal-600 text-white' : 'bg-gray-200 text-gray-600 hover:bg-gray-300'}`}
          on:click={() => setFilter('article')}
        >
          Articles
        </button>
        <button 
          class={`px-3 py-1 text-sm rounded-full transition ${filterType === 'ai' ? 'bg-teal-600 text-white' : 'bg-gray-200 text-gray-600 hover:bg-gray-300'}`}
          on:click={() => setFilter('ai')}
        >
          AI Chat
        </button>
        <button 
          class={`px-3 py-1 text-sm rounded-full transition ${filterType === 'faq' ? 'bg-teal-600 text-white' : 'bg-gray-200 text-gray-600 hover:bg-gray-300'}`}
          on:click={() => setFilter('faq')}
        >
          FAQs
        </button>
      </div>
    </div>
    
    <!-- Featured Resources -->
    <div class="mb-8">
      <h2 class="text-xl font-semibold text-teal-700 mb-4">Featured Resources</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {#each categories.flatMap(cat => cat.resources).filter(res => res.isFeatured) as resource}
          <div 
            class="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition border-l-4 border-teal-500"
            on:click={() => viewResourceDetails(resource)}
            on:keydown={(e) => e.key === 'Enter' && viewResourceDetails(resource)}
            tabindex="0"
            role="button"
          >
            <div class="p-5">
              <div class="flex justify-between items-start mb-2">
                <h3 class="font-bold text-gray-800">{resource.title}</h3>
                {#if resource.type === 'pdf'}
                  <span class="bg-red-100 text-red-600 text-xs px-2 py-1 rounded-full">PDF</span>
                {:else if resource.type === 'tool'}
                  <span class="bg-blue-100 text-blue-600 text-xs px-2 py-1 rounded-full">Tool</span>
                {:else if resource.type === 'article'}
                  <span class="bg-purple-100 text-purple-600 text-xs px-2 py-1 rounded-full">Article</span>
                {:else if resource.type === 'ai'}
                  <span class="bg-green-100 text-green-600 text-xs px-2 py-1 rounded-full">AI Chat</span>
                {:else}
                  <span class="bg-amber-100 text-amber-600 text-xs px-2 py-1 rounded-full">FAQ</span>
                {/if}
              </div>
              <p class="text-gray-600 text-sm mb-4">{resource.description}</p>
              <div class="flex justify-end">
                <button class="text-sm text-teal-600 hover:text-teal-800 font-medium flex items-center gap-1">
                  View Resource
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
                  </svg>
                </button>
              </div>
            </div>
          </div>
        {/each}
      </div>
    </div>
    
    <!-- Resource Categories -->
    {#each filteredCategories as category}
      <div class="mb-6">
        <div 
          class="flex items-center justify-between bg-white p-4 rounded-lg shadow-sm cursor-pointer"
          on:click={() => toggleCategory(category.id)}
          on:keydown={(e) => e.key === 'Enter' && toggleCategory(category.id)}
          tabindex="0"
          role="button"
        >
          <h2 class="text-xl font-semibold text-gray-800 flex items-center">
            <span class="mr-2">{category.title}</span>
            {#if !category.expanded}
              <span class="bg-teal-100 text-teal-700 text-xs px-2 py-1 rounded-full">{category.resources.length}</span>
            {/if}
          </h2>
          <svg 
            xmlns="http://www.w3.org/2000/svg" 
            class={`h-5 w-5 text-gray-500 transition-transform ${category.expanded ? 'rotate-180' : ''}`} 
            fill="none" 
            viewBox="0 0 24 24" 
            stroke="currentColor"
          >
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
          </svg>
        </div>
        
        {#if category.expanded}
          <div class="p-1 bg-white rounded-b-lg shadow-md mb-6">
            <p class="text-gray-600 mb-4 px-4 pt-2">{category.description}</p>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 p-4">
              {#each category.resources as resource}
                <div 
                  class="bg-white border border-gray-200 hover:border-teal-500 rounded-lg p-4 flex flex-col transition hover:shadow-md cursor-pointer"
                  on:click={() => viewResourceDetails(resource)}
                  on:keydown={(e) => e.key === 'Enter' && viewResourceDetails(resource)}
                  tabindex="0"
                  role="button"
                >
                  <div class="flex justify-between items-start mb-2">
                    <h3 class="font-medium text-gray-800">{resource.title}</h3>
                    <div class="flex gap-1">
                      {#if resource.isNew}
                        <span class="bg-amber-100 text-amber-600 text-xs px-2 py-1 rounded-full">New</span>
                      {/if}
                      
                      {#if resource.type === 'pdf'}
                        <span class="bg-red-100 text-red-600 text-xs px-2 py-1 rounded-full">PDF</span>
                      {:else if resource.type === 'tool'}
                        <span class="bg-blue-100 text-blue-600 text-xs px-2 py-1 rounded-full">Tool</span>
                      {:else if resource.type === 'article'}
                        <span class="bg-purple-100 text-purple-600 text-xs px-2 py-1 rounded-full">Article</span>
                      {:else if resource.type === 'ai'}
                        <span class="bg-green-100 text-green-600 text-xs px-2 py-1 rounded-full">AI Chat</span>
                      {:else}
                        <span class="bg-amber-100 text-amber-600 text-xs px-2 py-1 rounded-full">FAQ</span>
                      {/if}
                    </div>
                  </div>
                  
                  <p class="text-gray-600 text-sm flex-grow">{resource.description}</p>
                  
                  <div class="mt-4 flex justify-end">
                    <button class="text-sm text-teal-600 hover:text-teal-800 font-medium flex items-center gap-1">
                      Access Resource
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
                      </svg>
                    </button>
                  </div>
                </div>
              {/each}
            </div>
          </div>
        {/if}
      </div>
    {/each}
    
    {#if filteredCategories.length === 0}
      <div class="bg-white rounded-lg shadow-md p-8 text-center">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12 text-gray-400 mx-auto mb-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <h3 class="text-lg font-medium text-gray-700 mb-2">No resources found</h3>
        <p class="text-gray-500 mb-4">Try adjusting your search or filters to find what you're looking for.</p>
        <button 
          class="px-4 py-2 bg-teal-600 text-white rounded-lg hover:bg-teal-700 transition"
          on:click={() => { searchQuery = ''; filterType = null; }}
        >
          Clear filters
        </button>
      </div>
    {/if}
  </div>
  
  <!-- Resource Detail Modal -->
  {#if showResourceModal && activeResource}
    <div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
      <div class="bg-white rounded-lg shadow-xl max-w-2xl w-full max-h-[90vh] overflow-y-auto">
        <div class="p-6">
          <div class="flex justify-between items-center mb-4">
            <h2 class="text-2xl font-bold text-gray-800">{activeResource.title}</h2>
            <button 
              class="text-gray-500 hover:text-gray-700"
              on:click={closeModal}
              aria-label="Close"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
          
          <div class="mb-6">
            <div class="flex gap-2 mb-4">
              {#if activeResource.type === 'pdf'}
                <span class="bg-red-100 text-red-600 text-xs px-2 py-1 rounded-full">PDF</span>
              {:else if activeResource.type === 'tool'}
                <span class="bg-blue-100 text-blue-600 text-xs px-2 py-1 rounded-full">Tool</span>
              {:else if activeResource.type === 'article'}
                <span class="bg-purple-100 text-purple-600 text-xs px-2 py-1 rounded-full">Article</span>
              {:else if activeResource.type === 'ai'}
                <span class="bg-green-100 text-green-600 text-xs px-2 py-1 rounded-full">AI Chat</span>
              {:else}
                <span class="bg-amber-100 text-amber-600 text-xs px-2 py-1 rounded-full">FAQ</span>
              {/if}
              
              {#if activeResource.isNew}
                <span class="bg-amber-100 text-amber-600 text-xs px-2 py-1 rounded-full">New</span>
              {/if}
              
              {#if activeResource.isFeatured}
                <span class="bg-teal-100 text-teal-600 text-xs px-2 py-1 rounded-full">Featured</span>
              {/if}
            </div>
            
            <p class="text-gray-600 mb-4">{activeResource.description}</p>
            
            {#if activeResource.type === 'pdf'}
              <div class="bg-gray-100 rounded-lg p-4 mb-4">
                <p class="text-sm text-gray-600">This resource is available as a downloadable PDF document.</p>
              </div>
            {:else if activeResource.type === 'ai'}
              <div class="bg-green-50 rounded-lg p-4 mb-4">
                <p class="text-sm text-gray-600">This resource connects you to our AI assistant for personalized guidance.</p>
              </div>
            {/if}
          </div>
          
          <div class="flex gap-3 justify-end">
            <button 
              class="px-4 py-2 bg-gray-200 text-gray-700 rounded-lg hover:bg-gray-300 transition"
              on:click={closeModal}
            >
              Close
            </button>
            <a 
              href={activeResource.link} 
              class="px-4 py-2 bg-teal-600 text-white rounded-lg hover:bg-teal-700 transition flex items-center gap-2"
            >
              {#if activeResource.type === 'pdf'}
                Download PDF
              {:else if activeResource.type === 'tool'}
                Use Tool
              {:else if activeResource.type === 'article'}
                Read Article
              {:else if activeResource.type === 'ai'}
                Start AI Chat
              {:else}
                View FAQ
              {/if}
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
              </svg>
            </a>
          </div>
        </div>
      </div>
    </div>
  {/if}
  
  <!-- Newsletter Signup -->
  <div class="bg-teal-700 rounded-lg shadow-lg p-6 my-8 max-w-7xl mx-auto">
    <div class="flex flex-col md:flex-row items-center justify-between gap-6">
      <div>
        <h3 class="text-xl font-bold text-white mb-2">Stay Updated on Green Career Trends</h3>
        <p class="text-teal-100">Get the latest resources, job opportunities, and skill-building tips delivered to your inbox.</p>
      </div>
      <div class="w-full md:w-auto flex flex-col sm:flex-row gap-2">
        <input 
          type="email" 
          placeholder="Your email address" 
          class="px-4 py-2 rounded-lg border-2 border-teal-600 focus:ring-2 focus:ring-amber-400 focus:border-amber-400 w-full"
        />
        <button class="bg-amber-500 hover:bg-amber-600 text-white font-medium px-4 py-2 rounded-lg transition whitespace-nowrap">
          Subscribe
        </button>
      </div>
    </div>
  </div>
</div>

<!-- Footer -->
 <Footer />

<style>
  /* Additional styles if needed */
  :global(body) {
    background-color: #f9fafb;
  }
</style>