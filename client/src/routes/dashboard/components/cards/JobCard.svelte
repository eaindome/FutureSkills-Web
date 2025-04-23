<script lang="ts">
  export let job: {
    title: string;
    growthRate: number;
    skillMatch: string;
    description: string;
    salary: string;
  };
  
  // Calculate skill match percentage (assuming it comes as "70%" or similar)
  $: skillMatchNum = parseInt(job.skillMatch) || 0;
  
  // Get appropriate color for skill match
  $: skillMatchColor = getSkillMatchColor(skillMatchNum);
  
  function getSkillMatchColor(match: number) {
    if (match >= 70) return {
      text: 'text-teal-600',
      bg: 'bg-teal-100',
      border: 'border-teal-200'
    };
    if (match >= 40) return {
      text: 'text-sky-600',
      bg: 'bg-sky-50',
      border: 'border-sky-200'
    };
    return {
      text: 'text-amber-600',
      bg: 'bg-amber-50',
      border: 'border-amber-200'
    };
  }
</script>

<div class="bg-white rounded-xl shadow-lg border border-gray-100 overflow-hidden h-full flex flex-col" aria-label="Job Suggestion: {job.title}">
  <!-- Header section with gradient -->
  <div class="bg-gradient-to-r from-green-600 to-teal-600 p-4">
    <h3 class="text-lg font-semibold text-white flex items-center gap-2">
      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect>
        <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path>
      </svg>
      {job.title}
    </h3>
  </div>
  
  <div class="p-5 flex-grow flex flex-col">
    <!-- Growth and match indicators -->
    <div class="flex flex-wrap gap-2 mb-4">
      <span class="inline-flex items-center gap-1 bg-green-100 text-green-700 text-sm px-3 py-1 rounded-full font-medium">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="m12 19 7-7-7-7"></path>
          <path d="M19 12H5"></path>
        </svg>
        +{job.growthRate}% Growth by 2030
      </span>
      
      <span class="inline-flex items-center gap-1 {skillMatchColor.bg} {skillMatchColor.text} text-sm px-3 py-1 rounded-full font-medium">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
          <path d="m9 11 3 3L22 4"></path>
        </svg>
        {job.skillMatch} Match
      </span>
    </div>
    
    <!-- Description box -->
    <div class="bg-gray-50 p-4 rounded-lg mb-4">
      <h4 class="text-sm font-medium text-gray-700 mb-2 flex items-center gap-1">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10"></circle>
          <line x1="12" y1="8" x2="12" y2="16"></line>
          <line x1="8" y1="12" x2="16" y2="12"></line>
        </svg>
        About This Role
      </h4>
      <p class="text-gray-600">{job.description}</p>
    </div>
    
    <!-- Salary section -->
    <div class="flex items-center space-x-2 mb-4">
      <div class="p-2 rounded-full bg-teal-50">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-teal-600">
          <line x1="12" y1="1" x2="12" y2="23"></line>
          <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>
        </svg>
      </div>
      <div>
        <h4 class="text-sm font-medium text-gray-600">Salary Range</h4>
        <p class="text-gray-800 font-semibold">{job.salary}</p>
      </div>
    </div>
    
    <!-- Skills section -->
    <div class="flex items-center space-x-2 mb-4">
      <div class="p-2 rounded-full bg-sky-50">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-sky-600">
          <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path>
        </svg>
      </div>
      <div>
        <h4 class="text-sm font-medium text-gray-600">Skill Match</h4>
        <p class="text-gray-800 font-semibold flex items-center">
          <span class="{skillMatchColor.text}">{job.skillMatch}</span>
          <span class="mx-2 text-gray-400">•</span>
          <span class="text-sm text-gray-500">Based on your profile</span>
        </p>
      </div>
    </div>
  
    <!-- Action buttons -->
    <div class="mt-auto pt-4 space-y-3">
      <button class="w-full py-2 px-4 bg-teal-600 hover:bg-teal-700 text-white rounded-lg font-medium transition-colors flex items-center justify-center gap-2">
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path>
          <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path>
        </svg>
        See Reskilling Path
      </button>
      
      <button class="w-full py-2 px-4 border border-teal-600 text-teal-600 hover:bg-teal-50 rounded-lg font-medium transition-colors flex items-center justify-center gap-2">
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path>
        </svg>
        Save Job
      </button>
    </div>
  </div>
</div>