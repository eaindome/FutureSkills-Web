<script lang="ts">
  import RiskCard from './components/cards/RiskCard.svelte';
  import JobCard from './components/cards/JobCard.svelte';
  import ProgressTracker from './components/ui/ProgressTracker.svelte';
  import DashboardHeader from './components/layout/DashboardHeader.svelte';
  import JobTrendsChart from './components/charts/JobTrendsChart.svelte';
  import JobComparisonChart from './components/charts/JobComparisonChart.svelte';
  
  // Tab state management
  let activeTab = 'trends';
  
  // Mock data - in a real app this would come from API or store
  const userData = {
    name: "Alex Johnson",
    currentJob: "Retail Cashier",
    riskScore: 75,
    riskExplanation: "Cashier jobs face high automation risk due to increasing self-checkout technology and AI-powered retail solutions.",
    completedSteps: ["profile", "assessment"],
    nextSteps: ["reskilling", "mentoring"]
  };
  
  const greenJobs = [
    {
      title: "Solar Sales Support Specialist",
      growthRate: 15,
      skillMatch: "Uses your customer service and sales skills",
      description: "Assist customers with solar panel purchases and installation plans",
      salary: "$45,000 - $60,000"
    },
    {
      title: "Eco-Retail Coordinator",
      growthRate: 12,
      skillMatch: "Uses your inventory and management experience",
      description: "Manage sustainable product lines and green initiatives in retail stores",
      salary: "$42,000 - $55,000"
    }
  ];
  
  // Job trends data
  const jobTrendsData = {
    currentJob: {
      name: "Retail Cashier",
      data: [
        { year: 2020, jobs: 100 },
        { year: 2021, jobs: 95 },
        { year: 2022, jobs: 90 },
        { year: 2023, jobs: 85 },
        { year: 2024, jobs: 80 },
        { year: 2025, jobs: 70 },
        { year: 2026, jobs: 60 },
        { year: 2027, jobs: 50 },
        { year: 2028, jobs: 45 },
        { year: 2029, jobs: 40 },
        { year: 2030, jobs: 35 }
      ]
    },
    recommendedJob: {
      name: "Solar Sales Support",
      data: [
        { year: 2020, jobs: 40 },
        { year: 2021, jobs: 50 },
        { year: 2022, jobs: 55 },
        { year: 2023, jobs: 60 },
        { year: 2024, jobs: 65 },
        { year: 2025, jobs: 70 },
        { year: 2026, jobs: 75 },
        { year: 2027, jobs: 80 },
        { year: 2028, jobs: 85 },
        { year: 2029, jobs: 95 },
        { year: 2030, jobs: 105 }
      ]
    }
  };
  
  // Job comparison data
  const jobComparisonData = [
    { name: "Retail Cashier", sustainability: 25, futureProof: 15, salary: 30 },
    { name: "Solar Sales Support", sustainability: 85, futureProof: 80, salary: 60 },
    { name: "Eco-Retail Coordinator", sustainability: 75, futureProof: 70, salary: 55 },
    { name: "Traditional Retail Manager", sustainability: 35, futureProof: 40, salary: 65 }
  ];
  
  // Dashboard summary cards
  const summaryCards = [
    {
      title: "Your Risk Level",
      value: `${userData.riskScore}%`,
      description: "Automation Risk",
      trend: "increasing",
      icon: "alert-triangle"
    },
    {
      title: "Green Jobs Match",
      value: "73%",
      description: "Skill Compatibility",
      trend: "neutral",
      icon: "briefcase"
    },
    {
      title: "Earning Potential",
      value: "$55K",
      description: "After Transition",
      trend: "increasing",
      icon: "trending-up"
    },
    {
      title: "Training Time",
      value: "12 wks",
      description: "Avg. Reskilling Time",
      trend: "decreasing",
      icon: "clock"
    }
  ];

  // Function to get the Udemy search URL for the recommended job
  function getUdemySearchUrl(jobTitle: string) {
    const searchQuery = encodeURIComponent(jobTitle.toLowerCase());
    return `https://www.udemy.com/courses/search/?q=${searchQuery}`;
  }
  
  // Button interaction
  let isRefreshing = false;
  const refreshData = () => {
    isRefreshing = true;
    // Simulate API call
    setTimeout(() => {
      isRefreshing = false;
    }, 1500);
  };
  
  // Hover states for buttons
  let hoveredJobCard: number | null = null;
</script>

<div class="min-h-screen bg-gray-50">
  <DashboardHeader userName={userData.name} />
  
  <main class="container mx-auto px-4 py-6 max-w-7xl">
    <!-- Dashboard Header -->
    <div class="flex flex-col md:flex-row md:items-center justify-between mb-8">
      <div>
        <h1 class="text-3xl font-bold text-green-600 mb-2">Your Future Skills Dashboard</h1>
        <p class="text-gray-500">Welcome back, {userData.name}. Let's continue your journey to a sustainable career.</p>
      </div>
      <div class="flex items-center mt-4 md:mt-0">
        <span class="text-gray-500 mr-3">Last updated: Apr 18, 2025</span>
        <button 
          class="flex items-center {isRefreshing ? 'bg-green-200 cursor-wait' : 'bg-green-100 hover:bg-green-200'} text-green-600 px-4 py-2 rounded-md transition-all duration-200 ease-in-out transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-green-300 focus:ring-opacity-50"
          on:click={refreshData}
          disabled={isRefreshing}
        >
          <svg xmlns="http://www.w3.org/2000/svg" 
            class="h-5 w-5 mr-2 {isRefreshing ? 'animate-spin' : ''}" 
            viewBox="0 0 20 20" 
            fill="currentColor"
          >
            <path fill-rule="evenodd" d="M4 2a1 1 0 011 1v2.101a7.002 7.002 0 0111.601 2.566 1 1 0 11-1.885.666A5.002 5.002 0 005.999 7H9a1 1 0 010 2H4a1 1 0 01-1-1V3a1 1 0 011-1zm.008 9.057a1 1 0 011.276.61A5.002 5.002 0 0014.001 13H11a1 1 0 110-2h5a1 1 0 011 1v5a1 1 0 11-2 0v-2.101a7.002 7.002 0 01-11.601-2.566 1 1 0 01.61-1.276z" clip-rule="evenodd" />
          </svg>
          {isRefreshing ? 'Refreshing...' : 'Refresh Data'}
        </button>
      </div>
    </div>
    
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <!-- Left column - Main content -->
      <div class="lg:col-span-2 space-y-6">
        <!-- Risk Assessment Card -->
        <RiskCard 
          score={userData.riskScore} 
          jobTitle={userData.currentJob} 
          explanation={userData.riskExplanation} 
        />
        
        <!-- Data Visualization Section -->
        <div class="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden transition-all duration-200 hover:shadow-md">
          <div class="px-6 py-4 border-b border-gray-200 bg-gray-50">
            <h2 class="text-xl font-semibold text-gray-700">Career Insights</h2>
          </div>
          <div class="flex border-b border-gray-200">
            <button 
              class="py-3 px-6 transition-all duration-200 {activeTab === 'trends' ? 'text-green-600 border-b-2 border-green-600 font-medium bg-green-50' : 'text-gray-500 hover:text-green-600 hover:bg-green-50'}"
              on:click={() => activeTab = 'trends'}
            >
              Job Trends
            </button>
            <button 
              class="py-3 px-6 transition-all duration-200 {activeTab === 'comparison' ? 'text-green-600 border-b-2 border-green-600 font-medium bg-green-50' : 'text-gray-500 hover:text-green-600 hover:bg-green-50'}"
              on:click={() => activeTab = 'comparison'}
            >
              Job Comparison
            </button>
          </div>
          
          <!-- Chart content with fixed height -->
          <div class="p-6">
            {#if activeTab === 'trends'}
              <div class="h-120">
                <p class="text-gray-600 mb-4">See how your current job outlook compares to recommended green jobs over the next decade.</p>
                <JobTrendsChart data={jobTrendsData} />
              </div>
            {:else if activeTab === 'comparison'}
              <div class="h-80">
                <p class="text-gray-600 mb-4">Compare sustainability, future-proofing, and salary potential across various career options.</p>
                <JobComparisonChart data={jobComparisonData} />
              </div>
            {/if}
          </div>
        </div>
        
        <!-- Recommendations Section -->
        <div class="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden transition-all duration-200 hover:shadow-md">
          <div class="px-6 py-4 border-b border-gray-200 bg-gray-50">
            <h2 class="text-xl font-semibold text-gray-700">Recommended Green Jobs</h2>
          </div>
          <div class="p-6">
            <p class="text-gray-600 mb-4">Based on your skills and interests, these sustainable careers have the highest match potential.</p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              {#each greenJobs as job, i}
                <div 
                  class="border border-gray-200 rounded-lg p-4 hover:border-green-400 transition-all duration-200 hover:shadow-md {hoveredJobCard === i ? 'bg-green-50 border-green-400' : ''}"
                  role="button"
                  tabindex="0"
                  on:mouseenter={() => hoveredJobCard = i}
                  on:mouseleave={() => hoveredJobCard = null}
                >
                  <div class="flex justify-between items-start mb-2">
                    <h3 class="text-lg font-semibold text-gray-800">{job.title}</h3>
                    <span class="bg-green-100 text-green-700 px-2 py-1 rounded-full text-xs font-medium">+{job.growthRate}% Growth</span>
                  </div>
                  <p class="text-sm text-green-600 mb-2">{job.skillMatch}</p>
                  <p class="text-gray-600 text-sm mb-2">{job.description}</p>
                  <p class="text-gray-700 font-medium">{job.salary}</p>
                  <button class="mt-3 w-full bg-green-600 hover:bg-green-700 text-white font-medium py-2 px-4 rounded transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-green-300 focus:ring-opacity-50">
                    View Job Details
                  </button>
                </div>
              {/each}
            </div>
            <div class="mt-6 flex justify-center">
              <button class="group text-green-600 hover:text-green-700 font-medium flex items-center transition-all duration-200 hover:scale-105">
                Explore more green jobs
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-1 group-hover:translate-x-1 transition-transform" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H5a1 1 0 110-2h7.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                </svg>
              </button>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Right column - Sidebar -->
      <div class="space-y-6">
        <!-- AI Mentor Card - Moved to top of sidebar -->
        <div class="bg-white rounded-lg shadow-sm border border-green-200 p-6 transition-all duration-200 hover:shadow-md hover:border-green-300 hover:bg-green-50">
          <div class="flex items-center mb-4">
            <div class="bg-green-100 rounded-full p-2 mr-3">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
              </svg>
            </div>
            <h2 class="text-xl font-semibold text-green-600">AI Career Mentor</h2>
          </div>
          <p class="text-gray-600 mb-4">Have questions about your career transition or need personalized advice?</p>
          <a href="/chat" class="block w-full bg-green-600 hover:bg-green-700 text-white font-medium py-3 px-4 rounded-md text-center transition-all duration-200 transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-green-300 focus:ring-opacity-50">
            Talk to Your AI Mentor
          </a>
        </div>
        
        <!-- Progress Tracker -->
        <ProgressTracker 
          completedSteps={userData.completedSteps}
          nextSteps={userData.nextSteps}
        />
        
        <!-- Quick Resources -->
        <div class="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden transition-all duration-200 hover:shadow-md">
          <div class="px-4 py-3 border-b border-gray-200 bg-gray-50">
            <h2 class="text-lg font-medium text-gray-700">Quick Resources</h2>
          </div>
          <div class="p-4">
            <ul class="space-y-3">
              <li>
                <a href="/resources/green-jobs-guide" class="flex items-center text-blue-600 hover:text-blue-800 group p-2 rounded-md hover:bg-blue-50 transition-all duration-200">
                  <div class="bg-blue-100 rounded-full p-1 mr-2 group-hover:bg-blue-200 transition-colors">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-blue-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
                    </svg>
                  </div>
                  <span class="group-hover:translate-x-1 transition-transform">Green Jobs Guide 2025</span>
                </a>
              </li>
              <li>
                <a href="/input" class="flex items-center text-blue-600 hover:text-blue-800 group p-2 rounded-md hover:bg-blue-50 transition-all duration-200">
                  <div class="bg-blue-100 rounded-full p-1 mr-2 group-hover:bg-blue-200 transition-colors">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-blue-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
                    </svg>
                  </div>
                  <span class="group-hover:translate-x-1 transition-transform">Free Skills Assessment</span>
                </a>
              </li>
              <li>
                <a href={getUdemySearchUrl(greenJobs[0].title)} target="_blank" rel="noopener noreferrer" class="flex items-center text-blue-600 hover:text-blue-800 group p-2 rounded-md hover:bg-blue-50 transition-all duration-200">
                  <div class="bg-blue-100 rounded-full p-1 mr-2 group-hover:bg-blue-200 transition-colors">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-blue-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
                    </svg>
                  </div>
                  <span class="group-hover:translate-x-1 transition-transform">Training Courses</span>
                </a>
              </li>
            </ul>
          </div>
        </div>
        
        <!-- Newsletter Signup -->
        <div class="bg-teal-50 rounded-lg shadow-sm border border-teal-200 p-5 transition-all duration-200 hover:shadow-md">
          <h3 class="font-medium text-teal-700 mb-2">Stay Updated</h3>
          <p class="text-sm text-teal-600 mb-3">Get the latest green job opportunities and skills trends in your inbox.</p>
          <div class="flex">
            <input type="email" placeholder="Your email" class="flex-grow px-3 py-2 rounded-l-md border border-gray-300 focus:outline-none focus:ring-1 focus:ring-teal-500">
            <button class="bg-teal-600 hover:bg-teal-700 text-white px-3 py-2 rounded-r-md transition-colors focus:outline-none focus:ring-2 focus:ring-teal-300 focus:ring-opacity-50">
              Subscribe
            </button>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Navigation to Skills Page -->
    <div class="mt-8 text-center">
      <a href="/skills" class="inline-flex items-center px-6 py-3 bg-teal-600 hover:bg-teal-700 text-white font-medium rounded-lg transition-all duration-300 transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-teal-300 focus:ring-opacity-50 shadow-md hover:shadow-lg">
        View Your Skills & Development Plan
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2 group-hover:translate-x-1 transition-transform" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H5a1 1 0 110-2h7.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
        </svg>
      </a>
    </div>
    
    <!-- Footer -->
    <div class="mt-10 pt-6 border-t border-gray-200">
      <div class="flex flex-col md:flex-row justify-between items-center">
        <p class="text-gray-500 text-sm">© 2025 FutureSkills Coach | Supporting SDG 8: Decent Work and Economic Growth</p>
        <div class="flex space-x-6 mt-4 md:mt-0">
          <button class="text-gray-500 hover:text-gray-700 text-sm hover:underline transition-colors">Privacy Policy</button>
          <button class="text-gray-500 hover:text-gray-700 text-sm hover:underline transition-colors">Terms of Use</button>
          <button class="text-gray-500 hover:text-gray-700 text-sm hover:underline transition-colors">Contact Us</button>
        </div>
      </div>
    </div>
  </main>
</div>