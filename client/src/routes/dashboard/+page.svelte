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
        <button class="flex items-center bg-green-100 hover:bg-green-200 text-green-600 px-4 py-2 rounded-md transition-colors">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M4 2a1 1 0 011 1v2.101a7.002 7.002 0 0111.601 2.566 1 1 0 11-1.885.666A5.002 5.002 0 005.999 7H9a1 1 0 010 2H4a1 1 0 01-1-1V3a1 1 0 011-1zm.008 9.057a1 1 0 011.276.61A5.002 5.002 0 0014.001 13H11a1 1 0 110-2h5a1 1 0 011 1v5a1 1 0 11-2 0v-2.101a7.002 7.002 0 01-11.601-2.566 1 1 0 01.61-1.276z" clip-rule="evenodd" />
          </svg>
          Refresh Data
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
        <div class="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden">
          <div class="px-6 py-4 border-b border-gray-200 bg-gray-50">
            <h2 class="text-xl font-semibold text-gray-700">Career Insights</h2>
          </div>
          <div class="flex border-b border-gray-200">
            <button 
              class="py-3 px-6 {activeTab === 'trends' ? 'text-green-600 border-b-2 border-green-600 font-medium' : 'text-gray-500 hover:text-green-600'}"
              on:click={() => activeTab = 'trends'}
            >
              Job Trends
            </button>
            <button 
              class="py-3 px-6 {activeTab === 'comparison' ? 'text-green-600 border-b-2 border-green-600 font-medium' : 'text-gray-500 hover:text-green-600'}"
              on:click={() => activeTab = 'comparison'}
            >
              Job Comparison
            </button>
          </div>
          
          <!-- Chart content with fixed height -->
          <div class="p-6">
            {#if activeTab === 'trends'}
              <div class="h-80">
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
        <div class="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden">
          <div class="px-6 py-4 border-b border-gray-200 bg-gray-50">
            <h2 class="text-xl font-semibold text-gray-700">Recommended Green Jobs</h2>
          </div>
          <div class="p-6">
            <p class="text-gray-600 mb-4">Based on your skills and interests, these sustainable careers have the highest match potential.</p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              {#each greenJobs as job}
                <JobCard {job} />
              {/each}
            </div>
            <div class="mt-4 flex justify-center">
              <button class="text-green-600 hover:text-green-700 font-medium flex items-center">
                Explore more green jobs
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-1" viewBox="0 0 20 20" fill="currentColor">
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
        
        <!-- Progress Tracker -->
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
                <a href="#" class="flex items-center text-blue-600 hover:text-blue-800">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
                  </svg>
                  Green Jobs Guide 2025
                </a>
              </li>
              <li>
                <a href="#" class="flex items-center text-blue-600 hover:text-blue-800">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z" />
                  </svg>
                  Sustainable Career Webinar
                </a>
              </li>
              <li>
                <a href="#" class="flex items-center text-blue-600 hover:text-blue-800">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
                  </svg>
                  Free Skills Assessment
                </a>
              </li>
              <li>
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
    
    <!-- Navigation to Skills Page -->
    <div class="mt-8 text-center">
      <a href="/skills" class="inline-flex items-center px-6 py-3 bg-teal-600 hover:bg-teal-700 text-white font-medium rounded-lg transition-colors">
        View Your Skills & Development Plan
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H5a1 1 0 110-2h7.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
        </svg>
      </a>
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