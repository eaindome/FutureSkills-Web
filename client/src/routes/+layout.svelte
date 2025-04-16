<script lang="ts">
	import Navbar from '../lib/components/layout/Navbar.svelte';
	import '../app.css';
  </script>
  
  <div class="min-h-screen flex flex-col bg-white">
	<Navbar />
	<main class="flex-grow">
	  <slot />
	</main>
	<!-- <footer class="py-6 bg-gray-100">
	  <div class="container mx-auto px-4 text-center text-gray-600 text-sm">
		<p>FutureSkills Coach - SDG 8: Decent Work and Economic Growth</p>
		<p class="mt-1">Call for Code Hackathon 2025</p>
	  </div>
	</footer> -->
  </div>

<!-- {@render children()} -->
