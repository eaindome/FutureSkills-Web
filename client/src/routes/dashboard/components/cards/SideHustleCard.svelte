<script lang="ts">
    import Button from '$lib/components/ui/Button.svelte';
    export let hustle: {
      title: string;
      potentialIncome: number;
      startupCost: number;
      timeCommitment: string;
      skillsUsed: string;
      greenImpactScore: number;
    };


    function getGreenColor(score: number): string {
      if (score >= 80) return '#10B981'; // Green-600
      if (score >= 60) return '#34D399'; // Green-400
      if (score >= 40) return '#FBBF24'; // Amber-400
      if (score >= 20) return '#F59E0B'; // Amber-500
      return '#EF4444'; // Red-500
    }

    let loading: boolean = false;
</script>
  
<div class="bg-white rounded-lg shadow-md border border-gray-200 p-5" aria-label="Side Hustle: {hustle.title}">
    <h3 class="text-lg font-semibold text-green-600 mb-2">{hustle.title}</h3>
    
    <div class="flex items-center mb-3">
      <span class="text-2xl font-bold text-green-600">${hustle.potentialIncome}</span>
      <span class="text-gray-600 ml-1">/month</span>
    </div>
    
    <div class="space-y-2 mb-4">
      <div class="flex items-start">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-500 mr-2 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <div>
          <p class="text-sm text-gray-700">Startup Cost: <span class="font-medium">${hustle.startupCost}</span></p>
        </div>
      </div>
      
      <div class="flex items-start">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-500 mr-2 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <div>
          <p class="text-sm text-gray-700">Time Commitment: <span class="font-medium">{hustle.timeCommitment}</span></p>
        </div>
      </div>
      
      <div class="flex items-start">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-500 mr-2 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
        </svg>
        <div>
          <p class="text-sm text-gray-700">Skills Used: <span class="font-medium">{hustle.skillsUsed}</span></p>
        </div>
      </div>

      <div class="flex items-center mb-4">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-500 mr-2 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z" />
        </svg>
        <div class="flex-1">
          <div class="flex items-center">
            <span class="text-sm text-gray-700 mr-2">Green Impact:</span>
            <div class="flex-1 h-2 bg-gray-200 rounded-full overflow-hidden">
              <div 
                class="h-full rounded-full" 
                style="width: {hustle.greenImpactScore}%; background-color: {getGreenColor(hustle.greenImpactScore)}">
              </div>
            </div>
            <span class="ml-2 text-sm font-semibold" style="color: {getGreenColor(hustle.greenImpactScore)}">
              {hustle.greenImpactScore}
            </span>
          </div>
        </div>
      </div>
    </div>

    <Button type="submit" variant="secondary" fullWidth={true} loading={loading}>
      Learn More
    </Button>
</div>