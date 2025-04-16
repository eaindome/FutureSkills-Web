<script lang="ts">
    export let option: {
      title: string;
      provider: string;
      cost: number;
      duration: string;
      url: string;
      skills: string[];
};
  </script>
  
<div class="bg-white rounded-lg shadow-md border border-gray-200 p-5" aria-label="Reskilling Option: {option.title}">
    <div class="flex justify-between items-start">
      <div>
        <h3 class="text-lg font-semibold text-green-600">{option.title}</h3>
        <p class="text-gray-600">{option.provider}</p>
      </div>
      <div class="text-right">
        <p class="font-medium">${option.cost}</p>
        <p class="text-sm text-gray-600">{option.duration}</p>
      </div>
    </div>
    
    <div class="mt-3">
      <h4 class="text-sm font-medium text-gray-600">Skills You'll Learn:</h4>
      <ul class="mt-1">
        {#each option.skills as skill}
          <li class="text-gray-700 flex items-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-green-500 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
            {skill}
          </li>
        {/each}
      </ul>
    </div>
    
    <a href={option.url} class="mt-4 block bg-blue-500 hover:bg-blue-600 text-white font-medium py-2 px-4 rounded-md text-center transition-colors">
      View Course Details
    </a>
</div>