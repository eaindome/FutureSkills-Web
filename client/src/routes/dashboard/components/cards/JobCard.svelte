<script lang="ts">
  export let job: {
    title: string;
    growthRate: number;
    skillMatch: string;
    description: string;
    salary: string;
    greenImpactScore: number;
  };
  
  // Calculate skill match percentage (assuming it comes as "70%" or similar)
  $: skillMatchNum = parseInt(job.skillMatch) || 0;
  
  function getImpactColor(score: number): string {
    if (score >= 80) return '#10B981'; // Green-600
    if (score >= 60) return '#34D399'; // Green-400
    if (score >= 40) return '#6EE7B7'; // Green-300
    return '#A7F3D0'; // Green-200
  }
</script>

<div class="bg-white rounded-lg shadow-sm border border-gray-100 overflow-hidden h-full flex flex-col transition-all duration-200 hover:shadow-md">
  <!-- Header section -->
  <div class="border-b border-gray-100 p-4">
    <h3 class="text-lg font-semibold text-gray-800">{job.title}</h3>
    <div class="flex items-center mt-2 gap-3">
      <span class="text-green-600 text-sm font-medium">+{job.growthRate}% Growth</span>
      <span class="text-gray-400">•</span>
      <span class="text-green-600 text-sm font-medium">{job.skillMatch} Match</span>
    </div>
  </div>
  
  <div class="p-4 flex-grow flex flex-col gap-4">
    <!-- Green Impact -->
    <div class="flex items-center">
      <span class="text-sm font-medium text-gray-600 mr-2 min-w-[90px]">Green Impact</span>
      <div class="flex-1 h-1.5 bg-gray-100 rounded-full overflow-hidden">
        <div 
          class="h-full rounded-full" 
          style="width: {job.greenImpactScore}%; background-color: {getImpactColor(job.greenImpactScore)}">
        </div>
      </div>
      <span class="ml-2 text-xs font-medium text-gray-500">{job.greenImpactScore}%</span>
    </div>
    
    <!-- Description -->
    <div>
      <p class="text-gray-600 text-sm">{job.description}</p>
    </div>
    
    <!-- Salary -->
    <div class="flex items-center">
      <span class="text-sm font-medium text-gray-600 mr-2 min-w-[90px]">Salary Range</span>
      <span class="text-gray-700">{job.salary}</span>
    </div>
  
    <!-- Action buttons -->
    <div class="mt-auto pt-3 grid grid-cols-2">
      <button class="py-2 px-3 bg-green-600 hover:bg-green-700 text-white rounded-md text-sm font-medium transition-colors">
        View Details
      </button>
    </div>
  </div>
</div>