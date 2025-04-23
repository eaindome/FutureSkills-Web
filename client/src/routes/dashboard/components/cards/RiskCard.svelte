<script lang="ts">
  export let score: number;
  export let jobTitle: string;
  export let explanation: string;
  
  // Determine risk level and color
  $: riskLevel = score >= 70 ? 'High' : score >= 40 ? 'Moderate' : 'Low';
  
  // Get color classes based on risk level
  $: colorClasses = getColorClasses(score);
  
  function getColorClasses(score: number) {
    if (score >= 70) return {
      text: 'text-amber-500',
      bg: 'bg-amber-500',
      lightBg: 'bg-amber-50',
      border: 'border-amber-500'
    };
    if (score >= 40) return {
      text: 'text-yellow-500',
      bg: 'bg-yellow-500',
      lightBg: 'bg-yellow-50',
      border: 'border-yellow-500'
    };
    return {
      text: 'text-sky-500',
      bg: 'bg-sky-500',
      lightBg: 'bg-sky-50',
      border: 'border-sky-500'
    };
  }
</script>

<div class="bg-white rounded-xl shadow-lg border border-gray-100 overflow-hidden" aria-label="Automation Risk Assessment">
  <!-- Header with gradient background -->
  <div class="bg-gradient-to-r from-teal-600 to-green-600 px-6 py-4">
    <h2 class="text-xl font-bold text-white flex items-center gap-2">
      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="12" r="10"></circle>
        <line x1="12" y1="8" x2="12" y2="12"></line>
        <line x1="12" y1="16" x2="12.01" y2="16"></line>
      </svg>
      Automation Risk Assessment
    </h2>
  </div>
  
  <div class="p-6">
    <!-- Job title section -->
    <div class="mb-6 flex flex-col md:flex-row justify-between items-start md:items-center">
      <div class="flex items-center gap-2 mb-4 md:mb-0">
        <div class="p-2 rounded-full bg-teal-50">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-teal-600">
            <path d="M20 7h-3a2 2 0 0 0-2 2v9a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V7"></path>
            <path d="M9 1v4"></path>
            <path d="M15 1v4"></path>
            <path d="M9 11h6"></path>
            <path d="M9 16h6"></path>
          </svg>
        </div>
        <div>
          <p class="text-gray-500 text-sm">Current Job</p>
          <p class="font-medium text-gray-800">{jobTitle}</p>
        </div>
      </div>
      
      <!-- Risk score display -->
      <div class="flex items-center gap-4">
        <div class="p-2 rounded-full {colorClasses.lightBg}">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="{colorClasses.text}">
            <path d="M3 12a9 9 0 1 0 18 0 9 9 0 0 0-18 0"></path>
            <path d="M12 8v4l2 2"></path>
          </svg>
        </div>
        <div class="text-right">
          <div class="flex items-center gap-2">
            <p class="text-3xl font-bold {colorClasses.text}">{score}%</p>
            <div class="px-2 py-1 rounded-full {colorClasses.lightBg} text-sm font-medium {colorClasses.text}">
              {riskLevel} Risk
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Progress bar -->
    <div class="w-full h-3 bg-gray-100 rounded-full overflow-hidden mb-6" aria-label="Risk visualization bar">
      <div class="{colorClasses.bg} h-full rounded-full" style="width: {score}%"></div>
    </div>
    
    <!-- Explanation -->
    <div class="space-y-4">
      <div class="bg-gray-50 p-4 rounded-lg">
        <h3 class="text-sm font-medium text-gray-700 mb-2">Analysis</h3>
        <p class="text-gray-600">{explanation}</p>
      </div>
      
      <div class="p-4 rounded-lg {colorClasses.lightBg} border-l-4 {colorClasses.border}">
        <div class="flex gap-3">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="{colorClasses.text}">
            <circle cx="12" cy="12" r="10"></circle>
            <line x1="12" y1="16" x2="12" y2="12"></line>
            <line x1="12" y1="8" x2="12.01" y2="8"></line>
          </svg>
          <div>
            <h3 class="text-sm font-medium {colorClasses.text} mb-1">Pro Tip</h3>
            <p class="text-sm text-gray-600">Jobs with lower automation risk typically involve creativity, complex problem-solving, and human interaction.</p>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Action button -->
    <div class="mt-6">
      <button class="w-full py-2 px-4 bg-teal-600 hover:bg-teal-700 text-white rounded-lg font-medium transition-colors flex items-center justify-center gap-2">
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
          <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
          <path d="m9 14 2 2 4-4"></path>
        </svg>
        Explore Green Job Alternatives
      </button>
    </div>
  </div>
</div>