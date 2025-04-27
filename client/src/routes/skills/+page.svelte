<script lang="ts">
    import Navbar from '$lib/components/layouts/Navbar.svelte';
    import SkillsRadarChart from '../dashboard/components/charts/SkillsRadarChart.svelte';
    import ReskillingCard from '../dashboard/components/cards/ReskillingCard.svelte';
    import SideHustleCard from '../dashboard/components/cards/SideHustleCard.svelte';
    import ProgressTracker from '../dashboard/components/ui/ProgressTracker.svelte';
    import DashboardHeader from '../dashboard/components/layout/DashboardHeader.svelte';
    
    // Mock data - in a real app this would come from API or store
    const userData = {
      name: "Alex Johnson",
      currentJob: "Retail Cashier",
      riskScore: 75,
      completedSteps: ["profile", "assessment","reskilling"],
      nextSteps: ["mentoring"]
    };
    
    const reskillingOptions = [
      {
        title: "Green Retail Operations Certificate",
        provider: "Coursera",
        cost: 50,
        duration: "3 weeks",
        url: "#",
        skills: ["Sustainable inventory", "Eco-friendly merchandising", "Green customer service"]
      },
      {
        title: "Solar Energy Basics",
        provider: "edX",
        cost: 75,
        duration: "4 weeks",
        url: "#",
        skills: ["PV technology", "Solar market basics", "Customer consultation"]
      },
      {
        title: "Sustainable Business Practices",
        provider: "LinkedIn Learning",
        cost: 35,
        duration: "2 weeks",
        url: "#",
        skills: ["Carbon footprint reduction", "Sustainable supply chain", "Green marketing"]
      }
    ];
    
    const sideHustles = [
      {
        title: "Eco-friendly Crafts on Etsy",
        potentialIncome: 200,
        startupCost: 50,
        timeCommitment: "5-10 hours/week",
        skillsUsed: "Creativity, customer service, basic crafting"
      },
      {
        title: "Sustainability Blogger",
        potentialIncome: 150,
        startupCost: 0,
        timeCommitment: "3-5 hours/week",
        skillsUsed: "Writing, social media, basic web skills"
      },
      {
        title: "Used Item Reseller",
        potentialIncome: 250,
        startupCost: 100,
        timeCommitment: "8-12 hours/week",
        skillsUsed: "Photography, negotiation, inventory management"
      }
    ];
    
    // Skill metrics data
    const currentSkills = [
      { name: "Customer Service", value: 85, relevance: "High" },
      { name: "Cash Handling", value: 90, relevance: "Low" },
      { name: "Inventory Management", value: 70, relevance: "Medium" },
      { name: "Sales", value: 65, relevance: "High" },
      { name: "Product Knowledge", value: 75, relevance: "Medium" }
    ];
    
    const requiredSkills = [
      { name: "Customer Service", value: 90, gap: 5 },
      { name: "Sales", value: 80, gap: 15 },
      { name: "Sustainable Products", value: 70, gap: 70 },
      { name: "Solar Technology", value: 60, gap: 60 },
      { name: "Digital Tools", value: 50, gap: 30 }
    ];
    
    // Function to get color classes based on relevance
    function getRelevanceColors(relevance: string) {
      switch (relevance) {
        case "High":
          return { text: "text-teal-600", bg: "bg-teal-500", light: "bg-teal-100" };
        case "Medium":
          return { text: "text-yellow-600", bg: "bg-yellow-500", light: "bg-yellow-100" };
        default:
          return { text: "text-gray-600", bg: "bg-gray-400", light: "bg-gray-100" };
      }
    }
    
    // Current learning items for the timeline
    const learningPath = [
      {
        title: "Green Retail Basics",
        progress: 75,
        status: "In Progress",
        dueDate: "May 10, 2025"
      },
      {
        title: "Solar Energy Fundamentals",
        progress: 25,
        status: "In Progress",
        dueDate: "June 15, 2025"
      },
      {
        title: "Sustainable Inventory",
        progress: 0,
        status: "Not Started",
        dueDate: "July 1, 2025"
      }
    ];
</script>

<svelte:head>
  <title>Skills - FutureSkills Coach</title>
</svelte:head>

<div class="min-h-screen bg-gray-50">
    <Navbar isLoggedIn={true}/>

    <main class="container mx-auto px-4 py-6 max-w-7xl">
        <!-- Page Header -->
        <div class="flex flex-col md:flex-row md:items-center justify-between mb-6">
          <div>
            <h1 class="text-3xl font-bold text-green-600 mb-2">Your Skills Development</h1>
            <p class="text-gray-500">Track your progress and build the skills you need for a sustainable career.</p>
          </div>
          <div class="flex items-center mt-4 md:mt-0">
            <span class="text-gray-500 mr-3">Last updated: Apr 18, 2025</span>
            <div class="flex space-x-2">
                <a href="/dashboard" class="flex items-center bg-gray-100 hover:bg-gray-200 text-gray-600 px-4 py-2 rounded-md transition-colors mr-3">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M9.707 14.707a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 1.414L7.414 9H15a1 1 0 110 2H7.414l2.293 2.293a1 1 0 010 1.414z" clip-rule="evenodd" />
                    </svg>
                    Back to Dashboard
                </a>
              <button class="flex items-center bg-green-100 hover:bg-green-200 text-green-600 px-4 py-2 rounded-md transition-colors">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M4 2a1 1 0 011 1v2.101a7.002 7.002 0 0111.601 2.566 1 1 0 11-1.885.666A5.002 5.002 0 005.999 7H9a1 1 0 010 2H4a1 1 0 01-1-1V3a1 1 0 011-1zm.008 9.057a1 1 0 011.276.61A5.002 5.002 0 0014.001 13H11a1 1 0 110-2h5a1 1 0 011 1v5a1 1 0 11-2 0v-2.101a7.002 7.002 0 01-11.601-2.566 1 1 0 01.61-1.276z" clip-rule="evenodd" />
                </svg>
                Refresh Skills
              </button>
            </div>
          </div>
        </div>

        <!-- Main Content Wrapper -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
            <!-- Main Content Column -->
            <div class="lg:col-span-8 space-y-6">
                <!-- Skills Summary Card -->
                <div class="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden">
                    <div class="bg-gradient-to-r from-teal-600 to-green-600 px-6 py-4">
                        <h2 class="text-xl font-bold text-white flex items-center gap-2">
                            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <circle cx="12" cy="12" r="10"></circle>
                                <path d="m8 12 3 3 6-6"></path>
                            </svg>
                            Skills Overview
                        </h2>
                    </div>
                    <div class="p-6">
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div>
                                <h3 class="text-lg font-medium text-gray-700 mb-4 flex items-center gap-2">
                                    <div class="p-1.5 rounded-full bg-teal-100">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-teal-600">
                                            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                                            <path d="m9 11 3 3L22 4"></path>
                                        </svg>
                                    </div>
                                    Your Current Skills
                                </h3>
                                <div class="h-64">
                                    <SkillsRadarChart 
                                        skills={currentSkills} 
                                        chartType="current" 
                                        showLegend={true}
                                    />
                                </div>
                            </div>
                            <div>
                                <h3 class="text-lg font-medium text-gray-700 mb-4 flex items-center gap-2">
                                    <div class="p-1.5 rounded-full bg-sky-100">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-sky-600">
                                            <path d="M18 6 7 17l-5-5"></path>
                                            <path d="m22 10-7.5 7.5L13 16"></path>
                                        </svg>
                                    </div>
                                    Skills Gap Analysis
                                </h3>
                                <div class="h-64">
                                    <SkillsRadarChart skills={requiredSkills} chartType="required" />
                                </div>
                            </div>
                        </div>
                        
                        <!-- Recommendation Box -->
                        <div class="mt-6 p-5 rounded-lg border-l-4 border-teal-500 bg-gradient-to-r from-teal-50 to-green-50 flex gap-4">
                            <div class="flex-shrink-0">
                                <div class="p-2 bg-teal-100 rounded-full">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-teal-600">
                                        <circle cx="12" cy="12" r="10"></circle>
                                        <path d="m8 12 3 3 6-6"></path>
                                    </svg>
                                </div>
                            </div>
                            <div>
                                <h4 class="font-semibold text-teal-800 mb-1">Skill Development Recommendation</h4>
                                <p class="text-teal-700">Focus on developing <span class="font-medium">Sustainable Product Knowledge</span> and <span class="font-medium">Solar Technology Basics</span> to qualify for the recommended green jobs.</p>
                                
                                <!-- <div class="mt-4 flex flex-wrap gap-2">
                                    <button class="px-4 py-2 bg-sky-600 hover:bg-sky-700 text-white rounded-lg text-sm font-medium transition-colors flex items-center gap-1">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                            <path d="M22 10v6M2 10l10-5 10 5-10 5z"></path>
                                            <path d="M6 12v5c3 3 9 3 12 0v-5"></path>
                                        </svg>
                                        Explore Courses
                                    </button>
                                </div> -->
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Current Skills & Development Path -->
                <div class="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden">
                    <div class="px-6 py-4 border-b border-gray-200 bg-gray-50">
                        <h2 class="text-xl font-semibold text-gray-700">Skills Analysis</h2>
                    </div>
                    <div class="p-6">
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <!-- Current Skills Card -->
                            <div class="bg-gray-50 rounded-lg p-5 border border-gray-100">
                                <h3 class="text-lg font-semibold text-gray-800 mb-4">Current Skills</h3>
                                
                                <div class="space-y-4">
                                    {#each currentSkills as skill}
                                        {@const colors = getRelevanceColors(skill.relevance)}
                                        <div>
                                            <div class="flex justify-between mb-2">
                                                <span class="text-gray-700 font-medium">{skill.name}</span>
                                                <span class="text-sm font-medium px-2 py-0.5 rounded-full {colors.light} {colors.text}">
                                                    {skill.relevance} Relevance
                                                </span>
                                            </div>
                                            <div class="flex items-center">
                                                <div class="w-full bg-gray-200 rounded-full h-3 mr-2">
                                                    <div class="{colors.bg} h-3 rounded-full" style="width: {skill.value}%"></div>
                                                </div>
                                                <span class="text-sm font-medium text-gray-700 w-8 text-right">{skill.value}%</span>
                                            </div>
                                        </div>
                                    {/each}
                                </div>
                            </div>
                            
                            <!-- Skills to Develop Card -->
                            <div class="bg-gray-50 rounded-lg p-5 border border-gray-100">
                                <h3 class="text-lg font-semibold text-gray-800 mb-4">Skills to Develop</h3>
                                
                                <div class="space-y-4">
                                    {#each requiredSkills as skill}
                                        <div>
                                            <div class="flex justify-between mb-2">
                                                <span class="text-gray-700 font-medium">{skill.name}</span>
                                                <span class="text-sm font-medium px-2 py-0.5 rounded-full bg-sky-100 text-sky-600">
                                                    Gap: {skill.gap}%
                                                </span>
                                            </div>
                                            <div class="flex items-center">
                                                <div class="w-full bg-gray-200 rounded-full h-3 mr-2 relative">
                                                    <!-- Current skill level -->
                                                    <div class="bg-sky-500 h-3 rounded-full" style="width: {100 - skill.gap}%"></div>
                                                    
                                                    <!-- Target indicator -->
                                                    <div class="absolute right-0 top-0 bottom-0 border-r-2 border-sky-700 h-3" style="left: calc(100% - 1px);">
                                                        <div class="bg-sky-700 h-5 w-1.5 absolute -top-1 -right-0.75 rounded"></div>
                                                    </div>
                                                </div>
                                                <span class="text-sm font-medium text-gray-700 w-12 text-right">
                                                    {100 - skill.gap}% / 100%
                                                </span>
                                            </div>
                                        </div>
                                    {/each}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Learning Path Timeline -->
                <div class="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden">
                    <div class="px-6 py-4 border-b border-gray-200 bg-gray-50">
                        <h2 class="text-xl font-semibold text-gray-700">Your Learning Path</h2>
                    </div>
                    <div class="p-6">
                        <div class="relative">
                            <!-- Timeline line -->
                            <div class="absolute top-0 left-6 bottom-0 w-0.5 bg-gray-200"></div>
                            
                            <!-- Timeline items -->
                            <div class="space-y-6">
                                <!-- Step 1 -->
                                <div class="flex items-start relative">
                                    <div class="absolute left-4 top-0 w-4 h-4 rounded-full bg-teal-500 border-4 border-teal-100 z-10"></div>
                                    <div class="pl-16">
                                        <div class="bg-teal-50 p-4 rounded-lg border border-teal-100 relative">
                                            <span class="absolute -left-2 top-4 transform -translate-y-1/2 w-4 h-4 bg-teal-50 border-l border-t border-teal-100 rotate-45"></span>
                                            <h4 class="font-medium text-teal-700">Start with Fundamentals</h4>
                                            <p class="text-teal-600 text-sm mt-1">Take "Introduction to Sustainable Products" online course (4 weeks)</p>
                                        </div>
                                    </div>
                                </div>
                                
                                <!-- Step 2 -->
                                <div class="flex items-start relative">
                                    <div class="absolute left-4 top-0 w-4 h-4 rounded-full bg-sky-500 border-4 border-sky-100 z-10"></div>
                                    <div class="pl-16">
                                        <div class="bg-sky-50 p-4 rounded-lg border border-sky-100 relative">
                                            <span class="absolute -left-2 top-4 transform -translate-y-1/2 w-4 h-4 bg-sky-50 border-l border-t border-sky-100 rotate-45"></span>
                                            <h4 class="font-medium text-sky-700">Build Technical Knowledge</h4>
                                            <p class="text-sky-600 text-sm mt-1">Complete "Solar Technology Certificate" (8 weeks part-time)</p>
                                        </div>
                                    </div>
                                </div>
                                
                                <!-- Step 3 -->
                                <div class="flex items-start relative">
                                    <div class="absolute left-4 top-0 w-4 h-4 rounded-full bg-gray-400 border-4 border-gray-100 z-10"></div>
                                    <div class="pl-16">
                                        <div class="bg-gray-50 p-4 rounded-lg border border-gray-200 relative">
                                            <span class="absolute -left-2 top-4 transform -translate-y-1/2 w-4 h-4 bg-gray-50 border-l border-t border-gray-200 rotate-45"></span>
                                            <h4 class="font-medium text-gray-700">Get Certified</h4>
                                            <p class="text-gray-600 text-sm mt-1">Obtain "Green Certification" (2-day workshop + exam)</p>
                                        </div>
                                    </div>
                                </div>
                                
                                <!-- Step 4 -->
                                <div class="flex items-start relative">
                                  <div class="absolute left-4 top-0 w-4 h-4 rounded-full bg-gray-400 border-4 border-gray-100 z-10"></div>
                                  <div class="pl-16">
                                      <div class="bg-gray-50 p-4 rounded-lg border border-gray-200 relative">
                                          <span class="absolute -left-2 top-4 transform -translate-y-1/2 w-4 h-4 bg-gray-50 border-l border-t border-gray-200 rotate-45"></span>
                                          <h4 class="font-medium text-gray-700">Get Certified</h4>
                                          <p class="text-gray-600 text-sm mt-1">Obtain "Green Certification" (2-day workshop + exam)</p>
                                      </div>
                                  </div>
                              </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Bottom Sections -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <!-- Recommended Courses -->
                    <div class="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden h-full">
                        <div class="px-4 py-3 border-b border-gray-200 bg-gray-50 flex items-center justify-between">
                            <h2 class="text-lg font-medium text-gray-700">Recommended Courses</h2>
                            <button class="text-green-600 text-sm font-medium hover:text-green-700 flex items-center">
                                View All
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 ml-1" viewBox="0 0 20 20" fill="currentColor">
                                    <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
                                </svg>
                            </button>
                        </div>
                        <div class="p-4 space-y-4">
                            {#each reskillingOptions as option}
                                <ReskillingCard {option} />
                            {/each}
                        </div>
                    </div>
                    
                    <!-- Side Hustles -->
                    <div class="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden h-full">
                        <div class="px-4 py-3 border-b border-gray-200 bg-gray-50 flex items-center justify-between">
                            <h2 class="text-lg font-medium text-gray-700">Side Hustle Ideas</h2>
                            <button class="text-green-600 text-sm font-medium hover:text-green-700 flex items-center">
                                View All
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 ml-1" viewBox="0 0 20 20" fill="currentColor">
                                    <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
                                </svg>
                            </button>
                        </div>
                        <div class="p-4 space-y-4">
                            {#each sideHustles as hustle}
                                <SideHustleCard {hustle} />
                            {/each}
                        </div>
                    </div>
                </div>
            </div>

            <!-- Sidebar -->
            <div class="lg:col-span-4 space-y-6">
                <!-- AI Mentor Card - Priority 1 -->
                <div class="bg-white rounded-lg shadow-sm border border-green-200 p-6">
                    <div class="flex items-center mb-4">
                        <div class="bg-green-100 rounded-full p-2 mr-3">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
                            </svg>
                        </div>
                        <h2 class="text-xl font-semibold text-green-600">AI Career Mentor</h2>
                    </div>
                    <p class="text-gray-600 mb-4">Have questions about your career transition or need personalized advice?</p>
                    <a href="/chat" class="block w-full bg-green-600 hover:bg-green-700 text-white font-medium py-3 px-4 rounded-md text-center transition-colors">
                        Talk to Your AI Mentor
                    </a>
                </div>
                
                <!-- Progress Tracker - Priority 2 -->
                <ProgressTracker 
                    completedSteps={userData.completedSteps}
                    nextSteps={userData.nextSteps}
                />
        
              <!-- Action Plan Card -->
              <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
                <h2 class="text-xl font-semibold text-green-600 mb-4">Your Action Plan</h2>
                <div class="space-y-4">
                  <div class="flex items-start">
                    <div class="bg-green-100 rounded-full p-1.5 mr-3 mt-0.5">
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
                      </svg>
                    </div>
                    <div>
                      <h3 class="font-medium text-gray-800">This Week</h3>
                      <p class="text-gray-600 text-sm">Begin "Sustainable Inventory" free module</p>
                      <div class="flex items-center mt-1">
                        <div class="w-full bg-gray-200 rounded-full h-1.5 mr-1">
                          <div class="bg-green-500 h-1.5 rounded-full" style="width: 0%"></div>
                        </div>
                        <span class="text-xs text-gray-500">0%</span>
                      </div>
                    </div>
                  </div>
                  <div class="flex items-start">
                    <div class="bg-blue-100 rounded-full p-1.5 mr-3 mt-0.5">
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                      </svg>
                    </div>
                    <div>
                      <h3 class="font-medium text-gray-800">Next 30 Days</h3>
                      <p class="text-gray-600 text-sm">Complete "Green Retail Operations" certificate</p>
                    </div>
                  </div>
                  <div class="flex items-start">
                    <div class="bg-purple-100 rounded-full p-1.5 mr-3 mt-0.5">
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-purple-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                      </svg>
                    </div>
                    <div>
                      <h3 class="font-medium text-gray-800">Next 90 Days</h3>
                      <p class="text-gray-600 text-sm">Apply for "Eco-Retail Coordinator" positions</p>
                    </div>
                  </div>
                </div>
                <a href="/plan" class="mt-4 block w-full text-green-600 hover:text-green-700 text-center font-medium py-2 px-4 border border-green-600 hover:border-green-700 rounded-md transition-colors">
                  View Full Plan
                </a>
              </div>
              
              <!-- Quick Resources -->
              <div class="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden">
                <div class="px-4 py-3 border-b border-gray-200 bg-gray-50">
                  <h2 class="text-lg font-medium text-gray-700">Quick Resources</h2>
                </div>
                <div class="p-4">
                  <ul class="space-y-2">
                    <li>
                      <!-- svelte-ignore a11y_invalid_attribute -->
                      <a href="#" class="flex items-center text-blue-600 hover:text-blue-800">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
                        </svg>
                        Green Jobs Guide 2025
                      </a>
                    </li>
                    <li>
                      <!-- svelte-ignore a11y_invalid_attribute -->
                      <a href="#" class="flex items-center text-blue-600 hover:text-blue-800">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z" />
                        </svg>
                        Sustainable Career Webinar
                      </a>
                    </li>
                    <li>
                      <!-- svelte-ignore a11y_invalid_attribute -->
                      <a href="#" class="flex items-center text-blue-600 hover:text-blue-800">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
                        </svg>
                        Free Skills Assessment
                      </a>
                    </li>
                    <li>
                      <!-- svelte-ignore a11y_invalid_attribute -->
                      <a href="#" class="flex items-center text-blue-600 hover:text-blue-800">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
                        </svg>
                        Join Green Skills Community
                      </a>
                    </li>
                  </ul>
                </div>
              </div>
      </div>
    </div>

    <!-- Footer -->
    <div class="mt-10 pt-6 border-t border-gray-200">
      <div class="flex flex-col md:flex-row justify-between items-center">
        <p class="text-gray-500 text-sm">© 2025 FutureSkills Coach | Supporting SDG 8: Decent Work and Economic Growth</p>
        <div class="flex space-x-4 mt-4 md:mt-0">
          <button class="text-gray-500 hover:text-gray-700 text-sm">Privacy Policy</button>
          <button class="text-gray-500 hover:text-gray-700 text-sm">Terms of Use</button>
          <button class="text-gray-500 hover:text-gray-700 text-sm">Contact Us</button>
        </div>
      </div>
    </div>
  </main>
</div>
