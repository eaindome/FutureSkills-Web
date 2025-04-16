<script lang="ts">
    import RiskCard from './components/cards/RiskCard.svelte'
    import JobCard from './components/cards/JobCard.svelte';
    import ReskillingCard from './components/cards/ReskillingCard.svelte';
    import SideHustleCard from './components/cards/SideHustleCard.svelte';
    import ProgressTracker from './components/ui/ProgressTracker.svelte';
    import DashboardHeader from './components/layout/DashboardHeader.svelte';
  
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
      }
    ];
  </script>
  
  <div class="min-h-screen bg-gray-50">
    <DashboardHeader userName={userData.name} />
    
    <main class="container mx-auto px-4 py-6">
      <h1 class="text-3xl font-bold text-green-600 mb-6">Your Future Skills Dashboard</h1>
      
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <!-- Left column -->
        <div class="lg:col-span-2">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <!-- Risk Assessment -->
            <div class="md:col-span-2">
              <RiskCard 
                score={userData.riskScore} 
                jobTitle={userData.currentJob} 
                explanation={userData.riskExplanation} 
              />
            </div>
            
            <!-- Green Jobs -->
            <div class="md:col-span-2">
              <h2 class="text-2xl font-semibold text-green-600 mb-3">Recommended Green Jobs</h2>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                {#each greenJobs as job}
                  <JobCard {job} />
                {/each}
              </div>
            </div>
            
            <!-- Reskilling Plan -->
            <div>
              <h2 class="text-2xl font-semibold text-green-600 mb-3">Your Reskilling Path</h2>
              <div class="space-y-4">
                {#each reskillingOptions as option}
                  <ReskillingCard {option} />
                {/each}
              </div>
            </div>
            
            <!-- Side Hustles -->
            <div>
              <h2 class="text-2xl font-semibold text-green-600 mb-3">Side Hustle Ideas</h2>
              <div class="space-y-4">
                {#each sideHustles as hustle}
                  <SideHustleCard {hustle} />
                {/each}
              </div>
            </div>
          </div>
        </div>
        
        <!-- Right column -->
        <div class="space-y-6">
          <ProgressTracker 
            completedSteps={userData.completedSteps}
            nextSteps={userData.nextSteps}
          />
          
          <div class="bg-white rounded-lg shadow-md p-6 border border-gray-200">
            <h2 class="text-xl font-semibold text-green-600 mb-3">Need Guidance?</h2>
            <p class="text-gray-600 mb-4">Have questions about your career transition or need personalized advice?</p>
            <a href="/chat" class="block w-full bg-green-600 hover:bg-green-700 text-white font-medium py-2 px-4 rounded-md text-center transition-colors">
              Talk to AI Mentor
            </a>
          </div>
        </div>
      </div>
    </main>
</div>