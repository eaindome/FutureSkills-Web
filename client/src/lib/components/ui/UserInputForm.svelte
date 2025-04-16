<script lang="ts">
    import { createEventDispatcher } from 'svelte';
    
    const dispatch = createEventDispatcher();
    
    let jobTitle = '';
    let experience = '';
    let interests = '';
    let resumeText = '';
    let uploadedFile: File | null = null;
    let isLoading = false;
    
    const experienceOptions = [
      { value: '', label: 'Select experience' },
      { value: '0-2', label: '0-2 years' },
      { value: '2-5', label: '2-5 years' },
      { value: '5-10', label: '5-10 years' },
      { value: '10+', label: '10+ years' }
    ];
    
    function handleFileChange(event: Event) {
      const target = event.target as HTMLInputElement;
      if (target.files && target.files[0]) {
        uploadedFile = target.files[0];
      }
    }
    
    function handleSubmit() {
      isLoading = true;
      // Simulate API call
      setTimeout(() => {
        dispatch('formSubmit', {
          jobTitle,
          experience,
          interests,
          resumeText,
          uploadedFile
        });
        isLoading = false;
        
        // Navigate to dashboard (in real app we'd use Svelte navigation)
        window.location.href = '/dashboard';
      }, 1500);
    }
</script>
  
  <section id="input-form" class="py-12 bg-gray-50">
    <div class="container mx-auto px-4">
      <div class="max-w-3xl mx-auto">
        <div class="bg-white rounded-xl shadow-lg overflow-hidden">
          <div class="px-6 py-8 md:p-10">
            <h2 class="text-2xl md:text-3xl font-bold text-gray-800 mb-2">Discover Your Future Career Path</h2>
            <p class="text-gray-600 mb-8">Input your job details below to see automation risks, explore green career options, and find side hustles that match your skills.</p>
            
            <form on:submit|preventDefault={handleSubmit} class="space-y-6">
              <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <!-- Job Title -->
                <div class="col-span-1">
                  <label for="jobTitle" class="block text-sm font-medium text-gray-700 mb-1">Current Job Title</label>
                  <input 
                    type="text" 
                    id="jobTitle" 
                    bind:value={jobTitle} 
                    class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-green-500 focus:border-green-500" 
                    placeholder="E.g., Cashier, Office Assistant"
                    required
                  />
                </div>
                
                <!-- Experience Level -->
                <div class="col-span-1">
                  <label for="experience" class="block text-sm font-medium text-gray-700 mb-1">Experience Level</label>
                  <select 
                    id="experience" 
                    bind:value={experience} 
                    class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-green-500 focus:border-green-500 bg-white" 
                    required
                  >
                    {#each experienceOptions as option}
                      <option value={option.value}>{option.label}</option>
                    {/each}
                  </select>
                </div>
              </div>
              
              <!-- Interests -->
              <div>
                <label for="interests" class="block text-sm font-medium text-gray-700 mb-1">Skills & Interests</label>
                <textarea 
                  id="interests" 
                  bind:value={interests} 
                  rows="3" 
                  class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-green-500 focus:border-green-500" 
                  placeholder="E.g., technology, environment, customer service, DIY projects"
                ></textarea>
                <p class="text-xs text-gray-500 mt-1">Separate multiple interests with commas</p>
              </div>
              
              <!-- Resume Text (Optional) -->
              <div>
                <label for="resumeText" class="block text-sm font-medium text-gray-700 mb-1">
                  Resume Content (Optional)
                </label>
                <textarea 
                  id="resumeText" 
                  bind:value={resumeText} 
                  rows="4" 
                  class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-green-500 focus:border-green-500" 
                  placeholder="Paste your resume content here for more personalized recommendations..."
                ></textarea>
              </div>
              
              <!-- File Upload (Optional) -->
              <div>
                <label for="resumeUpload" class="block text-sm font-medium text-gray-700 mb-1">
                  Upload Resume (Optional)
                </label>
                <div class="flex items-center justify-center w-full">
                  <label 
                    for="resumeUpload" 
                    class="flex flex-col items-center justify-center w-full h-32 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 hover:bg-gray-100"
                  >
                    <div class="flex flex-col items-center justify-center pt-5 pb-6">
                      <svg class="w-8 h-8 mb-3 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path>
                      </svg>
                      <p class="mb-2 text-sm text-gray-500">
                        <span class="font-medium">Click to upload</span> or drag and drop
                      </p>
                      <p class="text-xs text-gray-500">PDF, DOCX, or TXT (MAX. 5MB)</p>
                    </div>
                    <input 
                      id="resumeUpload" 
                      type="file" 
                      on:change={handleFileChange} 
                      accept=".pdf,.docx,.txt" 
                      class="hidden" 
                    />
                  </label>
                </div>
                {#if uploadedFile}
                  <p class="text-sm text-green-600 mt-2">File uploaded: {uploadedFile.name}</p>
                {/if}
              </div>
              
              <!-- Submit Button -->
              <div class="pt-4">
                <button 
                  type="submit" 
                  class="w-full bg-green-600 hover:bg-green-700 text-white py-3 px-6 rounded-lg font-medium text-lg transition-colors duration-300 flex items-center justify-center"
                  disabled={isLoading}
                >
                  {#if isLoading}
                    <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                      <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                      <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                    </svg>
                    Analyzing Your Future...
                  {:else}
                    Analyze My Future <span class="ml-2">→</span>
                  {/if}
                </button>
                <p class="text-center text-sm text-gray-500 mt-4">
                  Your data is secure and only used for analysis purposes.
                </p>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
</section>