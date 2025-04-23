<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  import { fade, fly } from 'svelte/transition';
  
  const dispatch = createEventDispatcher();
  
  let jobTitle = '';
  let experience = '';
  let interests = '';
  let resumeText = '';
  let uploadedFile: File | null = null;
  let isLoading = false;
  let activeTab = 'basic'; // 'basic' or 'advanced'
  
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
    if (!jobTitle || !experience) {
      return;
    }
    
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
    }, 1500);
  }
  
  function setTab(tab: string) {
    activeTab = tab;
  }
  
  function removeFile() {
    uploadedFile = null;
    const input = document.getElementById('resumeUpload') as HTMLInputElement;
    if (input) input.value = '';
  }
</script>

<section class="py-12 bg-gradient-to-br from-green-50 to-blue-50">
<div class="container mx-auto px-4">
  <div class="max-w-3xl mx-auto">
    <div class="bg-white rounded-2xl shadow-xl overflow-hidden border border-green-100">
      <!-- Header with decorative element -->
      <div class="relative bg-gradient-to-r from-green-600 to-teal-600 py-8 px-6 md:px-10">
        <div class="absolute top-0 right-0 w-32 h-32 opacity-10">
          <svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
            <path fill="#FFFFFF" d="M42.7,-62.9C53.9,-52.8,60.9,-38.5,65.9,-23.7C70.9,-8.9,73.9,6.4,70.8,20.9C67.8,35.4,58.7,49.1,46.1,58.7C33.4,68.3,16.7,73.8,0.2,73.5C-16.3,73.3,-32.6,67.3,-45.9,57.1C-59.1,46.9,-69.4,32.4,-74.6,15.5C-79.9,-1.4,-80.1,-20.7,-72.3,-35.9C-64.5,-51.1,-48.6,-62.2,-33,-68.4C-17.3,-74.7,-1.9,-76,-1.1,-74.3C-0.2,-72.5,-13.6,-67.7,1,-69.6C15.5,-71.4,31.5,-73,42.7,-62.9Z" transform="translate(100 100)" />
          </svg>
        </div>
        <h2 class="text-2xl md:text-3xl font-bold text-white mb-2 relative z-10">Discover Your Future Career Path</h2>
        <p class="text-green-50 md:text-lg relative z-10">Find sustainable career opportunities that match your skills and interests.</p>
      </div>
      
      <!-- Form tabs -->
      <div class="flex border-b border-gray-200">
        <button 
          class={`w-1/2 py-4 text-center text-sm md:text-base font-medium transition-colors duration-200 ${activeTab === 'basic' ? 'text-green-600 border-b-2 border-green-600' : 'text-gray-500 hover:text-green-500'}`} 
          on:click={() => setTab('basic')}
        >
          Basic Info
        </button>
        <button 
          class={`w-1/2 py-4 text-center text-sm md:text-base font-medium transition-colors duration-200 ${activeTab === 'advanced' ? 'text-green-600 border-b-2 border-green-600' : 'text-gray-500 hover:text-green-500'}`} 
          on:click={() => setTab('advanced')}
        >
          Resume & Details
        </button>
      </div>

      <div class="px-6 py-8 md:p-10">
        <form on:submit|preventDefault={handleSubmit} class="space-y-6">
          <!-- Basic Info Tab -->
          {#if activeTab === 'basic'}
            <div in:fade={{ duration: 300 }}>
              <div class="mb-8">
                <div class="flex items-center mb-4">
                  <div class="w-8 h-8 rounded-full bg-green-100 flex items-center justify-center text-green-600 mr-3">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd" />
                    </svg>
                  </div>
                  <h3 class="text-lg font-medium text-gray-800">Your Current Role</h3>
                </div>
                <p class="text-gray-600 mb-6">Tell us about your current position to help us analyze automation risks.</p>
              </div>

              <!-- Job Title -->
              <div class="mb-6">
                <label for="jobTitle" class="block text-sm font-medium text-gray-700 mb-1">Current Job Title <span class="text-green-600">*</span></label>
                <div class="relative">
                  <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M6 6V5a3 3 0 013-3h2a3 3 0 013 3v1h2a2 2 0 012 2v3.57A22.952 22.952 0 0110 13a22.95 22.95 0 01-8-1.43V8a2 2 0 012-2h2zm2-1a1 1 0 011-1h2a1 1 0 011 1v1H8V5zm1 5a1 1 0 011-1h.01a1 1 0 110 2H10a1 1 0 01-1-1z" clip-rule="evenodd" />
                    </svg>
                  </div>
                  <input 
                    type="text" 
                    id="jobTitle" 
                    bind:value={jobTitle} 
                    class="w-full pl-10 pr-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-green-500 focus:border-green-500 transition-colors" 
                    placeholder="E.g., Cashier, Office Assistant"
                    required
                  />
                </div>
              </div>
              
              <!-- Experience Level -->
              <div class="mb-6">
                <label for="experience" class="block text-sm font-medium text-gray-700 mb-1">Experience Level <span class="text-green-600">*</span></label>
                <div class="relative">
                  <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clip-rule="evenodd" />
                    </svg>
                  </div>
                  <select 
                    id="experience" 
                    bind:value={experience} 
                    class="w-full pl-10 pr-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-green-500 focus:border-green-500 bg-white appearance-none transition-colors" 
                    required
                  >
                    {#each experienceOptions as option}
                      <option value={option.value}>{option.label}</option>
                    {/each}
                  </select>
                  <div class="absolute inset-y-0 right-0 flex items-center px-2 pointer-events-none">
                  </div>
                </div>
              </div>
              
              <!-- Interests -->
              <div>
                <label for="interests" class="block text-sm font-medium text-gray-700 mb-1">Skills & Interests</label>
                <div class="relative">
                  <div class="absolute top-3 left-3 flex items-start pointer-events-none">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M7 4a3 3 0 016 0v4a3 3 0 11-6 0V4zm4 10.93A7.001 7.001 0 0017 8a1 1 0 10-2 0A5 5 0 015 8a1 1 0 00-2 0 7.001 7.001 0 006 6.93V17H6a1 1 0 100 2h8a1 1 0 100-2h-3v-2.07z" clip-rule="evenodd" />
                    </svg>
                  </div>
                  <textarea 
                    id="interests" 
                    bind:value={interests} 
                    rows="3" 
                    class="w-full pl-10 pr-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-green-500 focus:border-green-500 transition-colors" 
                    placeholder="E.g., technology, environment, customer service, DIY projects"
                  ></textarea>
                </div>
                <p class="text-xs text-gray-500 mt-1">Separate multiple interests with commas</p>
              </div>
              
              <!-- Next Button -->
              <div class="pt-6 flex justify-end">
                <button 
                  type="button" 
                  class="flex items-center bg-green-600 hover:bg-green-700 text-white py-2 px-6 rounded-lg font-medium transition-colors duration-300"
                  on:click={() => setTab('advanced')}
                >
                  Next
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H5a1 1 0 110-2h7.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                  </svg>
                </button>
              </div>
            </div>
          {:else}
            <!-- Advanced Tab -->
            <div in:fade={{ duration: 300 }}>
              <div class="mb-8">
                <div class="flex items-center mb-4">
                  <div class="w-8 h-8 rounded-full bg-green-100 flex items-center justify-center text-green-600 mr-3">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4zm2 6a1 1 0 011-1h6a1 1 0 110 2H7a1 1 0 01-1-1zm1 3a1 1 0 100 2h6a1 1 0 100-2H7z" clip-rule="evenodd" />
                    </svg>
                  </div>
                  <h3 class="text-lg font-medium text-gray-800">Resume & Additional Details</h3>
                </div>
                <p class="text-gray-600 mb-6">For more personalized recommendations, add your resume or additional details (optional).</p>
              </div>
              
              <!-- Resume Text (Optional) -->
              <div class="mb-6">
                <label for="resumeText" class="block text-sm font-medium text-gray-700 mb-1">
                  Resume Content (Optional)
                </label>
                <textarea 
                  id="resumeText" 
                  bind:value={resumeText} 
                  rows="4" 
                  class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-green-500 focus:border-green-500 transition-colors" 
                  placeholder="Paste your resume content here for more personalized recommendations..."
                ></textarea>
              </div>
              
              <!-- File Upload (Optional) -->
              <div class="mb-6">
                <label for="resumeUpload" class="block text-sm font-medium text-gray-700 mb-1">
                  Upload Resume (Optional)
                </label>
                <div class="flex items-center justify-center w-full">
                  {#if !uploadedFile}
                    <label 
                      for="resumeUpload" 
                      class="flex flex-col items-center justify-center w-full h-32 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 hover:bg-gray-100 transition-colors"
                    >
                      <div class="flex flex-col items-center justify-center pt-5 pb-6">
                        <svg class="w-10 h-10 mb-3 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
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
                  {:else}
                    <div class="w-full p-4 bg-green-50 border border-green-200 rounded-lg">
                      <div class="flex items-center justify-between">
                        <div class="flex items-center">
                          <div class="w-10 h-10 rounded-full bg-green-100 flex items-center justify-center text-green-600 mr-3">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
                              <path fill-rule="evenodd" d="M3 17a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm3.293-7.707a1 1 0 011.414 0L9 10.586V3a1 1 0 112 0v7.586l1.293-1.293a1 1 0 111.414 1.414l-3 3a1 1 0 01-1.414 0l-3-3a1 1 0 010-1.414z" clip-rule="evenodd" />
                            </svg>
                          </div>
                          <div>
                            <p class="font-medium text-gray-800">{uploadedFile.name}</p>
                            <p class="text-xs text-gray-500">{Math.round(uploadedFile.size / 1024)} KB</p>
                          </div>
                        </div>
                        <button 
                          type="button"
                          class="text-red-600 hover:text-red-800 transition-colors"
                          on:click={removeFile}
                          aria-label="Remove uploaded file"
                        >
                          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                            <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                          </svg>
                        </button>
                      </div>
                    </div>
                  {/if}
                </div>
              </div>
              
              <!-- Navigation Buttons -->
              <div class="pt-6 flex justify-between">
                <button 
                  type="button" 
                  class="flex items-center bg-gray-200 hover:bg-gray-300 text-gray-700 py-2 px-6 rounded-lg font-medium transition-colors duration-300"
                  on:click={() => setTab('basic')}
                >
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M9.707 14.707a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 1.414L7.414 9H15a1 1 0 110 2H7.414l2.293 2.293a1 1 0 010 1.414z" clip-rule="evenodd" />
                  </svg>
                  Back
                </button>
                <button 
                  type="submit" 
                  class="flex items-center bg-green-600 hover:bg-green-700 text-white py-2 px-6 rounded-lg font-medium transition-colors duration-300"
                  disabled={isLoading || !jobTitle || !experience}
                >
                  {#if isLoading}
                    <svg class="animate-spin h-5 w-5 mr-3" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                      <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                      <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                    </svg>
                    Analyzing...
                  {:else}
                    Analyze My Future
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                    </svg>
                  {/if}
                </button>
              </div>
            </div>
          {/if}
          
          <!-- Form Security Note -->
          <div class="mt-8 pt-6 border-t border-gray-200">
            <div class="flex items-center justify-center text-gray-500">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-2" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M2.166 4.999A11.954 11.954 0 0010 1.944 11.954 11.954 0 0017.834 5c.11.65.166 1.32.166 2.001 0 5.225-3.34 9.67-8 11.317C5.34 16.67 2 12.225 2 7c0-.682.057-1.35.166-2.001zm11.541 3.708a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
              </svg>
              Your data is secure and only used for analysis purposes
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</div>
</section>