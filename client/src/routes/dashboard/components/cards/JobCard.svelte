<script lang="ts">
    export let job: {
      title: string;
      growthRate: number;
      skillMatch: string;
      description: string;
      salary: string;
    };
</script>
  
<div class="bg-white rounded-lg shadow-md border border-gray-200 p-5 h-full flex flex-col" aria-label="Job Suggestion: {job.title}">
    <h3 class="text-xl font-semibold text-green-600 mb-2">{job.title}</h3>
    
    <div class="mb-3 flex items-center">
      <span class="inline-block bg-green-100 text-green-800 text-sm px-2 py-1 rounded">
        +{job.growthRate}% Growth by 2030
      </span>
    </div>
    
    <p class="text-gray-700 mb-3">{job.description}</p>
    
    <div class="mb-3">
      <h4 class="text-sm font-medium text-gray-600">Salary Range</h4>
      <p class="text-gray-800">{job.salary}</p>
    </div>
    
    <div class="mt-auto">
      <h4 class="text-sm font-medium text-gray-600">Skill Match</h4>
      <p class="text-gray-800">{job.skillMatch}</p>
      
      <button class="mt-4 w-full text-blue-500 hover:text-blue-700 text-center font-medium py-2 px-4 border border-blue-500 hover:border-blue-700 rounded-md transition-colors">
        See Reskilling Path
      </button>
    </div>
</div>