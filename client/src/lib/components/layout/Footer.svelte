<script lang="ts">
    const currentYear = new Date().getFullYear();
</script>
  
<footer class="bg-gray-800 text-white py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-7xl mx-auto">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
        <!-- Logo and brief description -->
        <div class="col-span-1 md:col-span-2">
          <div class="flex items-center mb-4">
            <span class="text-2xl font-bold text-white">FutureSkills<span class="text-green-400">Coach</span></span>
          </div>
          <p class="text-gray-300 mb-6">
            Empowering workers and students to transition to sustainable, future-proof careers in green industries.
          </p>
          <div class="flex space-x-4">
            <!-- svelte-ignore a11y_invalid_attribute -->
            <a href="#" class="text-gray-300 hover:text-white transition-colors">
              <span class="sr-only">GitHub</span>
              <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
                <path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd" />
              </svg>
            </a>
            <!-- svelte-ignore a11y_invalid_attribute -->
            <a href="#" class="text-gray-300 hover:text-white transition-colors">
              <span class="sr-only">Twitter</span>
              <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
                <path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" />
              </svg>
            </a>
            <!-- svelte-ignore a11y_invalid_attribute -->
            <a href="#" class="text-gray-300 hover:text-white transition-colors">
              <span class="sr-only">LinkedIn</span>
              <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
                <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z" />
              </svg>
            </a>
          </div>
        </div>
        
        <!-- Navigation -->
        <div>
          <h3 class="text-lg font-semibold text-white mb-4">Navigate</h3>
          <ul class="space-y-2">
            <li><a href="/" class="text-gray-300 hover:text-green-400 transition-colors">Home</a></li>
            <li><a href="/demo" class="text-gray-300 hover:text-green-400 transition-colors">Demo</a></li>
            <li><a href="/about" class="text-gray-300 hover:text-green-400 transition-colors">About</a></li>
            <li><a href="/faq" class="text-gray-300 hover:text-green-400 transition-colors">FAQ</a></li>
          </ul>
        </div>
        
        <!-- Resources -->
        <div>
          <h3 class="text-lg font-semibold text-white mb-4">Resources</h3>
          <ul class="space-y-2">
            <li><a href="#sdg8" class="text-gray-300 hover:text-green-400 transition-colors">SDG 8 Overview</a></li>
            <li><a href="#future-jobs" class="text-gray-300 hover:text-green-400 transition-colors">Future Jobs Report</a></li>
            <li><a href="#hackathon" class="text-gray-300 hover:text-green-400 transition-colors">Call for Code</a></li>
            <li><a href="#ibm-granite" class="text-gray-300 hover:text-green-400 transition-colors">IBM Granite Models</a></li>
          </ul>
        </div>
      </div>
      
      <div class="border-t border-gray-700 mt-8 pt-8 flex flex-col md:flex-row justify-between">
        <p class="text-gray-400">© {currentYear} FutureSkills Coach. Created for Call for Code 2025.</p>
        <div class="flex space-x-6 mt-4 md:mt-0">
          <a href="#privacy" class="text-gray-400 hover:text-gray-300 transition-colors">Privacy Policy</a>
          <a href="#terms" class="text-gray-400 hover:text-gray-300 transition-colors">Terms of Use</a>
          <a href="#contact" class="text-gray-400 hover:text-gray-300 transition-colors">Contact</a>
        </div>
      </div>
      
      <div class="mt-8 flex items-center justify-center">
        <span class="text-gray-400 text-sm">Powered by </span>
        <svg class="h-5 w-auto mx-2" viewBox="0 0 512 512" fill="currentColor">
          <path fill="#ffffff" d="M214 512h-72V234h72v278zm144 0h-72V234h72v278zm144 0h-72V234h72v278zM142 128h84v78h-84v-78zm142 0h86v78h-86v-78zm144 0h84v78h-84v-78zM250 0l130 128H120L250 0z"/>
        </svg>
        <span class="text-gray-400 text-sm">IBM Granite Models</span>
      </div>
    </div>
</footer>