<script lang="ts">
  import { fly, fade } from 'svelte/transition';
  import { onMount } from 'svelte';
  
  let visible = false;
  
  onMount(() => {
    visible = true;
  });
  
  const scrollToDemo = () => {
    const demoSection = document.getElementById('mini-demo');
    if (demoSection) {
      demoSection.scrollIntoView({ behavior: 'smooth' });
    }
  };
 </script>
 
 <section class="bg-gradient-to-br from-green-50 via-teal-50 to-blue-50 py-24 px-4 sm:px-6 lg:px-8 overflow-hidden relative">
   <!-- Background decorative elements -->
   <div class="absolute inset-0 overflow-hidden">
     <div class="absolute -top-24 -right-24 w-96 h-96 bg-green-100 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-blob"></div>
     <div class="absolute top-1/2 -left-24 w-96 h-96 bg-blue-100 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-blob animation-delay-4000"></div>
     <div class="absolute -bottom-32 right-1/4 w-96 h-96 bg-amber-100 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-blob animation-delay-2000"></div>
     
     <!-- Grid pattern -->
     <div class="absolute inset-0 bg-grid-pattern opacity-[0.015]"></div>
   </div>
   
   <div class="max-w-7xl mx-auto relative">
     <div class="flex flex-col lg:flex-row items-center">
       <!-- Left Content -->
       <div class="lg:w-1/2 mb-12 lg:mb-0 z-10">
         {#if visible}
           <div in:fly={{ y: 30, duration: 800, delay: 200 }}>
             <div class="inline-block px-4 py-2 rounded-full bg-green-100 text-green-700 font-medium text-sm mb-6 animate-pulse">
               <span class="flex items-center">
                 <span class="w-2 h-2 rounded-full bg-green-500 mr-2"></span>
                 Call for Code 2025 Hackathon Project
               </span>
             </div>
           </div>
         
           <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold leading-tight mb-6" in:fly={{ y: 30, duration: 800, delay: 400 }}>
             <span class="text-gray-800">Empowering Your </span>
             <span class="bg-gradient-to-r from-green-600 to-teal-500 bg-clip-text text-transparent">Future Career</span>
             <span class="text-gray-800"> in Green Industries</span>
           </h1>
           
           <p class="text-lg md:text-xl text-gray-600 mb-8 leading-relaxed max-w-xl" in:fly={{ y: 30, duration: 800, delay: 600 }}>
             Navigate job automation risks, discover sustainable careers, and find your path to financial stability with AI-powered guidance tailored to tomorrow's economy.
           </p>
           
           <div class="flex flex-col sm:flex-row gap-4 sm:items-center" in:fly={{ y: 30, duration: 800, delay: 800 }}>
             <button
               on:click={scrollToDemo}
               class="px-8 py-4 rounded-xl bg-gradient-to-r from-green-600 to-teal-500 text-white font-medium hover:from-green-700 hover:to-teal-600 transition-all shadow-lg hover:shadow-xl transform hover:-translate-y-1 duration-300 flex items-center justify-center"
             >
               <span>Try the Demo</span>
               <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2" viewBox="0 0 20 20" fill="currentColor">
                 <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd" />
               </svg>
             </button>
             
             <a href="#how-it-works" class="px-8 py-4 rounded-xl border-2 border-teal-500 text-teal-600 font-medium hover:bg-teal-50 transition-all flex items-center justify-center group">
               <span>Learn More</span>
               <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2 group-hover:translate-y-1 transition-transform" viewBox="0 0 20 20" fill="currentColor">
                 <path fill-rule="evenodd" d="M16.707 10.293a1 1 0 010 1.414l-6 6a1 1 0 01-1.414 0l-6-6a1 1 0 111.414-1.414L9 14.586V3a1 1 0 012 0v11.586l4.293-4.293a1 1 0 011.414 0z" clip-rule="evenodd" />
               </svg>
             </a>
           </div>
           
           <div class="mt-10 flex items-center space-x-6" in:fade={{ duration: 1000, delay: 1200 }}>
             <div class="flex -space-x-2">
               <div class="w-10 h-10 rounded-full bg-green-200 flex items-center justify-center text-green-700 text-sm font-medium border-2 border-white">UN</div>
               <div class="w-10 h-10 rounded-full bg-blue-200 flex items-center justify-center text-blue-700 text-sm font-medium border-2 border-white">IBM</div>
               <div class="w-10 h-10 rounded-full bg-amber-200 flex items-center justify-center text-amber-700 text-sm font-medium border-2 border-white">SDG</div>
             </div>
             <p class="text-gray-600 text-sm">Supporting <span class="font-medium">SDG 8</span>: Decent Work and Economic Growth</p>
           </div>
         {/if}
       </div>
       
       <!-- Right Content - Hero Illustration -->
       <div class="lg:w-1/2 flex justify-center z-10">
         {#if visible}
           <div class="relative w-full max-w-lg" in:fly={{ x: 30, duration: 800, delay: 600 }}>
             <!-- Decorative elements -->
             <div class="absolute top-0 -left-4 w-72 h-72 bg-teal-300 rounded-full mix-blend-multiply filter blur-xl opacity-40 animate-blob"></div>
             <div class="absolute top-0 -right-4 w-72 h-72 bg-amber-300 rounded-full mix-blend-multiply filter blur-xl opacity-40 animate-blob animation-delay-2000"></div>
             <div class="absolute -bottom-8 left-20 w-72 h-72 bg-blue-300 rounded-full mix-blend-multiply filter blur-xl opacity-40 animate-blob animation-delay-4000"></div>
             
             <!-- Hero image container with floating animation -->
             <div class="relative p-4 animate-float">
               <!-- You can replace this with your actual hero image -->
               <div class="bg-white rounded-2xl shadow-xl overflow-hidden">
                 <div class="p-1 bg-gradient-to-r from-green-400 via-teal-500 to-blue-500 rounded-2xl">
                   <div class="bg-white p-4 rounded-xl">
                     <div class="w-full aspect-video bg-gradient-to-br from-green-100 to-teal-50 rounded-lg p-6 relative overflow-hidden">
                       <!-- Dashboard mockup content -->
                       <div class="absolute top-0 left-0 right-0 h-10 bg-white/80 backdrop-blur-sm flex items-center px-3 border-b">
                         <div class="w-3 h-3 rounded-full bg-red-400 mr-2"></div>
                         <div class="w-3 h-3 rounded-full bg-amber-400 mr-2"></div>
                         <div class="w-3 h-3 rounded-full bg-green-400 mr-2"></div>
                         <div class="h-5 w-40 bg-gray-100 rounded-md mx-auto"></div>
                       </div>
                       
                       <div class="mt-12 flex space-x-4">
                         <div class="w-1/3 h-24 bg-white rounded-lg shadow-sm p-2">
                           <div class="w-full h-3 bg-green-500 rounded-full mb-2"></div>
                           <div class="w-1/2 h-2 bg-gray-200 rounded-full mb-2"></div>
                           <div class="w-3/4 h-2 bg-gray-200 rounded-full mb-2"></div>
                           <div class="w-2/3 h-2 bg-gray-200 rounded-full"></div>
                         </div>
                         <div class="w-1/3 h-24 bg-white rounded-lg shadow-sm p-2">
                           <div class="w-full h-3 bg-blue-500 rounded-full mb-2"></div>
                           <div class="w-1/2 h-2 bg-gray-200 rounded-full mb-2"></div>
                           <div class="w-3/4 h-2 bg-gray-200 rounded-full mb-2"></div>
                           <div class="w-2/3 h-2 bg-gray-200 rounded-full"></div>
                         </div>
                         <div class="w-1/3 h-24 bg-white rounded-lg shadow-sm p-2">
                           <div class="w-full h-3 bg-amber-500 rounded-full mb-2"></div>
                           <div class="w-1/2 h-2 bg-gray-200 rounded-full mb-2"></div>
                           <div class="w-3/4 h-2 bg-gray-200 rounded-full mb-2"></div>
                           <div class="w-2/3 h-2 bg-gray-200 rounded-full"></div>
                         </div>
                       </div>
                       
                       <div class="mt-4 w-full h-32 bg-white rounded-lg shadow-sm p-3">
                         <div class="flex justify-between items-center mb-2">
                           <div class="w-24 h-3 bg-gray-200 rounded-full"></div>
                           <div class="w-12 h-4 bg-green-500 rounded-md"></div>
                         </div>
                         <div class="mt-2 flex items-end space-x-2 h-16">
                           <div class="w-1/12 h-1/4 bg-green-200 rounded-t-sm"></div>
                           <div class="w-1/12 h-2/6 bg-green-300 rounded-t-sm"></div>
                           <div class="w-1/12 h-3/6 bg-green-400 rounded-t-sm"></div>
                           <div class="w-1/12 h-4/6 bg-green-500 rounded-t-sm"></div>
                           <div class="w-1/12 h-5/6 bg-green-600 rounded-t-sm"></div>
                           <div class="w-1/12 h-full bg-green-700 rounded-t-sm"></div>
                           <div class="w-1/12 h-5/6 bg-green-600 rounded-t-sm"></div>
                           <div class="w-1/12 h-4/6 bg-green-500 rounded-t-sm"></div>
                           <div class="w-1/12 h-3/6 bg-green-400 rounded-t-sm"></div>
                           <div class="w-1/12 h-2/6 bg-green-300 rounded-t-sm"></div>
                           <div class="w-1/12 h-1/4 bg-green-200 rounded-t-sm"></div>
                           <div class="w-1/12 h-1/6 bg-green-100 rounded-t-sm"></div>
                         </div>
                       </div>
                     </div>
                   </div>
                 </div>
               </div>
             </div>
           </div>
         {/if}
       </div>
     </div>
   </div>
 </section>
 
 <style>
 @keyframes blob {
   0%, 100% { transform: translate(0, 0) scale(1); }
   25% { transform: translate(10px, -10px) scale(1.1); }
   50% { transform: translate(0, 10px) scale(0.9); }
   75% { transform: translate(-10px, -5px) scale(1.05); }
 }
 
 .animate-blob {
   animation: blob 15s infinite alternate;
 }
 
 .animation-delay-2000 {
   animation-delay: -2s;
 }
 
 .animation-delay-4000 {
   animation-delay: -4s;
 }
 
 @keyframes float {
   0%, 100% { transform: translateY(0); }
   50% { transform: translateY(-10px); }
 }
 
 .animate-float {
   animation: float 6s ease-in-out infinite;
 }
 
 .bg-grid-pattern {
   background-image: 
     linear-gradient(to right, rgba(0, 128, 0, 0.05) 1px, transparent 1px),
     linear-gradient(to bottom, rgba(0, 128, 0, 0.05) 1px, transparent 1px);
   background-size: 30px 30px;
 }
 </style>