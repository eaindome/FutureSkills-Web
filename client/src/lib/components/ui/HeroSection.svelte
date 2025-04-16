<script lang="ts">
    // We can add animations or interactive elements later if needed
</script>
  
<section class="py-16 md:py-24">
    <div class="container mx-auto px-4">
      <div class="flex flex-col md:flex-row items-center justify-between">
        <div class="md:w-1/2 mb-10 md:mb-0">
          <h1 class="text-4xl md:text-5xl font-bold text-gray-800 leading-tight">
            From Job Fear to <span class="text-green-600">Green Careers</span>—AI's Got You
          </h1>
          <p class="mt-6 text-lg text-gray-600 max-w-lg">
            See your job's automation risk, find sustainable careers in growing green industries, 
            and discover side hustles to support your transition to a 
            <span class="text-amber-500 font-medium">future-proof</span> career.
          </p>
          <div class="mt-8 flex flex-col sm:flex-row gap-4">
            <a href="#input-form" class="bg-green-600 hover:bg-green-700 text-white px-6 py-3 rounded-lg text-center font-medium transition-colors duration-300">
              Analyze My Future
            </a>
            <a href="/chat" class="text-blue-500 hover:text-blue-600 flex items-center justify-center px-6 py-3">
              <span>Ask our AI Mentor now!</span>
              <svg class="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
              </svg>
            </a>
          </div>
        </div>
        <div class="md:w-1/2 flex justify-center md:justify-end">
          <div class="relative w-full max-w-md">
            <!-- Eco-themed illustration -->
            <svg class="w-full h-auto" viewBox="0 0 500 400" xmlns="http://www.w3.org/2000/svg">
              <!-- Sky background -->
              <rect x="0" y="0" width="500" height="300" fill="#e0f2fe" />
              
              <!-- Sun -->
              <circle cx="400" cy="80" r="40" fill="#fcd34d" />
              
              <!-- Ground -->
              <rect x="0" y="300" width="500" height="100" fill="#d1fae5" />
              
              <!-- Wind turbines -->
              <g>
                <!-- Turbine 1 -->
                <line x1="100" y1="300" x2="100" y2="180" stroke="#475569" stroke-width="8" />
                <circle cx="100" cy="180" r="5" fill="#475569" />
                
                <!-- Blades -->
                <g transform="translate(100,180)">
                  <path d="M0,0 L-60,-20 L-70,-40 L-10,-10 Z" fill="#e2e8f0" />
                  <path d="M0,0 L40,-50 L30,-70 L0,-10 Z" fill="#e2e8f0" transform="rotate(120,0,0)" />
                  <path d="M0,0 L40,-50 L30,-70 L0,-10 Z" fill="#e2e8f0" transform="rotate(240,0,0)" />
                </g>
              </g>
              
              <!-- Turbine 2 -->
              <g>
                <line x1="250" y1="300" x2="250" y2="150" stroke="#475569" stroke-width="8" />
                <circle cx="250" cy="150" r="5" fill="#475569" />
                
                <!-- Blades -->
                <g transform="translate(250,150)">
                  <path d="M0,0 L-60,-20 L-70,-40 L-10,-10 Z" fill="#e2e8f0" />
                  <path d="M0,0 L40,-50 L30,-70 L0,-10 Z" fill="#e2e8f0" transform="rotate(120,0,0)" />
                  <path d="M0,0 L40,-50 L30,-70 L0,-10 Z" fill="#e2e8f0" transform="rotate(240,0,0)" />
                </g>
              </g>
              
              <!-- Turbine 3 -->
              <g>
                <line x1="400" y1="300" x2="400" y2="170" stroke="#475569" stroke-width="8" />
                <circle cx="400" cy="170" r="5" fill="#475569" />
                
                <!-- Blades -->
                <g transform="translate(400,170)">
                  <path d="M0,0 L-60,-20 L-70,-40 L-10,-10 Z" fill="#e2e8f0" />
                  <path d="M0,0 L40,-50 L30,-70 L0,-10 Z" fill="#e2e8f0" transform="rotate(120,0,0)" />
                  <path d="M0,0 L40,-50 L30,-70 L0,-10 Z" fill="#e2e8f0" transform="rotate(240,0,0)" />
                </g>
              </g>
              
              <!-- Solar panels -->
              <g>
                <rect x="150" y="320" width="80" height="40" fill="#0c4a6e" />
                <line x1="170" y1="320" x2="170" y2="360" stroke="#e2e8f0" stroke-width="1" />
                <line x1="190" y1="320" x2="190" y2="360" stroke="#e2e8f0" stroke-width="1" />
                <line x1="210" y1="320" x2="210" y2="360" stroke="#e2e8f0" stroke-width="1" />
                <line x1="150" y1="340" x2="230" y2="340" stroke="#e2e8f0" stroke-width="1" />
              </g>
              
              <!-- Person with laptop -->
              <g>
                <!-- Body -->
                <circle cx="330" cy="330" r="15" fill="#2563eb" />
                <rect x="325" y="345" width="10" height="20" fill="#2563eb" />
                
                <!-- Laptop -->
                <rect x="310" y="340" width="30" height="20" fill="#94a3b8" transform="rotate(-15,310,340)" />
                <rect x="310" y="340" width="30" height="15" fill="#64748b" transform="rotate(-15,310,352)" />
              </g>
            </svg>
          </div>
        </div>
      </div>
    </div>
</section>