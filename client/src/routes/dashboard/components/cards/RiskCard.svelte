<script lang="ts">
    export let score: number;
    export let jobTitle: string;
    export let explanation: string;
    
    // Determine risk level and color
    $: riskLevel = score >= 70 ? 'High' : score >= 40 ? 'Moderate' : 'Low';
    $: riskColor = score >= 70 ? 'text-amber-500' : score >= 40 ? 'text-yellow-500' : 'text-blue-500';
    $: barColor = score >= 70 ? 'bg-amber-500' : score >= 40 ? 'bg-yellow-500' : 'bg-blue-500';
</script>
  
<div class="bg-white rounded-lg shadow-md border border-gray-200 p-6" aria-label="Automation Risk Assessment">
    <div class="flex flex-col md:flex-row md:items-center justify-between mb-4">
      <div>
        <h2 class="text-2xl font-bold text-green-600">Automation Risk Assessment</h2>
        <p class="text-gray-600">Current job: <span class="font-medium">{jobTitle}</span></p>
      </div>
      <div class="mt-4 md:mt-0 text-right">
        <p class="text-3xl font-bold {riskColor}">{score}%</p>
        <p class="font-medium {riskColor}">{riskLevel} Risk</p>
      </div>
    </div>
    
    <div class="w-full h-3 bg-gray-200 rounded-full overflow-hidden mb-4" aria-label="Risk visualization bar">
      <div class="{barColor} h-full rounded-full" style="width: {score}%"></div>
    </div>
    
    <div class="text-gray-700">
      <p>{explanation}</p>
      <div class="mt-4 p-3 bg-gray-50 rounded-md border-l-4 border-blue-500">
        <p class="text-sm text-gray-600"><strong>Pro Tip:</strong> Jobs with lower automation risk typically involve creativity, complex problem-solving, and human interaction.</p>
      </div>
    </div>
</div>