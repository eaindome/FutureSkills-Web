<script lang="ts">
    export let completedSteps: string[];
    export let nextSteps: string[];
    
    const stepLabels = {
      profile: "Create Profile",
      assessment: "Job Risk Assessment",
      reskilling: "Start Reskilling Path",
      mentoring: "Talk to AI Mentor",
      networking: "Connect with Green Network"
    };
    
    type StepKey = keyof typeof stepLabels;
</script>
  
<div class="bg-white rounded-lg shadow-md p-6 border border-gray-200">
    <h2 class="text-xl font-semibold text-green-600 mb-4">Your Progress</h2>
    
    <div class="space-y-4">
      {#each [...completedSteps, ...nextSteps] as step, i}
        {@const isCompleted = completedSteps.includes(step)}
        <div class="flex items-center">
          <div class="relative">
            <div class="{isCompleted ? 'bg-green-600' : 'bg-gray-300'} rounded-full h-8 w-8 flex items-center justify-center">
              {#if isCompleted}
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
              {:else}
                <span class="text-white font-medium">{i + 1}</span>
              {/if}
            </div>
            {#if i < completedSteps.length + nextSteps.length - 1}
              <div class="absolute top-8 left-4 w-0.5 h-8 {i < completedSteps.length ? 'bg-green-600' : 'bg-gray-300'}"></div>
            {/if}
          </div>
          <div class="ml-4">
            <p class="{isCompleted ? 'text-green-600 font-medium' : 'text-gray-600'}">{stepLabels[step as StepKey]}</p>
            {#if isCompleted}
              <span class="text-xs text-gray-500">Completed</span>
            {:else if i === completedSteps.length}
              <span class="text-xs font-medium text-blue-500">Next Step</span>
            {:else}
              <span class="text-xs text-gray-500">Final Step</span>
            {/if}
          </div>
        </div>
      {/each}
    </div>
    
    <div class="mt-6 pt-4 border-t border-gray-200">
      <div class="flex items-center justify-between">
        <div>
          <span class="text-sm text-gray-600">Progress</span>
          <p class="font-medium">{Math.round((completedSteps.length / (completedSteps.length + nextSteps.length)) * 100)}% Complete</p>
        </div>
        <div class="w-20 h-2 bg-gray-200 rounded-full overflow-hidden">
          <div class="bg-green-600 h-full rounded-full" style="width: {(completedSteps.length / (completedSteps.length + nextSteps.length)) * 100}%"></div>
        </div>
      </div>
    </div>
</div>