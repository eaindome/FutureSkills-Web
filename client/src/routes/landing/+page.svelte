<script lang="ts">
    import Hero from '$lib/components/ui/Hero.svelte';
    import HowItWorks from '$lib/components/ui/HowItWorks.svelte';
    import WhyItMatters from '$lib/components/ui/WhyItMatters.svelte';
    import MiniDemo from '$lib/components/ui/MiniDemo.svelte';
    import Footer from '$lib/components/layout/Footer.svelte';
  </script>
  
<svelte:head>
    <title>FutureSkills Coach | Green Careers with AI</title>
    <meta name="description" content="AI-driven career guidance for sustainable jobs and green industries" />
</svelte:head>
  
<main class="min-h-screen">
    <Hero />
    <HowItWorks />
    <WhyItMatters />
    <MiniDemo />
    <Footer />
</main>